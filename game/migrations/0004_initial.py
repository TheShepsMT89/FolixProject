# Generated by Django 5.0 on 2023-12-11 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('game', '0003_remove_words_exercise_remove_words_topic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_phrase', models.CharField(max_length=255, verbose_name='English phrase')),
                ('spa_phrase', models.CharField(max_length=255, verbose_name='Spanish phrase')),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=36, verbose_name='Word')),
                ('trans', models.CharField(max_length=36, verbose_name='Translation of the word')),
                ('highlighted', models.BooleanField(default=False, verbose_name='Highlighted')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.exercise')),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
    ]