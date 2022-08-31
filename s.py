from ntpath import join
import os
from timeit import repeat
import itertools

def menu():
    print('''----------Menu----------
1. Crear protocolo
2. Agregar paso
3. Eliminar paso
4. Consulta los pasos existentes
5. Salir 
**Hay un maximo de 20 pasos**
-------------------------''')

protocolo = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    menu()
    opc = int(input("¿Que quieres hacer?: "))
    if opc == 1:
        print("Se ha creado la lista ")
        print("------------------------")
        print("")
    elif opc == 2:
        a = input("Escriba el paso: ")
        protocolo.append(a)
        more = input ("¿Deseas escribir otro paso? si/no: ")
        if more == "si":
            pasos = int(input("¿Cuantos pasos vas a agregar?: "))
            for x in itertools.repeat(None, pasos):
                a = input("Escriba el paso: ")
                protocolo.append(a)
        elif more == "no":
            print("")
            menu() 
        else: 
            print("Opción indefinida")
            print("")
    elif opc == 3:
        elim = int(input("¿Que paso quieres eliminar?: "))
        protocolo.pop(elim)
        print ("Se ha eliminado el paso",elim)
        print("")
    elif opc == 4:
        union = list(zip(num, protocolo))
        for i in union:
            print(i)
    elif opc == 5:
        print("Hasta luego")
        break
    else:
        print("Escoja una opción valida")