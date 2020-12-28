from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'test1'

urlpatterns = [
    path('', views.test1, name='test1'),
]
