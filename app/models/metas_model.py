from pydantic import BaseModel

class Meta(BaseModel):
    id: str
    id_usuario: str
    descripcion: str
    monto_objetivo: float
    monto_actual: float = 0.0
    fecha_limite: str  # 'YYYY-MM-DD'
    estado: str  # 'Pendiente' o 'Completada'
