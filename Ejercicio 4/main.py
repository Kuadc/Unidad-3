from ManejadorCalefactores import Manejador

from ClaseMenu import Menu

if __name__ == '__main__':
    dimension = int(input("Ingrese la cantidad de calefactores: "))
    arreglo = Manejador(dimension)
    arreglo.AbrirArchivoGas()
    arreglo.AbrirArchivoElectrico()
    unmenu = Menu()
    while True:
        print("------Menu--------")
        print("1) - Mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.")
        print("2) - Mostrar marca  y modelo del calefactor eléctrico de menor consumo.")
        print("3) - Mostrar tipo de calefactor y todos los datos del calefactor de menor consumo..")
        print("4) - Salir ")
        opcion = input("Ingrese la opcion deseada")
        unmenu.opcion(opcion,arreglo)
