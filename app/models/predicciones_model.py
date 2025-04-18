from pydantic import BaseModel

class Prediccion(BaseModel):
    id: str
    id_usuario: str
    periodo: str  # '2025-04'
    gasto_estimado: float
    gasto_real: float
    probabilidad_exceso: float  # % Ej: 75.50
