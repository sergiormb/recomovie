# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com
import BeautifulSoup
import requests


def get_average_movie_filmaffinity(title):
    page_results = requests.get('http://www.filmaffinity.com/es/search.php?stext=' + title)
    soup = BeautifulSoup.BeautifulSoup(page_results.content)
    movie = soup.find("div", {"class": 'movie-card movie-card-1'})
    if movie:
        id_film = int(movie['data-movie-id'])
        page = requests.get('http://www.filmaffinity.com/es/film' + str(id_film) +'.html')
        soup = BeautifulSoup.BeautifulSoup(page.content)
        average = soup.find("div", {"id":'movie-rat-avg'})
        if average:
            return float(average['content'])
    return None
