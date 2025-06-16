import firebase_admin
from firebase_admin import credentials, db
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

# Firebase 초기화
try:
    cred = credentials.Certificate('firebase-credentials.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://jiwonq-68dbb-default-rtdb.firebaseio.com'
    })
    logger.info("Firebase 초기화 성공")
except Exception as e:
    logger.error(f"Firebase 초기화 실패: {str(e)}")
    raise

def parse_date(date_str):
    """여러 날짜 포맷을 지원하는 robust 파서"""
    for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d', '%Y.%m/%d', '%Y/%m.%d'):
        try:
            return datetime.strptime(date_str, fmt)
        except Exception:
            continue
    return datetime.min  # 파싱 실패시 가장 오래된 날짜로 처리

def get_announcements():
    """공고 데이터를 가져오는 함수"""
    try:
        ref = db.reference('/announcements')
        logger.info("Firebase reference 생성 성공")
        
        # 데이터 구조 확인을 위한 로깅
        logger.info("Firebase 데이터베이스 경로: /announcements")
        
        announcements = ref.get()
        logger.info(f"Firebase에서 가져온 원본 데이터 타입: {type(announcements)}")
        # logger.info(f"Firebase에서 가져온 원본 데이터: {announcements}")
        
        if announcements:
            # 딕셔너리를 리스트로 변환
            announcements_list = [value for value in announcements.values()]
            # logger.info(f"리스트로 변환된 데이터: {announcements_list}")
            
            # robust 정렬
            announcements_list.sort(
                key=lambda x: parse_date(str(x.get('공고일', ''))),
                reverse=True
            )
            # logger.info(f"정렬된 데이터: {announcements_list}")
            
            return announcements_list
        else:
            logger.warning("Firebase에서 데이터를 가져오지 못했습니다.")
            return []
    except Exception as e:
        logger.error(f"Firebase 데이터 가져오기 실패: {str(e)}")
        return [] 