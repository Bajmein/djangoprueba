from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Paisajes(models.Model):
    categoria = models.CharField(max_length=15)
    lugar = models.CharField(max_length=15)
    pais = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=300)


class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.titulo} -by {self.user.username}'