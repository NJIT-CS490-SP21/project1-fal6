import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)

load_dotenv(find_dotenv()) # Loads API keys
spotify_id = os.getenv("SPOT_ID")
spotify_secret = os.getenv("SPOT_SECRET")

auth_url="https://accounts.spotify.com/api/token"

auth = requests.post(auth_url,
    {
        'grant_type' : 'client_credentials',
        'client_id' : spotify_id,
        'client_secret' : spotify_secret,
    }
)
auth_token = auth.json()["access_token"]



@app.route('/')
def hello_world():
    return "Hello World"

app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)