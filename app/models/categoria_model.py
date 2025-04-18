from pydantic import BaseModel

class Categoria(BaseModel):
    id: str
    id_usuario: str
    nombre_categoria: str
    color_hex: str = "#FFFFFF"
