import json

class Nodo:
    __electrodomestico=None
    __siguiente=None

    def __init__(self, electro):
        self.__electrodomestico=electro
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__electrodomestico

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
        Electrodomestico = self.__electrodomestico
        )
        )
        return d
