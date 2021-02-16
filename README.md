# Music Web App
Web App written using flask as a backend as well as the Spotify and Genius API. 
You can search any artist and a random song from their top songs will be displayed as well as information about the artist, lyrics, preview and album image for the song 

## Technologies
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
* [Spotify API](https://developer.spotify.com/documentation/web-api/)
* [Genius API](https://docs.genius.com/)
* Python
* HTML
* CSS

## Requirements
```
pip install -r requirements.txt
``` 
## Setup
1. Create [Spotify](https://developer.spotify.com/documentation/web-api/) and [Genius](https://docs.genius.com/) developer accounts
2. Create a .env file in the main directory
3. Add your spotify and genius keys to .env:
```
export SPOT_ID='YOURKEY'
export SPOT_SECRET='YOURKEY'
export GEN_TOKEN='YOURKEY'
```
## Run Application
1. Run command from terminal `python main.py`
2. Go to 127.0.0.1:8080 on your browser 

## Issues encountered
1. Some songs did not return a song preview. **Solution**: Default song preview for those that do not return one.
2. Browser kept cacheing CSS files. **Solution**: Set file age to 0 in flask.```app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0```
3. There were errors when trying to handle null previews. **Solution**: Added null checks and replaced them as stated in solution 1
4. Some artist's names had symbols in their names in one API but not the other. **Solution**: Used [unidecode](https://pypi.org/project/Unidecode/) to remove them
5. Giberish queries would sometimes lead to the app crashing when no artist was found. **Solution**: Provide a default artist when an artist is not found
6. After one hour, the spotify access token would expire. **Solution**: Update the token after making an expired get request

## Known problems
1. Some artists that do not have lyrics end up displaying another song's lyrics
2. Some artists do not have any information available about them
3. Audio preview is very small

## Future improvements
* Update Spotify Access token a better way
* Add a nicer frontend with a framework like react
* Find more information on the artists
* Provide more information on the songs
* Display the song lyrics in real time

## Visit it here
http://artistdiscovery.herokuapp.com/

## To deploy to heroku
1. Create a heroku account at https://signup.heroku.com/login
2. Install heroku cli https://devcenter.heroku.com/articles/heroku-cli
3. Set up a requirements.txt with needed modules
4. Create a Procfile with `web: python main.py`
5. Commit all files using git
```
heroku login -i
heroku create
git push heroku main
heroku open
```
6. Visit https://dashboard.heroku.com/apps and add your environmental keys
7. Run `heroku open`
