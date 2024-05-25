import requests
import json

# Vytvoření API requestu
response = requests.get("https://cat-fact.herokuapp.com/facts")
data = response.json()

# Získání hodnot, které jsou přiřazené ke klíči "text"
cat_facts = [fact["text"] for fact in data if "text" in fact]

# Vytvoření číslovaného seznamu
numbered_cat_facts = [f"{i + 1}. {fact}" for i, fact in enumerate(cat_facts[:10])]

# Vytvoření JSON souboru s fakty o kočkách
with open("kocici_fakta.json", "w") as file:
     json.dump(numbered_cat_facts, file, indent=4)



