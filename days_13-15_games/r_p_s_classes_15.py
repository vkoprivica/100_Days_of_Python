import csv


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, other):
        wins = rolls_mapping()
        if other.name in wins[self.name].keys():
            return True
        else:
            return False


def rolls_mapping():
    with open(
        "/Users/Vule/Documents/Python/100_Days_of_Code/days_13-15_games/battle_table.csv"
    ) as fin:
        reader = csv.DictReader(fin)
        win_map = {}
        for row in reader:
            attacker = row["Attacker"]
            del row["Attacker"]
            win_map[attacker] = {k: v for k, v in row.items() if v == "win"}

    return win_map

