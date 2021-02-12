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

def get_artist_info(artist_name):
    '''
    Returns information about the artist
    '''
    
    search_url = url+'search'
    data = {"q":artist_name}
    response = requests.get(search_url,data=data,headers=headers)
    response_json = response.json()
    artist_id = None
    for artist in response_json["response"]["hits"]:
        if unidecode(artist["result"]["primary_artist"]["name"].lower()) == unidecode(artist_name.lower()):
            artist_id = artist["result"]["primary_artist"]["id"]
            break
    info_url = url+'artists/'+str(artist_id)
    data = "text_format=html"
    response = requests.get(info_url+'?'+data,headers=headers)
    response_json = response.json()
    if response_json["meta"]["status"]==404:
        return "<p>Sorry, no info</p>"
    info=response_json["response"]["artist"]["description"]["html"]
    return info
