from django.views.generic import TemplateView
from firebase_config import get_announcements
import logging
import os
from django.conf import settings

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            announcements = get_announcements()
            # 각 announcement에 file_link 키 추가
            for ann in announcements:
                ann['file_link'] = ann.get('공고파일 링크', '#')
            # logger.info(f"View에서 받은 announcements 데이터: {announcements}")
            context['announcements'] = announcements
        except Exception as e:
            logger.error(f"View에서 데이터 처리 중 오류 발생: {str(e)}")
            context['announcements'] = []

        # 광고 이미지 리스트 추가
        ad_dir = os.path.join(getattr(settings, 'STATIC_ROOT', None) or settings.STATICFILES_DIRS[0], 'asset/ad')
        ad_images = []
        if os.path.exists(ad_dir):
            for fname in sorted(os.listdir(ad_dir)):
                if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    ad_images.append(f'asset/ad/{fname}')
        context['ad_images'] = ad_images
        return context 