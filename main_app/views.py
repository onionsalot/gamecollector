from django.shortcuts import render, redirect
from django.http import HttpResponse   
from .models import Game, Store
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ReviewForm



def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  stores_game_not_in = Store.objects.exclude(id__in = game.stores.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'games/detail.html', { 'game': game, 'review_form': review_form, 'stores': stores_game_not_in})

# Create your views here.
def home(request):
    return redirect('/games')

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

def assoc_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.add(store_id)
    return redirect('detail', game_id=game_id)

def assoc_store_delete(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.remove(store_id)
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