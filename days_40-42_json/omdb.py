import json
import requests
from pprint import pprint

# http://www.omdbapi.com/?apikey=[yourkey]&
# http://img.omdbapi.com/?apikey=[yourkey]&

r = requests.get("http://www.omdbapi.com/?apikey=[REMOVED_KEY]&t=Rambo")

print(r.status_code)
print(r.text)

data = json.loads(r.text)

for k in data.keys():
    print(k)
