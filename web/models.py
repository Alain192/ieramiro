from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=8, unique=True)
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.user.get_full_name()

class BeckResultado(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    nivel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.paciente.username} - {self.nivel} ({self.puntuacion})"