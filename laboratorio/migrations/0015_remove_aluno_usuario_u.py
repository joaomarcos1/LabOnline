# Generated by Django 2.2.1 on 2019-05-29 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0014_auto_20190528_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='usuario_u',
        ),
    ]
