

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import time
from dotenv import load_dotenv
import os
import grpc
import sgotipy_pb2
import sgotipy_pb2_grpc
import uvloop

from grpc_asyncio import AsyncioExecutor

import json
import threading

process_event = threading.Event()

def parse_artists(artists):
    if len(artists) == 0:
        return ''
    if len(artists) > 1:
        return artists[0]['name'] + ',' + artists[1]['name']
    return artists[0]['name']
class SgotifyServicer(sgotipy_pb2_grpc.SgotipyServicer):

    def __init__(self):
        self.running = False
    
    async def StartSgotipy(self, request, context):
        auth = {
            'access_token': request.access_token,
            'token_type': request.token_type,
            'scope': request.scope,
            'expires_at': request.expires_in,
            'refresh_token': request.refresh_token, 
        }
        with open(".cache", "w+", encoding = 'utf-8') as f:
            f.write(json.dumps(auth))
        process_event.set()
        self.running = True
        print("[INFO] SgotifyServicer -- Running: " + str(self.running))
        result = {'message': "OK"}

        return sgotipy_pb2.StartSgotipyResponse(**result)

    async def StopSgotipy(self, request, context):
        process_event.clear()
        try:
            os.remove('.cache')
        except:
            print('[ERR] SgotifyServicer -- Missing .cache file (wtf ?!?)')
        
        self.running = False
        print("[INFO] SgotifyServicer -- Running: " +  str(self.running))
        result = {'message': "OK"}
        self.running = False
        return sgotipy_pb2.StopSgotipyResponse(**result)
    
    async def SgotipyStatus(self, request, context):
        device = ''
        device_status = ''
        current_song = {}
        status = "NOT_RUNNING"
        if self.running == True:
            status = "RUNNING"
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
            playback = sp.current_playback()
            device = ''
            device_status = ''
            current_song = {}
            if playback:
                if playback['device']:
                    device = playback["device"]["name"]
                if playback["is_playing"]:
                    device_status = "PLAYING"
                else:
                    device_status = "NOT_PLAYING"
                if playback and playback["item"]:
                    current_song = {'id': playback["item"]["id"], 'title': playback["item"]["name"], 'artists': parse_artists(playback["item"]["artists"])}
            print(current_song)
            print(device)
            print(device_status)
        result = {'status': status, 'device': device, 'device_status': device_status, 'current_song': current_song}
        return sgotipy_pb2.SgotipyStatusResponse(**result)

load_dotenv()

SGOTIFY_BASE_URL = os.getenv('SGOTIFY_BASE_URL')

scope = "user-read-recently-played,app-remote-control,streaming,user-read-playback-state"

if __name__ == "__main__":
    loop = uvloop.new_event_loop()
    executor = AsyncioExecutor(loop=loop)
    server = grpc.server(executor)
    sgotipy_pb2_grpc.add_SgotipyServicer_to_server(SgotifyServicer(), server)
    server.add_insecure_port("[::]:4040")
    server.start()
    last_three = []
    while True:
        process_event.wait()
        try:
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
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
        time.sleep(20)