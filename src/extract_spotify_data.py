# print("starting spotify extraction")
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open("config/secrets.json","r") as file:
    creds = json.load(file)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    redirect_uri=creds["redirect_uri"],
    scope="user-top-read"
))

# https://yourname-yourrepo-xxxxx.github.dev/callback

results = sp.current_user_recently_played(limit=10)

print(results)

