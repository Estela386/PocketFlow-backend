from pydantic import BaseModel, EmailStr

class VerificarCorreoRequest(BaseModel):
    correo: EmailStr

class CambiarContrasenaRequest(BaseModel):
    correo: EmailStr
    nueva_contrasena: str
