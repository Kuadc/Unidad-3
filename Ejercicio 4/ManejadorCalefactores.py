import numpy as np

import csv

from ClaseCalefactores import Calefactores

from ClaseCalefactorElectrico import Electric

from ClaseCalefactorGas import Gas
class Manejador:
    __dimension=0
    __actual = 0
    __calefactores = None

    def __init__(self, dimension=5):
        self.__calefactores = np.empty(dimension, dtype=Calefactores)
        self.__dimension = dimension
        self.__actual = 0

    def AgregarCalefactores(self, uncalefactor):
        self.__calefactores[self.__actual] = uncalefactor
        self.__actual+=1

    def CalcularCalorias(self):
        pass

    def AbrirArchivoGas(self):
        archivo = open("Calefactorgas.csv")
        reader = csv.reader(archivo,delimiter=",")
        encontrado = False
        for fila in reader:
            if not encontrado:
                encontrado = True
            else:
                marca = fila[0]
                modelo = fila[1]
                matricula = fila[2]
                calorias = fila[3]
                ungas = Gas(marca, modelo, matricula, calorias)
                self.AgregarCalefactores(ungas)
        archivo.close()

    def AbrirArchivoElectrico(self):
            archivo = open("CalefactorElectrico.csv")
            reader = csv.reader(archivo,delimiter=",")
            encontrado = False
            for fila in reader:
                if not encontrado:
                    encontrado = True
                else:
                    marca = fila[0]
                    modelo = fila[1]
                    potencia = fila[2]
                    uncalefactor = Electric(marca, modelo, potencia)
                    self.AgregarCalefactores(uncalefactor)
            archivo.close()

    def BuscarMenorConsumo(self):
        menor = 0
        i = 0
        indice = 0
        while i< self.__actual:
            calorias = self.__calefactores[i].getCalorias()
            if menor <calorias:
                menor = calorias
                indice = i
                i+=1
            else:
                i+=1
        return indice



