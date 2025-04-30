class Art:
    def __init__(self, name):
        self.name = name

class Tier:
    def __init__(self, name, art_name):
        self.name = name
        #self.art = art
        #Achtung, Kompositionsbeziehung zu Art
        self.art = Art(art_name)

class Pfleger:
    def __init__(self, name):
        self.name = name
        self.tiere = []

    def tier_hinzufuegen(self, tier: Tier):
        self.tiere.append(tier)

    def tiere_anzeigen(self):
        print(f"Pfleger {self.name} kümmert sich um:")
        for tier in self.tiere:
            print(f"- {tier.name} der Art {tier.art.name}")

class Fuetterung:
    def __init__(self, pfleger: Pfleger, tier: Tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self):
        print(f"Pfleger {self.pfleger.name} füttert das Tier {self.tier.name} (Art: {self.tier.art.name})")

# Erstellung
tier_obj_simba = Tier("Simba", "Löwe")
tier_obj_melman = Tier("Melman", "Giraffe")
pfleger_obj_tom = Pfleger("Tom")
pfleger_obj_tom.tier_hinzufuegen(tier_obj_simba)
pfleger_obj_tom.tier_hinzufuegen(tier_obj_melman)

pfleger_obj_tom.tiere_anzeigen()
# Fuetterung
futterrunde = Fuetterung(pfleger_obj_tom, tier_obj_simba)
futterrunde.starten()
# Ausgabe:
# Pfleger Tom füttert das Tier Simba (Art: Löwe).

# andere Tests
