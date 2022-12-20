# 사용자가 접속하는 path에 따라 그 요청을 어떻게 처리할지 지정해주는 파일
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# http://127.0.0.1/
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
