""" 4 třídy, které budou dohromady tvořit zoologickou zahradu """

""" Třída zvíře obsahuje atributy "jmeno:str, druh:str a vaha:int". Všechny parametry 
se nastavují pomocí metody __init__()
Přidej třídě metodu __str__()
Přidej metodu "export_to_dict() """

class Zvire:
    def __init__(self, jmeno:str, druh:str, vaha:int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return f"Zvíře {self.jmeno} je {self.druh} a váží {self.vaha}kg."
    
    def export_to_dict(self):
        return {"jmeno": self.jmeno, "druh": self.druh, "vaha": self.vaha}
    
pavouk = Zvire ("Adolf", "Tarantule Velká", 0.1)
pavouk_export = pavouk.export_to_dict()
assert pavouk_export["jmeno"] == "Adolf"
assert pavouk_export ["druh"] == "Tarantule Velká"
assert pavouk_export ["vaha"] == 0.1

""" ## Třída `Zamestnanec`

Tato třída bude obsahovat atributy `cele_jmeno:str`, `rocni_plat:int` a 
`pozice:str`. Všechny parametry jsou povinné a budou se nastavovat v metodě `__init__()`

Zaměstnanci dále přidej:

* metodu `__str__()`, formát výpisu je na tobě
* metodu `ziskej_inicialy()`, která bude vracet výstup ve formátu `A.W.`, 
uvažuj pouze změstnance se dvěma jmény. """
    
class Zamestnanec:
    def __init__(self, cele_jmeno: str, rocni_plat:int, pozice: str ):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice

    def __str__(self):
        return f"Zaměstnanec {self.cele_jmeno} pracuje na pozici {self.pozice} a jeho roční plat je {self.rocni_plat}."
    
    def ziskej_inicialy (self):
        jmena = self.cele_jmeno.split()
        return f"{jmena[0][0]}.{jmena[1][0]}."
    
""" Třída "ředitel":
Tato třída bude dědit od třídy `Zamestnanec`, 
jediné co bude mít navíc je parametr `oblibene_zvire: Zvire`, 
parametr bude typu `Zvire` (třída kterou jsi už vytvořil/a). 
Parametr `pozice` rovnou nastav na `'Reditel'`.  """

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str, oblibene_zvire):
        super().__init__(cele_jmeno, rocni_plat, pozice="reditel")
        self.oblibene_zvire = oblibene_zvire
    
    def __str__(self):
         return f"{super().__str__()}, jeho oblíbené zvíře je {self.oblibene_zvire.jmeno}."

""" Třída "Zoo"
Třída `Zoo`

Třída `Zoo` bude mít 5 atributů:

* `jmeno:str`
* `adresa:str`
* `reditel: Reditel` - objekt typu `Reditel`
* `zamestnanci: List[Zamestnanec]` - list objektů typu `Zamestnanec` (naši vytvoření zaměstnanci)
* `zvirata: List[Zvire]` - list objektů typu `Zvire` (naše vytvořená zvířata)

a dvě metody:

*`vaha_vsech_zvirat_v_zoo()` - vrací číslo reprezentující součet váhy všech zvířat v zoologické zahradě
*`mesicni_naklady_na_zamestnance()` - vrací číslo reprezentující **měsíční** náklady na zaměstnance zoologické zahrady (Nezapomeň na ředitele!)
 """

class Zoo:
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, zamestnanci: list[Zamestnanec], zvirata: list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata
    
    def vaha_vsech_zvirat_v_zoo(self) -> int:
        return sum(zvire.vaha for zvire in self.zvirata)

    def mesicni_naklady_na_zamestnance(self) -> int:
        total_plat = sum(zamestnanec.rocni_plat for zamestnanec in self.zamestnanci)
        total_plat += self.reditel.rocni_plat  # Přidáváme plat ředitele
        return total_plat // 12  # Převádíme roční platy na měsíční

   

 # Vytvoř objekty typu "zvire" z následujícího seznamu slovníků (použij for cyklus):

zvirata_dict = [
   {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700}, 
]

zvirata = []
for zvire in zvirata_dict:
    objekt_zvire = Zvire(jmeno=zvire['jmeno'], druh=zvire['druh'], vaha=zvire['vaha'])
    zvirata.append(objekt_zvire)

for zvire in zvirata:
    print(zvire)

 
 # ytvoř objekty typu `Zamestnanec` z následujícího seznamu slovníků (použij for cyklus):

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

zamestnanci = []
for zamestnanec in zamestnanci_dict:
        novy_zamestnanec = Zamestnanec(cele_jmeno=zamestnanec['cele_jmeno'],
        rocni_plat=zamestnanec['rocni_plat'], pozice=zamestnanec['pozice'])
        zamestnanci.append(novy_zamestnanec)

for zamestnanec in zamestnanci:
    print (zamestnanec)
   
# Vytvoření objektu ředitele
reditel = Reditel("Jan Novák", 900000, "reditel", zvirata[0])

# Vytvoření objektu Zoo
zoo = Zoo("Zoo Praha", "U Trojského zámku 120/3, Praha 7", reditel, zamestnanci, zvirata)

# Tisk celkové váhy zvířat v zoo
print("Celková váha zvířat v zoo:", zoo.vaha_vsech_zvirat_v_zoo(), "kg")

# Tisk měsíčních nákladů na zaměstnance
print("Měsíční náklady na zaměstnance:", zoo.mesicni_naklady_na_zamestnance(), "CZK")