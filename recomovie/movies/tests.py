# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com

from django.test import TestCase
from recomovie.movies.themoviedb import TheMovieDbApi
from recomovie.movies.imdb import get_movie_imdb
from recomovie.movies.filmaffinity import get_average_movie_filmaffinity


class TheMovieDbTest(TestCase):
    """Comprobamos que la API de TheMovieDb funciona correctamente."""

    def test_len_random_top_250(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        size = 4
        themoviedb = TheMovieDbApi()
        list_movies = themoviedb.get_random_top_250(size)
        self.assertEqual(len(list_movies), size)

    def test_repeat_random_top(self):
        u"""Prueba de que no exista ninguna pelicula.

        repetida en la lista aleatoria de peliculas.
        """
        size = 4
        themoviedb = TheMovieDbApi()
        list_movies = themoviedb.get_random_top_250(size)
        list_titles = []
        for movie in list_movies:
            if movie.title not in list_titles:
                list_titles.append(movie.title)
        self.assertEqual(size, len(list_titles))


class ImdbTest(TestCase):
    """Comprobamos que la API de imdb funciona correctamente."""

    def test_imdb_api(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        movie_average = get_movie_imdb('tt0137523')
        assert float(movie_average['imdb_rating'])


class FilmaffinityTest(TestCase):
    """Comprobamos que la API de imdb funciona correctamente."""

    def test_filmaffinity_api(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        average = get_average_movie_filmaffinity('Batman')
        assert float(average)
