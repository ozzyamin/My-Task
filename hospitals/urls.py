from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Patients', views.PatientView)
router.register('Doctor', views.DoctorView)
router.register('Diagnosis', views.DiagnosisView)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('<int:patient_id>', views.detail, name='detail'),
]