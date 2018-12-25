import datetime

help(datetime)   # info sobre la librería

print("\n# ---------- FECHA Y HORA -------------------------------\n")

print("\n# ---------- DATETIME -------------------------------\n")
print(datetime.datetime.now())    # se le puede pasar una zona horaria
print(datetime.datetime.today())  # no se le puede pasar una zona horaria

now = datetime.datetime.now()  # timestamp

print(now.day)
print(now.minute)
print(now.second)
print(now.year)
print(now.month)

print(now)
print(now.replace(minute=0,second=0))
print(now)

print("\n# ---------- TIME -------------------------------\n")

tiempo_transcurrido = datetime.datetime.now() - now
print(tiempo_transcurrido)  #devuelve 0:00:00.000024  dia:segundos:microsegundos

print(tiempo_transcurrido.days)                  # dias
print(tiempo_transcurrido.seconds)               # segundos
print(round(tiempo_transcurrido.seconds / 60))   # minutos

print("\n# ---------- DELTATIME -------------------------------\n")
now + datetime.timedelta(days=5)    #suma 5 dias a la fecha actual
print(now)

now + datetime.timedelta(days=5,minutes=30)    #suma 5 dias a la fecha actual y 30 min
print(now)

print("\n# ---------- FORMATEO DE FECHAS -------------------------------\n")

# http://strftime.org/
print(now.strftime("%B %d, %Y"))        # formatear fecha


fecha_formato = datetime.datetime.strptime("12/12/2018", "%d/%m/%Y")  # pasar cadena texto a fecha
print(fecha_formato)

print("\n# ---------- ZONAS HORARIAS -------------------------------\n")

central_time = datetime.timezone(datetime.timedelta(hours=-1))
print(central_time)

now = datetime.datetime.now(central_time)
print(now)
