def write_cards(file_path, cards):
    with open(file_path, "w") as file:
        for card in cards:
            line = f"{card['Id']},{card['Name']},{card['Rarity']},{card['Availability']}\n"
            file.write(line)
