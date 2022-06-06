from CLaseElectrodomesticos import Electrodomesticos

class Lavarropas(Electrodomesticos):
    __Capacidad = ""
    __velocidad = ""
    __cantidadProgramas = 0
    __TipodeCarga = ""

    def __init__(self, marca, modelo, color, pais, preciobase,capacidad, velocidad,cantprog,tipocarga):
        super().__init__(marca, modelo, color, pais, preciobase)
        self.__Capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantidadProgramas = cantprog
        self.__TipodeCarga = tipocarga

    def __str__(self):
        return "%s Capacidad:%s \nVelocidad:%s \nCantidad de programas:%s \nTipo de Carga:%s" % (super().__str__(),self.__Capacidad,self.__velocidad,self.__cantidadProgramas,self.__TipodeCarga)

    def getCarga(self):
        return self.__TipodeCarga

    def toJSON(self):
         d = dict(
         __class__=self.__class__.__name__,
         __atributos__=dict(
             Marca=self.getMarca(),
             Modelo=self.getModelo(),
             Color=self.getColor(),
             Pais=self.getPais(),
             PrecioBase=self.getPrecioBase(),
             Capacidad=self.__Capacidad,
             velocidad=self.__velocidad,
             Cantidadprogramas=self.__cantidadProgramas,
             TipoCarga=self.__TipodeCarga
         )
         )
         return d
