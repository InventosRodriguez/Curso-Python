# ---------- CLASE  con herencia y diccionario--------------------------------
#object es el objeto del que hereda to do. El patriarca vamos.

#class PlayerHerencia(object):   # el patriarca object a partir de python3 no es obligatorio ponerlo
class PlayerHerencia:
#Definimos atributos que solo algunos players tendrán:
    vocation = "No vocation"
    hechizo = "Puff"
    movement_speed = "50"

    #dejamos los atributos comunes a todos los players
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    #métodp común a todas las clases, como el init. Es como el String de java. Formatea la salida
    def __str__(self):
        return "El {} tiene: {} hit_points y {} mana, puede lanzar {} y corre a {} " \
               "movement_speed\n".format(self.vocation,
                                         self.hit_points,
                                         self.mana,
                                         self.lanzar_hechizo(),
                                         self.movement_speed)

    def lanzar_hechizo(self):
        return  self.hechizo

#definimos nueva clase Sorcerer y además la clase dela que va a heredar
class Sorcerer(PlayerHerencia):
    vocation = "Sorcerer"
    spell = "Utevo Lux"
    movement_speed = "20"

    #sobrescribir un método del padre, pero en el hijo. Se pone el mismo nombre y python da prioridad al hijo:
    # de este modo, mantiene el valor del atributo del padre y le añade el valor del hijo
    def lanzar_hechizo(self):
        return "{} y Exura".format(self.spell)

#definimos nueva clase Knigth y además la clase dela que va a heredar
class Knigth(PlayerHerencia):
    vocation = "Knigth"
    spell = "Exori"
    movement_speed = "60"

    #sobrescribir un método del padre, pero en el hijo. Se pone el mismo nombre y python da prioridad al hijo:
    # de este modo, mantiene el valor del atributo del padre y le añade el valor del hijo
    def lanzar_hechizo(self):
        return "{} y Exura".format(self.spell)
