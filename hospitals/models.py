from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     is_patient = models.BooleanField(default=False)
#     is_doctor = models.BooleanField(default=False)
#     firstName = models.CharField(max_length=500)
#     lastName = models.CharField(max_length=500)
#     userName = models.EmailField(max_length=500)


class Doctor(models.Model):
    docName = models.CharField(max_length=500, blank = True)
    userName = models.EmailField(max_length=500)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True, default="Some String")

    def __str__(self):
        return self.docName


class Patient(models.Model):
    patName = models.CharField(max_length=500)
    userName = models.EmailField(max_length=500)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True, default="Some String")
    # doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.patName


class Diagnosis(models.Model):
    diagType = models.CharField(max_length=500)
    # pat = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.diagType
