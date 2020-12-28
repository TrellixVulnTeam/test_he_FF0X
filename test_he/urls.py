#from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test1/', include('test1.urls')),
]
