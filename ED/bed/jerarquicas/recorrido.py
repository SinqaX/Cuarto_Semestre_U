
def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol.clave)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)

def str_pre_orden(arbol_bin, sep = '|'):
    pass


#post orden
#__pre_orden(sub_arbol.der)
#__pre_orden(sub_arbol.izq)
        
# in orden
# __pre_orden(sub_arbol.izq)
# __pre_orden(sub_arbol.der)
# print(sub_arbol.clave)





