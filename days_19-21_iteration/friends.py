import itertools

friends = 'Bob Dante Julian Martin'.split()

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))
    else:
        return list(itertools.combinations(friends, team_size))


if __name__ == "__main__":
    print(friends_teams(friends))