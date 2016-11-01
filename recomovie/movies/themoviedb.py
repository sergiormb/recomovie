#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2015 email: sergiormb88@gmail.com

import random
import requests
from django.conf import settings
from recomovie.movies import Movie


def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])


class TheMovieDbApi(object):

    def __init__(self, api_key=None, locale=None, anonymize=True,
                 exclude_episodes=None, user_agent=None, cache=None,
                 proxy_uri=None, verify_ssl=None):
        super(TheMovieDbApi, self).__init__()
        self.locale = 'es_ES'
        self.caching_enabled = True
        self.anonymize = True
        # IMAGES
        self.the_movie_db_key = settings.THE_MOVIE_DB_KEY
        url = settings.THE_MOVIE_DB_CONFIG_PATTERN.format(key=self.the_movie_db_key)
        r = requests.get(url)
        config = r.json()
        if config.get('images', ''):
            self.base_url = config['images']['base_url']
            sizes = config['images']['poster_sizes']
            """
                'sizes' should be sorted in ascending order, so
                max_size = sizes[-1]
                should get the largest size as well.
            """
            self.max_size_poster = max(sizes[2:4], key=size_str_to_int)

    def get_movie_video(self, movie_id):
        response = requests.get(settings.VIDEO_URL.format(key=self.the_movie_db_key, movie_id=movie_id))
        api_response = response.json()
        results = api_response.get('results', None)
        if results:
            results = results
            video = results[0]
            return video['key']
        else:
            return None

    def get_movie_images(self, movie_id):
        response = requests.get(settings.IMG_PATTERN.format(key=self.the_movie_db_key, movie_id=movie_id))
        api_response = response.json()
        images_movie = {}
        # POSTER
        api_poster = api_response.get('posters', None)
        if api_poster:
            posters = api_poster
            poster = posters[0]
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(self.base_url, self.max_size_poster, rel_path)
            images_movie['poster'] = url
        # IMAGES
        api_backdrops = api_response.get('backdrops', None)
        if api_backdrops:
            backdrops = api_backdrops
            backdrops_urls = []
            backdrop = backdrops[0]
            rel_path = backdrop['file_path']
            width = 'w' + str(backdrop['width'])
            url = "{0}{1}{2}".format(self.base_url, width, rel_path)
            images_movie['photo'] = url
        return images_movie

    def get_movie_complete(self, movie):
        movie['images'] = self.get_movie_images(movie['id'])
        trailer = self.get_movie_video(movie['id'])
        if trailer:
            movie['trailer'] = trailer
        return movie

    def get_random_top_250(self, number=1):
        response = requests.get(settings.DISCOVER_URL.format(key=self.the_movie_db_key))
        api_response = response.json()
        results = api_response.get('results', '')
        movies = []
        if results:
            titles_movies = []
            while (len(movies) < number):
                movie_result = random.choice(results)
                movie_result = self.get_movie_complete(movie_result)
                movie = Movie(
                    title=movie_result['title'].encode("utf-8"),
                    description=movie_result['overview'].encode("utf-8"),
                    themoviedb_average=movie_result['vote_average'],
                    trailer=movie_result.get('trailer', None),
                    themoviedb_id=movie_result['id'],
                )
                if movie_result.get('images', ''):
                    movie.poster = movie_result['images']['poster']
                    movie.photo = movie_result['images']['photo']
                response = requests.get(
                    settings.MOVIE_PATTERN.format(
                        key=self.the_movie_db_key,
                        movie_id=movie.themoviedb_id
                        )
                    )
                movie_complete = response.json()
                if movie_complete.get('imdb_id', None):
                    movie.imdb_id = movie_complete['imdb_id']
                if movie.title not in titles_movies:
                    movies.append(movie)
                    titles_movies.append(movie.title)
        return movies

    def get_random_genre(self, genre):
        genre = Genre.objects.filter(name__contains=genre)
        response = requests.get(settings.GENRE_URL.format(key=self.the_movie_db_key, genre=genre[0].api_id))
        api_response = response.json()
        results = api_response['results']
        movie = random.choice(results)
        movie = self.get_movie_complete(movie)
        return movie
