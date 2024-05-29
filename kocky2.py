import sys
import requests
import json

# Pekna prace!
# Chvalim:
#   - strucnost a citelnost
#   - pouziti komentaru
#   - precteni dokumentace k requests a zjisteni, ze timeout akceptuje i tuple
#   - kontrolu, ze ta data take klic 'text' mit nemuseji
# Par nametu:
#   - Ktere hodnoty v kodu by bylo vhodne definovat jako konstanty?
#   - Seznam prochazime dvakrat (1. vytazeni 'text', 2. ocislovani); dalo by se zaridit, aby byl pruchod seznamem jen jeden?
#   - Funkce enumerate ma parametr `start`.

try:
    # Vytvoření API requestu s extrémně krátkým timeoutem
    # response = requests.get("https://cat-fact.herokuapp.com/facts", timeout=(0.001, 0.001))
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params={'amount': 10}, timeout=5)
    data = response.json()
except requests.exceptions.Timeout:
    print("Jsi příliš nedočkavý")
    # Je lepsi zkratit try blok na nezbytne minimum a oddelit tak 1. ziskani dat, 2. transformaci dat a 3. zapis dat.
    # Potom ale tady chceme program ukoncit.
    sys.exit(1)

# Získání hodnot, které jsou přiřazené ke klíči "text"
cat_facts = [fact["text"] for fact in data if "text" in fact]

# Vytvoření číslovaného seznamu
numbered_cat_facts = [f"{i + 1}. {fact}" for i, fact in enumerate(cat_facts[:10])]

# Vytvoření JSON souboru s fakty o kočkách
with open("kocici_fakta.json2", "w") as file:
    json.dump(numbered_cat_facts, file, indent=4)
