from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def list_patients(request):
    patiens = Patient.objects.all()
    serializer = PatientSerializer(patiens, many=True)
    return Response(serializer.data)