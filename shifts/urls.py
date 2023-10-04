from django.urls import path
from . import views

urlpatterns = [
    path('shifts/', views.shifts, name='shifts'),
]