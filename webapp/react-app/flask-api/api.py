import time
import os
import json
from flask import Flask
from igdb.wrapper import IGDBWrapper
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client_id = os.environ.get('CLIENT_ID')
access_token = os.environ.get('ACCESS_TOKEN')
wrapper = IGDBWrapper(client_id, access_token)
# print(client_id)
# print(access_token)

@app.route('/game')
def pull_game_request():
    name = 'Mario'
    result = wrapper.api_request('games', f'fields name, rating, first_release_date; where name ~ *\"{name}\"*; limit 25; sort rating desc;')
    return json.loads(result)