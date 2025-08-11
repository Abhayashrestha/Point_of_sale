import read
cards=[]

#function to display all available cards in the inventory
def display_inventory():
    cards=read.load_inventory('pos/pokemon_cards.txt')
    if cards:
        print("Number of cards")
        for card in cards:
            if card['Quantity'] >0:
                print (f"Id :{card['Id']},card name: {card['Name']},Rarity: {card['Rarity']},Quantity: {card['Quantity']}")
            else:
                print
                ("No cards available")


