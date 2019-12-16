import api
import requests.exceptions


def main():
    try:
        keyword = input('Keyword of title search: ')
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection.")
    except Exception as x:
        print(type(x))
        print("Oh, that did not work! {x}")

if __name__ == '__main__':
    main()