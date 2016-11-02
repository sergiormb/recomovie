# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com
from bs4 import BeautifulSoup
import requests


def get_movie_filmaffinity(id_movie):
    page = requests.get('http://www.filmaffinity.com/es/film' + str(id_movie) +'.html')
    soup = BeautifulSoup(page.content, "html.parser")
    average = soup.find("div", {"id": 'movie-rat-avg'})
    movie = {}
    if average:
        movie['average'] = float(average['content'])
    return movie


def get_average_movie_filmaffinity(title):
    page_results = requests.get('http://www.filmaffinity.com/es/search.php?stext=' + str(title))
    soup = BeautifulSoup(page_results.content, "html.parser")
    movie = soup.find("div", {"class": 'movie-card movie-card-1'})
    average = None
    if movie:
        id_movie = int(movie['data-movie-id'])
        movie = get_movie_filmaffinity(id_movie)
        if movie:
            average = movie['average']
    return average
