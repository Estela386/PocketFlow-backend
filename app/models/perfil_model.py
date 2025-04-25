from pydantic import BaseModel, EmailStr, validator

class ActualizarCorreoRequest(BaseModel):
    uid: str
    nuevo_correo: EmailStr

class ActualizarContrasenaRequest(BaseModel):
    uid: str
    contrasena_actual: str
    nueva_contrasena: str
    confirmar_contrasena: str

    @validator("confirmar_contrasena")
    def validar_contrasenas_iguales(cls, v, values):
        if "nueva_contrasena" in values and v != values["nueva_contrasena"]:
            raise ValueError("La nueva contraseña y su confirmación no coinciden")
        return v
