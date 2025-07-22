# spotify_datareader_pyspark - This project is used to extract the latest listened songs from spotify 
1.Set up authentication with Spotipy, first create an app here, you will get the client credentials, use them in the secrets.json
https://developer.spotify.com/dashboard

2.Fetched recent tracks using sp.current_user_recently_played()

Parsed the JSON and flattened nested fields

Converted it to a Spark DataFrame

Explored schema using .printSchema() / .select().show()

Exported it to CSV using df.write.csv()


#steps to deploy
git add .
git commit -m "comment"
git push origin main (to push to main )


#steps to install the required packages
pip install spotipy

#steps to install the pyspark
pip install pyspark
