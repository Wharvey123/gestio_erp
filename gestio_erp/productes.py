# gestio_erp/productes.py

# Definició de la classe `Producte`
# Aquesta classe representa un producte dins del sistema ERP, 
# amb un atribut per emmagatzemar el seu nom.

class Producte:
    # Constructor de la classe `Producte`
    # Inicialitza un objecte `Producte` amb el nom especificat.
    # Paràmetres:
    # - `nom`: Nom del producte (ex., "bicicleta", "casc").
    def __init__(self, nom):
        self.nom = nom  # Atribut que emmagatzema el nom del producte