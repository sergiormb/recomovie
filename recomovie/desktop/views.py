#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from recomovie.movies.imdb import ImdbApi

# Create your views here.
def home(request):
    imdb = ImdbApi()
    list_movies = imdb.get_random_top_250(6)
    return render(request, 'index.html', {'list_movies': list_movies})
