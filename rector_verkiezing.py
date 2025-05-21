from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
kandidaten = [
    RectorKandidaat("Prof Kanye West ", "Geneeskunde"),
    RectorKandidaat("Dr.Persoons ", "Ingenieurswetenschappen"),
    RectorKandidaat("Prof. Maes", "Rechten")
]

# Lijst van kiezers
kiezers = [Kiezer(f"Kiezer {i}") for i in range(1, 21)]

# Elke kiezer stemt op een willekeurige kandidaat
for kiezer in kiezers:
    gekozen = choice(kandidaten)
    stem = RectorStem(gekozen, gekozen.faculteit)
    gekozen.geef_stem(stem)
    print(f"{kiezer.naam} stemt: {stem}")

# Resultaten tonen
print("\nUitslag rectorverkiezing:")
for kandidaat in kandidaten:
    print(f"{kandidaat.naam}: {len(kandidaat.stemmen)} stemmen")