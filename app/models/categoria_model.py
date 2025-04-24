from pydantic import BaseModel

class Categoria(BaseModel):
    categoria: str
    descripcion: str
    uid_usuario: str
    clasificacion: str  # Nuevo campo para clasificar la categoría