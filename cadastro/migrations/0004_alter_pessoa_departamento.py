# Generated by Django 4.2.5 on 2023-09-06 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0003_alter_pessoa_crm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pessoa",
            name="departamento",
            field=models.ForeignKey(
                default="PAC",
                on_delete=django.db.models.deletion.CASCADE,
                to="cadastro.departamento",
            ),
        ),
    ]
