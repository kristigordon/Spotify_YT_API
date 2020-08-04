"""
Step 1: Log Into YT
Step 2: Grab Liked Videos
Step 3: Create New Playlist
Step 4: Search For The Song
Step 5: Add song into new Spotify playlist
"""
import json
from secrets import 
class CreatePlaylist

      def _init_(self):
          pass

    # Step 1: Log Into YT
      def get_youtube_client(self):
          pass

    # Step 2: Grab Liked Videos        
      def get_liked_videos(self):
          pass

    # Step 3: Create New Playlist
      def create_playlist(self):
          
          request_body =json.dumps({
              "name":"Youtube Like Vids",
              "description": "All Liked Youtube Videos",
              "public": True
          })
        
        query = "https://api.spotify.com/v1/users/{}/playlists".format()


    # Step 4: Search For The Song
      def get_spotify_uri(self):
          pass

    # Step 5: Add song into new Spotify playlist
      def add_song_to_playlist(self):
          pass