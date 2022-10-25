# TODO: Feature 3
from app import app, movie_repository
from src.models.movie import Movie

def test_get_movies_by_title_page():
    client = app.test_client()

    response = client.get("/movies/search", data={
        "name": "Pokemon",
        "director": "Satoshi",
        "rating": "5 Stars",
    })

    movie = movie_repository.get_movie_by_title("Pokemon")
    confirm_movie = Movie("Pokemon", "Satoshi", 5)
    
    assert movie.title == confirm_movie.title
    assert movie.director == confirm_movie.director
    assert movie.rating == confirm_movie.rating