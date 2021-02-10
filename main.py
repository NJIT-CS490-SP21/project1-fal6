import os
from flask import Flask, render_template
from spotify import get_artist, get_song, get_songs # Handles all spotify requests
from genius import get_lyric_link

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# main page
@app.route('/')
def hello_world():
    artist, name = get_artist()
    songs = get_songs(artist)
    song = get_song(songs)
    lyric_link = get_lyric_link(song["name"],name)
    return render_template("index.html", songs=songs,song = song,name = name,lyric=lyric_link)


app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)