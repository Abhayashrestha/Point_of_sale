"""Helper functions for writing card data back to the inventory file."""

from typing import List, Dict


def write_cards(file_path: str, cards: List[Dict[str, str]]) -> None:
    """Write the provided list of cards to ``file_path``.

    Each card is expected to be a dictionary containing the keys ``Id``,
    ``Name``, ``Rarity`` and ``Availability``.  The resulting file will contain
    one card per line in comma separated format.
    """

    with open(file_path, "w") as file:
        for card in cards:
            line = f"{card['Id']},{card['Name']},{card['Rarity']},{card['Availability']}\n"
            file.write(line)

