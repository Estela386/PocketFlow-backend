from fastapi import APIRouter, Path, Body
from app.models.categoria_model import Categoria

router = APIRouter()

from app.services.categoria_service import (
    agregar_categoria, obtener_categoria, eliminar_categoria,
    actualizar_categoria, filtrar
)

@router.put("/categorias/{uid_usuario}/{categoria_id}") #UPDATE
def modificar_categoria(uid_usuario: str, categoria_id: str, categoria: Categoria = Body(...)):
    actualizar_categoria(uid_usuario, categoria_id, categoria)
    return {"mensaje": "Categoría actualizada correctamente"}

@router.get("/{uid_usuario}/filtrar/{clasificacion}") #Mostrar por clasificacion
def categorias_por_clasificacion(uid_usuario: str, clasificacion: str):
    categorias = filtrar(uid_usuario, clasificacion)
    return {"categorias": categorias}

@router.post("/categorias") #Agregar
def crear_categoria(categoria: Categoria):
    agregar_categoria(categoria)
    return {"mensaje": "Categoría agregada correctamente"}

@router.get("/categorias/{uid_usuario}") #Mostrar por usuario
def listar_categorias(uid_usuario: str = Path(..., description="UID del usuario")):
    categorias = obtener_categoria(uid_usuario)
    return {"categorias": categorias}

@router.delete("/categorias/{uid_usuario}/{categoria_id}") #Borrar
def borrar_categoria(uid_usuario: str, categoria_id: str):
    eliminar_categoria(uid_usuario, categoria_id)
    return {"mensaje": "Categoría eliminada correctamente"}