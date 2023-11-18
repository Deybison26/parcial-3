from django.db import models

# Create your models here.

class BDprincipal(models.Model):
    Nombre_edificio = models.CharField(max_length=100)
    Apartamento = models.CharField(max_length=80)
    Habitaciones = models.CharField(max_length=60)
    Propietario = models.CharField(max_length=60)
    Baños = models.CharField(max_length=50)

def __str__(self):
    return self.Nombre_edificio+''+self.Apartamento+''+self.Habitaciones+''+self.Propietario+''+self.Baños