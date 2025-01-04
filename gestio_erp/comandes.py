# gestio_erp/comandes.py

# Importació d'excepcions personalitzades
# Es carreguen les excepcions `ProducteJaExisteixError` i `ProducteNoExisteixError` 
# per gestionar errors específics relacionats amb els productes en una comanda.
from gestio_erp.errors import ProducteJaExisteixError, ProducteNoExisteixError

# Definició de la classe `Comanda`
# Aquesta classe representa una comanda dins del sistema ERP, amb atributs per identificar-la,
# gestionar els productes associats i el seu estat.

class Comanda:
    # Constants d'estat
    # Es defineixen constants per representar els possibles estats d'una comanda:
    # - `ESTAT_PENDENT`: La comanda encara no ha estat enviada.
    # - `ESTAT_ENVIADA`: La comanda ja ha estat enviada.
    ESTAT_PENDENT = "Pendent"
    ESTAT_ENVIADA = "Enviada"

    # Constructor de la classe `Comanda`
    # Inicialitza una comanda amb un identificador únic (`id_comanda`), un diccionari buit de productes (`productes`),
    # i un estat inicial (`estat`) que per defecte és "Pendent".
    def __init__(self, id_comanda):
        self.id_comanda = id_comanda  # Identificador únic de la comanda
        self.productes = {}  # Diccionari per emmagatzemar els productes i les seves quantitats
        self.estat = self.ESTAT_PENDENT  # Estat inicial de la comanda

    # Mètode `afegir_producte`
    # Afegeix un producte a la comanda amb una quantitat especificada (per defecte, 1).
    # Si el producte ja existeix a la comanda, es llança una excepció `ProducteJaExisteixError`.
    def afegir_producte(self, producte, quantitat=1):
        if producte.nom in self.productes:
            raise ProducteJaExisteixError(f"El producte {producte.nom} ja existeix a la comanda.")
        self.productes[producte.nom] = quantitat

    # Mètode `modificar_quantitat`
    # Modifica la quantitat d'un producte existent a la comanda.
    # Si el producte no existeix, es llança una excepció `ProducteNoExisteixError`.
    def modificar_quantitat(self, producte, quantitat):
        if producte.nom not in self.productes:
            raise ProducteNoExisteixError(f"El producte {producte.nom} no existeix a la comanda.")
        self.productes[producte.nom] += quantitat

    # Mètode `modificar_estat`
    # Canvia l'estat de la comanda a un nou valor especificat.
    # Paràmetres:
    # - `estat`: Nou estat per a la comanda (ex., "Enviada").
    def modificar_estat(self, estat):
        self.estat = estat

    # Mètode `resum`
    # Retorna un diccionari amb un resum de la comanda, incloent-hi:
    # - `id`: Identificador de la comanda.
    # - `estat`: Estat actual de la comanda.
    # - `productes`: Diccionari de productes amb les seves quantitats.
    def resum(self):
        return {"id": self.id_comanda, "estat": self.estat, "productes": self.productes}