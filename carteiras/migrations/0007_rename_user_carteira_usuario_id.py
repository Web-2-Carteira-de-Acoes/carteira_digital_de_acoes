# Generated by Django 3.2.8 on 2023-02-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carteiras', '0006_remove_carteira_historico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carteira',
            old_name='user',
            new_name='usuario_id',
        ),
    ]
