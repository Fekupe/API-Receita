from django.contrib import admin
from receitas.models import Recipe
# Register your models here.

class Recipes(admin.ModelAdmin):
    list_display =['titulo', 'descricao', 'autor', 'datacriacao', 'categoria']
    list_display_links = ['titulo']
    search_fields = ['titulo', 'autor','datacriacao']
    
admin.site.register(Recipe, Recipes)