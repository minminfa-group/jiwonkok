"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .views import IndexView

class AdminTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'

urlpatterns = [
    # 메인 페이지
    path('', IndexView.as_view(), name='main'),
    
    # Django 기본 관리자 페이지
    path('django-admin/', admin.site.urls),
    
    # 관리자 로그인/로그아웃
    path('admin/login/', LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    path('admin/logout/', LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    
    # 커스텀 관리자 페이지 (로그인 필요)
    path('admin/', AdminTemplateView.as_view(template_name='dashboard/index.html'), name='admin_dashboard'),
    path('admin/advertisement/', AdminTemplateView.as_view(template_name='dashboard/advertisement.html'), name='admin_advertisement'),
    path('admin/content/', AdminTemplateView.as_view(template_name='dashboard/content.html'), name='admin_content'),
    path('admin/users/', AdminTemplateView.as_view(template_name='dashboard/users.html'), name='admin_users'),
    path('admin/revenue/', AdminTemplateView.as_view(template_name='dashboard/revenue.html'), name='admin_revenue'),
    path('admin/settings/', AdminTemplateView.as_view(template_name='dashboard/settings.html'), name='admin_settings'),
    path('admin/analytics/', AdminTemplateView.as_view(template_name='dashboard/analytics.html'), name='admin_analytics'),
    path('admin/system/', AdminTemplateView.as_view(template_name='dashboard/system.html'), name='admin_system'),
]
