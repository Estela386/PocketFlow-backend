import uuid
from firebase_admin import db
from fastapi import HTTPException
from passlib.context import CryptContext
from app.models.registro_model import RegistroResponse, RegistroRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_usuario(data: RegistroRequest) -> RegistroResponse:
    ref = db.reference("usuarios")  # Nodo raíz para usuarios
    usuarios = ref.get() or {}

    # Verificar si el correo ya existe
    if any(usuario["correo"] == data.correo for usuario in usuarios.values()):
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    uid = str(uuid.uuid4())  # UID único
    hashed_password = pwd_context.hash(data.contrasena)

    usuario_data = {
        "nombre": data.nombre,
        "correo": data.correo,
        "contrasena": hashed_password,
        "fecha_nacimiento": data.fecha_nacimiento.isoformat()  # Guardar como string ISO
    }

    ref.child(uid).set(usuario_data)

    return RegistroResponse(mensaje="Usuario registrado correctamente", correo=data.correo)
