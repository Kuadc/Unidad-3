

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self, op, arreglo):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(arreglo)
        else:
            func()

    def opcion1(self, arreglo):
        #
        costom3 = float(input("Ingrese el costo por metro cubico: "))
        consumo = int(input("Ingrese el consumo en metro cubicos: "))
        indice = arreglo.BuscarMenorConsumo()
        print(arreglo)



    def opcion2(self, arreglo):
        #




    def opcion3(self, arreglo):
        #Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
        pass


    def salir(self):
        exit()
