from fastapi import APIRouter
from app.models.login_model import LoginRequest, LoginResponse
from app.services.login_service import login_usuario

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("", response_model=LoginResponse)
def login_endpoint(login_data: LoginRequest):
    return login_usuario(login_data)
