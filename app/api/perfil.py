from fastapi import APIRouter, Query
from app.services.perfil_service import actualizar_correo, actualizar_contrasena, obtener_correo
from app.models.perfil_model import ActualizarCorreoRequest, ActualizarContrasenaRequest

router = APIRouter()

@router.put("/actualizar-correo")
def endpoint_actualizar_correo(data: ActualizarCorreoRequest):
    actualizar_correo(data.uid, data.nuevo_correo)
    return {"mensaje": "Correo actualizado correctamente"}

@router.put("/actualizar-contrasena")
def endpoint_actualizar_contrasena(data: ActualizarContrasenaRequest):
    actualizar_contrasena(data.uid, data.contrasena_actual, data.nueva_contrasena)
    return {"mensaje": "Contraseña actualizada correctamente"}

@router.get("/correo")
def endpoint_obtener_correo(uid: str = Query(..., description="UID del usuario")):
    correo = obtener_correo(uid)
    return {"correo": correo}
