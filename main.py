

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URL = os.getenv('SPOTIFY_REDIRECT_URL')
SGOTIFY_URL = os.getenv('SPOTIFY_REDIRECT_URL')
SGOTIFY_BASE_URL = os.getenv('SGOTIFY_BASE_URL')

scope = "user-read-recently-played,app-remote-control,streaming,user-read-playback-state"


last_three = []

while True:
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret= SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URL, scope=scope))
        sgotify_url = SGOTIFY_BASE_URL + "/admin/queue/new"
        r = requests.get(url = sgotify_url)
        data = r.json()
        if data and data["songs"] and len(data["songs"]):
            for i in range(0, 3):
                if len(data["songs"]) >= i + 1:
                    print(data["songs"][i]["Title"])
                    if len(last_three) < 3:
                        print("Add to queue.")
                        sp.add_to_queue(data["songs"][i]["Id"])
                        last_three.append(data["songs"][i]["Id"])
                        # patch current 
                        sgotify_url_patch = SGOTIFY_BASE_URL + "/admin/queue/"+data["songs"][i]["Id"]
                        r = requests.patch(url = sgotify_url_patch, json={"OnSpotify": "true"})
            #print(data["songs"][1])
            #sp.add_to_queue(data["songs"][1]["Id"])
            #print(sp.queue())
        #results = sp.current_user_recently_played()
        song = sp.current_user_playing_track()
        if song and song["item"]:
            print("Current Playing: " + song["item"]["name"])
            if song["item"]["id"] in last_three:
                print("Remove from last3.")
                last_three.remove(song["item"]["id"])
    except:
        print("ERROR.")
    time.sleep(10)
    print(sp._get("me/player/queue"))

#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " - ", track['name'])