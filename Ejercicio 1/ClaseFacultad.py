from ClaseCarrera import CarreraFacultad

class Facultad():
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localitad = ""
    __telefono= ""
    __carrera = None

    def __init__(self,cod,nom,dir,loc,tel,lista):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dir
        self.__localitad = loc
        self.__telefono = tel
        for fila in lista:
            code = fila[1]
            nombre = fila[2]
            dur = fila[3]
            titulo = fila[4]
            grado = fila[5]
            self.__carrera = CarreraFacultad(code,nombre,dur,titulo,grado)

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__codigo,self.__nombre,self.__direccion,self.__localitad,self.__telefono,self.__carrera)


