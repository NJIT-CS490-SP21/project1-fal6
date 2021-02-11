from dotenv import load_dotenv, find_dotenv
from unidecode import unidecode #To remove tildes and such
import requests, os

load_dotenv(find_dotenv()) # Loads API keys
genius_token = os.getenv("GEN_TOKEN")

url='https://api.genius.com/'

headers = {
    'Authorization': f'Bearer {genius_token}'
} # header for all requests

def get_lyric_link(song_name,artist_name):
    '''
    Returns a url and user id for the lyrics of a given song
    '''
    if "(with" in song_name: #Cleans songs with colabs for easier search
        song_name = song_name[:song_name.index("(with")-1]

    data = {'q': song_name+' by '+artist_name}
    response = requests.get(url+'search',headers=headers,data=data)
    response_json = response.json()
    
    for result in response_json["response"]["hits"]: #For each result
        if unidecode(artist_name.lower()) in unidecode(result["result"]["primary_artist"]["name"].lower()): # If the artists matches
            return result["result"]["url"] # Return the link
    
    song = response_json["response"]["hits"][0]["result"]
    return song["url"]
