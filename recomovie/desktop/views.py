#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from recomovie.movies.themoviedb import TheMovieDbApi

# Create your views here.
def home(request):
    themoviedb = TheMovieDbApi()
    list_movies = themoviedb.get_random_top_250(6)
    return render(request, 'index.html', {'list_movies': list_movies})
