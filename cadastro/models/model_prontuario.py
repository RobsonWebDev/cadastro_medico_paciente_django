from django.db import models
from .model_pessoa import Pessoa
from django.contrib.auth.models import User
from django.utils import timezone


class Prontuario(models.Model):
    class Meta:
        verbose_name = 'Prontuarios'
        verbose_name_plural = 'Prontuarios'

    arquivo = models.FileField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)
    proprietario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.proprietario} {self.data_criacao}'