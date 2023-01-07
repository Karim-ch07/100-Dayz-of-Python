import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy import *
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import json

CLIENT_ID = ""
SECRET = ""
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
CACHE_PATH = "token.txt"

URL = "https://www.billboard.com/charts/hot-100"

SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=CACHE_PATH,
        show_dialog=True,
    )
)

# user_id = sp.current_user()["id"]

# date = input("what year you would like to travel to? YYYY-MM-DD\t")

# response = requests.get(f"{URL}/{date}")
response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")
response.raise_for_status()
spotify_website = response.text

# print(spotify_website)

soup = BeautifulSoup(spotify_website, "html.parser")

# titles = soup.select(selector="li ul li h3", id="title-of-a-story")
# titles = [title.getText() for title in soup.find_all(name="h3", id="title-of-a-story")]
titles = [title.getText().strip("\n\t") for title in soup.select(selector="li ul li h3", id="title-of-a-story")]

# print(titles)
with open("token.txt", encoding="utf8") as file:
    content = json.load(file)
    access_token = content["access_token"]

headers = {
    "Authorization": "Bearer {token}".format(token=access_token)
}

titles = ["traaaaa", "treksdfd"]
for title in titles:
    params = {
        "q": title,
        "type": "track",
        # "year": "",
    }
    # try:
    track_info = requests.get(
        'https://api.spotify.com/v1/search',
        headers=headers,
        params=params,
    )
    print(track_info.json())
    # except:
    #     continue
    # else:
    #     pass
    # finally:
    #     pass
