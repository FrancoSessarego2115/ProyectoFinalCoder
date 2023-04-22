from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publicacion(models.Model):
    Titulo = models.TextField(max_length=30)
    Categoria = models.TextField(max_length=80)
    Descripccion_Posteo = models.TextField(max_length=500)
    Autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Autor")
    Imagen = models.ImageField(upload_to="Publicaciones")

    def __str__(self):
        return f"{self.id} -- {self.Titulo} -- {self.Categoria} -- {self.Descripccion_Posteo}"

class Perfil(models.Model):
    nombre = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="Perfil")
    Imagen = models.ImageField(upload_to="Perfil")



 