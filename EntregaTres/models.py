from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publicacion(models.Model):
    Tipo_Categoria = [
        ("Alienigenas","Alienigenas"),
        ("Reptilianos","Reptilianos"),
        ("Teorias","Teorias Conspirativas"), 
    ]
    Titulo = models.TextField(max_length=30)
    Categorias= models.CharField(max_length=60)
    Topico = models.CharField(max_length=30, choices=Tipo_Categoria)
    Descripccion_Posteo = models.TextField(max_length=500)
    Autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Autor")
    Imagen = models.ImageField(upload_to="Publicaciones")
    Creado_El = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.id} | TITULO: {self.Titulo} | TOPICO: {self.Topico} | CREADO EL: {self.Creado_El}"

class Perfil(models.Model):
    nombre = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="Perfil")
    apellido = models.TextField(max_length=100)
    edad = models.IntegerField()
    Imagen = models.ImageField(upload_to="Perfil")

    def __str__(self):
        return f"NOMBRE: {self.nombre} | Apellido: {self.apellido} | EDAD: {self.edad}"

class Mensajes(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")

    def __str__(self):
        return f"ENVIADO POR: {self.email} | MENSAJE: {self.mensaje}"