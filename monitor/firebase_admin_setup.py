# backend/monitor/firebase_admin_setup.py
import os
import firebase_admin
from firebase_admin import credentials

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, 'firebase_credentials.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)


