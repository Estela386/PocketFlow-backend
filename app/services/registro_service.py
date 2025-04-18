from fastapi import HTTPException
from passlib.context import CryptContext
from app.models.registro_model import RegistroResponse, RegistroRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulamos base de datos en memoria
fake_users_db = {}

def crear_usuario(data: RegistroRequest) -> RegistroResponse:
    if data.correo in fake_users_db:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    hashed_password = pwd_context.hash(data.contrasena)
    fake_users_db[data.correo] = {
        "nombre": data.nombre,
        "contrasena": hashed_password,
        "fecha_nacimiento": data.fecha_nacimiento
    }

    return RegistroResponse(mensaje="Usuario registrado correctamente", correo=data.correo)
