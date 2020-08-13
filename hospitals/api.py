from .models import Patient, Doctor, Diagnosis
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer, PatientSerializer, DiagnosisSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DiagnosisSerializer
