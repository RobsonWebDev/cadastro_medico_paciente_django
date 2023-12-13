from django.contrib import admin
from cadastro.models import Pessoa, Departamento, Telefone, Prontuario, Credencial, Endereco

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'nome', 'sobrenome', 'departamento',
    ordering = '-id',

@admin.register(Departamento)
class DepartamentoAdim(admin.ModelAdmin):
    list_display = 'id', 'nome',
    ordering = '-id',

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'numero', 'tipo',
    ordering = '-id',

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'proprietario', 'data_criacao',
    ordering = '-id',

@admin.register(Credencial)
class CredencialAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'especialidade', 'registro', 'situacao',
    ordering = '-id',

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'bairro', 'cidade', 'uf',
    ordering = '-id',