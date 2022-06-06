import csv

from ClaseJugador import Jugador

class listajugador():
    __lista = []

    def __init__(self):
        self.__lista = []

    def AgregarJugador(self,unjugador):
        self.__lista.append(unjugador)

    def AbrirArchivo(self):
        archivo = open("jugadores.csv")
        reader = csv.reader(archivo,delimiter=",")
        bandera = False
        for fila in reader:
            if not bandera:
                bandera = True
            else:
                nombre = fila[0]
                dni = int(fila[1])
                cuidad = fila[2]
                pais = fila[3]
                fechanac = fila[4]
                unjugador = Jugador(nombre, dni, cuidad, pais, fechanac)
                self.AgregarJugador(unjugador)
        archivo.close()

    def __str__(self):
        i=0
        cadena = "Jugador: \n"
        for fila in self.__lista:
            cadena+= str(i)+") " +str(fila) + "\n"
            i+=1
        return cadena

    def GetJugador(self, pos):
        return self.__lista[pos]






