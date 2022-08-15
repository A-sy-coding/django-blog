from django.shortcuts import render
from .models import Album, Photo
from django.views.generic import ListView, DetailView

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo