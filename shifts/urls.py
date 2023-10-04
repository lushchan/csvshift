from django.urls import path
from . import views

urlpatterns = [
    path('shifts/', views.shifts, name='shifts'),
    path('', views.main, name='main'),
]