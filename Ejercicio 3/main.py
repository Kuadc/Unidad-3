from ManejadorEquipos import arregloequipo

from ClaseMenu import Menu

from ManejadorContrato import ArregloContrato

from ManejadorJugadores import listajugador

if __name__ == '__main__':
    equipos = arregloequipo(5,5)
    equipos.AbrirArchivo()
    contratos = ArregloContrato(5,5)
    jugadores = listajugador()
    jugadores.AbrirArchivo()
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Generar contrato para un jugador.")
        print("2) - Consultar jugador contratado")
        print("3) - Consultar contratos")
        print("4) - Obtener importe de contratos")
        print("5) - Guardar contratos en el archivo")
        print("6) - Salir")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,jugadores,equipos,contratos)
