from django.shortcuts import render, redirect
from django.http import HttpResponse   
from .models import Game 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ReviewForm

# Add the Cat class & list and view function below the imports
# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# games = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  review_form = ReviewForm()
  return render(request, 'games/detail.html', { 'game': game, 'review_form': review_form})

# Create your views here.
def home(request):
    return HttpResponse('dsfdhfjkdsfhjksdjk')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games})

def add_review(request, game_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.game_id = game_id
        new_review.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['genre', 'description', 'release_year']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'