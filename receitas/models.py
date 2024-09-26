from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    classificacao = models.CharField(max_length=80)

class Recipe (models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=False,)
    ingredientes = models.TextField(blank=True, null=False)
    modopreparo = models.TextField(blank=True, null=False)
    tempopreparo = models.DurationField(blank=True, null=False)
    categoria = models.CharField(max_length=80)
    autor = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    datacriacao = models.DateField(blank=False, null=False)
    publi_priva = models.BooleanField(null=False)#default

class Rating (models.Model):
    receita = models.ForeignKey(Recipe, blank=True, null=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,blank=True, null=False, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=255, blank=False)