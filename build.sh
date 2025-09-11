#!/usr/bin/env bash
# Render 배포 스크립트

set -o errexit  # 에러 발생시 스크립트 중단

# 의존성 설치
pip install -r requirements.txt

# 정적 파일 수집
python manage.py collectstatic --clear --no-input

# 데이터베이스 마이그레이션
python manage.py migrate

# 관리자 계정 생성 (이미 있으면 스킵)
python create_admin.py