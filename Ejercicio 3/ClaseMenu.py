from ClaseContrato import Contrato

from datetime import date

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.salir
                          }

    def opcion(self, op, jugadores, equipos, contratos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3" or op=="4"  or op=="5":
            func(jugadores, equipos, contratos)
        else:
            func()

    def opcion1(self, jugadores, equipos, contratos):
            #realizar contrato a un jugador

            print(jugadores)
            pos= int(input("Elija opcion de jugador: "))
            unjugador = jugadores.GetJugador(pos)
            print(equipos)
            posequipo= int(input("Elija opcion de equipo: "))
            unequipo = equipos.getEquipo(posequipo)
            print("Ingrese la fecha fin de contrato")
            fecha = date(int(input("Ingrese Año: ")),int(input("Ingrese mes: ")),int(input("Ingrese dia: ")))
            pago = int(input("Ingrese pago mensual:"))
            uncontrato = Contrato(fecha, pago, unjugador, unequipo)
            contratos.AgregarContrato(uncontrato)
            contratos.MostrarDatos()


    def opcion2(self, jugadores, equipos, contratos):
        # Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.
        dni = float(input("Ingrese el dni del jugador: " ))
        contratos.BuscarContrato(dni)



    def opcion3(self, jugadores, equipos, contratos):
        #Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
        unequipo = input("Ingrese el nombre del equipo: ")
        contratos.BuscarEquipo(unequipo)

    def opcion4(self, jugadores, equipos, contratos):
        #Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.
        unequipo = input("Ingrese el nombre del equipo: ")
        total = contratos.BuscarImporteTotal(unequipo)
        print ("El importe total para el equipo:{} es de: {}".format(unequipo,total))

    def opcion5(self, jugadores, equipos, contratos):
        #Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.
        contratos.GuardarArchivo()

    def salir(self):
        exit()
