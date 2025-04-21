from app.core.firebase import db
import bcrypt
from fastapi import HTTPException
from app.models.login_model import LoginResponse, LoginRequest

def login_usuario(login_data: LoginRequest) -> LoginResponse:
    ref = db.reference("usuarios")
    usuarios = ref.get()

    if not usuarios:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados")

    for uid, datos in usuarios.items():
        if datos.get("correo") == login_data.correo:
            contrasena_db = datos.get("contrasena")
            if contrasena_db and bcrypt.checkpw(login_data.contrasena.encode(), contrasena_db.encode()):
                return LoginResponse(uid=uid, nombre=datos.get("nombre"))
            else:
                raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    raise HTTPException(status_code=404, detail="Usuario no encontrado")
