import uuid
from firebase_admin import db
from app.models.egreso_model import Egreso, EgresoCreate
from datetime import datetime
from typing import List
from fastapi import HTTPException

async def registrar_egreso(egreso: EgresoCreate) -> Egreso:
    try:
        egreso_id = str(uuid.uuid4())

        nuevo_egreso = Egreso(
            id=egreso_id,
            id_usuario=egreso.id_usuario,
            fecha=egreso.fecha,
            cantidad=egreso.cantidad,
            motivo=egreso.motivo
        )

        ref = db.reference(f"egresos/{egreso_id}")
        ref.set({
            "id": nuevo_egreso.id,
            "id_usuario": nuevo_egreso.id_usuario,
            "fecha": nuevo_egreso.fecha.isoformat(),
            "cantidad": nuevo_egreso.cantidad,
            "motivo": nuevo_egreso.motivo
        })

        return nuevo_egreso

    except Exception as e:
        print(f"Error al registrar egreso: {e}")
        raise HTTPException(status_code=500, detail="Error al registrar egreso")

async def obtener_egresos_por_usuario(id_usuario: str) -> List[Egreso]:
    try:
        ref = db.reference("egresos")
        snapshot = ref.order_by_child("id_usuario").equal_to(id_usuario).get()

        egresos = []
        if snapshot:
            for item in snapshot.values():
                egresos.append(
                    Egreso(
                        id=item["id"],
                        id_usuario=item["id_usuario"],
                        fecha=datetime.fromisoformat(item["fecha"]).date(),
                        cantidad=item["cantidad"],
                        motivo=item["motivo"]
                    )
                )
        return egresos

    except Exception as e:
        print(f"Error al obtener egresos: {e}")
        return []
