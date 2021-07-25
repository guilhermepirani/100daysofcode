'''Scrap billboards for the top 100 songs in a given date, then creates a spotify playlist'''

import requests
import spotipy
from bs4 import BeautifulSoup
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://example.com' # Must be manually defined on configs


# Authenticating with Spotify to manage private playlists
spotify_auth = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        client_id = CLIENT_ID, 
        client_secret = CLIENT_SECRET, 
        redirect_uri = REDIRECT_URI,
        scope = 'playlist-modify-private',
        show_dialog = True,
        cache_path = 'C:/100daysofcode/day046/musictimemachine/token.txt',
    )
)
# To actually trigger the validation it's needed to interact with the created object
user_id = spotify_auth.current_user()["id"]

# After auth a file is created at 'cache_path' and the above steps are skipped as long as it's still valid

# Date information needed
date_limit = datetime.strptime('1958-08-04', "%Y-%m-%d").date()
today = datetime.now().date()

# Get user input for a date to scrap
while True:
    user_date = input('To what past date would you like to time travel? YYYY-MM-DD: ')
    try:
        user_date = datetime.strptime(user_date, "%Y-%m-%d").date() # Str to date_obj
    except ValueError:
        print('Your date must be formatted as YYYY-MM-DD')
    else:
        # Check dates to confirm validity with billboard
        if user_date < today:
            if user_date < date_limit:
                print(f'The time machine doesn\'t go that far. Changing date to {date_limit}...')
                user_date = date_limit
            break
        else:
            print('Your must enter a past date')

# Scrap Billboard website in the given date
response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_date}')
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Identified the elements needed by looking the HTML:
    # span class="chart-element__information__song = song name
    # span class="chart-element__information__artist = artist name

# Get Top 100 songs and who performed the songs
songs = [song.getText() for song in soup.find_all(name='span', class_='chart-element__information__song')]

# Searching songs by title on Spotify
year = user_date.year
song_paths = []
for song in songs:
    result = spotify_auth.search(q=f"track:{song} year:{year}", type="track")
    try:
        # Add song URI to list
        uri = result["tracks"]["items"][0]["uri"]
        song_paths.append(uri)
    except IndexError:
        print(f"Couldn't locate {song} in Spotify. Skipped.")

# Creating a new private playlist
playlist = spotify_auth.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

# Adding songs to playlist
spotify_auth.playlist_add_items(playlist_id=playlist["id"], items=song_paths) 