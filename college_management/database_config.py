
import pyrebase


config = {
    "apiKey": "AIzaSyC94VHFbwUub8_pvXc-1zw-ol9wx5a42GM",
    "authDomain": "college-management-ff38c.firebaseapp.com",
    "databaseURL": "https://college-management-ff38c-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "college-management-ff38c",
    "storageBucket": "college-management-ff38c.appspot.com",
    "messagingSenderId": "89561927335",
    "appId": "1:89561927335:web:5243caec472d98f7ff5582",
}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import firestore

cred = credentials.Certificate('config.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()