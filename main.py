import os
from flask import Flask, render_template, request, redirect, url_for
from spotify import get_artist, get_song, get_songs # Handles all spotify requests
from genius import get_lyric_link, get_artist_info

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# main page
@app.route('/<name>')
def hello_world(name):
    artist, name = get_artist()
    songs = get_songs(artist)
    song = get_song(songs)
    lyric_link = get_lyric_link(song["name"],name)
    info = get_artist_info(name)
    return render_template(
        "index.html", songs=songs,
        song = song,name = name,
        lyric=lyric_link,info=info)

@app.route('/', methods=['POST','GET'])
def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        print(text)
        return redirect(url_for('hello_world',name=text))
    return render_template("search.html")

app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)