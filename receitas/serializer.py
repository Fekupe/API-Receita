from rest_framework import serializers
from receitas.models import Recipe
from datetime import date

class RecipeSerializers(serializers.ModelSerializer):
	datacriacao = serializers.SerializerMethodField()

	class Meta:
		model = Recipe
		fields = '__all__'

	def get_datacriacao(self, obj):
		return obj.datacriacao.date()

class CategoriaSerializers(serializers.ModelSerializer):
	categoria = serializers.SerializerMethodField()

	def  get_categoria(self, obj):
		return obj.categoria

	class Meta: 
		model = Recipe
		fields = ['categoria']