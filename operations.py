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
    try: 
        cards=read.load_inventory('pos/pokemon_cards.txt')
        for card in cards:
            if card['Id']==buy_id and card['Availability']=='Available':
                card ['Availability']=='Not Available'
                write.write_cards('pos/pokemon_cards.txt',cards)
                print ("purchase sucessfull") 
                break
            else:
                print(f"Card with ID {Id} is not available for rent.")
    except FileNotFoundError: #helps to handle the file not found error smoothly
            print("Error: File not found. Please check the file path.")
    except Exception as e: #helps to catch and fix general exceptions by displaying and error message
            print(f"Error renting land: {e}")

def purchase():
    try:
        pass
    except:
        pass
    


