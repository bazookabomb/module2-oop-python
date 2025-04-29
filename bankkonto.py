class BankKonto:
    inhaber: str
    kontonummer: int
    kontostand: float

    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def kontostand_anzeigen(self):
        print(f"Kontoauszug für {self.inhaber} mit Kontonummer {self.kontonummer}")
        print(f"Aktueller Kontostand: {self.kontostand}")

    def einzahlen(self, betrag):
        if betrag > 0:
            print(f"Es soll der Betrag {betrag} eingezahlt werden")
            self.kontostand += betrag
            print(f"Der neue Kontostand beträgt {self.kontostand}")
        else:
            print("Diese Transaktion war ungültig")
        
    def abheben(self, betrag):
        if betrag > 0 and self.kontostand >= betrag:
            print(f"Es soll der Betrag {betrag} abgehoben werden")
            self.kontostand -= betrag
            print(f"Der neue Kontostand beträgt {self.kontostand}")
        else:
            print("Transaktion ungültig, vielleicht ist das Konto nicht gedeckt")

joels_bankkonto = BankKonto("Joel", 123456, 50)
joels_bankkonto.kontostand_anzeigen()
print("Es soll 50 Euro eingezahlt werden")
joels_bankkonto.einzahlen(-50)
joels_bankkonto.abheben(-50)
joels_bankkonto.kontostand_anzeigen()