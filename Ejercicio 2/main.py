from ManejadorFlores import arregloFlor
from ManejadorRamos import Ramos
from ClaseMenu import Menu
if __name__ == '__main__':
    arre = arregloFlor(5,5)
    arre.AbrirArchivo()
    ramos = Ramos()
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Registrar Venta de Ramo.")
        print("2) - Mostrar el nombre de las 5 flores  más pedidas en un ramo")
        print("3) - Consulta de flores segun el tamaño de ramo")
        print("3) - Finalizar")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,arre,ramos)
