
class Flor():
    __numero  = 0
    __nombre = ""
    __color = ""
    __descripcion = ""

    def __init__(self,num,nombre,color,descrip):
        self.__numero = num
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descrip

    def __str__(self):
        return "%s %s %s %s" % (self.__numero,self.__nombre,self.__color,self.__descripcion)

    def mostrarflores(self):
        return "%s %s %s %s" % (self.__numero,self.__nombre,self.__color,self.__descripcion)

    def getflor(self):
        return self.__nombre
