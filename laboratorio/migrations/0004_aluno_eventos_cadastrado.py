# Generated by Django 2.2.1 on 2019-05-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_professor_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='eventos_cadastrado',
            field=models.ManyToManyField(to='laboratorio.Evento'),
        ),
    ]
