# Generated by Django 4.2.16 on 2024-09-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(default='Principal', max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]