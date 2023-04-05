from src.models import Movie
from src.models import db


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return Movie.query.all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return Movie.query.filter_by(movie_id=movie_id).all()

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_mov = Movie(title=title, director=director, rating=rating)
        return db.session.add(new_mov)

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return Movie.title.like(title=title)


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
