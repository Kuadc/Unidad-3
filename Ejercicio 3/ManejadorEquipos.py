import csv

import numpy as np

from ClaseEquipo import Equipo

from ManejadorContrato import Contrato

class arregloequipo:
    def __init__(self, dimension,incremento=5):
        self.__equipo = np.empty(dimension,dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def AgregaEquipo(self,unequipo):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__equipo.resize(self.__dimension)
        self.__equipo[self.__cantidad]=unequipo
        self.__cantidad+=1


    def AbrirArchivo(self):
        archivo = open("equipos.csv")
        reader = csv.reader(archivo,delimiter=",")
        cant=next(reader)
        cantidad = int(cant[0])
        i=0
        bandera = True
        while bandera:
            fila = next(reader)
            while bandera and i<cantidad:
                nombre = fila[1]
                cuidad = fila[2]
                unequipo = Equipo(nombre,cuidad)
                self.AgregaEquipo(unequipo)
                i+=1
                try:
                    fila = next(reader)
                except StopIteration:
                    bandera = False
        archivo.close()

    def __str__(self):
        i=0
        cadena = ""
        for fila in range(self.__cantidad):
            cadena+= str(i)+') '+str(self.__equipo[fila]) + "\n"
            i+=1
        return cadena

    def getEquipo(self,pos):
        return self.__equipo[pos]
