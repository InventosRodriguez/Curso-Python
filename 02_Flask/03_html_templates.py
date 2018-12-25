print("\n# ---------- DESPLEGAR HTML: TEMPLATES Y HERENCIAS-------------------------------\n")
""" CODIGO HTMKL 

El código html hay que meterle en una carpeta llamada templates
Flask usa un motor de templates llamado jinja2. ¿que es eso? pues es lo que permite meter las 
variables del archivo .py dentro del archivo .html y poderlas usar. En el .html se meten entre {}
<>
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)  # dice que nuestra app apunte a Flask

print("\n# ---------- DESPLEGAR HTML: FORMA LARGA -------------------------------\n")

#http://127.0.0.1:5000/alvaro
@app.route("/")
@app.route("/<nombre>")
def hello_world(nombre = "invitado"):
    contexto = {'nombre': nombre}
    return render_template("index.html", **contexto)



@app.route("/suma/<int:num1>/<int:num2>") # http://127.0.0.1:5000/suma/5/3
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
def suma(num1=0, num2=0):

    #manera1:
    #return render_template("suma.html", num1=num1, num2=num2)   #aqui le pasamos la variables al .html

    #manera2:
    contexto = {'num1': num1, 'num2': num2}
    return render_template("suma.html", **contexto)  # aqui le pasamos la variables al .html


@app.route("/contacto/")
def contacto():
    return render_template("contacto.html")


@app.route("/enviar", methods=['POST'])
def enviar():
    return "Exito"


if __name__ == "__main__":
    app.run(debug=True)








