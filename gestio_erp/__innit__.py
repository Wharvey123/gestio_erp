# gestio_erp/__init__.py
# Aquest fitxer permet tractar "gestio_erp" com un paquet.
# Es poden fer imports rellevants aquí si es vol exposar directament des del paquet.

from .clients import Client
from .comandes import Comanda
from .productes import Producte
from .errors import (
    GestioERPErrors,
    ProducteJaExisteixError,
    ProducteNoExisteixError,
)