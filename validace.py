import re

class Validace:

    @staticmethod
    def jeCislo(text): # vríté číslo nebo false pokud nenajde číslo
        if text is None:
            return False
        nalezeno = re.search("^\d+$", text) # hledá ve stringu číslo (musí obsahovat jen číslo "d")
        if not nalezeno:
            return False
        return int(text)

    @staticmethod
    def jeVek(text):
        cislo = Validace.jeCislo(text)
        if not cislo:
            return False
        if cislo < 150:
            return True
        return False

    @staticmethod
    def jeTelefon(text):
        if text is None:
            return False
        regex = "^([\+]?[(]?[0-9]{3}[)]?[-\s\.]?)?((([0-9]{3}[-\s\.]?){3})|([0-9]{3}[-\s\.]?[0-9]{4,6}))$"
        nalezeno = re.search(regex, text)
        if not nalezeno:
            return False
        return True
