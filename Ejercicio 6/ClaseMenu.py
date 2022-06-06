
from ClaseTelevisor import Televisor
from ClaseLavarropas import Lavarropas
from ClaseHeladera import Heladera
from ClaseLista import Lista
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            '8':self.salir
                          }

    def opcion(self,op,lista,jsonf):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3" or op=='4' or op=='5' or op=='6' or op=='7':
            func(lista,jsonf)
        else:
            func()

    def opcion1(self,lista,jsonf):
        # Insertar un aparato en la colección en una posición determinada
        pos = int(input("Igrese la posicion donde desea agregar el elemento: "))
        dic = {'marca':'samsung','modelo':"g400",'color':'azul','pais':'arg','precio':'300','pantalla':'plana','pulgadas':'32','definicion':'HD','conexion':True}
        marca = dic['marca']
        modelo = dic['modelo']
        color = dic['color']
        pais = dic['pais']
        precio = dic['precio']
        pantalla = dic['pantalla']
        pulgadas = dic['pulgadas']
        definicion = dic['pulgadas']
        conexion =  dic['conexion']
        untv = Televisor(marca,modelo,color,pais,precio,pantalla,pulgadas,definicion,conexion)
        try:
            lista.InsertarElemento(untv,pos)
        except IndexError:
            print("\n !Cuidado! - La posicion del elemento no es valida\n")

    def opcion2(self,lista,jsonf):
        #agregar un aparato a la coleccion
        aparato = input("Ingrese el tipo de aparato que desea agregar: ")
        if aparato == 'televisor':
            dic = {'marca':'samsung','modelo':"g400",'color':'azul','pais':'arg','precioBase':300,'tipoPantalla':'plana','pulgadas':'32','definicion':'HD','conexion':True}
            untv = Televisor(**dic)
            try:
                lista.AgregarElemento(untv)
            except AttributeError:
                print("El elemento pasado por parametro no es un objeto valido ")
        elif aparato == "lavarropas":
            dic = {'marca':'Philips','modelo':"h200",'color':'blanco','pais':'arg','precio':'299','capacidad':'7kg','velocidad':'3000rpm','cantprog':10,'tipoc':'superior'}
            unlavarropas = Lavarropas(dic['marca'],dic['modelo'],dic['color'],dic['pais'],dic['precio'],dic['capacidad'],dic['velocidad'],dic['cantprog'],dic['tipoc'])
            lista.AgregarElemento(unlavarropas)
        elif aparato == "heladera":
            dic = {'marca':'Whirpool','modelo':"WH3210",'color':'inoxidable','pais':'arg','precio':'96700','capacidad':'125 litros','freezer':True,'ciclica':False}
            unaHeladera = Heladera(dic['marca'],dic['modelo'],dic['color'],dic['pais'],dic['precio'],dic['capacidad'],dic['freezer'],dic['ciclica'])
            lista.AgregarElemento(unaHeladera)
        else:
            print("\nNo existe esa clase de aparato, intente nuevamente\n")

    def opcion3(self,lista,jsonf):
        #Dada una posición de la Lista: Mostrar el elemento
        pos = int(input("Ingrese la posicion del elemento que desea mostrar:"))
        try:
            lista.MostrarElemento(pos)
        except IndexError:
            print("\nLa posicion enviada no es correcta o no existe el elemento alguno en esa posicion\n")


    def opcion4(self,lista,jsonf):
        #Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips
        electro = "Philips"
        try:
            lista.BuscarMarca(electro)
        except IndexError:
            print("\n no se encuentra la marca philips\n")
        pass

    def opcion5(self,lista,jsonf):
        #Mostrar la marca de todos los lavarropas que tienen carga superior
        electro = 'superior'
        try:
            lista.BuscarMarca(electro)
        except IndexError:
            print("\n no se encuentra lavarropas con carga superior\n")

    def opcion6(self,lista,jsonf):
        #Mostrar los electrodomesticos
        for datos in lista:
            print(datos)
        pass

    def opcion7(self,lista,jsonf):
        #Verificar si dos conjuntos son iguales
        lista2 = Lista()
        d=lista.toJSON()
        jsonF.guardarJSONArchivo(d,'datosPuntos.json')
        diccionario=jsonF.leerJSONArchivo('datosPuntos.json')
        lista2=jsonF.decodificarDiccionario(diccionario)
        for datos in lista2:
            print(datos)
    def salir(self):
        exit()


