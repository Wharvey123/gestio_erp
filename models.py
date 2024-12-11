# Definim la classe Producte
class Producte:
    # Constructor per a crear un producte amb un nom
    def __init__(self, nom):
        self.nom = nom  # Guardem el nom del producte

# Definim la classe Comanda
class Comanda:
    # Constructor per a crear una comanda amb un id únic
    def __init__(self, id_comanda):
        self.id_comanda = id_comanda  # Guardem l'identificador de la comanda
        self.productes = {}  # Diccionari per emmagatzemar el nom del producte i la seva quantitat
        self.estat = "Pendent"  # Estat per defecte de la comanda

    # Mètode per afegir un producte a la comanda
    def afegir_producte(self, producte, quantitat=1):
        # Comprovem si el producte ja existeix a la comanda
        if producte.nom in self.productes:
            raise ProducteJaExisteixError(f"El producte {producte.nom} ja existeix a la comanda.")  # Llença un error si ja existeix
        self.productes[producte.nom] = quantitat  # Afegim el producte amb la quantitat

    # Mètode per afegir unitats d'un producte existent
    def afegir_unitats_producte(self, producte, quantitat=1):
        # Comprovem si el producte existeix a la comanda
        if producte.nom not in self.productes:
            raise ProducteNoTrobatError(f"El producte {producte.nom} no existeix a la comanda.")  # Llença un error si no existeix
        self.productes[producte.nom] += quantitat  # Afegim unitats addicionals al producte

    # Mètode per canviar l'estat de la comanda
    def canviar_estat(self, estat):
        self.estat = estat  # Actualitzem l'estat de la comanda

    # Mètode per mostrar un resum de la comanda
    def mostrar_resum(self):
        # Creem una cadena amb el nom i la quantitat de cada producte
        productes_str = ", ".join(f"{nom}: {quantitat}" for nom, quantitat in self.productes.items())
        # Retornem un resum de la comanda
        return f"Comanda {self.id_comanda} [{self.estat}]: {productes_str}"

# Definim la classe Client
class Client:
    # Constructor per crear un client amb id, nom i correu
    def __init__(self, id_client, nom, correu):
        self.id_client = id_client  # Guardem l'identificador del client
        self.nom = nom  # Guardem el nom del client
        self.correu = correu  # Guardem el correu del client
        self.comandes = []  # Llista de comandes associades al client

    # Mètode per afegir una comanda al client
    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)  # Afegim la comanda a la llista de comandes

    # Mètode per mostrar les comandes d'un client
    def mostrar_comandes(self):
        if not self.comandes:
            print(f"El client {self.nom} no té cap comanda.")  # Mostrem un missatge si no té comandes
            print("None")
            return
        # Mostrem el nombre de comandes i un resum de cada una
        print(f"Comandes del client {self.nom}: {len(self.comandes)}")
        for comanda in self.comandes:
            print(comanda.mostrar_resum())  # Mostrem el resum de cada comanda
        print("None")

# Definim l'excepció per quan el producte ja existeix a la comanda
class ProducteJaExisteixError(Exception):
    pass

# Definim l'excepció per quan el producte no es troba a la comanda
class ProducteNoTrobatError(Exception):
    pass