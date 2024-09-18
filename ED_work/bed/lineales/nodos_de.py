class Nodo_listaDE:
    """clase que modela un nodo para una estructura de lista doblemente enlazada
    """
    
    def __init__(self, dato):
        """metodo constructor para una lista doblemente enlazada

        Parameters
        ----------
        dato : object
            el dato que se pasa al nodo
        """
        self.dato = dato
        self.next = None
        self.back = None
    
    def __str__(self):
        """metodo que retorna una cadena con el dato del nodo

        Returns
        -------
        str
            la cadena ha ser retornada por el nodo que incluye el dato
        """
        return str(self.dato)


