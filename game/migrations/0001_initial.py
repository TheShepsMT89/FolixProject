# Generated by Django 5.0 on 2023-12-09 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_phrase', models.CharField(max_length=255, verbose_name='English phrase')),
                ('spa_phrase', models.CharField(max_length=255, verbose_name='Spanish phrase')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=36, verbose_name='Word')),
                ('trans', models.CharField(max_length=36, verbose_name='Translation of the word')),
                ('highlighted', models.BooleanField(default=False, verbose_name='Highlighted')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.exercise')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.topic')),
            ],
        ),
    ]
