from rest_framework import serializers
from receitas.models import Recipe

class RecipeSerializers(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = '__all__'
	
