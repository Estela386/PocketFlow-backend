from pydantic import BaseModel

class Usuario(BaseModel):
    id: str  # ID de documento Firebase
    nombre: str
    fecha_nacimiento: str  # 'YYYY-MM-DD'
    correo: str
    contrasena_hash: str
    fecha_registro: str  # 'YYYY-MM-DDTHH:MM:SS'
