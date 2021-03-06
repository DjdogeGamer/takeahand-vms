from django.db import models

class Voluntarios(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30) # t
    cpf = models.CharField(max_length=30) # t 
    funcao = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30) # t 
    telefone = models.CharField(max_length=30) # t
    horas_semanais = models.IntegerField()
    horas_contribuidas = models.IntegerField()

