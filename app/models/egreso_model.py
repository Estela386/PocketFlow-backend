from pydantic import BaseModel
from datetime import date

class EgresoCreate(BaseModel):  # Este lo usas para recibir datos del frontend
    id_usuario: str
    fecha: date
    cantidad: float
    motivo: str
    #Dejo esto comentado hasta que tengamos el apartado definitivo de las categorias
    #categoria_id: str  # ID de la categoría en Firestore


class Egreso(EgresoCreate):  # Este lo usas para responder con datos completos
    id: str