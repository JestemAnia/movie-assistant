from FilmwebService import FilmwebService

class RequestHandler:

    def __init__(self):
        self.filmweb_service = FilmwebService()


    def handle_request(self, request):
        action = request['result']['action']
        if action == 'movie.best':
            return self.filmweb_service.get_best_movie()
        elif action == 'movie.poster':
            return self.filmweb_service.get_movie_poster(request['result']['resolvedQuery'])