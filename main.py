def main():
    file_path='pokemon_cards.txt'
    print("----------------------------------------------------------")
    print("-------------Abhaya's Pokemon Card corner-----------------")
    print("----------------------------------------------------------")

    options=["Press 1 to view inverntory", "Press 2 to buy card", "Press 3 to sell cards","Press 4 to exit"]
    for option in options:
        print(option)
    try:   
        choice = int(input("Please Enter your choice here : "))
        if choice is 1:
            print("----------------------------------------------------------")
            print("-------------Abhaya's Pokemon Card corner-----------------")
            print("----------------------------------------------------------")

            

    except:
        pass



main()
__name__="main"


