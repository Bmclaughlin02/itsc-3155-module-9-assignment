# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_title():
    movie_repository = get_movie_repository()

    movie_searched = movie_repository.get_movie_by_title("Pokemon")
    test_movie = Movie("pokemon", "Satoshi", 5)

    assert movie_searched.title == test_movie.title
    assert movie_searched.director == test_movie.director
    assert movie_searched.rating == test_movie.rating