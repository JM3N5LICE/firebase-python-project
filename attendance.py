import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


def initialize_firestore():
    project_id = "attendance-eca04"

    cred = credentials.Certificate('auth.json')
    firebase_admin.initialize_app(cred, {
        'project_id': project_id,
    })

    db = firestore.client()
    return db
