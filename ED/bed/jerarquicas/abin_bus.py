from exepciones import DuplicatedKeyError, HomogeneityError
from nodos import nodoArbol_Bin
from abin import arbolBin

class arbolBinario_Bus(arbolBin):

    def adicionar(self, nueva_clave): #sobre-escribir metodo adicionar
        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    #nodos menores a la izquierda
    #nodos mayores a la derecha
    #no se aceptan claves duplicadas

    #evaluar homogeneidad riase HomogeneityError(nueva_clave)
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = nodoArbol_Bin(nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else:# nueva clave ya existe
            raise DuplicatedKeyError(nueva_clave)
    
        return sub_arbol

    def encontrar(self, clave_encontrar):
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            elif clave_encontrar < sub_arbol.clave: # 🔎 por izquierda
                return self.__encontrar(sub_arbol.izq, clave_encontrar)
            else: # 🔎 por dereecha
                return self.__encontrar(sub_arbol.der, clave_encontrar)
        return None
    
    def encontrar_minimo(self):
    #     metodo que busca y retorna la clave de menor valor 
    #     del arbol o None cuando el arbol esta vacio
        pass

    def encontrar_maximo(self):
    #     metodo que busca y retorna la clave de mayor valor 
    #     del arbol o None cuando el arbol esta vacio
        pass

    def remover(self, clave_remover, mayor=True):
    #     mayor -> True : remplazo el hijo mayor de los menores
    #     mayor -> False: remplazo el hijo menor de los mayores
        pass


    

    

    


    