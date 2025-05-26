from fastapi import APIRouter
from app.models.login_model import LoginRequest, LoginResponse
from app.models.recuperacion_model import VerificarCorreoRequest, CambiarContrasenaRequest
from app.services.login_service import login_usuario, verificar_correo, cambiar_contrasena

router = APIRouter()

@router.post("/auth", response_model=LoginResponse)
def login_endpoint(login_data: LoginRequest):
    return login_usuario(login_data)

@router.post("/verificar-correo")
def verificar_correo_endpoint(request: VerificarCorreoRequest):
    return verificar_correo(request)

@router.post("/cambiar-contrasena")
def cambiar_contrasena_endpoint(request: CambiarContrasenaRequest):
    return cambiar_contrasena(request)

