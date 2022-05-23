import csv
from ClaseFacultad import Facultad

class ListaFacultad():
    __lista = []

    def __init__(self):
        self.__lista = []

    def AbrirArchivo(self):
        archivo = open("facultad.csv")
        reader = csv.reader(archivo,delimiter =",")
        Bandera = True
        fila=next(reader)
        print('Facultad')
        listacarrera = []
        while Bandera:
            #print('fila')
            #print('carreras:')
            filacarrera = next(reader)
            while Bandera and fila[0] == filacarrera[0]:
                #print(filacarrera)
                listacarrera.append(filacarrera)
                nuevafacultad = Facultad(fila[0],fila[1],fila[2],fila[3],fila[5],listacarrera)
                self.__lista.append(nuevafacultad)
                listacarrera = []
                try:
                    filacarrera = next(reader)
                except StopIteration:
                    Bandera = False
            fila=filacarrera
        archivo.close()

    def __str__(self):
        cadena=""
        for fila in self.__lista:
            cadena+= str(fila) + "\n"
        return cadena








            #agregar a la linea de facultad del archivo la cantidad de carreras,

