import json
class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.amigos = []
    
    def __str__(self):
        return f'Soy {self.nombre}, identificado con {self.id}. Tengo {self.edad} anios.'
    
    def getId(self) -> int:
        return self.id
    
    def getNombre(self) -> str:
        return self.nombre
    
    def getEdad(self) -> int:
        return self.edad
    
    def getAmigos(self) -> list:
        return self.amigos

class Mensaje:
    def __init__(self, envia, recibe, msg, time):
        self.envia = envia #Instancia de la clase persona
        self.recibe = recibe #Instancia de la clase persona
        self.msg = msg #STR
        self.time = time #Int

    def __str__(self):
        return f'Enviado por {self.envia} a {self.recibe} a las {self.time}: "{self.msg}."'
    
    def getEnvia(self) -> Persona:
        return self.envia
    
    def getRecibe(self) -> Persona:
        return self.recibe
    
    def getMsg(self) -> str:
        return self.msg
    
    def getTime(self) -> int:
        return self.time
    
class HistorialMensajes:
    def __init__(self):
        self.historial = {}
        with open("historialMsg.json", "w"):
            pass

    def nuevoMsg(self, msg):
        codigo = ""
        if msg.getEnvia().getId() < msg.getRecibe().getId():
            codigo = str(msg.getEnvia().getId())+str(msg.getRecibe().getId())
        else:
            codigo = str(msg.getRecibe().getId())+str(msg.getEnvia().getId())
        # codigo = int(codigo)
        if codigo not in self.historial:
            self.historial[codigo] = []
        nombreEnvia = msg.getEnvia().getNombre()
        nombreRecibe = msg.getRecibe().getNombre()
        mensaje = msg.getMsg()
        hora = msg.getTime()
        self.historial[codigo].append({
                                        "envia": nombreEnvia,
                                        "recibe": nombreRecibe,
                                        "msg": mensaje,
                                        "hora": hora 
                                    })
        with open("historialMsg.json", "w") as historial:
            mensajes = []
            for key in self.historial:
                mensajes.append(self.historial[key])
            json.dump(mensajes, historial, indent=2)

if __name__ == "__main__":
    historial = HistorialMensajes()
    a = Persona(1, "Santiago", 18)
    b = Persona(2, "Johan", 17)
    c = Persona(3, "Emanuel", 33)
    m1 = Mensaje(a, b, "AAAAA", 2205)
    m2 = Mensaje(a, c, "CCCCC", 1205)
    m3 = Mensaje(a, b, "AKSLA", 2230)
    m4 = Mensaje(b, a, "AKSLDK", 2350)
    m5 = Mensaje(b, c, "YOYOOYOY", 2000)
    historial.nuevoMsg(m1)
    historial.nuevoMsg(m2)
    historial.nuevoMsg(m3)
    historial.nuevoMsg(m4)
    historial.nuevoMsg(m5)