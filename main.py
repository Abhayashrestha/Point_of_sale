#importing necessary files
import read
import operations
#creating a simple list to store card info
cards=[]

def main():
    file_path='pos/pokemon_cards.txt'
    read.load_inventory(file_path)
    print("----------------------------------------------------------")
    print("-------------Abhaya's Pokemon Card corner-----------------")
    print("----------------------------------------------------------")

    options=["Press 1 to view inverntory", "Press 2 to buy card", "Press 3 to sell cards","Press 4 to exit"]
    for option in options:
        print(option)
    try:   
        choice = int(input("Please Enter your choice here : "))
        if choice == 1:
            print("----------------------------------------------------------")
            print("-------------Abhaya's Pokemon Card corner-----------------")
            print("----------------------------------------------------------")
            operations.display_inventory()
    except:
        pass
    try:  
        if choice == 2:
            while True:
                print("----------------------------------------------------------")
                print("-------------Abhaya's Pokemon Card corner-----------------")
                print("----------------------------------------------------------")
                operations.display_inventory()
                name=input("Please enter your name: ")
                buy_id=int(input("Please enter the ID of the card you would like to purchase: "))
                buy_quantity=int(input("Please enter the quantity of card you would like to purchase: "))
                
    except:
        pass


main()
__name__="main"


