NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return [name.title() for name in set(NAMES)]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(NAMES)
    return sorted(names, key=lambda x: x.split()[-1], reverse=True)
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    first_name_sort = sorted(names, key=lambda x: x.split(), reverse=False)
    return first_name_sort[0].split()[0]


if __name__ == "__main__":
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))
