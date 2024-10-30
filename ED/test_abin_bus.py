import unittest
from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.exepciones import DuplicatedKeyError, HomogeneityError
from bed.jerarquicas.nodos import nodoArbol_Bin
from bed.jerarquicas.recorrido import (
    str_pre_orden, 
    str_in_orden, 
    str_post_orden
)

class TestNodoArbolBin(unittest.TestCase):
    def setUp(self):
        self.nodo = nodoArbol_Bin(10)
        
    def test_creacion_nodo(self):
        self.assertEqual(self.nodo.clave, 10)
        self.assertIsNone(self.nodo.izq)
        self.assertIsNone(self.nodo.der)
        
    def test_tiene_hijos(self):
        self.assertFalse(self.nodo.tiene_hijos())
        self.nodo.izq = nodoArbol_Bin(5)
        self.assertTrue(self.nodo.tiene_hijos())
        
    def test_str_representation(self):
        self.assertEqual(str(self.nodo), "10")

class TestArbolBinarioBus(unittest.TestCase):
    def setUp(self):
        self.arbol = ArbolBinario_Bus()
        # Crear una estructura de árbol completa para las pruebas
        self.valores_prueba = [50, 30, 70, 20, 40, 60, 80]
        for valor in self.valores_prueba:
            self.arbol.adicionar(valor)
            
    def test_arbol_vacio(self):
        arbol_vacio = ArbolBinario_Bus()
        self.assertIsNone(arbol_vacio.raiz)
        self.assertEqual(len(arbol_vacio), 0)
        
    def test_adicionar_y_buscar(self):
        # Probar que todos los valores se pueden encontrar
        for valor in self.valores_prueba:
            self.assertEqual(self.arbol.encontrar(valor), valor)
        
        # Probar que un valor que no existe retorna None
        self.assertIsNone(self.arbol.encontrar(100))
            
    def test_duplicated_key_error(self):
        with self.assertRaises(DuplicatedKeyError):
            self.arbol.adicionar(50)  # Intentar agregar un valor que ya existe
            
    def test_homogeneity_error(self):
        with self.assertRaises(HomogeneityError):
            self.arbol.adicionar("50")  # Intentar agregar string cuando hay enteros
            
    def test_encontrar_minimo_maximo(self):
        self.assertEqual(self.arbol.encontrar_minimo(), 20)
        self.assertEqual(self.arbol.encontrar_maximo(), 80)
        
        # Probar con árbol vacío
        arbol_vacio = ArbolBinario_Bus()
        self.assertIsNone(arbol_vacio.encontrar_minimo())
        self.assertIsNone(arbol_vacio.encontrar_maximo())
        
    def test_remover_hoja(self):
        self.arbol.remover(20)  # Remover una hoja
        self.assertIsNone(self.arbol.encontrar(20))
        self.assertEqual(len(self.arbol), len(self.valores_prueba) - 1)
        
    def test_remover_nodo_con_un_hijo(self):
        # Primero agregamos un hijo a 20 para crear la situación
        self.arbol.adicionar(10)
        self.arbol.remover(20)
        self.assertIsNone(self.arbol.encontrar(20))
        self.assertIsNotNone(self.arbol.encontrar(10))
        
    def test_remover_nodo_con_dos_hijos(self):
        self.arbol.remover(30)  # Nodo con dos hijos
        self.assertIsNone(self.arbol.encontrar(30))
        # Verificar que los hijos siguen existiendo
        self.assertIsNotNone(self.arbol.encontrar(20))
        self.assertIsNotNone(self.arbol.encontrar(40))
        
    def test_remover_raiz(self):
        self.arbol.remover(50)  # Remover la raíz
        self.assertIsNone(self.arbol.encontrar(50))
        # Verificar que el árbol sigue siendo válido
        self.assertTrue(self.__es_arbol_binario_busqueda_valido(self.arbol.raiz))
        
    def __es_arbol_binario_busqueda_valido(self, nodo, min_valor=float('-inf'), max_valor=float('inf')):
        if nodo is None:
            return True
            
        if nodo.clave <= min_valor or nodo.clave >= max_valor:
            return False
            
        return (self.__es_arbol_binario_busqueda_valido(nodo.izq, min_valor, nodo.clave) and
                self.__es_arbol_binario_busqueda_valido(nodo.der, nodo.clave, max_valor))
        
    def test_len(self):
        self.assertEqual(len(self.arbol), len(self.valores_prueba))
        self.arbol.remover(50)
        self.assertEqual(len(self.arbol), len(self.valores_prueba) - 1)

class TestRecorridos(unittest.TestCase):
    def setUp(self):
        self.arbol = ArbolBinario_Bus()
        valores = [50, 30, 70, 20, 40, 60, 80]
        for valor in valores:
            self.arbol.adicionar(valor)
            
    def test_str_pre_orden(self):
        resultado = str_pre_orden(self.arbol)
        self.assertIn("[🌲]50", resultado)  # Raíz
        self.assertIn("(🌿)30", resultado)  # Nodo interno
        self.assertIn("(🍂)20", resultado)  # Hoja
        
    def test_str_in_orden(self):
        resultado = str_in_orden(self.arbol)
        # Verificar que los números aparecen en orden
        numeros = [int(''.join(filter(str.isdigit, parte))) 
                  for parte in resultado.split(':') if any(c.isdigit() for c in parte)]
        self.assertEqual(numeros, sorted(numeros))
        
    def test_str_post_orden(self):
        resultado = str_post_orden(self.arbol)
        self.assertTrue(resultado.endswith("[🌲]50"))  # En post-orden, la raíz debe ser el último
        
    def test_tipos_nodos_en_recorridos(self):
        for recorrido in [str_pre_orden, str_in_orden, str_post_orden]:
            resultado = recorrido(self.arbol)
            # Solo debe haber una raíz
            self.assertEqual(resultado.count("[🌲]"), 1)
            # Debe haber al menos una hoja
            self.assertGreater(resultado.count("(🍂)"), 0)

if __name__ == '__main__':
    unittest.main()