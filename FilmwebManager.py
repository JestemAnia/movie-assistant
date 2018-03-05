from filmweb.filmweb import Filmweb

class FilmwebManager:

    def __init__(self):
        self.filmweb = Filmweb()

    def get_best_movie(self):
        return self.filmweb.get_popular_films()[0]
