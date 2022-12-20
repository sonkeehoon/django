# 사용자가 접속하는 path에 따라 그 요청을 어떻게 처리할지 지정해주는 파일
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index),
    path('create/',views.create),
    path('read/<id>/',views.read),
    path('delete/',views.delete)
]
