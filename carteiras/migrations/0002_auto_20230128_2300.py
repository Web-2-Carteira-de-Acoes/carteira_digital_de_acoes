# Generated by Django 3.2.8 on 2023-01-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0003_auto_20221211_2041'),
        ('carteiras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteira',
            name='acao',
        ),
        migrations.AddField(
            model_name='carteira',
            name='acao',
            field=models.ManyToManyField(to='acoes.Acoes'),
        ),
    ]