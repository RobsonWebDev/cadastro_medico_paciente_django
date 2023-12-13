from django.db import models

class Departamento(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    