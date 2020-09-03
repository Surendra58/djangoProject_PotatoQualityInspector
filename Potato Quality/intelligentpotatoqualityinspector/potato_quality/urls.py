# from django.conf.urls import url

from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name='index'),
]

#  It will go to index url:http://127.0.0.1:8000/cal/index/
from . import views
from django.urls import path
urlpatterns = [
    path('index/', views.index,name='index'),
]