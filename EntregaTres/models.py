from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publicacion(models.Model):
    Titulo = models.TextField(max_length=30)
    Categoria = models.TextField(max_length=80)
    Descripccion_Posteo = models.TextField(max_length=500)
    Autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Autor")

    def __str__(self):
        return f"{self.id} -- {self.Titulo} -- {self.Categoria} -- {self.Descripccion_Posteo}"

class Persona(models.Model):
    nombre = models.TextField(max_length=50)
    apellido = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.id} -- {self.nombre} -- {self.apellido}"


