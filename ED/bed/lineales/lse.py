from nodos import Nodo_listaSE


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
        #metodo que recorre la lista imprimiendo cada uno de los datos que contenga siempre y cuando no sa una lista vacia
        actual = self.__cab
        while actual:
            print(actual)
            actual = actual.sig

 
if __name__ == "__main__":

    lista = Lista_SE()
    lista.adicionar(5)
    lista.adicionar(10)
    lista.adicionar(12)
    lista.adicionar("k")
    
    lista.recorrer()
    
