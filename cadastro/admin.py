from django.contrib import admin
from cadastro.models import Pessoa, Departamento

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'nome', 'sobrenome', 'departamento',
    ordering = '-id',

@admin.register(Departamento)
class DepartamentoAdim(admin.ModelAdmin):
    list_display = 'id', 'nome',
    ordering = '-id',