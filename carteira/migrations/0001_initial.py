# Generated by Django 3.2.8 on 2022-10-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('acao', models.CharField(max_length=200)),
                ('historico', models.CharField(max_length=200)),
            ],
        ),
    ]
