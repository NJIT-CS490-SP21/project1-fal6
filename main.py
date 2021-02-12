import os
from flask import Flask, render_template, request, redirect, url_for
from spotify import get_artist, get_song, get_songs # Handles all spotify requests
from genius import get_lyric_link, get_artist_info

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# main page
@app.route('/random/<artist_name>')
def random_song(artist_name):
    '''Displays a random song, and info from the given artist'''
    artist,name = get_artist(artist_name)
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
    '''Main page with a text box to search artists '''
    if request.method == 'POST':
        text = request.form['text']
        return redirect(url_for('random_song',artist_name=text))
    return render_template("search.html")

app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)