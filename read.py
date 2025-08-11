
def load_inventory(file_path):
    #creation of empty list land
    cards=[]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                #cleaning data
                data= line.strip().split(",")
                if len(data)==4:
                    card={'Id':data[0],
                          'Name':data[1], 
                            'Rarity':data[2],
                            'Quantity':int(data[3]) 
                            }
                    cards.append(card)
                else:
                    print("issue") 
                    
        pass
    except FileNotFoundError:
        pass

    return cards

