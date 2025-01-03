# gestio_erp/errors.py
class GestioERPErrors(Exception):
    pass

class ProducteJaExisteixError(GestioERPErrors):
    pass

class ProducteNoExisteixError(GestioERPErrors):
    pass