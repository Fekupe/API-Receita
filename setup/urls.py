"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from receitas.views import RecipeViewSet, CategoriaViewSet, CategoriaRecipesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Recipe', RecipeViewSet, basename='Recipe')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include(router.urls)),  # existing URL pattern
    path('recipes/filter/', RecipeViewSet.as_view({'get': 'list'}), name='recipe-filter'),  # new URL pattern
    path('categorias/', CategoriaViewSet.as_view({'get': 'list'}), name='categoria-list'),
    path('', include(router.urls)),
    path('categorias/recipes/', CategoriaRecipesViewSet.as_view({'get': 'list'}), name='categoria-recipes'),

]
