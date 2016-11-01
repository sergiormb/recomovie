import omdb

def get_average_imdb(imdb_id):
    movie = omdb.imdbid(imdb_id)
    return movie.imdb_rating
