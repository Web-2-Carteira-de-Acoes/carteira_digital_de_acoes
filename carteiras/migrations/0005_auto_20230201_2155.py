# Generated by Django 3.2.8 on 2023-02-02 00:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carteiras', '0004_carteira_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteira',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carteira',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
