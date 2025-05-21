from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")
from random import choice

# Lijst van decaankandidaten
kandidaten = [
    DecaanKandidaat("Dr. Jupiler", "Communicatiewetenschappen"),
    DecaanKandidaat("Prof. Stella", "Bierkunde"),
    DecaanKandidaat("Prof. Corona", "Geschiedenis")
]

# Lijst van decaankiezers (verdeeld over opleidingen)
opleidingen = ["Communicatiewetenschappen", "Toegepaste Taalkunde", "Geschiedenis", "Wiskunde"]
kiezers = [DecaanKiezer(f"Kiezer {i}", choice(opleidingen)) for i in range(1, 21)]

# Laat elke kiezer proberen te stemmen
for kiezer in kiezers:
    gekozen = choice(kandidaten)
    kiezer.stem(gekozen)

# Toon resultaten
print("\nUitslag decaanverkiezing:")
for kandidaat in kandidaten:
    print(f"{kandidaat.naam} ({kandidaat.opleiding}): {len(kandidaat.stemmen)} stemmen")
