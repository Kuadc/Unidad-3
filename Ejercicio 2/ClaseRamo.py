from CLaseFlor import Flor
class Ramo():
    __tamaño = ""
    __ListaFlores = []

    def __init__(self,tamaño,lista):
        self.__tamaño = tamaño
        self.__ListaFlores = []
        self.__ListaFlores.append(lista)

    def __str__(self):
        return "%s %s" % (self.__tamaño,self.__ListaFlores)

    def GetTamaño(self):
        return self.__tamaño

    def GetRamo(self):
        for i in range(len(self.__ListaFlores)):
            for j in range(len(self.__ListaFlores[i])):
                print(self.__ListaFlores[i][j].mostrarflores())

    def Getramos(self):
        florrosa=0
        florjazmin=0
        clavel=0
        flor5=0
        for i in range(len(self.__ListaFlores)):
            for j in range(len(self.__ListaFlores[i])):
                if self.__ListaFlores[i][j].getflor() == "rosa":
                    florrosa+=1
                elif self.__ListaFlores[i][j].getflor() == "jazmin":
                    florjazmin+=1
                elif self.__ListaFlores[i][j].getflor() == "clavel":
                    clavel+=1
                elif self.__ListaFlores[i][j].getflor() == "milandra":
                    flor5+=1
