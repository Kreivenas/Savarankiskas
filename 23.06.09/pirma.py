class Banko_saskaita:
    def __init__(self, saskaitos_numeris):
        self.Tavo_saskaita = saskaitos_numeris
        self.balansas = 0

    def papildymas(self, isuma):
        self.balansas += isuma
        return f"Papildymas: {isuma} Euru. Naujas likutis: {self.balansas}"

    def ismokejimas(self, issuma):
        if self.balansas >= issuma:
            self.balansas -= issuma
            return f"Ismokejimas: {issuma} euru. Naujas likutis: {self.balansas}"
        else:
            return "Nepakanka lesu "

    def Likutis(self):
        return self.balansas


saskaita = Banko_saskaita("1234567890")

print(saskaita.papildymas(1200))

print(saskaita.ismokejimas(50))

galutinis_balansas = saskaita.Likutis()
print("Likutis:", galutinis_balansas)
