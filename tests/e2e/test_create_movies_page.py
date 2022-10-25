# TODO: Feature 2
from app import app, movie_repository
from src.models.movie import Movie

def test_create_movies_page():
    client = app.test_client()

    response = client.post("/movies", data={
        "name": "Flask",
        "director": "Python",
        "rating": 5
    })

    movie = movie_repository.get_movie_by_title("Flask")
    confirm_movie = Movie("Flask", "Python", 5)
    
    assert movie.director == confirm_movie.director