from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

#GET /api/patiens => Listar
#POST /api/patiens => Crear
#GET /api/patiens/<id> => Lista a Detalle
#PUT /api/patiens/<id> => Modificacion

# @api_view(["GET","POST"])
# def list_patients(request):
#     if request.method == 'GET':
#         patiens = Patient.objects.all()
#         serializer = PatientSerializer(patiens, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)

class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET","POST","HEAD","OPTIONS"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


# @api_view(["GET","PUT","DELETE"])
# def detail_patients(request, id):
#     try:
#         patient = Patient.objects.get(id=id)
#     except Patient.DoesNotExist:
#         return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_202_ACCEPTED)
    
#     if request.method == 'DELETE':
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET","PUT","DELETE","HEAD","OPTIONS"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

