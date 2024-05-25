import requests
import json

try:
    # Vytvoření API requestu s extrémně krátkým timeoutem
    response = requests.get("https://cat-fact.herokuapp.com/facts", timeout=(0.001, 0.001))  # timeout for connect and read
    data = response.json()

    # Získání hodnot, které jsou přiřazené ke klíči "text"
    cat_facts = [fact["text"] for fact in data if "text" in fact]

    # Vytvoření číslovaného seznamu
    numbered_cat_facts = [f"{i + 1}. {fact}" for i, fact in enumerate(cat_facts[:10])]

    # Vytvoření JSON souboru s fakty o kočkách
    with open("kocici_fakta.json2", "w") as file:
        json.dump(numbered_cat_facts, file, indent=4)

except requests.exceptions.Timeout:
    print("Jsi příliš nedočkavý")