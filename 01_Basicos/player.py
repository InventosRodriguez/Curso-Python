# ---------- CLASE --------------------------------
#tiene que haberun metodo con el mismo nombre que la clase pero en mayusculas (osea el constructor)


class Player:
    # METODOS: funciones dentro de una clase

    """ se puede definir aqui tb las variables, pero lo suyo es definirlas en el __init__
    hit_points = 50
    mana = 50
    vocation = "No vocation"
    hechizo = "Puff"
    """

    print("\n# ---------- __init__ --------------------------------\n")
    # lo tienen todas las clases

    def __init__(self, hit_points=50, mana=50, vocation="No vocation", hechizo="Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo


    print("\n# ---------- METODOS DE CLASES--------------------------------\n")

    def lanzar_hechizo(self):
        return  self.hechizo


