from ClaseCalefactores import Calefactores

class Gas(Calefactores):
    __matricula = ""
    __calorias = ""

    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    def __str__(self):
        return "Matricula: %s \nCalorias: %s \nCalefactor: %s" % (self.__matricula,self.__calorias,super.__str__())

    def getCalorias(self):
        return self.__calorias
