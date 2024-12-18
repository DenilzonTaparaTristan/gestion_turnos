# Generated by Django 5.0.1 on 2024-12-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=255),
        ),
        migrations.AddField(
            model_name='paciente',
            name='dni',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]