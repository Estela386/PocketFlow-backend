from pydantic import BaseModel

class Egreso(BaseModel):
    id: str
    id_usuario: str
    fecha: str
    cantidad: float
    motivo: str
    categoria_id: str
