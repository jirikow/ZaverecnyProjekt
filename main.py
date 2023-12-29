from spravaPojistenych import SpravaPojistenych

pojisteni = SpravaPojistenych()
volba = None
while volba != "4":
    print(""" 
----------------------------
EVIDENCE POJIŠTĚNÝCH
----------------------------
1. Přidat nového pojištěného
2. Vypsat všechny pojištěné
3. Vyhledat pojištěného
4. Konec
    """)
    volba = input("Zadejte prosím voĺbu (1-4): ")
    if volba == "1":
        print("** Přidat nového pojištěného **")
        jmeno = None
        prijmeni = None
        telefon = None
        vek = None
        while not jmeno: # zkontroluje zda bylo něco zadáno, jinak opakuje volbu
            jmeno = input("Zadejte křestní jméno: ").strip().capitalize()
        while not prijmeni:
            prijmeni = input("Zadejte příjmeni: ").strip().capitalize()
        while not telefon:
            telefon = input("Zadejte telefoní číslo: ").strip()
        while not vek:
            vek = input("Zadejte věk: ")

        pojisteni.pridat(jmeno, prijmeni, telefon, vek)
        print("Nový pojištěnce byl přidán.")

    elif volba == "2":
        print("** Seznam pojištěných **")
        vypis = pojisteni.vypsat() # stringový seznam pojistěnců nebo prázdný string
        if not vypis:
            print("Seznam pojištěných je prázdný")
        else:
            print(vypis)

    elif volba == "3":
        hledany_vyraz = input("Zadejte jméno nebo příjmení k vyhledání pojištěného: \n").capitalize()
        nalezeno = pojisteni.vyhledat(hledany_vyraz)
        if not nalezeno:
            print("Nic nenalezeno")
        else:
            print(nalezeno)

    elif volba == "4":
        print("Ukončuji program...")
        break

    else:
        print("Špatná volba, prosím zadejte hodnotu mezi 1-4. ")

