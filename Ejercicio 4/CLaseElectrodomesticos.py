
class Electrodomesticos():
    __marca = ""
    __modelo = ""
    __color = ""
    __pais = ""
    __precioBase = 0

    def __init__(self, marca, modelo, color, pais, precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precioBase = precioBase

    def __str__(self):
        cadena = "\nElectrodomestico \n"
        cadena+= "Marca: {}\nModelo: {}\nColor: {}\nPais: {}\nPrecio Base: {}".format(self.__marca,self.__modelo,self.__color,self.__pais,self.__precioBase) + '\n'
        return cadena

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPais(self):
        return self.__pais

    def getPrecioBase(self):
        return self.__precioBase

    def toJSON(self):
        d = dict(
         __class__=self.__class__.__name__,
         __atributos__=dict(
             Marca=self.getMarca(),
             Modelo=self.getModelo(),
             Color=self.getColor(),
             Pais=self.getPais(),
             PrecioBase=self.getPrecioBase()
         )
         )
        return d
