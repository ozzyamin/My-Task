from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Patient, Doctor, Diagnosis


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')


class PatientSerializer(serializers.ModelSerializer):
    doc = DoctorSerializer(many=False)

    class Meta:
        model = Patient
        fields = ('__all__')
        validators = [
            UniqueTogetherValidator(
                queryset=Patient.objects.all(),
                fields=('__all__')
            )
        ]

    def create(self, validated_data):
        doc = Doctor.objects.get_or_create(
            name=validated_data.get('doc'.get('docName')))
        return Patient.objects.create(name=validated_data.get('docName'), Doctor=doc)

    def update(self, instance, validated_data):
        doc = validated_data.get('doc')
        if doc:
            instance.doc = Doctor.objects.get_or_create(
                name=doc.get('docName'))
        instance.docName = validated_data.get('docName', instance.docName)
        instance.save()
        return instance


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('__all__')
