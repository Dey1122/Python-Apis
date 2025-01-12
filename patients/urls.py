from django.contrib import admin
from django.urls import path

from .views import list_patients,detail_patients

urlpatterns = [
    path('patients/', list_patients),
    path('patients/<int:id>/', detail_patients),
]
