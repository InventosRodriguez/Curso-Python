import re

print("\n# ---------- FICHEROS -------------------------------\n")

archivo = open("sample.txt", encoding="utf-8")   # abre el fichero

information = archivo.read()                     # lee el contenido y lo guarda en una variable

archivo.close()                                  # cierra el fichero

print(information)                               # imprime el fichero

print("\n# ---------- BUSCAR -------------------------------\n")

print(re.match(r"abcdefghijklmnopqrstuvwxyz", information))   # busca el texto indicado en la primera linea del fichero

# busca en to.do el fichero, independientemente de en que linea esté
# cuando encuentra el priemro para
print(re.search(r"0123456789", information))

#para buscar la misma cadena todas las veces que aparezca en el fichero usamos:
print(re.findall(r"0123456789", information))

"""
Podemos buscar por clases de caracteres, según indica la siguiente tabla.
En la web regexr:
https://regexr.com/

Character classes
.	any character except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace

Anchors
^abc$	start / end of the string
\b\B	word, not-word boundary
Escaped characters
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return
Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead
"""
print(re.search(r"\+\d", information))

print("\n# ---------- CUANTIFICADORES -------------------------------\n")
"""
Quantifiers & Alternation
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
"""

print("\n# ---------- CONJUNTOS -------------------------------\n")
"""
Expresiones regulares que van entre corchetes:
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
"""
print(re.search(r"[a-c]", information))   #devuelve to.do lo que contenga una a, b y c

print("\n# ---------- ESCRIBIR -------------------------------\n")

#en "w" se pone asi para crear el fichero en modo escritura
#pero tiene otros modos, por ejemplo solo-lectura.
archivo_lista = open("lista.txt", "w")

archivo_lista.write("mi primer archivo creado en python\n")
archivo_lista.write("otra linea")

archivo.close()