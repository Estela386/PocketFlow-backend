from fastapi import APIRouter, HTTPException
from app.models.ingreso_model import Ingreso, IngresoCreate
from app.services.ingreso_service import registrar_ingreso, obtener_ingresos_por_usuario

router = APIRouter(
    prefix="/ingresos",
    tags=["Ingresos"]
)

@router.post("", response_model=Ingreso)
async def crear_ingreso(ingreso: IngresoCreate):
    ingreso_creado = await registrar_ingreso(ingreso)
    if ingreso_creado:
        return ingreso_creado
    raise HTTPException(status_code=500, detail="Error al registrar el ingreso.")

@router.get("/{id_usuario}", response_model=list[Ingreso])
async def listar_ingresos(id_usuario: str):
    ingresos = await obtener_ingresos_por_usuario(id_usuario)
    return ingresos
