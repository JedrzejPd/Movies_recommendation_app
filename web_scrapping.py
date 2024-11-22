import requests
import json

base_url = "https://www.filmweb.pl/api/v1/film"

movies = []

def get_movie_data(movie_id):
    url = f"{base_url}/{movie_id}/preview"
    response = requests.get(url, headers={'referer': 'https://www.filmweb.pl/films/search', 'x-locale' : 'pl'})
    movie_data = response.json()
    return movie_data


for movie_id in range(1):

    movie_data = get_movie_data(movie_id+1)

    movies[movie_id] = {
        "title" : movie_data["title"]["title"],
        "year" : movie_data["year"],
        "synopsis" : movie_data["plotOrDescriptionSynopsis"]
    }

print(movies)

# json_object = json.dumps(movie_data, indent=2)

# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)




# print(movie_data["plotOrDescriptionSynopsis"])