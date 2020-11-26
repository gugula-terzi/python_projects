from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('/<str:slug>', views.homework, name='homework')
]