print("\n# ---------- DESPLEGAR HTML -------------------------------\n")
""" CODIGO HTMKL 

El código html hay que meterlo entre las 3 comillas
<>
"""

from flask import Flask


app = Flask(__name__)  # dice que nuestra app apunte a Flask

print("\n# ---------- DESPLEGAR HTML: FORMA LARGA -------------------------------\n")

@app.route("/suma/<int:num1>/<int:num2>") # http://127.0.0.1:5000/suma/5/3
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")

def suma(num1=0, num2=0):

    return """ 
<!doctype html>
<html>
    <head>
        <title>Suma</title>
    </head>
    <body>
        <h1>{} mas {} es igua a {}</h1>
    </body>
</html> 
""".format(num1, num2, num1 + num2)
    #return "{} mas {} es igua a {}".format(num1, num2, num1 + num2)



if __name__ == "__main__":
    app.run(debug=True)








