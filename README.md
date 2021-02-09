# Music Web App
Web App written using flask as a backend as well as the Spotify and Genius API. 
In this Web App, you are able to see information from a random song selected from a list of top songs by an artist retrieved by the Spotify API.

## Requirements
```
pip install flask
pip install requests
pip install python-dotenv
``` 
## Setup
1. Create a .env file in the main directory
2. Add your spotify and genius keys to .env:
```
export SPOT_ID='YOURKEY'
export SPOT_SECRET='YOURKEY'
export GEN_ID='YOURKEY'
export GEN_SERCRET='YOURKEY'
```
## Run Application
1. Run command from terminal `python main.py`
2. Go to 127.0.0.1:8080 on your browser 

## Issues encountered
1. Some songs did not return a song preview. **Solution**: Default song preview for those that do not return one.
2. Browser kept cacheing CSS files. **Solution**: Set file age to 0 in flask.
3. There were errors when trying to handle null previews. **Solution**: Handled the null previews and replaced them as stated in solution 1

## Known problems
Currently there aren't any major problems but there are many missing features.

## Future improvements
Some future improvements would be to add a better frontend using a framework like react. Also, add search features so that the user is able to search their own artist. 
