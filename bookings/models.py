from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.
class Apointment(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='appointments', on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor, related_name='appointments', on_delete=models.CASCADE
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=10)

class MedicalNote(models.Model):
    appointment = models.ForeignKey(
        Apointment, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
    