from bed.jerarquicas.abin_bus import ArbolBinario_Bus

def test_arbol_binario_bus():
    # Crear árbol
    arbol = ArbolBinario_Bus()

    # Adicionar elementos
    arbol.adicionar(50)
    arbol.adicionar(40)
    arbol.adicionar(60)
    arbol.adicionar(30)
    arbol.adicionar(41)
    arbol.adicionar(55)
    arbol.adicionar(75)
    arbol.adicionar(25)
    arbol.adicionar(35)
    arbol.adicionar(65)
    arbol.adicionar(86)

    # Test de búsqueda
    assert arbol.encontrar(50) == 50
    assert arbol.encontrar(75) == 75
    assert arbol.encontrar(35) == 35
    assert arbol.encontrar(100) is None

    # Test de mínimo y máximo
    assert arbol.econtrar_minimo() == 25
    assert arbol.econtrar_maximo() == 86

    # Test de eliminación (mayor)
    arbol.remover(40, mayor=True)
    assert arbol.encontrar(40) is None
    assert arbol.encontrar(35) == 35  # Verificar que el mayor de los menores (35) ha reemplazado a 40

    # Test de eliminación (menor)
    arbol.remover(60, mayor=False)
    assert arbol.encontrar(60) is None
    assert arbol.encontrar(65) == 65  # Verificar que el menor de los mayores (65) ha reemplazado a 60

    print("Todos los tests pasaron correctamente.")

# Ejecutar pruebas
test_arbol_binario_bus()
