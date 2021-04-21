from flask import jsonify, request
from werkzeug.exceptions import abort

from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.movie import Movie
from services.movie_service import MovieService


def route(app):
    @app.route("/movies", methods=['GET'])
    def get_all_movies():
        return jsonify(MovieService.all_movies()), 200

    @app.route("/movies/<movie_id>", methods=['GET'])
    def get_movie(movie_id):
        try:
            movie = MovieService.get_movie_by_id(int(movie_id))
            return jsonify(movie.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/movies/search", methods=['GET'])
    def get_movie_above_price():
        price = request.args["price"]
        print(price)
        movies = MovieService.get_movie_above_price(float(price))
        return jsonify(movies)

    @app.route("/movies", methods=["POST"])
    def post_movie():
        movie = Movie.json_parse(request.json)
        movie = MovieService.create_movie(movie)
        return jsonify(movie.json()), 201

    @app.route("/movies/<movie_id>", methods=["PUT"])
    def put_movie(movie_id):
        movie = Movie.json_parse(request.json)
        movie.movie_id = int(movie_id)
        movie = MovieService.update_movie(movie)
        return jsonify(movie.json()), 200

    @app.route("/movies/<movie_id>", methods=["DELETE"])
    def del_movie(movie_id):
        MovieService.delete_movie(int(movie_id))
        return '', 204

    @app.route("/movies/<movie_id>", methods=["PATCH"])
    def patch_movie(movie_id):
        action = request.json['action']

        # if action == 'checkout':
        #     try:
        #         title = MovieService.checkout_movie(int(movie_id))
        #         return f'Successfully Checked out: {title}', 200
        #     except ResourceUnavailable as e:
        #         return e.message, 422
        # elif action == 'checkin':
        #     try:
        #         title = MovieService.checkin_movie(int(movie_id))
        #         return f"Successfully Checked in: {title}. Thank you, Come Again!", 200
        #     except ResourceUnavailable as e:
        #         return e.message, 422

        if action == 'checkin' or action == 'checkout':
            try:
                title = MovieService.checkout_movie(
                    int(movie_id)) if action == 'checkout' else MovieService.checkin_movie((int(movie_id)))
                return f"Successfully Checked {'in' if action == 'checkin' else 'out'} movie: {title}", 200
            except ResourceUnavailable as e:
                return e.message, 422
        else:
            abort(400, "Body must contain a JSON with an action property and values of checkin or checkout")
