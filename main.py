import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"
app.run(
    port=int(os.getenv("PORT",8080)),
    host=os.getenv("IP","0.0.0.0"),
    debug=True
)