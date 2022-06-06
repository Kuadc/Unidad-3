from ClaseCalefactores import Calefactores

class Electric(Calefactores):
    __potenciaMax = ""

    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potenciaMax = potencia

    def __str__(self):
        return "potencia: %s \nCalefactor: %s" % (self.__potenciaMax,super.__str__())
