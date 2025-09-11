#!/usr/bin/env python
"""
관리자 계정을 자동으로 생성하는 스크립트
"""
import os
import sys
import django

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    """관리자 계정 생성"""
    username = 'admin'
    email = 'admin@unitech.co.kr'
    password = 'unitech2025!'
    
    if User.objects.filter(username=username).exists():
        print(f"관리자 계정 '{username}'이 이미 존재합니다.")
        user = User.objects.get(username=username)
    else:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"관리자 계정이 생성되었습니다:")
        print(f"  아이디: {username}")
        print(f"  이메일: {email}")
        print(f"  비밀번호: {password}")
    
    return user

if __name__ == '__main__':
    try:
        admin_user = create_admin()
        print("관리자 계정 준비 완료!")
    except Exception as e:
        print(f"에러 발생: {e}")
        sys.exit(1)