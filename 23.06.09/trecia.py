import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def skaiciuoti_plota_ir_perimetra(ilgis, plotis):
    plotas = ilgis * plotis
    perimetras = 2 * (ilgis + plotis)
    return plotas, perimetras

def main():
    ilgis = float(input("Įveskite stačiakampio ilgį: "))
    plotis = float(input("Įveskite stačiakampio plotį: "))

    plotas, perimetras = skaiciuoti_plota_ir_perimetra(ilgis, plotis)

    print("Stačiakampio plotas:", plotas)
    print("Stačiakampio perimetras:", perimetras)

    logging.info(f"Stačiakampio plotas: {plotas}")
    logging.info(f"Stačiakampio perimetras: {perimetras}")

if __name__ == "__main__":
    main()
