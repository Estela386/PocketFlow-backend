from fastapi import APIRouter
from app.services.analisis_service import AnalisisService

router = APIRouter()
analisis_service = AnalisisService()

@router.get("/analisis/")
def get_analisis():
    return analisis_service.obtener_analisis()
