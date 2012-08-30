from django.db import models

class Usuario(models.Model):
    userId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
