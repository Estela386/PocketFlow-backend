from pydantic import BaseModel
from typing import List

class EgresoItem(BaseModel):
    id_usuario: str
    fecha: str
    cantidad: float
    motivo: str
    id: str

class HuellaResponse(BaseModel):
    motivo: str
    cantidad: float
    co2_kg: float
