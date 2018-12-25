
print("\n# ---------- BASES DE DATOS: PEEWEE --------------------------------\n")

"""
-ORM -- CONJUNTODE CLASES PARA ENCAPSULAR LAS CONSULTAS SQL. UNA DE ELLAS ES PEEWEE.
-Está escrito en Python y tiene soporte para las versiones 2.6.+ y 3.2.+
-Soporte para trabajar con SQLite, MySQL y PostGreSQL.

http://docs.peewee-orm.com/en/latest/peewee/quickstart.html
pip install peewee

-CRUD-- CREATE READ WRITE DELETE
"""

from peewee import *
from datetime import date

db = SqliteDatabase('people.db')   #damos nombre a la base de datos

#definimos una clase para cada tabla. Esta es la tabla Person y tiene 3 atributos/columnas
class Person(Model):
    name = CharField()            # columna name en formato char
    birthday = DateField()        # columna burthay en formato date
    is_relative = BooleanField()  # columna boolean en formato boleano

    class Meta:
        database = db # This model uses the "people.db" database.

#definimos una clase para cada tabla. Esta es la tabla Pet y tiene 3 atributos/columnas
class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')    #clave foranea que asocia Persons y Pets
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

print("\n# ---------- BASES DE DATOS: crear tablas y conectar a la db --------------------------------\n")
def create_and_connect():
    db.connect()            #crea la db, en este caso con el nombre people.db

    db.create_tables([Person, Pet], safe=True)  #Crear una/varias tablas, en este caso la clase Person

print("\n# ---------- BASES DE DATOS: INSERTAR --------------------------------\n")

def create_family_members():
    tania = Person(name="Tania", birthday=date(1982, 12, 9), is_relative=True)  #se cre un objeto con el contenido de la tabla person

    tania.save()    #inserta el registro

    #con el método .crete no es necesario llamar luego a alvaro.save
    alvaro = Person.create(name="Álvaro", birthday=date(1985, 8, 5), is_relative=False)  #se cre un objeto con el contenido de la tabla person

    tania_will = Pet.create(owner=tania, name="Will", animal_type="Gato")
    alvaro_elsa = Pet.create(owner=alvaro, name="Elsa", animal_type="Gato")

    print("\n# ---------- BASES DE DATOS: UPDATE --------------------------------\n")

    tania_will.name = "Rei"
    tania_will.save()

print("\n# ---------- BASES DE DATOS: CONSULTAR --------------------------------\n")

#select * from table:
def get_family_members():
    for person in Person.select():
        print("Nombre: {} fechanac: {} ".format(person.name, person.birthday))

#select * from table WHERE:
def get_family_member_birthay1(name):
    tania = Person.select().where(Person.name == name).get()
    print("el comple de tania es el: {}".format(tania.birthday))

#select * from table WHERE: Pero devuelve un unico registro em caso de haber varios.
#select ROW 1 VAMOS
def get_family_member_birthay2(name):
    tania = Person.get(Person.name == name)
    print("el comple de tania es el: {}".format(tania.birthday))

print("\n# ---------- BASES DE DATOS: BORRAR --------------------------------\n")
def delete_pet(name):
    delete = Pet.delete().where(Pet.name == name)

#    delete.execute()                        #se peude poner así solo pero mejor hacerlo como está justo debajo:
    delete_entries = delete.execute()        #nº de registros borrados
    print("registros borrados: {}".format( delete_entries))


create_and_connect()
create_family_members()
get_family_members()
get_family_member_birthay1("Tania")
get_family_member_birthay2("Tania")
delete_pet("Rei")

"""
D:\InventosRodriguez\Diseno\Curso Python\clasesdb>sqlite3 people.db
sqlite> .tables
person  pet
sqlite> .schema person
CREATE TABLE IF NOT EXISTS "person" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative"
 INTEGER NOT NULL);
 
sqlite>

"""


