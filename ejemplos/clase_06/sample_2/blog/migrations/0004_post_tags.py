# Generated by Django 4.2.16 on 2024-09-30 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog.tag'),
        ),
    ]