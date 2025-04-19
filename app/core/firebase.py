import firebase_admin
from firebase_admin import credentials, db

# Ruta a tu archivo de credenciales descargado desde Firebase
cred = credentials.Certificate("pocket-flow-827cf-firebase-adminsdk-fbsvc-aaa30269cf.json")

# URL de tu Realtime Database (la puedes sacar desde la consola de Firebase)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://pocket-flow-827cf-default-rtdb.firebaseio.com/"
})