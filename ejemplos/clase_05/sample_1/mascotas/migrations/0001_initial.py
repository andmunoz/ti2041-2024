# Generated by Django 5.1.1 on 2024-09-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=1)),
            ],
        ),
    ]
