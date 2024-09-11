
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE
else:
    from bed.lineales.nodos import Nodo_listaSE

class Lista_SE:
    """clase que crea una lista simplemente enlazada 
    """
    def __init__(self):
        """método para crear una lista simplemente enlazada
        """
        self.__cab = None #debe iniciar vacía 
    
    def es_vacia(self):
        """método para comprobar si la lista simplemente enlazada es vacía

        Returns:
            bool: retorna True si la lista es vacía, False en caso contrario
        """
        if not self.__cab:    #self.__cab is None:
            return True
        return False    #no requiere el else
                        #otra forma, return self.__cab in None
                        #not None va a dar True
    
    def adicionar(self,nuevo_dato):
        if isinstance(nuevo_dato, int):
            nuevo_nodo = Nodo_listaSE(nuevo_dato)
            if self.es_vacia():
                self.__cab = nuevo_nodo
            else:
            #cuando la lista no está vacía 
                actual = self.__cab
                while actual.sig is not None:     #while actual.sig:
                    actual = actual.sig
                actual.sig = nuevo_nodo
        else:
            print(f"El dato ingresado {nuevo_dato} no es numérico")
    
    def recorrer (self):
        """método que recorre cada uno de los datos siempre y cuando no sea una lista vacía 
        """
        actual = self.__cab

        while actual:
            print(actual)  #ya se había hecho un str, por eso se imprime actual
            actual = actual.sig

    def encontar (self, dato_encontrar):
        """método que permite realizar una búsqueda del dato en la lista

        Parameters
        ----------
        dato_encontrar : object
            dato que se va a buscar 

        Returns
        -------
        object | None
            object si se encuentra el dato en la lista, de lo contrario None
        """
        actual = self.__cab
        while actual:
            if actual.dato == dato_encontrar:
                return actual.dato
            actual = actual.sig
        # while actual and actual.dato != dato_encontrar:
        #     actual = actual.sig
        # return actual.dato if actual else None
    
    def remover (self, item, por_pos = True):
        #item porque puede ser dato o posición)
        if por_pos:
            return self.__remover_pos(item)
        #CONSULTA 
        return self.__remover_dato(item)
    
    def __remover_pos(self, pos_elm):
        actual = self.__cab
        indice = 0 
        anterior = None

        if pos_elm >= 0:
            while actual and indice < pos_elm:
                anterior = actual
                actual = actual.sig
                indice+= 1

            if indice == 0 and actual:
                self.__cab = actual.sig
            elif actual:
                anterior.sig = actual.sig
            
        return True if actual and pos_elm == indice else False


    def __remover_dato(self, dato_elm):
        actual = self.__cab
        while actual:
            if actual.dato is dato_elm:
                pass
    
    #devuelve valor booleano

if __name__ == "__main__":
    lista = Lista_SE()
    lista.adicionar(5)
    lista.adicionar(7)
    lista.adicionar(9)
    lista.recorrer()
    print(lista.encontar(2))
    print(lista.encontar(9))
    print(lista.remover(1))
    print(lista.remover(-5))
    print(lista.remover(0))
    print(lista.remover(4))