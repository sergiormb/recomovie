#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from recomovie.movies import get_list_movies

# Create your views here.
def home(request):
    list_movies = get_list_movies(6)
    return render(request, 'index.html', {'list_movies': list_movies})
