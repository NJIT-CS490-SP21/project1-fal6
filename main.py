from flask import Flask, render_template
from spotify import * # Handles all spotify requests


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# main page
@app.route('/')
def hello_world():
    artist, name = get_artist()
    songs = get_songs(artist)
    song = get_song(songs)
    return render_template("index.html", songs=songs,song = song,name = name)


app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)