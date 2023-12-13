from django.db import models
from .model_departamento import Departamento
from django.utils import timezone



class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField(auto_now=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    show = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default='Paciente')

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'