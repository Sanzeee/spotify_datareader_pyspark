# print("starting spotify extraction")
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pyspark.sql import SparkSession

with open("config/secrets.json","r") as file:
    creds = json.load(file)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    redirect_uri=creds["redirect_uri"],
    scope="user-read-recently-played"
))

# https://yourname-yourrepo-xxxxx.github.dev/callback

results = sp.current_user_recently_played(limit=10)
results_json= results['items']

for i in results_json:
    track = i['track']["name"]
    artists = i['track']["album"]["artists"][0]["name"]
    print(track)
    # for j in track:
    #     songs= (j["external_urls"]["name"])
    #     print(songs)
    # album = track["album"]
    # artist= album["artists"][0]
    # external_urls = artists["external_urls"]=============

    # items[track[album[artists[external_urls[name

# print(results)

