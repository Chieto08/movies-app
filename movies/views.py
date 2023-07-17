from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie


def movies(request):
    all_movies = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': all_movies})


def home(request):
    return HttpResponse("Hello homepage")


def movie_detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')


def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exist")
    movie.delete()

    return HttpResponseRedirect("/movies")
