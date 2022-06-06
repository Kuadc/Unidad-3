import numpy as np

from ClaseContrato import Contrato

from datetime import date

from dateutil.relativedelta import relativedelta

class ArregloContrato:
    def __init__(self,dimension,incremento=5):
        self.__contrato = np.empty(dimension,dtype=Contrato)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0

    def AgregarContrato(self,uncontrato):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__contrato.rezise(self.__dimension)
        self.__contrato[self.__cantidad] = uncontrato
        self.__cantidad+=1

    def MostrarDatos(self):
        for fila in range(self.__cantidad):
            print("--------Contratos------")
            print(self.__contrato[fila])

    def BuscarContrato(self, elemento):
        encontrado = False
        i=0
        while not encontrado and i < self.__cantidad:
            if self.__contrato[i].getJugador().getDni() == elemento:
                encontrado = True
                print("--------Contrato------")
                print(self.__contrato[i])
            else:
                i+=1
        if not encontrado:
            print("No hay jugador contratado con ese dni")

    def BuscarEquipo(self, elemento):
        i=0
        encontrado = False
        while i < self.__cantidad:
            if self.__contrato[i].getEquipo().GetNombre() == elemento:
                hoy = date.today()
                fincontrato = self.__contrato[i].getFechaFin()
                meses = relativedelta(months=6)
                if hoy + meses == fincontrato:
                    print(self.__contrato[i].getJugador())
                    i+=1
                    encontrado = True
                else:
                    i+=1
            else:
                i+=1
        if not encontrado:
            print("No hay contratos que vencen en 6 meses para el equipo solicitado")

    def BuscarImporteTotal(self, elemento):
        i=0
        total=0
        while i < self.__cantidad:
            if self.__contrato[i].getEquipo().GetNombre() == elemento:
                total+=self.__contrato[i].getPago()
                i+=1
            else:
                i+=1
        return total

    def GuardarArchivo(self):
        #DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.
        lista =[]
        for i in range(self.__cantidad):
            lista2 = [self.__contrato[i].getJugador().getDni(),self.__contrato[i].getEquipo().GetNombre(),self.__contrato[i].GetFechaInicio(),self.__contrato[i].getFechaFin(),self.__contrato[i].getPago()]
            lista.append(lista2)
            lista2 = []
        np.savetxt("contratos.csv", lista, delimiter =",",fmt ='% s')

