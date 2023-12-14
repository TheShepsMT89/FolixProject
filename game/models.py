from django.db import models
from core.models import Topic, Subtopic


class Exercise(models.Model):
    eng_phrase = models.CharField(max_length=255, verbose_name="English phrase")
    spa_phrase = models.CharField(max_length=255, verbose_name="Spanish phrase")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exercise: {self.eng_phrase})"


class Words(models.Model):
    word = models.CharField(max_length=36, verbose_name="Word")
    trans = models.CharField(max_length=36, verbose_name="Translation of the word")
    highlighted = models.BooleanField(default=False, verbose_name="Highlighted")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Word: {self.word}, highlighted is {self.highlighted}"
