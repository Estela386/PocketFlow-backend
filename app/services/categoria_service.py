


from app.models.categoria_model import Categoria
from app.core.firebase import db
from fastapi import HTTPException

def agregar_categoria(categoria: Categoria):
    try:
        # Referencia al nodo de categorías del usuario
        ref = db.reference(f"categorias/{categoria.uid_usuario}")
        nueva_categoria_ref = ref.push()

        nueva_categoria_ref.set({
            "categoria": categoria.categoria,
            "descripcion": categoria.descripcion,
            "clasificacion": categoria.clasificacion,
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar categoría: {str(e)}")

def obtener_categoria(uid_usuario: str):
    try:
        ref = db.reference(f"categorias/{uid_usuario}")
        categorias_snapshot = ref.get()
      
        if not categorias_snapshot:
            return []

        categorias = []
        for key, value in categorias_snapshot.items():
            categorias.append({
                "id": key,
                "categoria": value.get("categoria"),
                "descripcion": value.get("descripcion"),  # ← COMA agregada aquí
                "clasificacion": value.get("clasificacion")
            })

        return categorias
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener categorías: {str(e)}")


def eliminar_categoria(uid_usuario: str, categoria_id: str):
    try:
        ref = db.reference(f"categorias/{uid_usuario}/{categoria_id}")
        if ref.get() is None:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")

        ref.delete()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar categoría: {str(e)}")
    
def actualizar_categoria(uid_usuario: str, categoria_id: str, categoria: Categoria):
    try:
        ref = db.reference(f"categorias/{uid_usuario}/{categoria_id}")
        if ref.get() is None:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")

        ref.update({
            "categoria": categoria.categoria,
            "descripcion": categoria.descripcion,
            "clasificacion": categoria.clasificacion
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar categoría: {str(e)}")


def filtrar(uid_usuario: str, clasificacion: str):
    try:
        ref = db.reference(f"categorias/{uid_usuario}")
        snapshot = ref.get()

        if not snapshot:
            return []

        categorias_filtradas = []
        for key, value in snapshot.items():
            if value.get("clasificacion") == clasificacion:
                categorias_filtradas.append({
                    "id": key,
                    "categoria": value.get("categoria"),
                    "descripcion": value.get("descripcion"),
                    "clasificacion": value.get("clasificacion")
                })

        return categorias_filtradas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al filtrar categorías: {str(e)}")