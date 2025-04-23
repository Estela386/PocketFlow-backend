from pydantic import BaseModel
from datetime import date

class Egreso(BaseModel):
    id: str
    id_usuario: str
    fecha: date
    cantidad: float
    motivo: str
    # Dejo esto comentado hasta que tengamos el apartado definitivo de las categorias
    # categoria_id: str  # ID de la categoría en Firestore