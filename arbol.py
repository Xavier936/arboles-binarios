from nodo import Nodo

class Arbol:
    #funciones privadas
    def __init__(self,dato):
        self.raiz = Nodo(dato)
    
    #se inserta datos de forma recursiva
    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda,dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha,dato)

    #recorrido del arbol
    def __inorden_recursivo(self,nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=" -> ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self,nodo):
        if nodo is not None:
            print(nodo.dato, end=" -> ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)
    
    def __postorden_recursivo(self,nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=" -> ")

    #Busqueda dentro del arbol
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda,busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    
    #funciones publicas

    def agregar(self,dato):
        self.__agregar_recursivo(self.raiz, dato)
    
    def inorden(self):
        print("Imprimiendo árbol Inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")
    
    def preorden(self):
        print("Imprimiendo árbol Preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol Postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)