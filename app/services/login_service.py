from app.core.firebase import db
import bcrypt
from fastapi import HTTPException
from app.models.login_model import LoginResponse, LoginRequest
from app.models.recuperacion_model import VerificarCorreoRequest, CambiarContrasenaRequest

def login_usuario(login_data: LoginRequest) -> LoginResponse:
    ref = db.reference("usuarios")
    usuarios = ref.get()

    if not usuarios:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados")

    for uid, datos in usuarios.items():
        if datos.get("correo") == login_data.correo:
            contrasena_db = datos.get("contrasena")
            if contrasena_db and bcrypt.checkpw(login_data.contrasena.encode(), contrasena_db.encode()):
                return LoginResponse(uid=uid, nombre=datos.get("nombre"))
            else:
                raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# --------------------------------------------------------
# ✅ Servicio: Verificar si un correo existe
# --------------------------------------------------------
def verificar_correo(request: VerificarCorreoRequest) -> dict:
    ref = db.reference("usuarios")
    usuarios = ref.get()

    if not usuarios:
        return {"existe": False}

    for _, datos in usuarios.items():
        if datos.get("correo") == request.correo:
            return {"existe": True}

    return {"existe": False}


# --------------------------------------------------------
# 🔄 Servicio: Cambiar contraseña
# --------------------------------------------------------
def cambiar_contrasena(request: CambiarContrasenaRequest) -> dict:
    ref = db.reference("usuarios")
    usuarios = ref.get()

    if not usuarios:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados")

    for uid, datos in usuarios.items():
        if datos.get("correo") == request.correo:
            nueva_contrasena_hash = bcrypt.hashpw(request.nueva_contrasena.encode(), bcrypt.gensalt()).decode()
            db.reference(f"usuarios/{uid}").update({"contrasena": nueva_contrasena_hash})
            return {"mensaje": "Contraseña actualizada correctamente"}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")

