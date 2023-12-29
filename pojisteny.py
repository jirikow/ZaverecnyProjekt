class Pojisteny():
    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek
    def cele_jmeno(self):
        return f"{self.jmeno} {self.prijmeni}"
    def __str__(self): # přetížení metody toString
        return f"{self.jmeno}\t {self.prijmeni}\t {self.telefon}\t {self.vek}"
