# gestio_erp/comandes.py
from gestio_erp.errors import ProducteJaExisteixError, ProducteNoExisteixError

class Comanda:
    ESTAT_PENDENT = "Pendent"
    ESTAT_ENVIADA = "Enviada"

    def __init__(self, id_comanda):
        self.id_comanda = id_comanda
        self.productes = {}
        self.estat = self.ESTAT_PENDENT

    def afegir_producte(self, producte, quantitat=1):
        if producte.nom in self.productes:
            raise ProducteJaExisteixError(f"El producte {producte.nom} ja existeix a la comanda.")
        self.productes[producte.nom] = quantitat

    def modificar_quantitat(self, producte, quantitat):
        if producte.nom not in self.productes:
            raise ProducteNoExisteixError(f"El producte {producte.nom} no existeix a la comanda.")
        self.productes[producte.nom] += quantitat

    def modificar_estat(self, estat):
        self.estat = estat

    def resum(self):
        return {"id": self.id_comanda, "estat": self.estat, "productes": self.productes}