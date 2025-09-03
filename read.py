import csv

def load_inventory(file_path):
    """Load inventory data from a CSV file into a list of dicts."""
    cards = []
    try:
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file, fieldnames=['Id', 'Name', 'Rarity', 'Availability'])
            cards = list(reader)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    return cards
