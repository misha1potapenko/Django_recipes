from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from . import models


def home(request):
  recipes = models.Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, 'recipesapp/home.html', context)


def about(request):
  return render(request, 'recipesapp/about.html', {'title': 'about page'})