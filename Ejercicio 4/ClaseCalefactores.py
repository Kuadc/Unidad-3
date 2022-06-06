

class Calefactores():
    __marca = ""
    __modelo = ""

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return "Marca: %s \nModelo: %s " % (self.__marca,self.__modelo)

