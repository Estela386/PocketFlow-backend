import uuid
from firebase_admin import db
from app.models.ingreso_model import Ingreso, IngresoCreate
from datetime import datetime
from typing import List

async def registrar_ingreso(ingreso: IngresoCreate) -> Ingreso:
    try:
        ingreso_id = str(uuid.uuid4())
        ingreso.id = ingreso_id

        ref = db.reference(f"ingresos/{ingreso_id}")
        ref.set({
            "id": ingreso.id,
            "id_usuario": ingreso.id_usuario,
            "fecha": ingreso.fecha.isoformat(),  # Guardar como string ISO
            "cantidad": ingreso.cantidad,
            "motivo": ingreso.motivo
        })
        return ingreso
    except Exception as e:
        print(f"Error al registrar ingreso: {e}")
        return None

async def obtener_ingresos_por_usuario(id_usuario: str) -> List[Ingreso]:
    try:
        ref = db.reference("ingresos")
        snapshot = ref.order_by_child("id_usuario").equal_to(id_usuario).get()

        ingresos = []
        if snapshot:
            for item in snapshot.values():
                ingresos.append(
                    Ingreso(
                        id=item["id"],
                        id_usuario=item["id_usuario"],
                        fecha=datetime.fromisoformat(item["fecha"]).date(),
                        cantidad=item["cantidad"],
                        motivo=item["motivo"]
                    )
                )
        return ingresos

    except Exception as e:
        print(f"Error al obtener ingresos: {e}")
        return []
