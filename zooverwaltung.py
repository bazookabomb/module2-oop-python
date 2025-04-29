class Art:
    def __init__(self, name):
        self.name = name

class Tier:
    def __init__(self, name, art: Art):
        self.name = name
        self.art = art

class Pfleger:
    def __init__(self, name):
        self.name = name
        self.tiere = []

    def tier_hinzufuegen(self, tier: Tier):
        self.tiere.append(tier)

class Fuetterung:
    def __init__(self, pfleger: Pfleger, tier: Tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self):
        print(f"Pfleger {self.pfleger.name} füttert das Tier {self.tier.name} (Art: {self.tier.art})")

# Erstellung
simba = Tier("Simba", "Löwe")
melman = Tier("Melman", "Giraffe")
pfleger = Pfleger("Tom")
pfleger.tier_hinzufuegen(simba)
pfleger.tier_hinzufuegen(melman)
# Fuetterung
futterrunde = Fuetterung(pfleger, simba)
futterrunde.starten()
# Ausgabe:
# Pfleger Tom füttert das Tier Simba (Art: Löwe).

# andere Tests
