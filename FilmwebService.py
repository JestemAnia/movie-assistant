from filmweb.filmweb import Filmweb
from filmweb.filmweb import Person, Film


def filter(items, class_name):
    filtered = []
    for i in items:
        if type(i) is class_name:
            filtered.append(i)
    return filtered

class FilmwebService:

    def __init__(self):
        self.filmweb = Filmweb()

    def get_best_movie(self):
        return self.filmweb.get_popular_films()[0].url

    def get_movie_poster(self, movie_name):
        movie = filter(self.filmweb.search(movie_name), Film)[0]
        return movie.get_poster()

    def known_for(self, actor_name):
        person = self.filmweb.search(actor_name)[0]
        return person.get_info()['film_known_for']

    def get_actor_photo(self, actor_name):
        person = filter(self.filmweb.search(actor_name), Person)[0]
        return person.get_poster()
