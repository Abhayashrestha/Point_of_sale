import read
import operations

def main():
    file_path = 'pokemon_cards.txt'
    cards = read.load_inventory(file_path)
    print("----------------------------------------------------------")
    print("-------------Abhaya's Pokemon Card corner-----------------")
    print("----------------------------------------------------------")

    options = [
        "Press 1 to view inverntory",
        "Press 2 to buy card",
        "Press 3 to sell cards",
        "Press 4 to exit",
    ]
    for option in options:
        print(option)
    choice = int(input("Please Enter your choice here : "))
    if choice == 1:
        print("----------------------------------------------------------")
        print("-------------Abhaya's Pokemon Card corner-----------------")
        print("----------------------------------------------------------")
        operations.display_inventory(cards)
    elif choice == 2:
        while True:
            print("----------------------------------------------------------")
            print("-------------Abhaya's Pokemon Card corner-----------------")
            print("----------------------------------------------------------")
            operations.display_inventory(cards)
            buy_id = input("Please enter the ID of the card you would like to purchase: ")
            operations.buy_card(cards, buy_id, file_path)
            break


if __name__ == "__main__":
    main()
