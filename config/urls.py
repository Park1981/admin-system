"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    """루트 URL에서 로그인 페이지로 리다이렉트"""
    return redirect('login')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', root_redirect, name='root'),
    path('auth/', include('authentication.urls')), # 기존 인증 URL
    path('api/', include('authentication.urls')), # API URL 추가
]
