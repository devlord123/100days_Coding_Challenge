import requests

API_KEY = '5177b56dc20815f8d29b3aa5ca01f136'
API_URL = 'https://api.themoviedb.org/3/search/movie'

log = {
    'api_key': API_KEY,
    'query': "Vagabond"
}

response = requests.get(url=API_URL, params=log)
response.raise_for_status()
data = response.json()
result = data['results']

for dt in result:
    print(dt['poster_path'])

