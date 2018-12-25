# ---------- CLASE --------------------------------

class PlayerDict:

    print("\n# ---------- __init__ con Diccionario --------------------------------\n")
    # lo tienen todas las clases

    """ En vez de inicializar los campos como hizimos antes:
    def __init__(self, hit_points=50, mana=50, vocation="No vocation", hechizo="Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo
        """
    """ ahora se inicializan usando el diccionario:"""
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)
        self.vocation = kwargs.get("vocation", "No vocation")
        self.hechizo = kwargs.get("hechizo", "Puff")


    print("\n# ---------- METODOS DE CLASES--------------------------------\n")

    def lanzar_hechizo(self):
        return  self.hechizo


