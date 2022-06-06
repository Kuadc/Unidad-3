from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu

if __name__ == "__main__":
    jsonF = ObjectEncoder()
    lista = Lista()
    bandera = True
    while bandera:
        menu = Menu()
        while True:
            print("1) - Insertar un aparato en la colección en una posición determinada.")
            print("2) - Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).")
            print("3) - Dada una posición de la Lista: Mostrar el elemento")
            print("4) - Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.")
            print("5) - Mostrar la marca de todos los lavarropas que tienen carga superior .")
            print("6) - Mostrar para todos los aparatos que la empresa tiene a la venta")
            print("7) - Almacenar los objetos de la colección Lista en el archivo")
            print("8) - Salir")
            opcion = input("Ingrese el la opcion deseada: ")
            menu.opcion(opcion, lista, jsonF)
