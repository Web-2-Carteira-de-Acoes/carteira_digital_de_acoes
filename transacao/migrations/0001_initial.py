# Generated by Django 3.2.8 on 2022-12-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.IntegerField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]
