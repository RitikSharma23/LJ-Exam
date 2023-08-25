import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import firestore

cred = credentials.Certificate('config.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

