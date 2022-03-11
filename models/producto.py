class Producto:
    def __init__(self, SKU, nombre, categoria, provedor, stock, valor_neto):
        self.SKU = SKU
        self.nombre = nombre
        self.categoria = categoria
        self.provedor = provedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19

    def get(self):
        return self.__dict__       