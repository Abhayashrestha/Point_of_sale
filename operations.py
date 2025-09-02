"""Operations for the simple Pokémon card point of sale application.

This module contains helper functions to display the card inventory,
purchase cards and search for specific cards.  The data for the cards is
stored in a simple comma separated file which is read and written using the
``read`` and ``write`` helper modules.
"""

import read
import write

# Location of the inventory file.  All operations read from and write to this
# file so keeping it as a constant makes updates easier and centralised.
INVENTORY_FILE = "pokemon_cards.txt"

#function to display all available cards in the inventory
def display_inventory():
    """Print a list of all cards in the inventory."""

    cards = read.load_inventory(INVENTORY_FILE)
    if not cards:
        print("No cards available")
        return

    print("Available cards")
    for card in cards:
        print(
            f"Id: {card['Id']}, card name: {card['Name']}, Rarity: {card['Rarity']}, "
            f"Availability: {card['Availability']}"
        )

def buy_card(card_id: str) -> None:
    """Mark the specified card as not available.

    Parameters
    ----------
    card_id: str
        The identifier of the card to purchase.
    """

    try:
        cards = read.load_inventory(INVENTORY_FILE)
        for card in cards:
            if card["Id"] == card_id:
                if card["Availability"] == "Available":
                    card["Availability"] = "Not Available"
                    write.write_cards(INVENTORY_FILE, cards)
                    print("Purchase successful")
                else:
                    print(f"Card with ID {card_id} is not available for sale.")
                break
        else:
            print(f"Card with ID {card_id} not found.")
    except FileNotFoundError:
        # Helps to handle the file not found error smoothly
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        # Helps to catch and fix general exceptions by displaying an error message
        print(f"Error purchasing card: {e}")


def search_card(name: str) -> None:
    """Search the inventory for a card by name.

    The search is case-insensitive and prints the details of the card if it is
    found.  If no matching card exists an informative message is displayed.
    """

    cards = read.load_inventory(INVENTORY_FILE)
    for card in cards:
        if card["Name"].lower() == name.lower():
            print(
                f"Id: {card['Id']}, card name: {card['Name']}, Rarity: {card['Rarity']}, "
                f"Availability: {card['Availability']}"
            )
            break
    else:
        print(f"{name} not found in inventory.")

def purchase():
    # Placeholder for potential future expansion of the system.
    pass

