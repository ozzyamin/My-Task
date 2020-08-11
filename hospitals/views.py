from django.http import HttpResponse
from django.shortcuts import render
from .models import Patient, Doctor, Diagnosis
from rest_framework import viewsets
from .serializers import PatientSerializer, DoctorSerializer, DiagnosisSerializer


def index(request):
    patients = Patient.objects.all()
    return render(request, 'hospitals\index.html', {'patients': patients})


def detail(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, 'hospitals\detail.html', {'patient': patient})


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DiagnosisView(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
