from django.urls import path
from . import views

app_name = 'Mobile'
urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.getdata, name='getdata')
]
