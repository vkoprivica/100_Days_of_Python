from time import sleep
import itertools
import random
import time

colours = "Red Green Amber".split()
rotation = itertools.cycle(colours)


def traffic_light():
    for color in rotation:
        if color == "Red":
            print("RED")
            sleep(5)
        elif color == "Amber":
            print("AMBER")
            sleep(2)
        else:
            print("GREEN")
            sleep(5)


if __name__ == "__main__":
    traffic_light()
