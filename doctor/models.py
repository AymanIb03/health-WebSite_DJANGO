from django.db import models
from django.http import request
from django.contrib.auth.models import AbstractUser
class Service(models.Model):
    name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255,default="")  # Ajout du champ pour le nom du médecin

    def __str__(self):
        return self.name
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255) # Ajout de l'attribut pour la localisation
   # doctor=

    def __str__(self):
        return self.name

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]



