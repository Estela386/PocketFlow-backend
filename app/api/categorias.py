from fastapi import APIRouter, Path
from app.models.categoria_model import Categoria
from app.services.categoria_service import agregar_categoria, obtener_categoria, eliminar_categoria

router = APIRouter()

@router.post("/categorias")
def crear_categoria(categoria: Categoria):
    agregar_categoria(categoria)
    return {"mensaje": "Categoría agregada correctamente"}

@router.get("/categorias/{uid_usuario}")
def listar_categorias(uid_usuario: str = Path(..., description="UID del usuario")):
    categorias = obtener_categoria(uid_usuario)
    return {"categorias": categorias}

@router.delete("/categorias/{uid_usuario}/{categoria_id}")
def borrar_categoria(uid_usuario: str, categoria_id: str):
    eliminar_categoria(uid_usuario, categoria_id)
    return {"mensaje": "Categoría eliminada correctamente"}