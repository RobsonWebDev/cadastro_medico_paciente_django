from django.db import models
from .model_pessoa import Pessoa

class Endereco(models.Model):
    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'

    rua = models.CharField(max_length=30, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'{self.cidade} {self.uf} {self.id_pessoa}'