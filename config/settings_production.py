"""
Production settings for Company Hub
"""

from .settings import *
import os

# 운영환경에서는 DEBUG 비활성화
DEBUG = False

# 허용할 호스트 설정 (Render 도메인 추가)
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Render 도메인
    '.vercel.app',    # Vercel 도메인 (프론트엔드용)
]

# 보안 설정 강화
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS 설정 (Render는 자동으로 HTTPS 제공)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# 정적 파일 설정 (Render용)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 로깅 설정
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# CORS 설정 (프론트엔드 도메인 추가)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173", 
    "https://localhost:5173",
    "https://admin-system-psp5v1rkq-park1981s-projects.vercel.app", # Vercel 배포 주소
    # Vercel 도메인은 배포 후 추가
]

# 환경변수에서 추가 설정 로드
if config('RENDER_EXTERNAL_HOSTNAME', default=''):
    ALLOWED_HOSTS.append(config('RENDER_EXTERNAL_HOSTNAME'))

# 프론트엔드 URL이 환경변수에 있으면 CORS에 추가
frontend_url = config('FRONTEND_URL', default='')
if frontend_url:
    CORS_ALLOWED_ORIGINS.append(frontend_url)