"""Entry point for the Pokémon card point of sale application."""

import operations


def main() -> None:
    """Run a small interactive command line interface.

    Users can view the inventory, purchase cards or search for a card by name.
    The loop continues until the user chooses to exit.
    """

    print("----------------------------------------------------------")
    print("-------------Abhaya's Pokemon Card Corner-----------------")
    print("----------------------------------------------------------")

    while True:
        options = [
            "Press 1 to view inventory",
            "Press 2 to buy card",
            "Press 3 to search for a card",
            "Press 4 to exit",
        ]
        for option in options:
            print(option)

        choice = input("Please enter your choice here: ")

        if choice == "1":
            operations.display_inventory()
        elif choice == "2":
            buy_id = input(
                "Please enter the ID of the card you would like to purchase: "
            )
            operations.buy_card(buy_id)
        elif choice == "3":
            name = input("Enter the name of the card you are looking for: ")
            operations.search_card(name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()



