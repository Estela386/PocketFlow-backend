from pydantic import BaseModel

class HuellaCarbono(BaseModel):
    id: str
    id_usuario: str
    fecha: str
    categoria_id: str
    co2_estimado_kg: float
