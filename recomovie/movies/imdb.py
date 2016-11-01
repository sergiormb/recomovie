import omdb


def get_movie_imdb(imdb_id):
    movie = omdb.imdbid(imdb_id)
    return movie
