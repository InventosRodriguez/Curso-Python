#los .py van en minusculas
#las clases en CamelCase
#los métodos en minusculas_separados_por_guiones

#from playerherencia import PlayerHerencia
import playerherencia       #importamos toda la clase para tener todos los métodpos

print("\n# ---------- HERENCIA Y CLASES -------------------------------\n")


sorcerer = playerherencia.Sorcerer(hit_points=40, mana=80)  # nos hemos traido los atributos del padre(player). Sin embargo los atributos propios del hechicero ya están peestablecidos en su propia clase.

print("El sorcerer tiene:")
print(sorcerer.hit_points)        #invoca a la variable de la clase sin usando el método
print(sorcerer.mana)              #invoca a la variable de la clase sin usando el método
print(sorcerer.vocation)          #invoca a la variable de la clase sin usando el método
print(sorcerer.lanzar_hechizo())  #invoca a la variable de la clase usando el método
print(sorcerer.movement_speed)

print(sorcerer)                   # ésto invoca al __str___

knigth = playerherencia.Knigth(hit_points=80, mana=20)

print("El knigth tiene:")
print(knigth.hit_points)
print(knigth.mana)
print(knigth.vocation)
print(knigth.lanzar_hechizo())
print(knigth.movement_speed)

print(knigth)                   # ésto invoca al __str___

