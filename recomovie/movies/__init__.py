#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2015 email: sergiormb88@gmail.com


class Movie(object):

    def __init__(
                self,
                title=None,
                netflix=False,
                imdb_id=None,
                description=None,
                poster=None,
                trailer=None,
                themoviedb_average=None,
                images=[]
                ):

        self.title = title
        self.description = description
        self.poster = poster
        self.trailer = trailer
        self.themoviedb_average = themoviedb_average
        self.images = images
        self.netflix = netflix
        self.imdb_id = imdb_id
        super(Movie, self).__init__()
