import os
import csv

field_names = []

def init():
    # Location independed way to find the file.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', "thanksgiving-2015-poll-data.csv")

    with open (filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        # for i in reader.fieldnames:
        #     print(f"'{i}'")
        for i in reader.fieldnames:
            field_names.append(i)

    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0

    records = []
    for i in field_names:
        if 'main' in i:
            print(f"main_{count_1+1} = '{i}'")
            records.append(f"main_{count_1+1},")
            count_1 += 1
            
        elif 'stuffing/dressing' in i:
            print(f"stuffing_{count_2+1} = '{i}'")
            records.append(f"stuffing_{count_2+1},")
            count_2 += 1
            
        elif 'side dish' in i:
            print(f"side_dish_{count_3+1} = '{i}'")
            records.append(f"side_dish_{count_3+1},")
            count_3 += 1

        elif 'pie' in i:
            print(f"pie_{count_4+1} = '{i}'")
            records.append(f"pie_{count_4+1},")
            count_4 += 1

        elif 'desserts' in i:
            print(f"desserts_{count_5+1} = '{i}'")
            records.append(f"desserts_{count_5+1},")
            count_5 += 1

    for i in records:
        print(i)


if __name__ == "__main__":
    init()