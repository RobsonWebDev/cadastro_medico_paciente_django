from django.db import models
from .model_pessoa import Pessoa

class Credencial(models.Model):
    class Meta:
        verbose_name= "Credencial"
        verbose_name_plural= "Credenciais"

    registro = models.CharField(max_length=12 , unique=True)
    data_de_inscricao = models.DateField(auto_now=False)
    especialidade = models.CharField(max_length=50)
    situacao = models.CharField(max_length=10)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'{self.regitro} {self.especialidade} {self.situacao} {self.id_pessoa}'