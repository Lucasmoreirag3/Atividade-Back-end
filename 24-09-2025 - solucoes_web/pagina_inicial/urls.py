from django.urls import path
from . import views

urlpatterns = [
    path('saudaccao/', views.saudacao, name='saudacao'),
]