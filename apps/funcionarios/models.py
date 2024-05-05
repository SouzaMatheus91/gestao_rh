from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
