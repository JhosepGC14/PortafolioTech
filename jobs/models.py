from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.TextField()


class Paradigma(models.Model):
    codigo = models.CharField(max_length=50)


class Lenguaje(models.Model):
    nombre = models.CharField(max_length=50)
    paradigma = models.ForeignKey(Paradigma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    lenguaje = models.ManyToManyField(Lenguaje)

    def __str__(self):
        return self.nombre

# Create your models here.
