# Importem les classes necessàries
from models import Client, Comanda, Producte, ProducteJaExisteixError, ProducteNoTrobatError

# Creem els productes
bicicleta = Producte("bicicleta")
casc = Producte("casc")
guants = Producte("guants")
maillot = Producte("maillot")
roda = Producte("roda")
pantalons = Producte("pantalons")
patinet = Producte("patinet")

# Creem els clients
anna = Client(1, "Anna", "anna@example.com")
pere = Client(2, "Pere", "pere@example.com")
joan = Client(3, "Joan", "joan@example.com")

# Creem les comandes
comanda1 = Comanda(101)
comanda2 = Comanda(102)
comanda3 = Comanda(103)
comanda4 = Comanda(104)

# Afegim els productes a les comandes
try:
    comanda1.afegir_producte(bicicleta, 1)  # Afegim bicicleta a la comanda1
    comanda1.afegir_producte(casc, 2)      # Afegim casc a la comanda1
    comanda2.afegir_producte(guants, 1)    # Afegim guants a la comanda2

    comanda3.afegir_producte(maillot, 1)   # Afegim maillot a la comanda3
    comanda3.afegir_producte(roda, 2)      # Afegim roda a la comanda3
    comanda4.afegir_producte(guants, 2)    # Afegim guants a la comanda4

    # Afegim les comandes als clients
    anna.afegir_comanda(comanda1)  # Afegim comanda1 a l'Anna
    anna.afegir_comanda(comanda2)  # Afegim comanda2 a l'Anna
    pere.afegir_comanda(comanda3)  # Afegim comanda3 al Pere
    pere.afegir_comanda(comanda4)  # Afegim comanda4 al Pere

    # Error: Intentant afegir un producte existent a una comanda
    comanda1.afegir_producte(bicicleta, 1)  # Intentem afegir bicicleta a la comanda1 de nou

except ProducteJaExisteixError as e:  # Capturem l'error de producte existent
    print(e)

# Error: Intentant afegir un producte que no existeix a una comanda
try:
    comanda1.afegir_producte(patinet, 1)  # Intentem afegir un producte que no existeix (patinet)
except ProducteNoTrobatError as e:  # Capturem l'error de producte no trobat
    print(e)

# Mostrem les comandes abans de modificar-les
print("COMANDES DELS CLIENTS")
anna.mostrar_comandes()  # Mostrem les comandes de l'Anna
pere.mostrar_comandes()  # Mostrem les comandes del Pere
joan.mostrar_comandes()  # Mostrem les comandes del Joan

# Canviem l'estat de les comandes
comanda1.canviar_estat("Enviada")  # Canviem l'estat de la comanda1 a "Enviada"
comanda1.afegir_unitats_producte(bicicleta, 1)  # Afegim una unitat de bicicleta a la comanda1
comanda1.afegir_unitats_producte(casc, 2)      # Afegim dues unitats de casc a la comanda1
comanda1.afegir_producte(pantalons, 1)         # Afegim pantalons a la comanda1

# Mostrem les comandes després de modificar-les
print("COMANDES DELS CLIENTS")
anna.mostrar_comandes()  # Mostrem les comandes de l'Anna després de les modificacions