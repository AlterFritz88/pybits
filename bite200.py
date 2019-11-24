from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "temp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


rome_dict = {
    'I' :   1,
    'II':   2,
    'III':  3,
    'IV':   4,
    'V':    5,
    'VI':   6,
    'VII':  7,
    'VIII': 8
}

class Enchantment:
    """Minecraft enchantment class

    Implements the following:
        id_name, name, max_level, description, items
    """

    def __init__(self, id_name, name, max_level, decription, items=None):
        if items is None:
            items = []
        self.id_name = id_name
        self.name = " ".join([x.capitalize() if x != 'of' else x for x in name.split(" ") ])
        self.max_level = max_level
        self.description = decription
        self.items = items

    def __str__(self):
        return f'{self.name} ({self.max_level}): {self.description}'


class Item:
    """Minecraft enchantable item class

    Implements the following:
        name, enchantments
    """

    def __init__(self, name, items=None):
        if items is None:
            items = []
        self.name = name
        self.enchantments = items


    def __str__(self):
        answer_str = ""
        answer_str += " ".join([x.capitalize() for x in self.name.split("_")]) + ": \n"
        for_show = sorted(self.enchantments, key=lambda x: x.id_name)
        for i, item in enumerate(for_show):
            if i != len(self.enchantments) - 1:
                answer_str += f"  [{item.max_level}] {item.id_name}\n"
            else:
                answer_str += f"  [{item.max_level}] {item.id_name}"
        return answer_str


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects

    With the key being the id_name of the enchantment.
    """
    dict_ench = {}
    tfs = soup.find_all('tr')
    for tr in tfs[1:]:
        td = tr.find_all('td')
        items = []
        name = td[0].text.split('(')[0]
        id_name = td[0].find_all('em')[0].text
        max_level = rome_dict[td[1].text]
        description = td[2].text
        img = td[4].find('img')['data-src'].split('/')[-1].replace("enchanted_", "").replace("_sm", "").replace(".png", "")
        if 'fishing_rod' not in img:
            items = img.split('_')
        else:
            img = img.replace("_fishing_rod", "").replace("fishing_rod", "")
            items = img.split('_')
            items.append('fishing_rod')
            items = [x for x in items if x != '']
        dict_ench[id_name] = Enchantment(id_name, name, max_level, description, items)
    return dict_ench


def generate_items(data):
    """Generates a dictionary of Item objects

    With the key being the item name.
    """
    items = set()
    dict_items = {}

    for k, v in data.items():
        for chip in v.items:
            items.add(chip)
    items = sorted(items)
    for item in items:
        new_items = []
        for k, v in data.items():
            if item in v.items:
                new_items.append(v)
        new_item = Item(item, new_items)
        dict_items[new_item.name] = new_item
    return dict_items


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.

    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""