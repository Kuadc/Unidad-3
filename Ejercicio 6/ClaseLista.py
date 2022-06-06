
import json

from ClaseNodo import Nodo

from zope.interface import implementer

from ClaseInterfaz import EjercicioInterface

from ClaseLavarropas import Lavarropas

from CLaseElectrodomesticos import Electrodomesticos
@implementer(EjercicioInterface)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None


    def AgregarElemento(self, unelectro):
        #if isinstance(unelectro,object):
        nodo = Nodo(unelectro)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo
        self.__tope+=1
        #else:
            #raise AttributeError

    def InsertarElemento(self,elemento,pos):
        if pos == 0:
            self.AgregarElemento(elemento)
        else:
            i=0
            aux = self.__comienzo
            anterior = self.__comienzo
            while i<pos and aux != None: # inicializamos i en 0 para recorrer la lista de nodos
                anterior = aux
                aux = aux.getSiguiente()
                i+=1
            if pos == i:
                nodo = Nodo(elemento)
                anterior = nodo.getSiguiente()
                nodo.setSiguiente(aux)
            else:
                raise IndexError

    def MostrarElemento(self,pos):
        if isinstance(pos,int):
            i=0
            aux = self.__comienzo
            while i<pos and aux != None:
                aux = aux.getSiguiente()
                i+=1
            if pos == i:
                print(aux.getDato())
            else:
                raise IndexError

    def BuscarMarca(self,electro):
        if isinstance(electro,str):
            encontrado = False
            aux = self.__comienzo
            while not encontrado and aux != None:
                if aux.getDato().getMarca() == electro:
                    encontrado = True
                elif isinstance(aux.getDato(),Lavarropas):
                    if aux.getDato().getCarga() == electro:
                        encontrado = True
                    else:
                        aux = aux.getSiguiente()
                else:
                    aux = aux.getSiguiente()
            if encontrado:
                print(aux.getDato())
            else:
                raise IndexError
        else:
            print("el parametro recibido no es correcto")

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            Electrodomesticos = [Electrodomesticos.toJSON() for nodos in self.__comienzo]
            )
        return d

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato


