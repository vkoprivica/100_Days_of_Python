import requests
import collections
from typing import List


Search = collections.namedtuple("Search", "category, id, url, title, description")


def find_episodes_by_title(keyword: str) -> List:
    url = f"https://search.talkpython.fm/api/search?q={keyword}"

    response = requests.get(url)
    response.raise_for_status()

    results = response.json()
    search_results = []
    for r in results.get("results"):
        search_results.append(Search(**r))
    return search_results
