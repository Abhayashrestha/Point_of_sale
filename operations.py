"""Operations for managing the Pokémon card inventory."""

from typing import List, Dict

import read
import write

DEFAULT_INVENTORY_FILE = "pokemon_cards.txt"


def display_inventory(file_path: str = DEFAULT_INVENTORY_FILE) -> None:
    """Display all available cards in the inventory."""
    cards = read.load_inventory(file_path)
    if not cards:
        print("No cards available")
        return

    print("Available cards")
    for card in cards:
        if card.get("Availability") == "Available":
            print(
                f"Id: {card['Id']}, card name: {card['Name']}, "
                f"Rarity: {card['Rarity']}, Availability: {card['Availability']}"
            )


def buy_card(card_id: str, file_path: str = DEFAULT_INVENTORY_FILE) -> None:
    """Mark the card with ``card_id`` as purchased if it is available."""
    try:
        cards = read.load_inventory(file_path)
        for card in cards:
            if card["Id"] == card_id and card["Availability"] == "Available":
                card["Availability"] = "Not Available"
                write.write_cards(file_path, cards)
                print("Purchase successful")
                return
        print(f"Card with ID {card_id} is not available for purchase.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error purchasing card: {e}")
