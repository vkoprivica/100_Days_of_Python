import api
import webbrowser


def main():
    keyword = input("Keyword for title search: ")
    results = api.find_episodes_by_title(keyword)

    print()
    print(f"Lenght of results: {len(results)}")
    print()

    episode_id = [r.id for r in results]

    episode_id_enum = enumerate(episode_id, 1)
    for count, element in episode_id_enum:
        print(count, element)

    id_input = int(input("Please enter desired episode ID: "))

    for r in results:
        if r.id == episode_id[id_input - 1]:
            url_end = r.url

    full_url = f"https://talkpython.fm{url_end}"
    webbrowser.open(full_url, new=2)


if __name__ == "__main__":
    main()
