from pojisteny import Pojisteny

class SpravaPojistenych:
    def __init__(self):
        self.seznamPojistenych = list()

    def pridat(self, jmeno, prijmeni, telefon, vek): # vytvoří objekt pojištěnce a přidá do seznamu
        pojistenec = Pojisteny(jmeno, prijmeni, telefon, vek)
        self.seznamPojistenych.append(pojistenec)

    def vypsat(self): # projde seznam pojistencu a zavolá nad jednotlivýma objektama metodu toString nebo vrátí prázdný string
        vysledek = ""
        for pojistenec in self.seznamPojistenych:
            vysledek += str(pojistenec) + "\n"
        return vysledek

    def vyhledat(self, hledany_vyraz): # projde seznam pojištěnců a vyhledá výraz, zavolá toString nad nalezenýma objektama nebo vrátí prázdný string
        vysledek = ""
        for pojistenec in self.seznamPojistenych:
            if hledany_vyraz in pojistenec.cele_jmeno():
                vysledek += str(pojistenec) + "\n"
        return vysledek
