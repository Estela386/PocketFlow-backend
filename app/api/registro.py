from fastapi import APIRouter
from app.models.registro_model import RegistroRequest, RegistroResponse
from app.services import registro_service

router = APIRouter()

@router.post("", response_model=RegistroResponse)
def registrar_usuario(data: RegistroRequest):
    return registro_service.crear_usuario(data)