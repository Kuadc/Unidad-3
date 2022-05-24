
from ClaseRamo import Ramo

class Ramos():
    __listaRamos = []

    def __init__(self):
        self.__listaRamos = []

    def VenderRamo(self,arre):
        print(arre)
        tamaño = input("Ingrese el tipo de tamaño (chico, mediano o grande):")
        flores = int(input("Ingrese el codigo de la flor que quiere para el ramo, ingrese 0 para terminar: "))
        listaventa =[]
        while flores != 0:
            listaventa.append(arre.Getflor(flores-1))
            flores = int(input("Ingrese el codigo de la flor que quiere para el ramo, ingrese 0 para terminar: "))

        unramo = Ramo(tamaño,listaventa)
        self.__listaRamos.append(unramo)
    def __str__(self):
        cadena = ""
        for fila in self.__listaRamos:
            cadena+= str(fila) + "\n"
        return cadena

    def BuscarRamo(self,tamaño):
        for i in range(len(self.__listaRamos)):
            if self.__listaRamos[i].GetTamaño() == tamaño:
                self.__listaRamos[i].GetRamo()

    def buscarflores(self):
        for i in range(len(self.__listaRamos)):
            self.__listaRamos[i].Getramos()
        #hya una lista ramos para colocataar las flores que tiene el ramo,
        #y luego se agrega la lista de las ramos, la lista flores y el tamaño del ramo

