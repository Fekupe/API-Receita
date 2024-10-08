# Generated by Django 5.1.1 on 2024-09-10 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_alter_rating_usuario_alter_recipe_autor_delete_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comentario',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='receita',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='receitas.recipe'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredientes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='modopreparo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tempopreparo',
            field=models.DurationField(blank=True),
        ),
    ]
