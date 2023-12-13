from django.db import models
from .model_pessoa import Pessoa

class Telefone(models.Model):
    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    numero = models.CharField(max_length=15)
    tipo = models.CharField(max_length=10)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'{self.numero} {self.tipo}'
    