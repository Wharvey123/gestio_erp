# main.py
from gestio_erp.clients import Client
from gestio_erp.comandes import Comanda
from gestio_erp.productes import Producte
from gestio_erp.errors import ProducteJaExisteixError, ProducteNoExisteixError

def main():
    # Crear clients
    anna = Client(1, "Anna", "anna@example.com")
    pere = Client(2, "Pere", "pere@example.com")
    joan = Client(3, "Joan", "joan@example.com")

    # Crear productes
    bicicleta = Producte("bicicleta")
    casc = Producte("casc")
    guants = Producte("guants")
    maillot = Producte("maillot")
    roda = Producte("roda")
    pantalons = Producte("pantalons")

    # Crear comandes
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

    # Assignar comandes a clients
    anna.afegir_comanda(comanda_anna_1)
    anna.afegir_comanda(comanda_anna_2)

    pere.afegir_comanda(comanda_pere_1)
    pere.afegir_comanda(comanda_pere_2)

    # Primera sortida de comandes
    print("COMANDES DELS CLIENTS")
    for client in [anna, pere]:
        print(f"Comandes del client {client.nom}: {len(client.llistar_comandes())}")
        for comanda in client.llistar_comandes():
            resum = comanda.resum()
            productes = ", ".join([f"{nom}: {quantitat}" for nom, quantitat in resum["productes"].items()])
            print(f"Comanda {resum['id']} [{resum['estat']}]: {productes}")
    print("El client Joan no té cap comanda.")

    # Gestionar errors
    try:
        comanda_anna_1.afegir_producte(bicicleta)
    except ProducteJaExisteixError as e:
        print(e)

    try:
        comanda_anna_1.modificar_quantitat(Producte("patinet"), 1)
    except ProducteNoExisteixError as e:
        print(e)

    # Modificar comandes
    comanda_anna_1.modificar_quantitat(bicicleta, 1)
    comanda_anna_1.modificar_quantitat(casc, 2)
    comanda_anna_1.afegir_producte(pantalons, 1)
    comanda_anna_1.modificar_estat(Comanda.ESTAT_ENVIADA)

    # Segona sortida de comandes
    print("COMANDES DELS CLIENTS")
    for client in [anna, pere]:
        print(f"Comandes del client {client.nom}: {len(client.llistar_comandes())}")
        for comanda in client.llistar_comandes():
            resum = comanda.resum()
            productes = ", ".join([f"{nom}: {quantitat}" for nom, quantitat in resum["productes"].items()])
            print(f"Comanda {resum['id']} [{resum['estat']}]: {productes}")
    print("None")

if __name__ == "__main__":
    main()