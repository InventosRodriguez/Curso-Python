print("\n# ---------- SLICES --------------------------------\n")

numeros = [0,1,2,3,4,5,6,7,8,9,10]
print(numeros)

print(numeros[1])
print(numeros[0:6])    # EL SLICE CORTA UNA REBANADA DE LA LISTA. INDICAR LAS POSICIONES COMO EN COBOL
print(numeros[5:])     #SI NO PONES NADA TRAS LOS PUNTOS SACA TODA LA LISTA DESDE EL PUNTO INICIAL HASTA EL FINAL
print(numeros[:5])     #Y VICEVERSA
print(numeros[:])     #Y SINO PONE SNADA SACA TODAS
print(numeros[-6:8])     #INDICE NEGATIVO


print("\n# ---------- SLICES - STEPS------------------------------\n")
#Nº DE PASOS ENTRE CADA UNO DE LOS ELEMENTOS DE LA REBANADA
print(numeros[::2])    # se salta los indices que pongas en el 3er parametro

print("\n# ---------- SLICES - reemplazar y borrar------------------------------\n")

del numeros[0]   # borra el indice 0
print(numeros)

numeros[1:2] = numeros[3:4]   # reemplazar
print(numeros)

del numeros[2:4]   # borra el indice del 5:2
print(numeros)

numeros[1:2] = [80,80]
print(numeros)

print("\n# ---------- DICCIONARIOS ------------------------------\n")
lista_calificaciones = [9,10,6,5]
print(lista_calificaciones)

diccionario_calificaciones = {"Pablo":9, "Alvaro":10, "Tania":6, "Pepe":5}
print(diccionario_calificaciones)

print(diccionario_calificaciones["Alvaro"])

diccionario_calificaciones["Alvaro"] = 8
print(diccionario_calificaciones)

print(dict([["pepe",7],["maria",4]]))   # esto es lo mismo pero usando la funcion dict, que es mas lioso


print("\n# ---------- DICCIONARIOS - Agregar,borrar y actualizar-----------\n")

dias_semana = {"lunes":9,
               "martes": 10,
               "miercoles": 11}
print(dias_semana)

dias_semana["jueves"] = 12   # añadir campo al diccionario
print(dias_semana)

del dias_semana["lunes"]     # eliminar campo del diccionario
print(dias_semana)

dias_semana.update({"viernes":13,   #con update, si no existe el campo lo inserta
                    "sabado":14})
print(dias_semana)

dias_semana.update({"sabado":15,   #con update si existe el campo lo actualiza
                    "domingo":16})
print(dias_semana)


print("\n# ---------- DICCIONARIOS - Iterar-----------\n")
#UN DICCIONARIO NO TIENE UN ORDEN PRESTABLECIDO, no fiarse del indice que veamos porque puede cambiar

calificaciones = {"alvaro":9,
                  "tania":10,
                  "pepe":12}
print(calificaciones)

for keys in calificaciones:
    print(keys)                   #con esto mostramos las keys
    print(calificaciones[keys])   #con esto mostramos los valores

for keys in calificaciones.keys():  #con esto mostramos tb las keys
    print(keys)

for valores in calificaciones.values():  #con esto mostramos tb los valores
    print(valores)

for keys_values in calificaciones.items():   # con esto mostramos ambas cosas. TUPLA
    print(keys_values)

print("\n# ---------- DICCIONARIOS - ordenado-----------\n")

def add_entry():
    """comentario add_entry"""
    print("addentry")

#hay una liberia q permite tener ordenado un diccionario
from collections import  OrderedDict
menu = OrderedDict([
    ('a', add_entry),     #tupla1. En add entry puedes poner el nombre de una funcion q tengas, de ese modo te la va a ejecutar
    ('v', 'view entry'),    #tupla2
    ('d', 'delete entry')   #tupla3
])

for key,value in menu.items():   #recorre las tuplas del diccionario
    print("{} {}".format(key, value))
    print("{} {}".format(key, value.__doc__))  # con el __doc__ accedes a los comentarios de la funcion, add_entry




print("\n# ---------- TUPLAS -----------\n")

#A DIFERENCIA DE LAS LISTAS, LAS TUPLAS son inmutables, so se pueden modficar elemtos, ni añador ni borrar
#ES ALGO ASÍ COMO UNA LISTA DE CONSTANTES
#LO QUE SI QUE SE PUEDE ES MODIFICAR UN OBJETO MUTABLE DENTRO DE LA TUPLA,
# #POR EJEMPLO, SI TIENES UNA LSITA DENTRO DE LA TUPLA,
# PUES PUEDES MODIFICAR LA LISTA PERO NO LA TUPLA.

tupla_1 = (1, 2, 3, 4)       # una manera definir la tupla
print(tupla_1)

tupla_2 = 1, 2, 3, 4         # otra manera de definirla. Es decir, los parentesis son standar pero no obligatorios
print(tupla_2)

#del tupla_1[0]               #ESTO NO LO PERMITE,PORQUE LAS TUPLAS SON INMUTABLES


print("\n# ---------- RANDOM -----------\n")

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

print("\n# ---------- CONJUNTOS -----------\n")

"""
Operation	              | Equivalent | Result
-----------------------------------------------------------------------------------------
len(s)	 	                             number of elements in set s (cardinality)
x in s	 	                             test x for membership in s
x not in s	 	                         test x for non-membership in s
s.issubset(t)	            s <= t	     test whether every element in s is in t
s.issuperset(t)	            s >= t	     test whether every element in t is in s
s.union(t)	                s | t	     new set with elements from both s and t
s.intersection(t)	        s & t	     new set with elements common to s and t
s.difference(t)	            s - t	     new set with elements in s but not in t
s.symmetric_difference(t)	s ^ t	     new set with elements in either s or t but not both
s.copy()	 	                         new set with a shallow copy of s
-----------------------------------------------------------------------------------------
"""
# NO SE PUEDEN MODIFICAR ELEMENTOS DE UN CONJUNTO
# NO SE GUARDAN EN EL ORDEN EN EL QUE SE INTRODUCEN
# QUITA DUPLICADOS

conjunto_x = set("1 2 3 4 5".split())
print(conjunto_x)

conjunto_x = set("12345")
print(conjunto_x)




conjunto_a = set("12345")
conjunto_b = set("567890")

print("\n# ---------- CONJUNTOS UNION-----------\n")
#UNE AMBOS CONJUNTOS

print(conjunto_a.union(conjunto_b))


print("\n# ---------- CONJUNTOS INTERSECCION-----------\n")
#GUARDA LOS ELEMENTOS IGUALES. CLAVES IGUALES

print(conjunto_a.intersection(conjunto_b))

print("\n# ---------- CONJUNTOS DIFERENCIA-----------\n")
#GUARDA LOS ELEMENTOS que sean diferentes respecto al otro conjunto
#CLAVES MAYOR O MENOR. TE GUARDA DEL CONJUNTO QUE PONGAS A LA IZQUIERDA

print(conjunto_a.difference(conjunto_b))

print("\n# ---------- CONJUNTOS DIFERENCIA SIMETRICA-----------\n")
#GUARDA TODOS LOS ELEMENTOS DIFERENTES DE AMBOS CONJUNTOS

print(conjunto_a.symmetric_difference(conjunto_b))






