import research


def main():
    print()
    for i in research.get_regions():
        print(i)
    region_input = input("Please choose region: ")
    region = [val for idx, val in research.get_regions() if idx == int(region_input)][0]
    print(region)

    print()
    for i in research.get_income_ranges():
        print(i)
    income_input = input("Please choose income: ")
    income = [
        val for idx, val in research.get_income_ranges() if idx == int(income_input)
    ][0]
    print(income)

    print()
    items = ["Main menu", "Stuffing", "Side Dish", "Pie", "Dessert"]

    for i in range(len(items)):
        print(f"{items[i]}: {research.region_menu(region, income)[i][0]}")
    print()


if __name__ == "__main__":
    main()
