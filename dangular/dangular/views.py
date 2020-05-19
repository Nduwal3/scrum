from django.http import HttpResponse
from django.shortcuts import render
from music.models import Albums


def home(request):
    return HttpResponse('Hello World')

def index(request):
    all_albums = Albums.objects.all()
    context = {
        'all_albums' : all_albums
    }
    return render(request , 'index.html', context)
