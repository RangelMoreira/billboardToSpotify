import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self):
        load_dotenv()
        self.SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.SPOTIPY_REDIRECT_URI =os.getenv('SPOTIPY_REDIRECT_URI')
        self.scope = 'playlist-modify-private'
        self.sp = self.authenticate()

    def authenticate(self):
        sp_oauth = SpotifyOAuth(
            client_id=self.SPOTIPY_CLIENT_ID,
            client_secret=self.SPOTIPY_CLIENT_SECRET,
            redirect_uri=self.SPOTIPY_REDIRECT_URI,
            scope=self.scope
        )
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        return sp

    def create_list(self, date, track_names):
        try:

            #Creating playlist
            playlist = self.sp.user_playlist_create(
                user=self.sp.me()["id"],
                name=f"{date} Billboard 100",
                public=False,
                description=f"{date} Billboard 100"
            )

            playlist_id = playlist["id"]

            track_ids = []

            # Search for songs and get their IDs
            for track_name in track_names:
                results = self.sp.search(q=track_name, type='track')
                if results['tracks']['items']:
                    track_ids.append(results['tracks']['items'][0]['id'])

            # Add songs to playlist
            self.sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)
            print("Playlist created successfully!")

        except Exception as e:
            print(f"An exception occurred: {e}")

