from django.db import models

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    texto = models.TextField(max_length=2000)