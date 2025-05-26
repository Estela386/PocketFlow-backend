from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime
import pandas as pd

from app.api.egreso import obtener_egresos_por_usuario  # 👈 Asegúrate de importar bien

router = APIRouter()

# Modelo de respuesta
class Prediccion(BaseModel):
    motivo: str
    cantidad_real: float
    cantidad_predicha: float

@router.get("/api/predicciones/{id_usuario}", response_model=List[Prediccion])
async def obtener_predicciones(id_usuario: str, periodo: str):
    # 🔄 Obtenemos objetos Egreso (no Pydantic)
    egresos_objs = await obtener_egresos_por_usuario(id_usuario)

    # ✅ Convertimos manualmente a dict para usar en DataFrame
    egresos = [
        {
            "id": eg.id,
            "id_usuario": eg.id_usuario,
            "fecha": eg.fecha,
            "cantidad": eg.cantidad,
            "motivo": eg.motivo
        }
        for eg in egresos_objs
    ]

    print(f"[🔍 INPUT] Egresos recibidos para usuario {id_usuario}:")
    for eg in egresos:
        print(eg)

    # 🧠 Pandas para análisis
    df = pd.DataFrame(egresos)
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["anio"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month
    df["semana"] = df["fecha"].dt.isocalendar().week

    ahora = datetime.now()
    if periodo == "semana":
        actual = ahora.isocalendar().week
        anterior = actual - 1
        df_periodo_actual = df[df["semana"] == actual]
        df_periodo_anterior = df[df["semana"] == anterior]
    elif periodo == "mes":
        actual = ahora.month
        anterior = actual - 1
        df_periodo_actual = df[df["mes"] == actual]
        df_periodo_anterior = df[df["mes"] == anterior]
    else:  # año
        actual = ahora.year
        anterior = actual - 1
        df_periodo_actual = df[df["anio"] == actual]
        df_periodo_anterior = df[df["anio"] == anterior]

    suma_anterior = df_periodo_anterior.groupby("motivo")["cantidad"].sum()
    suma_actual = df_periodo_actual.groupby("motivo")["cantidad"].sum()

    motivos = set(suma_anterior.index.tolist() + suma_actual.index.tolist())
    resultados = []

    for motivo in motivos:
        real = suma_anterior.get(motivo, 0.0)
        pred = suma_actual.get(motivo, 0.0)
        resultados.append(Prediccion(motivo=motivo, cantidad_real=real, cantidad_predicha=pred))

    print(f"[✅ OUTPUT] Predicciones retornadas:")
    for res in resultados:
        print(res)

    return resultados
