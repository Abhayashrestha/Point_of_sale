import read
import write


def _load_cards():
    return read.load_inventory('pokemon_cards.txt')


def display_inventory():
    cards = _load_cards()
    if cards:
        print("Available cards")
        for card in cards:
            print(f"Id: {card['Id']}, card name: {card['Name']}, Rarity: {card['Rarity']}, Availability: {card['Availability']}")
    else:
        print("No cards available")


def buy_card(buy_id):
    try:
        cards = _load_cards()
        for card in cards:
            if card['Id'] == buy_id:
                if card['Availability'] == 'Available':
                    card['Availability'] = 'Not Available'
                    write.write_cards('pokemon_cards.txt', cards)
                    print("purchase successful")
                else:
                    print(f"Card with ID {buy_id} is not available for purchase.")
                break
        else:
            print(f"Card with ID {buy_id} not found.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error purchasing card: {e}")


def sell_card(sell_id):
    try:
        cards = _load_cards()
        for card in cards:
            if card['Id'] == sell_id:
                card['Availability'] = 'Available'
                write.write_cards('pokemon_cards.txt', cards)
                print("card added to inventory")
                break
        else:
            print(f"Card with ID {sell_id} not found.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error selling card: {e}")
