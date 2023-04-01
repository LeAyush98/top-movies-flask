import requests

API_KEY = "173589bc6018a70cc128cebac4111119"

IMAGE_URL = "https://image.tmdb.org/t/p/w500"

params_search = {
    "api_key" : API_KEY,
    "query" : "captain america"
}

params_details = {
    "api_key" : API_KEY
}



def search():
    URL = "https://api.themoviedb.org/3/search/movie"
    response = requests.get(url=URL, params=params_search)
    data = response.json()["results"]
    return data

def get_details(id):
    URL = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(url=URL , params=params_details)
    data = response.json()
    return data

print(get_details(13995))