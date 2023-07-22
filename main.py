import time

class Pojisteny:
    pojistenci = []

    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek
        Pojisteny.pojistenci.append(self)


class SpravaPojisteni:
    @staticmethod
    def smazat_pojisteneho(jmeno, prijmeni):
        for pojisteny in Pojisteny.pojistenci:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                Pojisteny.pojistenci.remove(pojisteny)
                return True
        return False

    @staticmethod
    def zobrazit_seznam_pojistenych():
        if len(Pojisteny.pojistenci) > 0:
            for pojisteny in Pojisteny.pojistenci:
                print(f"Jméno: {pojisteny.jmeno.capitalize()}")
                print(f"Příjmení: {pojisteny.prijmeni.capitalize()}")
                print(f"Telefon: {pojisteny.telefon}")
                print(f"Věk: {pojisteny.vek}")
                print("------------------------")
        else:
            print("Žádní pojištěnci nenalezeni.")
            time.sleep(2)

while True:
    print("----------------------------------")
    print("Evidence pojištěných")
    print("----------------------------------")

    print("Vyberte číslo ze seznamu:")
    print("1. Vložit pojištěného")
    print("2. Smazat pojištěného")
    print("3. Vypsat seznam pojištěných osob")
    print("0. Konec")

    volba = input("Zadejte číslo a potvrdte Enter: ")

    if volba == "1":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")

        while not jmeno.isalpha() or not prijmeni.isalpha():
            print("Jméno a příjmení mohou obsahovat pouze písmena abecedy.")
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")

        jmeno = jmeno.upper()
        prijmeni = prijmeni.upper()

        while True:
            telefonni_cislo = input("Zadejte telefonní číslo bez předvolby (9 číslic): ")
            if len(telefonni_cislo) == 9 and telefonni_cislo.isdigit():
                break
            else:
                print("Neplatné telefonní číslo. Zadejte prosím telefoní číslo bez predvolby (9 číslic).")
        while True:
            vek = input("Zadejte věk: ")
            if vek.isdigit():
                break
            else:
                print("Neplatný věk. Zadejte prosím číslo.")
        pojisteny = Pojisteny(jmeno, prijmeni, telefonni_cislo, vek)
        print("Pojištěný byl úspěšně vložen.")

    elif volba == "2":
        jmeno = input("Zadejte jméno: ").upper()
        prijmeni = input("Zadejte příjmení: ").upper()
        if SpravaPojisteni.smazat_pojisteneho(jmeno, prijmeni):
            print("Pojištěný byl úspěšně smazán.")
        else:
            print("Pojištěný nebyl nalezen.")

    elif volba == "3":
        SpravaPojisteni.zobrazit_seznam_pojistenych()

    elif volba == "0":
        print("Dekuji za použití programu.")
        time.sleep(2)
        break

    else:
        print("Neplatná volba. Zadejte platné číslo.")
