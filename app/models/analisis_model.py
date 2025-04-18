from pydantic import BaseModel

class Analisis(BaseModel):
    id: int
    nombre: str
    resultado: str
