class Figūra:
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis

    def plotas(self):
        return self.ilgis * self.plotis

    def perimetras(self):
        return 2 * (self.ilgis + self.plotis)


class Stačiakampis(Figūra):
    def __init__(self, ilgis, plotis):
        super().__init__(ilgis, plotis)

    def plotas(self):
        return self.ilgis * self.plotis

    def perimetras(self):
        return 2 * (self.ilgis + self.plotis)


class StatusisTrikampis(Figūra):
    def __init__(self, ilgis, plotis):
        super().__init__(ilgis, plotis)

    def plotas(self):
        return 0.5 * self.ilgis * self.plotis

    def perimetras(self):
        return self.ilgis + self.plotis + self.hipotenuzė()

    def hipotenuzė(self):
        return (self.ilgis ** 2 + self.plotis ** 2) ** 0.5


stačiakampis = Stačiakampis(7, 22)
trikampis = StatusisTrikampis(5, 12)

print("Stačiakampio informacija:")
print("Plotas:", stačiakampis.plotas())
print("Perimetras:", stačiakampis.perimetras())
print()

print("Stačiojo trikampio informacija:")
print("Plotas:", trikampis.plotas())
print("Perimetras:", trikampis.perimetras())
