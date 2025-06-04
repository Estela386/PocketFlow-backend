from fastapi import APIRouter, HTTPException
from typing import List
from app.models.huella_model import EgresoItem, HuellaResponse
from app.services.huella_service import calcular_emision

router = APIRouter()

@router.post("/calculo", response_model=List[HuellaResponse])
def calcular_huella(gastos: List[EgresoItem]):
    try:
        resultados = []
        for gasto in gastos:
            emision = calcular_emision(gasto.motivo, gasto.cantidad)
            resultados.append(HuellaResponse(
                motivo=gasto.motivo,
                cantidad=gasto.cantidad,
                co2_kg=emision
            ))
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

