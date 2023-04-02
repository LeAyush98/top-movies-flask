import requests

class MovieAPI:
    API_KEY = "173589bc6018a70cc128cebac4111119"
    IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    SEARCH_URL = "https://api.themoviedb.org/3"
    MORE_INFO_URL = "https://api.themoviedb.org/3/movie"
    params_search = {
    "api_key" : API_KEY,
    "query" : "captain america"
    }

    def __init__(self, movie_name:str) -> None:
        """Enter the movie name to search"""
        self.params_search["query"] = movie_name

    def search(self) -> list: 
        response = requests.get(url=f"{self.SEARCH_URL}/search/movie", params=self.params_search)
        data = response.json()["results"]
        return data

