from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from receitas.models import Recipe
from .serializer import RecipeSerializers, CategoriaSerializers
# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    filter_backends = [SearchFilter]
    search_fields = ['titulo', 'autor', 'categoria']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Recipe.objects.all()
	serializer_class = CategoriaSerializers
	filter_backends = [SearchFilter]
	search_fields = ['categoria']

	def get_queryset(self):
		categoria = self.request.GET.get('categoria')
		if categoria:
			return Recipe.objects.filter(categoria=categoria)
		return Recipe.objects.all