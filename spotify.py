from dotenv import load_dotenv, find_dotenv
import requests, os, random

load_dotenv(find_dotenv()) # Loads API keys
spotify_id = os.getenv("SPOT_ID")
spotify_secret = os.getenv("SPOT_SECRET")

auth_url="https://accounts.spotify.com/api/token" 
artist_url="https://api.spotify.com/v1/artists/"


auth = requests.post(auth_url,
    {
        'grant_type' : 'client_credentials',
        'client_id' : spotify_id,
        'client_secret' : spotify_secret,
    }
)
auth_token = auth.json()["access_token"] # authorization token

headers = {
    'Authorization': f'Bearer {auth_token}'
} # header for all requests


def get_song(songs):
    '''
    Returns a random song from the list of top songs
    Sets null previews to Rickroll    
    '''
    song = songs[random.randint(0,len(songs)-1)]
    if not song["preview"]:
        song["preview"] = "https://p.scdn.co/mp3-preview/22bf10aff02db272f0a053dff5c0063d729df988?cid=0205bae2d141422e989258f24b431c8c"
    return song
    

def get_songs(artist):
    '''
    Returns a list of top songs given an artist
    '''
    song_response = requests.get(
        artist_url+artist+"/top-tracks"+"?market=US",
        headers=headers,
    ).json()
    songs = []
    for track in song_response["tracks"]:
        songs.append(
            {"name":track["name"],
            "id":track["id"],
            "preview":track["preview_url"],
            "image":track["album"]["images"][0]["url"],
            },
        )
    return songs
    
def get_artist():
    '''
    Returns a random artist from a list f 4 artists
    '''
    artists = ["6qqNVTkY8uBg9cP3Jd7DAH",
    "4q3ewBCX7sLwd24euuV69X",
    "7Ln80lUS6He07XvHI8qqHH",
    "2Otnykd696YidQYfEGVmNq",
    ]
    artist = artists[random.randint(0,3)]
    name=requests.get(
        artist_url+artist,
        headers=headers,
    ).json()["name"]
    return artist,name