from django.urls import path, include
from .api import DoctorViewSet, PatientViewSet, DiagnosisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/Patients', PatientViewSet, 'Patient')
router.register('api/Doctor', DoctorViewSet, 'Doctor')
router.register('api/Diagnosis', DiagnosisViewSet, 'Diagnosis')

urlpatterns = router.urls
