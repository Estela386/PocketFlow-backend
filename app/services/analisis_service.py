from models.analisis_model import Analisis

class AnalisisService:

    def obtener_analisis(self):
        # lógica de negocio, acceso a BD o procesamiento
        return [Analisis(id=1, nombre="Análisis X", resultado="Positivo")]
