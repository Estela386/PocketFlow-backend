from fastapi import FastAPI
from api import analisis, categorias, egreso

app = FastAPI()

app.include_router(analisis.router, prefix="/api")
app.include_router(categorias.router, prefix="/api")
app.include_router(egreso.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
