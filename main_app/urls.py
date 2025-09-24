"""
URL configuration for main_app project.

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
from accounts import views as accounts_views  # Импортируем views из accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.register_view, name='register'),  # Корень сразу ведёт на регистрацию
    path('accounts/', include('accounts.urls')),               # Авторизация, профиль и т.д.
    path('basket/', include('basket.urls')),                  # Если нужно
    path('captcha/', include('captcha.urls')),                # Если нужно
    path('tour/', include('tour.urls')),                      # Если нужно
]
