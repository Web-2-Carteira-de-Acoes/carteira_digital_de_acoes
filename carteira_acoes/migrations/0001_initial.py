# Generated by Django 3.2.8 on 2023-01-29 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carteiras', '0003_remove_carteira_acao'),
        ('acoes', '0005_delete_carteira_acoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira_Acoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acoes.acoes')),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carteiras.carteira')),
            ],
        ),
    ]