# Generated by Django 4.2.2 on 2023-06-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natureapp', '0002_comentarios_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(max_length=300),
        ),
    ]
