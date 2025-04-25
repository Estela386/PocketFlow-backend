from app.core.firebase import db
import bcrypt
from fastapi import HTTPException

def actualizar_correo(uid: str, nuevo_correo: str):
    ref = db.reference(f"usuarios/{uid}")
    usuario = ref.get()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    ref.update({"correo": nuevo_correo})


def actualizar_contrasena(uid: str, contrasena_actual: str, nueva_contrasena: str):
    ref = db.reference(f"usuarios/{uid}")
    usuario = ref.get()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    contrasena_guardada = usuario.get("contrasena")
    if not contrasena_guardada or not bcrypt.checkpw(contrasena_actual.encode(), contrasena_guardada.encode()):
        raise HTTPException(status_code=401, detail="La contraseña actual es incorrecta")

    nueva_contrasena_hashed = bcrypt.hashpw(nueva_contrasena.encode(), bcrypt.gensalt()).decode()
    ref.update({"contrasena": nueva_contrasena_hashed})

def obtener_correo(uid: str) -> str:
    ref = db.reference(f"usuarios/{uid}")
    usuario = ref.get()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    correo = usuario.get("correo")
    if not correo:
        raise HTTPException(status_code=404, detail="El usuario no tiene un correo registrado")

    return correo
