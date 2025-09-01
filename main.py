import read
import operations


def main():
    file_path = 'pokemon_cards.txt'
    read.load_inventory(file_path)
    print("----------------------------------------------------------")
    print("-------------Abhaya's Pokemon Card corner-----------------")
    print("----------------------------------------------------------")

    options = [
        "Press 1 to view inventory",
        "Press 2 to buy card",
        "Press 3 to sell card",
        "Press 4 to exit",
    ]
    for option in options:
        print(option)
    choice = int(input("Please Enter your choice here : "))
    try:
        if choice == 1:
            print("----------------------------------------------------------")
            print("-------------Abhaya's Pokemon Card corner-----------------")
            print("----------------------------------------------------------")
            operations.display_inventory()
        elif choice == 2:
            print("----------------------------------------------------------")
            print("-------------Abhaya's Pokemon Card corner-----------------")
            print("----------------------------------------------------------")
            operations.display_inventory()
            buy_id = input("Please enter the ID of the card you would like to purchase: ")
            operations.buy_card(buy_id)
        elif choice == 3:
            sell_id = input("Please enter the ID of the card you would like to sell: ")
            operations.sell_card(sell_id)
        elif choice == 4:
            print("Thank you for visiting!")
    except Exception:
        pass


if __name__ == "__main__":
    main()
