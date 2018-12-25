#los .py van en minusculas
#las clases en CamelCase
#los métodos en minusculas_separados_por_guiones

from player import Player

print("\n# ---------- CLASES Y METODOS-------------------------------\n")

#print("El jugador tiene:")
#print(Player.hit_points)
#print(Player.mana)
#print(Player.vocation)

print("\n# ---------- INSTANCIAR CLASES-------------------------------\n")

sorcerer = Player(40, 80, "sorcerer", "utevo lux")    #INSTANCIAMOS LA CLASE PLAYER PARA USARLA DE MANERA INDEPENDIENTE
#sorcerer = Player(40, 80, "sorcerer")                #ejemplo1 de si usaramos el valor por defecto del ultimo campo.
#sorcerer = Player()                                  #ejemplo2 de si usaramos el valor por defecto del ultimo campo.


#otra manera de informar los campos
#sorcerer.hit_points = 40
#sorcerer.mana = 80
#sorcerer.vocation = "sorcerer"
#sorcerer.hechizo = "utevo lux"

print("El sorcerer tiene:")
print(sorcerer.hit_points)        #invoca a la variable de la clase sin usando el método
print(sorcerer.mana)              #invoca a la variable de la clase sin usando el método
print(sorcerer.vocation)          #invoca a la variable de la clase sin usando el método
print(sorcerer.lanzar_hechizo())  #invoca a la variable de la clase usando el método

knigth = Player(80, 20, "knigth", "exori")                 #INSTANCIAMOS OTRA CLASE IGUAL PERO CON NOMBRE KNIGTH

print("El knigth tiene:")
print(knigth.hit_points)
print(knigth.mana)
print(knigth.vocation)
print(knigth.lanzar_hechizo())

print("\n# ---------- DICCIONARIO USANDO SUS PROPIOS METODOS -------------------------------\n")
#creando un diccionario mediante el método dict

dias = dict(lunes=1, martes=2, miercoles=3, jueves=4, viernes=5)
print(dias)
print(dias["lunes"])    #accede al valor por clave