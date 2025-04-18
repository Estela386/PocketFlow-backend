from pydantic import BaseModel, EmailStr
from datetime import date

class RegistroRequest(BaseModel):
    nombre: str
    correo: EmailStr
    contrasena: str
    fecha_nacimiento: date

class RegistroResponse(BaseModel):
    mensaje: str
    correo: EmailStr