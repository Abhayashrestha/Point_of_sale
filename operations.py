import read
import write
cards=[]

#function to display all available cards in the inventory
def display_inventory():
    cards=read.load_inventory('pos/pokemon_cards.txt')
    if cards:
        print("Available cards")
        for card in cards:
            if card['Availability']=="Available":
                print (f"Id :{card['Id']},card name: {card['Name']},Rarity: {card['Rarity']},Availability: {card['Availability']}")
            else:
                print
                ("No cards available")

def buy_card(buy_id, buy_quantity):
        cards=read.load_inventory('pos/pokemon_cards.txt')
        for card in cards:
            if card['Id']==buy_id and card['Availability']=='Available':
                print ("purchase sucessfull")
                card ['Availability']=='Not Available'
                write.write_cards('pos\pokemon_cards.txt',cards)
            else:
                print("error")

    

def purchase():
    try:
        pass
    except:
        pass
    


