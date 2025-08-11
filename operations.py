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

def buy_card():
    try:
        buy_id=int(input("Enter the id of the card you would like to buy"))
        if buy_id==list.id:
            print("The card is available for purchase")
            buy_quantity=int(input("Enter the number of card you would like to purchase"))
            print(f"You have sucessfully purchased {buy_quantity} of cards")
    except TypeError:
        print("please Enter valid input")
        pass
    


