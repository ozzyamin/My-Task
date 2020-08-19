from django.db import models


class Doctor(models.Model):
    docName = models.CharField(max_length=500, blank=True)
    user = models.EmailField(max_length=500, unique=True, blank=True)

    def __str__(self):
        return self.docName


class Patient(models.Model):
    patName = models.CharField(max_length=500, blank=True)
    user = models.EmailField(max_length=500, unique=True, blank=True)
    doc = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, default=False, null=True)

    def __str__(self):
        return self.patName


class Diagnosis(models.Model):
    diag = models.CharField(max_length=500, blank=True)
    pat = models.ForeignKey(
        Patient, on_delete=models.CASCADE, default=False, null=True)

    def __str__(self):
        return self.diag
