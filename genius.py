from dotenv import load_dotenv, find_dotenv
import requests, os

load_dotenv(find_dotenv()) # Loads API keys
genius_token = os.getenv("GEN_TOKEN")

search_url='https://api.genius.com/search'

headers = {
    'Authorization': f'Bearer {genius_token}'
} # header for all requests

def get_lyric_link(name):
    data = {'q': name}
    response = requests.get(search_url,headers=headers,data=data)
    link = response.json()["response"]["hits"][0]["result"]["url"]
    return link
    