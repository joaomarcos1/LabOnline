# Generated by Django 2.2.1 on 2019-05-29 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0016_aluno_usuario_u'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='usuario_u',
        ),
    ]
