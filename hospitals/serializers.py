from rest_framework import serializers
from .models import Patient, Doctor, Diagnosis


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'docName', 'userName')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'url', 'patName', 'userName', 'doc')


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'url', 'diagType', 'pat')
