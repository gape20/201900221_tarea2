from nodo import Nodo

class ListaCiurcular:

    def __init__(self):
        self. primero = None
        self.ultimo = None
    
    def Vacia(self):
        if self.primero == None: 
            return True
        else:
            return False
    
    def agregarInicio(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux 
        self.__unir()

    def agregarFinal(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux

    def __unir(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrerIF(self):
        aux = self.primero
        while aux:
            print('***********************')
            print(f'dato actual: {aux.dato}')
            print(f'dato anterior: {aux.anterior.dato}')
            print(f'dato siguiente: {aux.siguiente.dato}')
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrerFI(self):
        aux = self.ultimo
        while aux:
            print('***********************')
            print(f'dato actual: {aux.dato}')
            print(f'dato anterior: {aux.anterior.dato}')
            print(f'dato siguiente: {aux.siguiente.dato}')
            aux = aux.anterior
            if aux == self.ultimo:
                break