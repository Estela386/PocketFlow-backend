from pydantic import BaseModel

class Ingreso(BaseModel):
    id: str  # ID de documento Firebase
    id_usuario: str  # referencia al UID del usuario
    fecha: str  # 'YYYY-MM-DDTHH:MM:SS'
    cantidad: float
    motivo: str
    categoria_id: str  # ID de la categoría en Firestore
