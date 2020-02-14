import json
import requests
from pprint import pprint

# http://www.omdbapi.com/?apikey=[yourkey]&
# http://img.omdbapi.com/?apikey=[yourkey]&

r = requests.get("http://www.omdbapi.com/?apikey=[KEY_REMOVED]&t=Kralj Petar")

print(r.status_code)
print(r.text)

data = json.loads(r.text)

for k, v in data.items():
    print(k, v)
