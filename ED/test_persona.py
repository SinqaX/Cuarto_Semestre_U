from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.exepciones import HomogeneityError, DuplicatedKeyError
from bed.jerarquicas.recorrido import str_pre_orden, str_in_orden, str_post_orden
from persona import Persona


def test_personas():
    p1 = Persona("Maria", 25)
    p2 = Persona("Carlos", 40)
    p3 = Persona("Ana", 10)
    p4 = Persona("Pedro", 30)
    p5 = Persona("Juan", 20)
    p6 = Persona("Ana", 50)

    abb_per = ArbolBinario_Bus()
    abb_per.adicionar(p1)
    abb_per.adicionar(p2)
    abb_per.adicionar(p3)
    abb_per.adicionar(p4)
    abb_per.adicionar(p5)
    abb_per.adicionar(p6)
    
    print(str_pre_orden(abb_per))
    print(abb_per.encontrar(Persona("Ana",50)))
    print(abb_per.encontrar_maximo())
    print(abb_per.encontrar_minimo())
    print(abb_per.altura())
    print(len(abb_per))
    print(abb_per.hojas())
    print(abb_per.internos())
    




if __name__ == "__main__":
    test_personas()

