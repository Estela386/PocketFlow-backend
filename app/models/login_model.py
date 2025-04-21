from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    correo: str
    contrasena: str

class LoginResponse(BaseModel):
    uid: str
    nombre: str
