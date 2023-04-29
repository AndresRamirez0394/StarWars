import requests

def list_movies():
    movie_url = "https://swapi.dev/api/films/"
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    sorted_movies = sorted(movies, key=lambda x: x['id'], reverse=False)
    return sorted_movies

def movie_characters(movie_id):
    movie_url = f'https://swapi.dev/api/films/{movie_id}/'
    movie_data = requests.get(movie_url).json()
    characters = [character["name"] for character in movie_data["characters"]]
    return characters
