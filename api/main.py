from fastapi import FastAPI
from requests import *
from dotenv import load_dotenv
from os import getenv

from typing import List
from pydantic import BaseModel

app = FastAPI()

app.frontend("/", directory="src")

load_dotenv()
API_KEY = getenv("API_KEY")

headers = {"Authorization": API_KEY}

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

class nameList(BaseModel):
    artists: List[str]

@app.post("/get_artist")
async def main(names_list: nameList):
    common_films_list = set()
    for artist in range(len(names_list.artists)):
        name = names_list.artists[artist]
        name = name.replace(" ", "+")
        actor_id = get_actor_id(name)
        actors_films = get_actors_films_by_id(actor_id)
        if actors_films == -1:
            return ["ERROR"]
        if artist == 0:
            common_films_list = set(actors_films)
        else:
            common_films_list &= set(actors_films)
    return list(common_films_list)