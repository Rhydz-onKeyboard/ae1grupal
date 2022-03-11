class Vendedor:
    def __init__(self, rut, nombre, apellido, seccion, comision):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

    def get(self):
        return self.__dict__