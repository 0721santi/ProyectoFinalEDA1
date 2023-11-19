from Persona import Persona
from Mensaje import Mensaje
from Datos import datos
from Cola import cola
from HistorialMensajes import HistorialMensajes as Historial
import copy
import random
def generar_usuarios(total):
    dato = datos()
    return [Persona(random.randint(1000, 2000), random.choice(dato.nombres)+' '+random.choice(dato.apellidos), random.randint(18, 70)) for i in range(total)]

def calcula_frecuencia(msgs, lastTime, time, frecuencia):
    sum = frecuencia*msgs
    tiempo = time-lastTime
    sum += tiempo
    frecuencia = sum/(msgs+1)
    return frecuencia

def generar_mensajes(us1, us2):
    users = [us1, us2]
    mensajes = []
    cantidad = random.randint(1, 100)
    frecuencia = 0
    time = 0
    for i in range(cantidad):
        envia = random.choice(users)
        if envia==us1:
            recibe = us2
        else:
            recibe = us1            
        lastTime = time
        time = random.randint(time, time+60)
        mensajes.append(Mensaje(envia, recibe, time))
        frecuencia = calcula_frecuencia(i, lastTime, time, frecuencia)
        if time+60 >= 1440:
            break
        historial.nuevoMsg(mensajes[i])
    return mensajes, frecuencia

def generar_amistades(total):
    global amistades, usuarios_amigos
    usuarios = generar_usuarios(total)
    for usuario in usuarios:
        cantidad_amigos = random.randint(1, total)
        for i in range(cantidad_amigos):
            amigo = random.choice(usuarios)
            if amigo not in usuario.amigos and amigo!=usuario:
                usuario.amigos.append(amigo)
                amigo.amigos.append(usuario)
                mensajes = generar_mensajes(usuario, amigo)
                amistades.insert([(usuario, amigo), mensajes, random.randint(1, 12)])
        usuarios_amigos.insert([usuario, usuario.amigos])

if __name__ == "__main__":
    amistades = cola()
    usuarios_amigos = cola()
    historial = Historial()
    generar_amistades(20)

    for i in range(usuarios_amigos.size):
        u = usuarios_amigos.eliminar()
        print(u[0].nombre)
        print(len(u[1]))
        print()