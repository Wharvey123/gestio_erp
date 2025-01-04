# gestio_erp/clients.py

# Definició de la classe `Client`
# Aquesta classe representa un client del sistema ERP, amb atributs per identificar-lo 
# i gestionar les seves comandes.

class Client:
    # Constructor de la classe `Client`
    # Inicialitza un objecte client amb un identificador únic (`id_client`), nom (`nom`),
    # correu electrònic (`email`) i una llista buida de comandes (`comandes`).
    def __init__(self, id_client, nom, email):
        self.id_client = id_client  # Identificador únic del client
        self.nom = nom  # Nom del client
        self.email = email  # Correu electrònic del client
        self.comandes = []  # Llista de comandes associades al client

    # Mètode `afegir_comanda`
    # Aquest mètode permet afegir una comanda a la llista de comandes del client.
    # Paràmetres:
    # - `comanda`: objecte de tipus `Comanda` que es vol associar al client.
    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    # Mètode `llistar_comandes`
    # Retorna la llista de totes les comandes associades al client.
    # Aquest mètode és útil per obtenir un resum de les comandes del client.
    def llistar_comandes(self):
        return self.comandes