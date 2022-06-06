from CLaseElectrodomesticos import Electrodomesticos

class Televisor(Electrodomesticos):
    __tipoPantalla = ""
    __pulgadas = 0
    __definicion = ""
    __conexion = None

    def __init__(self, marca, modelo, color, pais, precioBase,tipoPantalla,pulgadas,definicion,conexion= None):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__definicion = definicion
        self.__conexion = conexion

    def __str__(self):
        return "%s Patanlla:%s \nDefinicion:%s \nPulgadas:%s" % (super().__str__(),self.__tipoPantalla,self.__definicion,self.__pulgadas)

    def toJSON(self):
         d = dict(
         __class__=self.__class__.__name__,
         __atributos__=dict(
             Marca=self.getMarca(),
             Modelo=self.getModelo(),
             Color=self.getColor(),
             Pais=self.getPais(),
             PrecioBase=self.getPrecioBase(),
             TipoPantalla=self.__tipoPantalla,
             Pulgadas=self.__pulgadas,
             Definicio=self.__definicion,
             conexion=self.__conexion
         )
         )
         return d


