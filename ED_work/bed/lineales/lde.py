from nodos_de import Nodo_listaDE

class Lista_DE:
    """Clase que implementa el funcionamiento de una lista doblemente enlazada
    """

    # (1) Método Constructor
    def __init__(self):
        """Método que realiza la creación e inicialización de la Lista Doblemente Enlazada.
        """
        self.__cab = None
        self.inverso = False
    
    # (2) Método es_vacia
    def es_vacia(self):
        """Método que verifica si la lista se encuentra vacía.

        Returns
        -------
        bool
            Retorna True si la lista es vacia. False en caso contrario.
        """
        return self.__cab is None
    
    # (3.1) Método adicionar al final de la lista
    def adicionar(self, nuevo_dato):
        """ Método que adiciona un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.

        Returns
        -------
        bool
            True cuando el dato es añadido en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaDE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            actual = self.__cab
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo
            nuevo_nodo.back = actual
        return True
    
    # (3.2) Método posicionar
    def posicionar(self, nuevo_dato, pos):
        """Método que inserta un nuevo nodo en cualquier posición de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaDE(nuevo_dato)
        
        # Caso 1: Insertar en la primera posición
        if pos == 0:
            nuevo_nodo.next = self.__cab  # El nuevo nodo apunta al antiguo primer nodo.
            
            if self.__cab:  # Si la lista no estaba vacía
                self.__cab.back = nuevo_nodo  # El antiguo primer nodo ahora apunta de vuelta al nuevo nodo
            
            nuevo_nodo.back = None  # El nuevo nodo es el primero, no tiene anterior, por lo que su back es None.
            self.__cab = nuevo_nodo  # Actualizamos la cabeza de la lista para que apunte al nuevo nodo.

        # Caso 2: Insertar en una posición intermedia o al final
        else:
            actual = self.__cab
            indice = 0
            
            # Recorrer la lista hasta llegar a la posición deseada
            while actual and indice < pos - 1:
                actual = actual.next
                indice += 1
            
            # Si hemos llegado a una posición válida (dentro de la lista)
            if actual:
                nuevo_nodo.next = actual.next  # El nuevo nodo apunta al siguiente de "actual"
                nuevo_nodo.back = actual       # El nuevo nodo apunta hacia atrás a "actual"
                if actual.next:  # Si hay un nodo después del actual, actualizamos su back
                    actual.next.back = nuevo_nodo
                actual.next = nuevo_nodo  # El nodo actual ahora apunta al nuevo nodo
            else:
                return False  # La posición no es válida, fuera de rango

        return True
    

    # (6) Método remover por dato (* CONSULTA) o posición
    def remover(self, item, por_pos=True):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            return self.__remover_dato(item)
    

        
    def __remover_pos(self, pos_elm):
        actual = self.__cab
        indice = 0

        if pos_elm >= 0:
            # Recorrer la lista hasta la posición deseada
            while actual and indice != pos_elm:
                actual = actual.next
                indice += 1
            
            # Caso: Eliminar el primer nodo
            if indice == 0 and actual:
                self.__cab = actual.next
                if self.__cab:  # Si la lista no queda vacía
                    self.__cab.back = None
                return True
            
            # Caso: Eliminar un nodo intermedio o final
            elif actual:
                actual.back.next = actual.next
                if actual.next:  # Si no es el último nodo, actualiza el back
                    actual.next.back = actual.back
                return True
        
        # Si no se encontró el nodo o la posición es inválida
        return False
            

    # (6.2) Método oculto remover por dato
    def __remover_dato(self, dato_eliminar):
        """Método que remueve todos los nodos que contengan el dato especificado.

        Parameters
        ----------
        dato_eliminar : object
            Corresponde al valor del dato a ser removido de la lista.

        Returns
        -------
        bool
            True si se eliminó al menos un nodo con el dato especificado, False en caso contrario.
        """
        eliminado = False
        anterior = None
        actual = self.__cab
        while actual:
            if actual.dato == dato_eliminar:
                if anterior:
                    anterior.sig = actual.sig
                else:
                    self.__cab = actual.sig
                eliminado = True
            else:
                anterior = actual
            actual = actual.sig
        return eliminado



       