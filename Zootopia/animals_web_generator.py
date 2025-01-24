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

def generate_animal_html(animal):
  """Generates HTML string for a single animal."""
  html_str = ""
  if 'name' in animal:
    html_str += f"<li>Name: {animal['name']}<br>"
  if 'characteristics' in animal and 'diet' in animal['characteristics']:
    html_str += f"Diet: {animal['characteristics']['diet']}<br>"
  if 'locations' and animal['locations']:
    html_str += f"Location: {animal['locations'][0]}<br>"
  if 'characteristics' in animal and 'type' in animal['characteristics']:
    html_str += f"Type: {animal['characteristics']['type']}<br></li>"
  return html_str

def generate_html_content(animals):
  """Generates the complete HTML string for all animals."""
  html_list = ""
  for animal in animals:
    html_list += generate_animal_html(animal)
  return html_list

def main():
  """Reads template, generates HTML, and writes to a new file."""
  with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

  with open("animals_data.json", "r") as data_file:
    animals_data = json.load(data_file)

  animal_html_list = generate_html_content(animals_data)

  # Replace placeholder with generated HTML
  new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html_list)

  with open("animals.html", "w") as output_file:
    output_file.write(new_html_content)

if __name__ == "__main__":
  main()