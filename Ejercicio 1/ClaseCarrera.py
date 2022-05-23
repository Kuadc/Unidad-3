
class CarreraFacultad():
    __codigo = 0
    __nombre = ""
    __duracion = 0
    __Titulo = ""
    __grado = ""

    def __init__(self,cod,nom,dur,tit,gr):
        self.__codigo = cod
        self.__nombre = nom
        self.__duracion = dur
        self.__Titulo = tit
        self.__grado = gr

    def __str__(self):
        return "%s %s %s %s %s" % (self.__codigo,self.__nombre,self.__duracion,self.__Titulo,self.__grado)

