# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movie():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Batman", "Robin", 3)

    movie_searched = movie_repository.get_movie_by_title("Batman")
    test_movie = Movie("Batman", "Robin", 3)

    assert movie_searched.director == test_movie.director