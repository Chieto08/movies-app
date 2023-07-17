from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies': [
        {
            'id': 1,
            'title': 'Witcher',
            'year': 2023
        },
        {
            'id': 2,
            'title': 'Ginny and Georgia',
            'year': 2022
        },
        {
            'id': 3,
            'title': 'Barbie',
            'year': 2023
        },
    ]
}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Hello homepage")
