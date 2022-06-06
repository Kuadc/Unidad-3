
class Equipo():
    __nombre = ""
    __cuidad = ""
    __id = 0
    def __init__(self,nom,cuidad):
        self.__nombre = nom
        self.__cuidad = cuidad

    def __str__(self):
        return "Equipo: %s            Cuidad: %s" % (self.__nombre,self.__cuidad)


    def GetNombre(self):
        return self.__nombre
