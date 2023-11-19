import json
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
    def agrega_json(self):
            with open("historialMsg.json", "w", encoding="UTF-8") as historial:
                mensajes = []
                for key in self.historial:
                    mensajes.append(self.historial[key])
                json.dump(mensajes, historial, indent=2, ensure_ascii=False)
