import write


def display_inventory(cards):
    """Print available cards from the provided inventory list."""
    if cards:
        print("Available cards")
        for card in cards:
            if card['Availability'] == "Available":
                print(
                    f"Id :{card['Id']},card name: {card['Name']},Rarity: {card['Rarity']},Availability: {card['Availability']}"
                )
    else:
        print("No cards available")


def buy_card(cards, buy_id, file_path):
    """Mark the card with `buy_id` as not available and persist the change."""
    for card in cards:
        if card['Id'] == buy_id and card['Availability'] == 'Available':
            card['Availability'] = 'Not Available'
            write.write_cards(file_path, cards)
            print("purchase successful")
            return
    print(f"Card with ID {buy_id} is not available for sale.")
