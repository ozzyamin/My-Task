from django.contrib import admin
from .models import Doctor, Patient, Diagnosis


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('docName'),


class PatientAdmin(admin.ModelAdmin):
    list_display = ('patName'),


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diag'),


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
