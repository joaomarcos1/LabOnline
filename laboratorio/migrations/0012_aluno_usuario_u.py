# Generated by Django 2.2.1 on 2019-05-29 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratorio', '0011_auto_20190513_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='usuario_u',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
