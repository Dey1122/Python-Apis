from django.contrib import admin
from django.urls import path

# from .views import list_patients,detail_patients
from .views import ListPatientsView, DetailPatientView

urlpatterns = [
    # path('patients/', list_patients),
    # path('patients/<int:id>/', detail_patients),
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:id>/', DetailPatientView.as_view()),
]
