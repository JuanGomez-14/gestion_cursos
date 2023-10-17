from django.db import models


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
