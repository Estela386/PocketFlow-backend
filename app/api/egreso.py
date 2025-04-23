from fastapi import APIRouter, HTTPException
from app.models.egreso_model import Egreso, EgresoCreate
from app.services.egreso_service import registrar_egreso, obtener_egresos_por_usuario

router = APIRouter(
    prefix="/egresos",
    tags=["Egresos"]
)

@router.post("", response_model=Egreso)
async def crear_egreso(egreso: EgresoCreate):
    egreso_creado = await registrar_egreso(egreso)
    if egreso_creado:
        return egreso_creado
    raise HTTPException(status_code=500, detail="Error al registrar el egreso.")

@router.get("/{id_usuario}", response_model=list[Egreso])
async def listar_egresos(id_usuario: str):
    egresos = await obtener_egresos_por_usuario(id_usuario)
    return egresos