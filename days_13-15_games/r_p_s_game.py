from r_p_s_classes import Player, Roll
import random


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    p1_count = 0
    p2_count = 0
    while count < 4:
        p2_roll = random.choice(build_the_three_rolls())
        p1_roll = Roll(input("\nPlease choose: rock (r), paper (p) or scissors (s)? "))
        outcome = p1_roll.can_defeat(p2_roll)
        print(f"Your choice {player1.name} was {p1_roll.name}.")
        print(f"Computer choice was {p2_roll.name}.")

        if p1_roll.name == p2_roll.name:
            print("Tie! Try again!")
            continue

        if outcome:
            p1_count += 1
        else:
            p2_count += 1

        count += 1

    # Compute who won
    if p1_count > p2_count:
        print(f"{player1.name} won!")
    else:
        print(f"{player2.name} won!")


def print_header():
    print("---------------------------------")
    print("          RPS Game               ")
    print("---------------------------------")
    print()


def get_players_name():
    return input("Please enter your name: ")


def build_the_three_rolls():
    return [Roll("rock"), Roll("paper"), Roll("scissors")]


if __name__ == "__main__":
    print(build_the_three_rolls())
