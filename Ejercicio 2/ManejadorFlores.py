import csv

import numpy as np

from CLaseFlor import Flor

class arregloFlor:
    def __init__(self, dimension, incremento = 5):
        self.__flores = np.empty(dimension,dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarFlor(self,unaflor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad]=unaflor
        self.__cantidad += 1

    def AbrirArchivo(self):
        archivo = open("flores2.csv")
        datos = csv.reader(archivo, delimiter=';')
        y=0
        print("\n------Comienza la carga de obejtos en el arreglo------\n")
        bandera = False
        for fila in datos:
            if not bandera:
                bandera= True #agregar siempre encabezados de lo contrario adhiere caracteres erroneos
            else:
                num = fila[0]
                nom = fila[1]
                color = fila[2]
                descrip = fila[3]
                p1 = Flor(num,nom,color,descrip)
                self.agregarFlor(p1)
        print("\n------Flores guardadas en el arreglo------\n")
        archivo.close()

    def __str__(self):
        s = ""
        for fila in self.__flores:
            s+= str(fila) + "\n"
        return s

    def Getflor(self,i):
        return self.__flores[i]
