
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self,op,arre,listaramo):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(arre,listaramo)
        else:
            func()

    def opcion1(self,arre,listaramo):
        # Registrar un ramo vendido (instancia de la clase ramo),
        # solicitando las flores que se pondrán en el ramo.
        listaramo.VenderRamo(arre)
        #print(listaramo.mostrardatos())

    def opcion2(self,arre,listaramo):
        # Mostrar el nombre de las 5 flores  más pedidas en un ramo
        #listaramo.buscarflores()
        pass

    def opcion3(self,arre,listaramo):
        #Verificar si dos conjuntos son iguales
        tamaño = str(input("\nIngrese el tamaño del ramo [chico,mediano o grande]: "))
        if isinstance(tamaño,str):
            listaramo.BuscarRamo(tamaño)

    def salir(self):
        exit()
