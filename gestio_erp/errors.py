# gestio_erp/errors.py

# Classe base per a errors personalitzats del paquet ERP
# Aquesta classe permet agrupar tots els errors relacionats amb el sistema ERP,
# facilitant-ne la gestió i identificació.

class GestioERPErrors(Exception):
    # `GestioERPErrors` hereta de la classe base `Exception` de Python.
    # Es pot utilitzar per capturar tots els errors específics del paquet ERP.
    pass

# Error per a productes duplicats en una comanda
# Aquesta classe representa una excepció que es llança quan s'intenta afegir
# un producte que ja existeix en una comanda.

class ProducteJaExisteixError(GestioERPErrors):
    # Hereta de `GestioERPErrors` per indicar que és un tipus específic d'error ERP.
    pass

# Error per a productes inexistents en una comanda
# Aquesta classe representa una excepció que es llança quan s'intenta modificar
# o accedir a un producte que no existeix en una comanda.

class ProducteNoExisteixError(GestioERPErrors):
    # També hereta de `GestioERPErrors` per mantenir consistència amb altres errors ERP.
    pass