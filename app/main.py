from fastapi import FastAPI
from app.api import analisis, registro, login, ingreso, categorias, egreso, perfil # Asegúrate de que estás corriendo desde raíz

app = FastAPI()

# Endpoints base
@app.get("/")
def root():
    return {"status": "ok", "message": "API funcionando correctamente"}

# Rutas con prefijos específicos
app.include_router(analisis.router, prefix="/api/analisis", tags=["Análisis"])
app.include_router(registro.router, prefix="/api/registro", tags=["Registro"])
app.include_router(login.router, prefix="/api/login", tags=["Login"])
app.include_router(ingreso.router, prefix="/api", tags=["Ingresos"])
app.include_router(categorias.router, prefix="/api/categorias", tags=["Categorías"])
app.include_router(egreso.router, prefix="/api", tags=["Egresos"])
app.include_router(perfil.router, prefix="/api/perfil", tags=["Perfil"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
