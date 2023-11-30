from datetime import datetime

class Szoba():
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam}-számban, ára: {self.ar}."

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam}-számban, ára: {self.ar}."

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, nap):
        for szoba in self.szobak:
            if szoba.szobaszam == int(szobaszam):
                if self.ervenyes_datum(nap):
                    foglalas = Foglalas(szoba, nap)
                    self.foglalasok.append(foglalas)
                    return f"A(z) {szobaszam}-számú szoba foglalva a(z) {nap}. napra. Ár: {szoba.ar}"
                else:
                    return "Érvénytelen dátum. Kérjük, adjon meg jövőbeni dátumot."
        return "Nincs ilyen szoba."


    def lemondas(self, szobaszam, nap):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.nap == nap:
                foglalas.szoba.foglalva = False
                self.foglalasok.remove(foglalas)
                return f"A(z) {szobaszam}-számú szoba foglalása lemondva a(z) {nap}. napra."
        return f"Nincs ilyen foglalás."

    def listaz_foglalasok(self):
        foglalasok_str = "\n".join([f"Foglalás a(z) {f.szoba.szobaszam}-számú szobára, {f.nap}. napra." for f in self.foglalasok])
        return f"Összes foglalás:\n{foglalasok_str}"

    def ervenyes_datum(self, nap):
        try:
            nap_obj = datetime.strptime(nap, "%Y-%m-%d")
            return nap_obj > datetime.now()
        except ValueError:
            return False

class Foglalas:
    def __init__(self, szoba, nap):
        self.szoba = szoba
        self.nap = nap
def inicializalas():
    szalloda = Szalloda(nev="La Panzió")
    szalloda.szoba_hozzaad(EgyagyasSzoba(szobaszam=31, ar=12000))
    szalloda.szoba_hozzaad(EgyagyasSzoba(szobaszam=32, ar=15000))
    szalloda.szoba_hozzaad(EgyagyasSzoba(szobaszam=33, ar=12000))
    szalloda.szoba_hozzaad(KetagyasSzoba(szobaszam=41, ar=24000))
    szalloda.szoba_hozzaad(EgyagyasSzoba(szobaszam=34, ar=14000))
    szalloda.szoba_hozzaad(KetagyasSzoba(szobaszam=42, ar=29000))

    szalloda.foglalas(szobaszam=31, nap="2023-12-21")
    szalloda.foglalas(szobaszam=32, nap="2023-12-23")
    szalloda.foglalas(szobaszam=33, nap="2023-12-30")
    szalloda.foglalas(szobaszam=41, nap="2024-01-09")
    szalloda.foglalas(szobaszam=34, nap="2024-02-17")

    return szalloda

def felhasznaloi_interfesz(szalloda):
    while True:
        print("\nVálassza ki a kívánt műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Listázása")

        valasztas = input("Választás: ")

        if valasztas == "foglalas" or valasztas == "1":
            szobaszam = input("Adja meg a szobaszámot: ")
            nap = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            print(szalloda.foglalas(szobaszam, nap))
        elif valasztas == "lemondas" or valasztas == "2":
            szobaszam = input("Adja meg a szobaszámot: ")
            nap = input("Adja meg a lemondás dátumát (YYYY-MM-DD): ")
            print(szalloda.lemondas(szobaszam, nap))
        elif valasztas == "listazas" or valasztas == "3":
            print(szalloda.listaz_foglalasok())
        else:
            print("Ez a választás nincs a listán. Kérem, válasszon újra.")



szalloda = inicializalas()
felhasznaloi_interfesz(szalloda)