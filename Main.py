from Persona import Persona
from Mensaje import Mensaje
from Datos import datos
from HistorialMensajes import HistorialMensajes as Historial
from Cola import cola
import random


def generar_usuarios(total):
    dato = datos()
    return [Persona(random.randint(1000, 2000), random.choice(dato.nombres)+' '+random.choice(dato.apellidos), random.randint(18, 70)) for i in range(total)]
def generar_mensajes(us1, us2):
    users = [us1, us2]
    mensajes = []
    lista = []
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
        frecuencia += time-lastTime 
        historial.nuevoMsg(mensajes[i])
        if time+60 >= 1440:
            break
    frecuencia/=cantidad
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
                mensajes, frecuencia = generar_mensajes(usuario, amigo)

                amistades.insert([(usuario, amigo), mensajes, int(frecuencia)])
    historial.agrega_json()

    for j in usuarios:
        usuarios_amigos.insert([j, j.amigos])
if __name__ == '__main__':
    historial = Historial()
    amistades = cola()
    #amistades es la cantidad de mensajes entre dos amigos y su frecuencia 
    usuarios_amigos = cola()
    #usuarios_amigos es la cantidad de amigos de cada usuario
    print("Digite la cantidad de usuarios para la simulación:")
    total = int(input())
    generar_amistades(total)

    informe = []
    informe.append('LOS USUARIOS CON MÁS AMIGOS SON: \n\n')

    for i in range(3):
        u = usuarios_amigos.eliminar()
        informe.append(f'{u[0].nombre} con {len(u[1])} amigos')
        informe.append(f'\nSus amigos son:\n')

        for j in u[0].amigos:
            informe.append(f'{j.nombre} \n')
        informe.append('\n\n')
    informe.append('LOS MEJORES AMIGOS SON: \n\n')
    for i in range(10):
        u = amistades.eliminar()
        informe.append(f'{u[0][0].nombre} y {u[0][1].nombre} con una cantidad de {len(u[1])} mensajes y {u[2]} mensajes por minuto \n\n')

    with open("Informe.txt", 'w', encoding='utf_8') as analisis:
        for a in informe:
            analisis.write(a)


