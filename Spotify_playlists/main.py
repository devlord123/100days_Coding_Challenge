from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


Client_id = '901e43378d154d78a9d10b7da0708080'
Client_key = '38d4bdfe22f54257a424d11c79a52500'
Redirect_url = 'https://www.devowoyemi.com'

# user = input("What year do you want to travel to? Type date in this format YYYY-MM-DD: ")

user = '2005-05-13'
content = f"https://www.billboard.com/charts/hot-100/{user}"

response = requests.get(url=content)
soup = BeautifulSoup(response.text, 'html.parser')
Songs = soup.find_all("h3", class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 \
lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis \
u-max-width-330 u-max-width-230@tablet-only')

title = [art.getText() for art in Songs]
song_list = []
for item in title:
    item = item.replace('\n', '')
    item = item.replace('\t', '')
    song_list.append(item)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=Redirect_url,
        client_id=Client_id,
        client_secret=Client_key,
        show_dialog=True,
        cache_path="token.txt"
    )
)

song_uris = []
user_id = sp.current_user()['id']
year = user.split("-")[0]

for song in song_list:
    res = sp.search(q=f'track:{song}, year:{year}', type='track')
    #print(res)

    try:
        uri = res['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=Client_id, name=f'{user} Billboard 100', public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

