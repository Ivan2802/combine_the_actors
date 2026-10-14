from fastapi import FastAPI
from requests import *

app = FastAPI()

app.frontend("/", directory="src")

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwM2Y2MDc2ZjU2OWZmYWFhNjNmYjE4YWUyZDVhMzdlNSIsIm5iZiI6MTc4ODEyODY1My4zNCwic3ViIjoiNmE5NGFkOGRkNDQwMjFkMmM0MjlhMzgzIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.I4REXF0dpza3vZynsR3aVhGxBzMc1tMoVHJIwyEhhK8"}

def get_actor_id(actor_name):
    url_actor_name = f"https://api.themoviedb.org/3/search/person?query={actor_name}"
    response_actor = get(url_actor_name, headers=headers)
    if response_actor.json()['results']:
        actor_id = response_actor.json()['results'][0]['id']
        return actor_id
    else:
        return -1

def get_actors_films_by_id(actor_id):
    if actor_id == -1:
        return -1
    url_actors_films = f"https://api.themoviedb.org/3/person/{actor_id}/combined_credits"
    response_films = get(url_actors_films, headers=headers).json()['cast']

    films_list = list()
    for film in response_films:
        if film['media_type'] == 'movie': # popularity
            films_list.append(film['original_title'])
    return films_list


@app.get("/get_artist/{name1}/{name2}") # reshape path
def main(name1, name2):
    name1 = name1.replace(" ", "+")
    actor_id_1 = get_actor_id(name1)
    actors_films_1 = get_actors_films_by_id(actor_id_1)
    name2 = name2.replace(" ", "+")
    actor_id_2 = get_actor_id(name2)
    actors_films_2 = get_actors_films_by_id(actor_id_2)
    if actors_films_1 != -1 and actor_id_2 != -1:
        return list(set(actors_films_1) & set(actors_films_2))
    else:
        return ["ERROR"]