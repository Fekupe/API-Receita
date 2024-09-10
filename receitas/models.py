from django.db import models

# Create your models here.
class User (models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False, unique=True)

class Category (models.Model):
    classificacao = models.CharField(max_length=80)

class Recipe (models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=False, null=False)
    ingredientes = models.TextField(blank=False, null=False)
    modopreparo = models.TextField(blank=False, null=False)
    tempopreparo = models.DurationField(blank=False, null=False)
    categoria = models.CharField(max_length=80)
    autor = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    datacriacao = models.DateTimeField(blank=False, null=False)
    publi_priva = models.BooleanField(null=False)

class Rating (models.Model):
    receita = models.ForeignKey(Recipe, blank=False, null=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,blank=False, null=False, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)