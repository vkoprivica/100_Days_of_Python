import os
import csv
import collections
from typing import List

def init():
    # Location independed way to find the file.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, "thanksgiving-2015-poll-data.csv")

    with open (filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin) #, quoting=csv.QUOTE_NONE)

        for i in reader.fieldnames:
            print(f"'{i},'")






if __name__ == "__main__":
    init()



