"""test2pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('ping/', views.ping),
    path('pong/', views.pong),
]

#  /ping : form 태그 및 input 태그를 통해 사용자 입력을 받아 pong/으로 보내는 것