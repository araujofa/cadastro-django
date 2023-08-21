from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)