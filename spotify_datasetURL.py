import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load the CSV file
df = pd.read_csv('C:/Users/NTC/Downloads/spotify-2023 (3).csv',
                 encoding='iso-8859-1')

# Initialize Spotify API credentials
client_id = 'f5c0b37bc6c24701ae28c5a76c4ba749'
client_secret = '9fd2e85679a049bdaee1cc32982f709d'
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get track or album cover URL


def get_cover_url(track_name):
    try:
        # Search for the track by name
        results = sp.search(q=track_name, type='track', limit=1)
        # Extract the first track from the search results
        track_info = results['tracks']['items'][0]
        # URL of the first (largest) image
        return track_info['album']['images'][0]['url']
    except:
        return None


# Add a new column for cover URLs
df['cover_url'] = df['track_name'].apply(get_cover_url)

# Save the modified CSV file
df.to_csv('C:\\Users\\NTC\\Downloads\\spotify-2023 (2).csv', index=False)
