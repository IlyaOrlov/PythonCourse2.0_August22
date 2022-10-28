from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Film
from .forms import FilmForm


def index(request):
    return render(request, 'coolapp/index.html')


def index2(request):
    return HttpResponse("Пока!!!")


def films(request):
    return render(request, 'coolapp/films.html', {'films': Film.objects.all()})


def new(request, film_id=None):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect(f'/{film.id}', film=film)  # http://127.0.0.1:8000/1
    if film_id:
        film = Film.objects.get(id=film_id)
    else:
        film = Film()
    return render(request, 'coolapp/new.html', {'form': FilmForm(instance=film)})
