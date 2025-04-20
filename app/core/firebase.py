from firebase_admin import credentials, initialize_app, db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, "credentials", "pocket-flow-827cf-firebase-adminsdk-fbsvc-e165323ed2.json")

cred = credentials.Certificate(cred_path)
initialize_app(cred, {
    'databaseURL': 'https://pocket-flow-827cf-default-rtdb.firebaseio.com/'
})
