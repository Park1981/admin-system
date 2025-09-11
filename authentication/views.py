from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from .models import Notice
from .serializers import NoticeSerializer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

def login_view(request):
    """로그인 페이지 및 로그인 처리"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '로그인에 성공했습니다.')
                return redirect('dashboard')
            else:
                messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
        else:
            messages.error(request, '아이디와 비밀번호를 입력해주세요.')
    
    return render(request, 'authentication/login.html')

def logout_view(request):
    """로그아웃 처리"""
    logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('login')

@login_required
def dashboard_view(request):
    """대시보드 페이지 (로그인 후 메인)"""
    return render(request, 'authentication/dashboard.html', {
        'user': request.user
    })


class NoticeViewSet(viewsets.ModelViewSet):
    """
    공지사항을 위한 API 뷰셋
    """
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    # 인증된 사용자는 CUD 가능, 아니면 읽기만 가능
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]