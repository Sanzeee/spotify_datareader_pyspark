# print("starting spotify extraction")
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pyspark.sql import SparkSession
from pyspark.sql.functions import  col

spark = SparkSession.builder.appName("spotify_datareader").getOrCreate()

with open("config/secrets.json","r") as file:
    creds = json.load(file)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    redirect_uri=creds["redirect_uri"],
    scope="user-read-recently-played"
))

# https://yourname-yourrepo-xxxxx.github.dev/callback

results = sp.current_user_recently_played()
results_json= results['items']


# print(rdd.first())
json_string = [json.dumps(record) for record in results_json]
rdd = spark.sparkContext.parallelize(json_string)
df = spark.read.json(rdd)
df.show(1)
df.printSchema()
df.select(col("track.name").alias("trackname"),col("track.album.name").alias("albumname"),col("played_at").alias("played_at")).show(truncate=False)
df.select(col("track.name").alias("trackname"),col("track.album.name").alias("albumname"),col("played_at").alias("played_at")).write.mode("overwrite").option("header" , True).csv("/workspaces/spotify_datareader_pyspark/data/raw/")

# df.printSchema()
# for i in results_json:
    
#     track = i['track']["name"]
#     artists = i['track']["album"]["artists"][0]["name"]
    # print(track)
    # for j in track:
    #     songs= (j["external_urls"]["name"])
    #     print(songs)
    # album = track["album"]
    # artist= album["artists"][0]
    # external_urls = artists["external_urls"]=============

    # items[track[album[artists[external_urls[name

"""
Top Tracks
Top Artists
Most Active Listening time
Most Listened Albums
LIstening sessions over time
Visualise using pandas
"""

#print(results)

