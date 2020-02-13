import os
import csv
import collections
from typing import List

"""
Functions:
get_regions():
get_income_ranges()
if_celebrate_thanks

"""
data = []

respondentID = "RespondentID"
main_1 = "What is typically the main dish at your Thanksgiving dinner?"
main_2 = "What is typically the main dish at your Thanksgiving dinner? - Other (please specify)"
stuffing_1 = "What kind of stuffing/dressing do you typically have?"
stuffing_2 = (
    "What kind of stuffing/dressing do you typically have? - Other (please specify)"
)
side_dish_1 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts"
side_dish_2 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots"
side_dish_3 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower"
side_dish_4 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Corn"
side_dish_5 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread"
side_dish_6 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Fruit salad"
side_dish_7 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Green beans/green bean casserole"
side_dish_8 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Macaroni and cheese"
side_dish_9 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Mashed potatoes"
side_dish_10 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Rolls/biscuits"
side_dish_11 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Squash"
side_dish_12 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Vegetable salad"
side_dish_13 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Yams/sweet potato casserole"
side_dish_14 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)"
side_dish_15 = "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)"
pie_1 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"
pie_2 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Buttermilk"
pie_3 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Cherry"
pie_4 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Chocolate"
pie_5 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Coconut cream"
pie_6 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Key lime"
pie_7 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Peach"
pie_8 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"
pie_9 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"
pie_10 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Sweet Potato"
pie_11 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - None"
pie_12 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)"
pie_13 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)"
desserts_1 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler"
desserts_2 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies"
desserts_3 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies"
desserts_4 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake"
desserts_5 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake"
desserts_6 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies"
desserts_7 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge"
desserts_8 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream"
desserts_9 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler"
desserts_10 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None"
desserts_11 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)"
desserts_12 = "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)"
household_earn = (
    "How much total combined money did all members of your HOUSEHOLD earn last year?"
)
us_region = "US Region"

main_dishes = [main_1, main_2]

stuffing_dishes = [stuffing_1, stuffing_2]

side_dishes = [
    side_dish_1,
    side_dish_2,
    side_dish_3,
    side_dish_4,
    side_dish_5,
    side_dish_6,
    side_dish_7,
    side_dish_8,
    side_dish_9,
    side_dish_10,
    side_dish_11,
    side_dish_12,
    side_dish_13,
    side_dish_14,
    side_dish_15,
]

pie_dishes = [
    pie_1,
    pie_2,
    pie_3,
    pie_4,
    pie_5,
    pie_6,
    pie_7,
    pie_8,
    pie_9,
    pie_10,
    pie_11,
    pie_12,
    pie_13,
]

dessert_dishes = [
    desserts_1,
    desserts_2,
    desserts_3,
    desserts_4,
    desserts_5,
    desserts_6,
    desserts_7,
    desserts_8,
    desserts_9,
    desserts_10,
    desserts_11,
    desserts_12,
]


def init():
    # Location independed way to find the file.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, "data", "thanksgiving-2015-poll-data.csv")

    with open(filename, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            data.append(row)
    return data


def get_regions():
    regions = []
    for row in init():
        if row[us_region] != "" and row[us_region] not in regions:
            regions.append(row[us_region])
    regions = enumerate(regions, 1)
    return regions


def get_income_ranges():
    income = []
    for row in init():
        if row[household_earn] != "" and row[household_earn] not in income:
            income.append(row[household_earn])
    income = enumerate(income, 1)
    return income


def region_menu(region_input, income_input):
    main_menu = []
    stuffing_menu = []
    side_dish_menu = []
    pie_menu = []
    dessert_menu = []

    for row in init():
        if row[us_region] == region_input and row[household_earn] == income_input:

            while main_menu == []:
                for i in range(len(main_dishes)):
                    if (
                        row[main_dishes[i]] != ""
                        and row[main_dishes[i]] != "Other (please specify)"
                    ):
                        main_menu.append(row[main_dishes[i]])
                    else:
                        continue
                    break
                break

            while stuffing_menu == []:
                for i in range(len(stuffing_dishes)):
                    if (
                        row[stuffing_dishes[i]] != ""
                        and row[stuffing_dishes[i]] != "Other (please specify)"
                    ):
                        stuffing_menu.append(row[stuffing_dishes[i]])
                    else:
                        continue
                    break
                break

            while side_dish_menu == []:
                for i in range(len(side_dishes)):
                    if (
                        row[side_dishes[i]] != ""
                        and row[side_dishes[i]] != "Other (please specify)"
                    ):
                        side_dish_menu.append(row[side_dishes[i]])
                    else:
                        continue
                    break
                break

            while pie_menu == []:
                for i in range(len(pie_dishes)):
                    if (
                        row[pie_dishes[i]] != ""
                        and row[pie_dishes[i]] != "Other (please specify)"
                    ):
                        pie_menu.append(row[pie_dishes[i]])
                    else:
                        continue
                    break
                break

            while dessert_menu == []:
                for i in range(len(dessert_dishes)):
                    if (
                        row[dessert_dishes[i]] != ""
                        and row[dessert_dishes[i]] != "Other (please specify)"
                    ):
                        dessert_menu.append(row[dessert_dishes[i]])
                    else:
                        continue
                    break
                break

    return main_menu, stuffing_menu, side_dish_menu, pie_menu, dessert_menu
