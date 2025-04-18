import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("pocket-flow-827cf-firebase-adminsdk-fbsvc-aaa30269cf.json")
firebase_admin.initialize_app(cred)

db = firestore.client()