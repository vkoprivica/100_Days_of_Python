from r_p_s_classes_15 import Player, Roll, rolls_mapping
import random
import csv
import os


def main():
    print_header()

    rolls = build_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    p1_count = 0
    p2_count = 0
    while count < 4:
        p2_roll = random.choice(build_rolls())

        p1_roll = Roll(input(f"\nPlease choose roll: "))
        print(f"Your choice was {p1_roll.name}.")
        print(f"Computer choice was {p2_roll.name}.")

        if p1_roll == p2_roll:
            print("Tie! Try again!")
            continue

        outcome = p1_roll.can_defeat(p2_roll)
        # print(f"Outcome: {outcome}")
        if outcome:
            p1_count += 1
            print(f"{player1.name} Count: {p1_count}")
        else:
            p2_count += 1
            print(f"{player2.name} Count: {p2_count}")

        count += 1

    # Compute who won
    if p1_count > p2_count:
        print(f"{player1.name} Won!")
    else:
        print(f"{player2.name} Won!")


def print_header():
    print("---------------------------------")
    print("          RPS Game               ")
    print("---------------------------------")
    print()


def get_players_name():
    return input("Please enter your name: ")


def build_rolls():
    return [Roll(key) for key in rolls_mapping().keys()]


if __name__ == "__main__":
    main()
