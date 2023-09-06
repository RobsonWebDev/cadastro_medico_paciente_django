# Generated by Django 4.2.5 on 2023-09-06 01:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
            },
        ),
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("sobrenome", models.CharField(max_length=50)),
                ("data_nascimento", models.DateField()),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("rg", models.CharField(max_length=10, unique=True)),
                ("email", models.EmailField(max_length=128)),
                ("crm", models.CharField(max_length=13, unique=True)),
                ("show", models.BooleanField(default=True)),
                (
                    "usuario",
                    models.CharField(
                        choices=[("MED", "medico"), ("PAC", "paciente")],
                        default="PAC",
                        max_length=3,
                    ),
                ),
                (
                    "data_cadastro",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cadastro.departamento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pessoa",
                "verbose_name_plural": "Pessoas",
            },
        ),
    ]
