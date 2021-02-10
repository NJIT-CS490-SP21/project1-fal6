from dotenv import load_dotenv, find_dotenv
from unidecode import unidecode
import requests, os

load_dotenv(find_dotenv()) # Loads API keys
genius_token = os.getenv("GEN_TOKEN")

search_url='https://api.genius.com/search'

headers = {
    'Authorization': f'Bearer {genius_token}'
} # header for all requests

def get_lyric_link(song_name,artist_name):
    if "(with" in song_name:
        song_name = song_name[:song_name.index("(with")-1]
    data = {'q': song_name+' by '+artist_name}
    response = requests.get(search_url,headers=headers,data=data)
    response_json = response.json()
    for result in response_json["response"]["hits"]:
        if unidecode(artist_name.lower()) in unidecode(result["result"]["primary_artist"]["name"].lower()):
            return result["result"]["url"]
    print(response_json["response"]["hits"])
    return None
    