# gestio_erp/__init__.py

# Aquest fitxer permet tractar "gestio_erp" com un paquet Python.
# La seva funció principal és facilitar l'accés als mòduls i classes del paquet
# quan s'importa des d'altres parts del projecte.

# Importació de classes i excepcions
# Aquestes importacions permeten accedir directament a les classes i excepcions
# més rellevants del paquet `gestio_erp` sense haver d'especificar els seus submòduls.
from .clients import Client  # Classe per gestionar clients
from .comandes import Comanda  # Classe per gestionar comandes
from .productes import Producte  # Classe per gestionar productes
from .errors import (  # Excepcions personalitzades per a la gestió d'errors
    GestioERPErrors,  # Classe base per a errors del paquet ERP
    ProducteJaExisteixError,  # Error quan s'intenta afegir un producte duplicat
    ProducteNoExisteixError,  # Error quan un producte no existeix en una comanda
)