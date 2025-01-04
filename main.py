# main.py

# Importacions de mòduls
# Importem les classes i excepcions necessàries del sistema ERP.
# Aquestes inclouen clients, comandes, productes i errors personalitzats per gestionar situacions específiques.
from gestio_erp.clients import Client
from gestio_erp.comandes import Comanda
from gestio_erp.productes import Producte
from gestio_erp.errors import ProducteJaExisteixError, ProducteNoExisteixError

# Funció principal
# Aquesta és la funció d'entrada principal del programa, on es defineixen i executen les operacions
# relacionades amb la gestió de clients, comandes i productes.

def main():
    # Creació de clients
    # En aquesta secció, es defineixen tres clients amb un identificador únic, nom i correu electrònic.
    anna = Client(1, "Anna", "anna@example.com")
    pere = Client(2, "Pere", "pere@example.com")
    joan = Client(3, "Joan", "joan@example.com")

    # Creació de productes
    # Aquí es defineixen diversos productes que es podran afegir a les comandes.
    # Cada producte només requereix un nom per inicialitzar-se.
    bicicleta = Producte("bicicleta")
    casc = Producte("casc")
    guants = Producte("guants")
    maillot = Producte("maillot")
    roda = Producte("roda")
    pantalons = Producte("pantalons")

    # Creació de comandes
    # Es creen comandes per als clients i s'hi afegeixen productes amb les quantitats desitjades.
    comanda_anna_1 = Comanda(101)
    comanda_anna_1.afegir_producte(bicicleta, 1)
    comanda_anna_1.afegir_producte(casc, 2)

    comanda_anna_2 = Comanda(102)
    comanda_anna_2.afegir_producte(guants, 1)

    comanda_pere_1 = Comanda(103)
    comanda_pere_1.afegir_producte(maillot, 1)
    comanda_pere_1.afegir_producte(roda, 2)

    comanda_pere_2 = Comanda(104)
    comanda_pere_2.afegir_producte(guants, 2)

    # Assignació de comandes a clients
    # Aquesta secció associa les comandes creades als clients corresponents.
    anna.afegir_comanda(comanda_anna_1)
    anna.afegir_comanda(comanda_anna_2)

    pere.afegir_comanda(comanda_pere_1)
    pere.afegir_comanda(comanda_pere_2)

    # Primera sortida de comandes
    # Es mostra un resum de les comandes de cada client.
    print("COMANDES DELS CLIENTS")
    for client in [anna, pere, joan]:
        print(f"Comandes del client {client.nom}: {len(client.llistar_comandes())}")
        if client.llistar_comandes():
            for comanda in client.llistar_comandes():
                resum = comanda.resum()
                productes = ", ".join([f"{nom}: {quantitat}" for nom, quantitat in resum["productes"].items()])
                print(f"Comanda {resum['id']} [{resum['estat']}]: {productes}")
        else:
            print(f"El client {client.nom} no té cap comanda.")

    # Gestió d'errors
    # Es gestionen situacions específiques utilitzant excepcions personalitzades.
    try:
        # Intentem afegir un producte que ja existeix a la comanda.
        comanda_anna_1.afegir_producte(bicicleta)
    except ProducteJaExisteixError as e:
        print(e)

    try:
        # Intentem modificar la quantitat d'un producte que no existeix.
        comanda_anna_1.modificar_quantitat(Producte("patinet"), 1)
    except ProducteNoExisteixError as e:
        print(e)

    # Modificació de comandes
    # Es realitzen canvis a una comanda existent, com modificar quantitats, afegir nous productes
    # i canviar l'estat de la comanda.
    comanda_anna_1.modificar_quantitat(bicicleta, 1)
    comanda_anna_1.modificar_quantitat(casc, 2)
    comanda_anna_1.afegir_producte(pantalons, 1)
    comanda_anna_1.modificar_estat(Comanda.ESTAT_ENVIADA)

    # Segona sortida de comandes
    # Es mostra el resum actualitzat de les comandes després de les modificacions.
    print("COMANDES DELS CLIENTS")
    print(f"Comandes del client {anna.nom}: {len(anna.llistar_comandes())}")
    for comanda in anna.llistar_comandes():
        resum = comanda.resum()
        productes = ", ".join([f"{nom}: {quantitat}" for nom, quantitat in resum["productes"].items()])
        print(f"Comanda {resum['id']} [{resum['estat']}]: {productes}")
    print("None")

# Punt d'entrada
# Aquesta condició assegura que la funció `main` només s'executi si el fitxer s'executa directament,
# no si es carrega com a mòdul en un altre script.
if __name__ == "__main__":
    main()