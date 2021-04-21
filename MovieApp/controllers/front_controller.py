from controllers import movie_controller, home_controller


def route(app):
    # Calls all other other controllers
    movie_controller.route(app)
    home_controller.route(app)
