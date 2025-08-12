import read
import write
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

def buy_card(name, buy_id, buy_quantity):
    try:
        cards=read.load_inventory('pos\pokemon_cards.txt')
        for card in cards:
            if card ['Id']==buy_id and card[['Quantity']]>buy_quantity:
                card ['Quantity']=card['Quantity']-buy_quantity
                write.write_cards('pos\pokemon_cards.txt',cards)
                


    except:
        pass
    

def purchase():
    try:
        pass
    except:
        pass
    


