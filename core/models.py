from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")

    def __str__(self):
        return self.name


class Subtopic(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(default=None, blank=True, verbose_name="Descripción")
    example = models.CharField(
        default=None, blank=True, max_length=255, verbose_name="Ejemplo"
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
