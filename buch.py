class Buch:
    titel: str
    autor: str
    seiten: int

    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten

    def info(self):
        print(f"Titel: {self.titel}, Autor: {self.autor}, Seiten: {self.seiten}")

    def lesezeit_schaetzen(self):
        # durchschnitt 40 seiten pro stunde
        lesedauer = self.seiten / 40
        print(f"Ungefähre Lesedauer (40 Seiten pro Stunde): {lesedauer:.2f} Stunden")

    def verbleibende_seiten(self, aktuelle_seite):
        if aktuelle_seite >= 0 and aktuelle_seite <= self.seiten:
            print(f"Verbleibende Seiten: {self.seiten - aktuelle_seite}")
        else:
            print("ungültige Seite")

harry_potter_1 = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 336)
harry_potter_2 = Buch("Harry Potter und die Kammer des Schreckens", "J.K. Rowling", 352)
harry_potter_3 = Buch("Harry Potter und der Gefangene von Askaban", "J.K. Rowling", 448)

harry_potter_1.info()
harry_potter_1.lesezeit_schaetzen()

harry_potter_2.info()
harry_potter_2.lesezeit_schaetzen()

harry_potter_3.info()
harry_potter_3.lesezeit_schaetzen()
