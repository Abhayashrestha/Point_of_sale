"""Utility functions for saving card inventory to disk."""

from typing import List, Dict


def write_cards(file_path: str, cards: List[Dict[str, str]]) -> None:
    """Write a list of card dictionaries to ``file_path``.

    Each card dictionary is expected to contain the keys ``Id``, ``Name``,
    ``Rarity`` and ``Availability``. The values are written as a comma
    separated line for each card.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        for card in cards:
            line = f"{card['Id']},{card['Name']},{card['Rarity']},{card['Availability']}\n"
            file.write(line)
