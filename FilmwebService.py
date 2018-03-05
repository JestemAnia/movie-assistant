from filmweb.filmweb import Filmweb


class FilmwebService:

    def __init__(self):
        self.filmweb = Filmweb()

    def get_best_movie(self):
        return self.filmweb.get_popular_films()[0].url

    def get_movie_poster(self, movie_name):
        movie = self.filmweb.search(movie_name)[0]
        return movie.get_poster()
