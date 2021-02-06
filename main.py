import requests, os, random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

# main page
@app.route('/')
def hello_world():
    artist, name = get_artist()
    songs = get_songs(artist)
    song = get_song(songs)
    return render_template("index.html", songs=songs,song = song,name = name)

def get_song(songs):
    song = songs[random.randint(0,len(songs)-1)]
    return song
    

def get_songs(artist):
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

app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)