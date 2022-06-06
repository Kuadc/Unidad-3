from CLaseElectrodomesticos import Electrodomesticos

class Heladera(Electrodomesticos):
    __capacidad = 0
    __freezer = None
    __ciclica = None

    def __init__(self, marca, modelo, color, pais, preciobase,capacidad, freezer = None,ciclica=None):
        super().__init__(marca, modelo, color, pais, preciobase)
        self.__capacidad = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica

    def __str__(self):
        return "%s Capacidad:%s \nFreezer:%s \nCiclica:%s" % (super().__str__(),self.__capacidad,self.__freezer,self.__ciclica)
