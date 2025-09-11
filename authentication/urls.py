from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API 라우터 설정
router = DefaultRouter()
router.register(r'notices', views.NoticeViewSet)

urlpatterns = [
    # 기존 URL
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # API URL
    path('', include(router.urls)),
]