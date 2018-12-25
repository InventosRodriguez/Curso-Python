print("\n# ---------- RECIBIR CONTENIDO POR LA URL-------------------------------\n")
"""
>
<
"""
from flask import Flask
from flask import request

app = Flask(__name__)  #dice que nuestra app apunte a Flask


"""
Los programas en flask se llaman app

Las routes son las carpetas de la app: 
    app/route/route  -- aqui se ve como la app sería la dirección ip y las routes cada una de las carpetas separadas por /
    http://127.0.0.1:5000/login/user

    app.route("/")
    app.route("/home")
    
    http://127.0.0.1:5000/home  -- ese  

@app.route("/")        #crea una ruta, donde va a ir esta app. Cada py podrá ir en una ruta.
def hello():           #se ejecutará cuando se ponga 127.0.0.1:5000/
    return "Hey World! q pacha"
"""

@app.route("/images")  #asocia la función hello_images con 127.0.0.1:5000/images
def hello_images():    #se ejecutará cuando se ponga 127.0.0.1:5000/images
    return "Hello Images"


print("\n# ---------- QUERY STRING, RECIBIR CONTENIDO POR LA URL CON LAS VARIABLES--------------------------------\n")

""" ejemplo de como se ponen las variables en la url:
1270.0.01:5000/?variable1=2&variable2=b

ejemplo:
1270.0.01:5000/?nombre_url=alvaro&apellido_url=rodriguez
"""
@app.route("/")  #asocia la función hello_images con 127.0.0.1:5000/
@app.route("/<nombre>/<apellido>")  #asocia las variables de la funcion con la url, con esto se puede poner directamente en la url: http://127.0.0.1:5000/alvaro/rodri
def recibir_datos(nombre="invitado", apellido='vacio'):    #se ejecutará cuando se ponga 127.0.0.1:5000/images

    # recibe el nombre que se mete por la url. Si no se recibe nada por defecto pone Invitado
    return "Hello {} {}".format(nombre, apellido)



#EJEMPLO1 de suma pasando por url los campos y los valores
#http://127.0.0.1:5000\suma1?num1=5&num2=3
@app.route("/suma1")
def suma1(num1 = 0, num2 = 0):
    num1 = request.args.get('num1', num1)
    num2 = request.args.get('num2', num2)

    resultado = int(num1) + int(num2)
    return "{} mas {} es igua a {}".format(num1, num2, resultado)



print("\n# ---------- QUERY STRING, RECIBIR CONTENIDO POR LA URL SIN USAR LAS VARIABLES EN LA URL --------------------------------\n")
"""EJEMPLO2 de suma SIN pssar por url los campos y los valores

    http://127.0.0.1:5000/suma2/5/3
"""
@app.route("/suma/<num1>/<num2>")
@app.route("/suma/<int:num1>/<int:num2>")  #otra manera para que autoconvierta en int los numeros
@app.route("/sumar/<int:num1>/<int:num2>")  #admite varios routes para que llamen a una misma funcion
def suma2(num1 = 0, num2 = 0):

    #resultado = int(num1) + int(num2)
    resultado = num1 + num2   #si hemos puesto el int en el "app.route pues no nos hace falta el int en cada campo
    return "{} mas {} es igua a {}".format(num1, num2, resultado)





if  __name__ == "__main__":
    app.run(debug = True)  # con ésto se actualiza constantemente nuestra app en el servidor
    #app.run()  # con esto no se actualiza. Tendremos que parar el servidor y volver a arrancar







