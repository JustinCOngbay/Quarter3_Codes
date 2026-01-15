import numpy as np

prices = [["apple", 30], ["banana", 20], ["orange", 25]]


def find_index(prices_list, item_name):
    for i, pair in enumerate(prices_list):
        if pair[0].lower() == item_name.lower():
            return i
    return -1


def update_price(prices_list):
    item = input("Enter item name to update (or leave blank to cancel): ").strip()
    if not item:
        print("Cancelled.")
        return
    idx = find_index(prices_list, item)
    if idx != -1:
        try:
            new_price = float(input(f"Enter new price for {prices_list[idx][0]}: ").strip())
        except ValueError:
            print("Invalid price. Update cancelled.")
            return
        prices_list[idx][1] = new_price
        print(f"Updated {prices_list[idx][0]} to {new_price}")
    else:
        resp = input(f"'{item}' not found. Add as new item? (y/n): ").strip().lower()
        if resp == 'y':
            try:
                new_price = float(input(f"Enter price for {item}: ").strip())
            except ValueError:
                print("Invalid price. Add cancelled.")
                return
            prices_list.append([item, new_price])
            print(f"Added {item} at {new_price}")


def show_prices(prices_list):
    print("\nCurrent prices:")
    for name, price in prices_list:
        print(f" - {name}: {price}")


def main():
    while True:
        show_prices(prices)
        print("\nOptions: [u]pdate, [a]dd, [q]uit")
        choice = input("Choice: ").strip().lower()
        if choice in ('u', 'update'):
            update_price(prices)
        elif choice in ('a', 'add'):
            item = input("Item name to add: ").strip()
            if not item:
                print("No item entered.")
                continue
            if find_index(prices, item) != -1:
                print("Item already exists. Use update instead.")
                continue
            try:
                new_price = float(input("Price: ").strip())
            except ValueError:
                print("Invalid price. Add cancelled.")
                continue
            prices.append([item, new_price])
            print(f"Added {item} at {new_price}")
        elif choice in ('q', 'quit'):
            print("Exiting.")
            break
        else:
            print("Unknown choice. Try again.")


if __name__ == '__main__':
    main()