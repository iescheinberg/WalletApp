from django.db import models

# Create your models here.
class Usuario(models.Model):
    dni = models.IntegerField()