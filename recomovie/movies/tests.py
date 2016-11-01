# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com

from django.test import TestCase
from recomovie.movies.themoviedb import TheMovieDbApi
from recomovie.movies.imdb import get_average_imdb


class TheMovieDbTest(TestCase):
    """Comprobamos que la API de TheMovieDb funciona correctamente."""

    def setUp(self):
        """Establece la longitud de la lista aleatoria de peliculas."""
        self.len = 6

    def tearDown(self):
        """Borra la longitud de la lista."""
        del self.len

    def test_len_random_top(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        themoviedb = TheMovieDbApi()
        list_movies = themoviedb.get_random_top_250(self.len)
        self.assertEqual(len(list_movies), self.len)

    def test_repeat_random_top(self):
        u"""Prueba de que no exista ninguna pelicula.

        repetida en la lista aleatoria de peliculas.
        """
        themoviedb = TheMovieDbApi()
        list_titles = []
        list_movies = themoviedb.get_random_top_250(self.len)
        for movie in list_movies:
            list_titles.append(movie.title)
        self.assertEqual(len(list_movies), len(set(list_titles)))


class ImdbTest(TestCase):
    """Comprobamos que la API de imdb funciona correctamente."""

    def test_imdb_api(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        movie_average = get_average_imdb('tt0137523')
        assert float(movie_average)
