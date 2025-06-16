import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings
import os

def initialize_firebase():
    """Firebase 초기화 함수"""
    try:
        # Firebase 서비스 계정 키 파일 경로
        cred = credentials.Certificate(
            os.path.join(settings.BASE_DIR, 'firebase-credentials.json')
        )
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as e:
        print(f"Firebase 초기화 중 오류 발생: {e}")
        return None

# Firebase 클라이언트 인스턴스
db = initialize_firebase() 