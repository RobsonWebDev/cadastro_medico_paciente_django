from django.db import models
from django.utils import timezone

class Departamento(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    MEDICO = 'MED'
    PACIENTE = 'PAC'

    USUARIOS_CHOICES = [
        (MEDICO, 'medico'),
        (PACIENTE, 'paciente')
    ]
    
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField(auto_now=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=128)
    crm = models.CharField(max_length=13, unique=True, blank=True)
    show = models.BooleanField(default=True)
    usuario = models.CharField(max_length=3, choices=USUARIOS_CHOICES, default=PACIENTE)
    data_cadastro = models.DateTimeField(default=timezone.now)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default='Paciente')

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'