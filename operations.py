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
                card ['Availability']=='Not Available'
                write.write_cards('pos/pokemon_cards.txt',cards)
                print ("purchase sucessfull")
                generate_rent_invoice(name, duration)#calling generate_rent_invoice function to generate a bill text file
                prnt_bills_rent(name, duration)#calling prnt_bills_rent to print bill on screen for user after renting a land 
                break
            

def purchase():
    try:
        pass
    except:
        pass
    


