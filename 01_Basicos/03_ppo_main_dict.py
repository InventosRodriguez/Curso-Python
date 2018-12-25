#los .py van en minusculas
#las clases en CamelCase
#los métodos en minusculas_separados_por_guiones

from playerdict import PlayerDict

print("\n# ---------- DICCIONARIO USANDO SUS PROPIOS METODOS -------------------------------\n")
#creando un diccionario mediante el método dict

dias = dict(lunes=1, martes=2, miercoles=3, jueves=4, viernes=5)
print(dias)
print(dias["lunes"])    #accede al valor por clave


print("\n# ---------- INSTANCIAR CLASES CON DICIONARIOS-------------------------------\n")

#sorcerer = PlayerDict()    #con ésto cogeríamos el diccionario por defecto
sorcerer = PlayerDict(hit_points=40, mana=80, vocation="sorcerer", hechizo="utevo lux")    #con ésto otro damos valor a los campos

print("El sorcerer tiene:")
print(sorcerer.hit_points)        #invoca a la variable de la clase sin usando el método
print(sorcerer.mana)              #invoca a la variable de la clase sin usando el método
print(sorcerer.vocation)          #invoca a la variable de la clase sin usando el método
print(sorcerer.lanzar_hechizo())  #invoca a la variable de la clase usando el método

knigth = PlayerDict(hit_points=80, mana=20, vocation="knigth", hechizo="exori")                 #INSTANCIAMOS OTRA CLASE IGUAL PERO CON NOMBRE KNIGTH

print("El knigth tiene:")
print(knigth.hit_points)
print(knigth.mana)
print(knigth.vocation)
print(knigth.lanzar_hechizo())

