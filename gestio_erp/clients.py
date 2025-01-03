# gestio_erp/clients.py
class Client:
    def __init__(self, id_client, nom, email):
        self.id_client = id_client
        self.nom = nom
        self.email = email
        self.comandes = []

    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    def llistar_comandes(self):
        return self.comandes