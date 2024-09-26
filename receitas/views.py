from django.shortcuts import render
from rest_framework import viewsets
from receitas.models import Recipe
from .serializer import RecipeSerializers
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
	'''Exibir todas as tarefas'''
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializers