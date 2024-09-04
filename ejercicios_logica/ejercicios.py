
def convertir_notas(notas):
    if notas:
        


def Almacenamiento_notas():
    notas_matematicas = []
    notas_fisica = []
    notas_quimica = []

    lista_materias = ["matematicas", "fisica", "quimica"]
    lista_numero_notas = int(input("Ingrese el numero de notas que va a digitar: "))
    lista_notas = []

    for i in range(lista_numero_notas):
        if lista_materias[i] != None:
            notas = input(f"Ingrese las notas de la materia de {lista_materias[i]}, separado por un espacio cada nota :")
            notas_finales = convertir_notas(notas)
            lista_notas.append(notas_finales)
        else:
            break

    for i in range(len(lista_materias)):
        print(f"notas de {lista_materias[i]} : {lista_notas[i]}")







Almacenamiento_notas()



