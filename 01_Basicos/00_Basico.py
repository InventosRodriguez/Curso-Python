print("hola mundo")

# comentario

"""comentario
multilínea"""

# ---------- CONDICIONES --------------------------------
"""        #doctring
==
>  
>=
<
<=
"""

print("\n# ---------- AYUDA PYTHON --------------------------------\n")

help(str)
help(list)


print("\n# ---------- CONDICIONES --------------------------------\n")

edad = 22 #comentario

if edad == 21:
    print("puedes entrar")
    print("y puedes beber")
else:
    print("no puedes entrar")
print("esto lo ejecuto siempre porque no lleva tabulador")

if edad == 21:
    print("puedes entrar")
elif edad >= 21:
    print("puedes entrar y ademas puedes beber")
else:
    print("no puedes entrar")

# ---------- FUNCIONES --------------------------------
# notación standar: minusculas_con_guiones_bajos
print("\n# ---------- FUNCIONES --------------------------------\n")

def pedir_pizza():
    print("Pedir pizza")

pedir_pizza()


def checar_entrada(edad2):
    if edad2 == 21:
        print("funcion: puedes entrar".capitalize())
    elif edad2 >= 21:
        print("funcion: puedes entrar y ademas puedes beber")
    else:
        print("funcion: no puedes entrar".capitalize())

edad2=18
checar_entrada(edad2)

# ---------- LISTAS --------------------------------
"""
A las listas no les importa lo que haya dentro, puede tener campos de varios tipos de dato. 
Incluso se puede meter una lista dentro de otra.
"""
print("\n# ---------- LISTAS --------------------------------\n")

lista = [1,2,3,4,5]    # definir lista
print(lista)

lista = lista + [5,6]  # añadir valores a la lista
print(lista)

lista2 = [7,8]         # añadir una lista a otra
lista = lista + lista2
print(lista)

lista += [9,10]        # añadir valores a la lista de otra manera
print(lista)

lista.append(11)       # añadir valores a la lista mediante un método. El append solo admite un valor
print(lista)

lista.extend([12,13])  # con extend si que podemos añadir varios valores
print(lista)

print(lista * 5)        # para mostrar 5 veces la misma lista

lista.append(["a", "b", "c"])
print(lista)

lista.remove(8)         # eliminar un valor de la lista
print(lista)

print("\n# ---------- SPLIT Y JOIN --------------------------------\n")

lista3 = list([1,2,3,4,5])  # otra manera de añadir valores a una lista
print(lista3)

listalvaro = list("alvaro") # mete cada letra en un campo
print(listalvaro)


print("alvaro rodriguez".split())    # split: separa en varios un mismo campo
print("alvaro,rodriguez".split())
print("alvaro,rodriguez".split(",")) # si no pones nada por defecto usa el espacio para separar. En este caso usamos la coma

lista_nombres = ["alvaro","tania","riri"]  # une los campos de una lista en uno, dependiendo del separador puesto
print(lista_nombres)
print(",".join(lista_nombres))

lista_nombres = ["alvaro","tania","riri"]  # une los campos de una lista en uno, dependiendo del separador puesto
print(lista_nombres)
print(", ".join(lista_nombres))


print("\n# ---------- INDICES--------------------------------\n")
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
alfabeto_lista = list(alfabeto)             #convertimos texto en lista
print(alfabeto_lista)
print(alfabeto_lista.index("A"))            #indice de la letra A
print(alfabeto_lista.index("B"))            #indice de la letra B
print(alfabeto_lista[10])                   #muestra el campo del indice 10
print(alfabeto_lista[-1])                   #se pueden usar indices negativos, lo que hace es empezar a contar desde el final hacia el principio


print(alfabeto.index("B"))                  #indice de la letra B pero de la cadena

print("\n# ---------- DEL--------------------------------\n")
vocales = "aeiou"
lista_vocales = list(vocales)
print(lista_vocales)
del lista_vocales[0]                       # borra la variable que haya en el indice, en este caso la "a"
print(lista_vocales)

variable_basura = "variable basura!!"
#del variable_basura                         #borra la variable
print(variable_basura)

print("\n# ---------- IN--------------------------------\n")
#identifica si algo está dentro de otro algo
#ejemplo: dice si una variable está dentro de una lsita

vocales2 = "aeiou"
lista_vocales2 = list(vocales2)
print("a" in vocales2)                     # devuelve true o false si la letra está en la lista o no

if "a" in vocales2:
    print("existe")
else:
    print("no existe")

if "a" not in vocales2:
    print("existe")
else:
    print("no existe")


print("\n# ---------- WHILE --------------------------------\n")
#>
#<

manzanas = 10

while manzanas > 0:
    print("me estoy comiendo una manzana: " + str(manzanas))
    manzanas = manzanas - 1


print("\n# ---------- FOR --------------------------------\n")

lista_numeros = ["a", "b", 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    print(numero)

for numero in lista_numeros:
    if numero == 3:
        break                         # con break rompes el bucle donde quieras. En este caso cuando llega al 3 se sale.
    print(numero)

for numero in lista_numeros:
    if numero == 3:
        continue                      # no rompe el bucle sino que se salta ese indice. En este caso se salta el 3
    print(numero)


print("\n# ---------- INPUT     --------------------------------\n")
#el imput siempre devuelve una cadena de texto

día_del_mes = input("que dia del mes es hoy???: ")
print(día_del_mes)

print("\n# ---------- CONVERSORES     --------------------------------\n")

diez_numerico = int("10")
print(diez_numerico)

diez_alfanumerico = str(10)
print(diez_alfanumerico)

print("\n# ---------- EXCEPCIONES     --------------------------------\n")

try:
    a = int(input("dame un numero"))
    b = int(input("dame un numero"))

except ValueError:                          # aqui ponemos lo que queremos que haga si falla.
    print("el numero debe ser numérico")
else:                                       # aqui ponemos lo que queremos que haga si va bien
    suma = a + b
    print("la suma es: " + str(suma))


print("\n# ---------- utilidades    --------------------------------\n")

#con este if indicamos que cuando importas una funion oslo se ejecute lo que metas dentro del if:
if __name__ == '__main__':
    print("main")

choise = None    #inicializa una variable cualquiera


