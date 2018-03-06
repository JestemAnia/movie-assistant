from FilmwebService import FilmwebService
from Response import Response

class RequestHandler:

    def __init__(self):
        self.filmweb_service = FilmwebService()


    def handle_request(self, request):
        action = request['result']['action']
        if action == 'movie.best':
            return Response(self.filmweb_service.get_best_movie(), request)
        elif action == 'movie.poster':
            return Response(self.filmweb_service.get_movie_poster(request['result']['resolvedQuery']), request)