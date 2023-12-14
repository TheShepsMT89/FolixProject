# Generated by Django 5.0 on 2023-12-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='description',
            field=models.TextField(blank=True, default=None, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='example',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Ejemplo'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
    ]