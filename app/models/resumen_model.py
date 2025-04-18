from pydantic import BaseModel

class ResumenFinanciero(BaseModel):
    id: str
    id_usuario: str
    periodo: str  # '2025-04'
    total_ingresos: float
    total_egresos: float
    ahorro_estimado: float
