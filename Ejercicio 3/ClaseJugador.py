
class Jugador():
    __nombre = ""
    __dni = 0
    __cuidad = ""
    __pais = ""
    __FechaNac =""

    def __init__(self,nom,dni,cuidad,pais,fecha):
        self.__nombre = nom
        self.__dni = dni
        self.__cuidad = cuidad
        self.__pais = pais
        self.__FechaNac = fecha

    def __str__(self):
        return "\nNombre: %s \nPais: %s \nCuidad: %s \nDNI: %s \nFecha Nacimiento: %s" % (self.__nombre,self.__pais,self.__cuidad,self.__dni,self.__FechaNac)

    def getDni(self):
        return self.__dni
