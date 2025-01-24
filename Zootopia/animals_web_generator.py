import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

def print_animal_info(animal):
    """Prints animal information
    Args:
      animal: A dictionary showing an animal from the JSON data.
    """
    if 'name' in animal:
        print(f"Name: {animal['name']}")
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")
    if 'locations' and animal['locations']:
        print(f"Location: {animal['locations'][0]}")
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        print(f"Type: {animal['characteristics']['type']}")
    print()


with open('animals_data.json', 'r') as f:
    data = json.load(f)
    for animal in data:
        print_animal_info(animal)

