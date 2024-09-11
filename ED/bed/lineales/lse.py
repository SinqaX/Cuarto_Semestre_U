# print(f"NAME: {__name__} PAQUETE: {__package__}")
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE
else:
    from bed.lineales.nodos import Nodo_listaSE


class Lista_SE:
    """Clase qie crea una lista simplemente enlazada
    """

    def __init__(self):
        """metodo contructor de un objeto de una lista simplemente enlazada
        """
        
        #este atributo va a quedar oculto con __
        self.__cab = None
    
    def es_vacia(self):
        """metodo que retorna un dato de tipo booleano si la lista esta vacia

        Returns
        -------
        bool
            True si la lista esta vacia de lo contrario retorna False
        """

        if not self.__cab:
            return True
        return False

    def adicionar (self,nuevo_dato):
        if isinstance(nuevo_dato, int):
            nuevo_nodo = Nodo_listaSE(nuevo_dato)
            if self.es_vacia():
                self.__cab = nuevo_nodo
            else:
                #caso cuando la lista no es vacia
                actual = self.__cab
                while actual.sig:
                    actual = actual.sig
                actual.sig = nuevo_nodo
        else:
            print(f"el dato ingresado {nuevo_dato} no es numerico")
            
    def recorrer (self):
        """metodo que recorre la lista imprimiendo cada uno de los datos que contenga siempre y cuando no sa una lista vacia
        """
        actual = self.__cab
        while actual:
            print(actual)
            actual = actual.sig
        
    def encontrar(self, dato_encontrar):
        """metodo que realiza una busqueda del dato en la lista

        Parameters
        ----------
        dato_encontrar : object
            dato que se va a buscar

        Returns
        -------
        object | None
            onject si se encuentra el dato en la lista de lo contraruo retornara None
        """
        actual = self.__cab
        while actual:
            if actual.dato is dato_encontrar:
                return actual.dato
            actual = actual.sig
    
    def remover(self, item, por_pos=True):# este item va a ser un dato o la posicion
        if por_pos:
            return self.__remover_pos(item)
        #consulta 
        return self.__remover_dato(item)
    
    def __remover_pos(self, pos_elim):
        actual = self.__cab
        indice = 0
        
        # Caso especial: lista vacía
        if actual is None:
            print("La lista está vacía.")
            return
        
        # Caso de eliminar el primer nodo (posición 0)
        if pos_elim == 0:
            self.__cab = actual.sig  # Mover la cabeza al siguiente nodo
            print(f"Nodo en la posición {pos_elim} eliminado.")
            return
        
        # Recorrer la lista para encontrar el nodo en la posición a eliminar
        anterior = None
        while actual:
            if indice == pos_elim:
                # Enlazar el nodo anterior al siguiente del nodo actual
                if anterior:
                    anterior.sig = actual.sig
                print(f"Nodo en la posición {pos_elim} eliminado.")
                return
            
            # Actualizar punteros y seguir recorriendo la lista
            anterior = actual
            actual = actual.sig
            indice += 1

    def __remover_dato(self, dato):
        pass



 
if __name__ == "__main__":

    lista = Lista_SE()
    lista.adicionar(5)
    lista.adicionar(10)
    lista.adicionar(12)
    lista.adicionar(16)
    
    lista.remover(-1)
    lista.remover(89)
    lista.remover(2)
    lista.remover(7)
    lista.recorrer()
    
