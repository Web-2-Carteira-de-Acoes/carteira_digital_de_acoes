# Generated by Django 3.2.8 on 2023-01-29 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteiras', '0003_remove_carteira_acao'),
        ('carteira_acoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira_acoes',
            name='carteira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteiras.carteira'),
        ),
    ]
