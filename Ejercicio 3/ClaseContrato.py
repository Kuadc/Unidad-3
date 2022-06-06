from datetime import date

class Contrato():
    __FechaInicio =""
    __FechaFin = ""
    __PagoMensual = 0.0
    __jugador = None
    __equipo = None

    def __init__(self,fechafin,pago,jugador,equipo):
        self.__FechaInicio = date.today()
        self.__FechaFin = fechafin
        self.__PagoMensual = pago
        self.__jugador = jugador
        self.__equipo = equipo

    def __str__(self):
        return "Fecha Inicio: %s \nFecha fin:%s \nPago Mensual:%s \n-----Jugador------:%s \n%s" % (self.__FechaInicio,self.__FechaFin,self.__PagoMensual,self.__jugador.__str__(),self.__equipo.__str__())


    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaFin(self):
        return self.__FechaFin

    def getPago(self):
        return self.__PagoMensual

    def GetFechaInicio(self):
        return self.__FechaInicio
