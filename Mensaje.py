from Persona import Persona
from Datos import datos
import random
class Mensaje:
    def __init__(self, envia, recibe, time):
        
        self.envia = envia #Instancia de la clase persona
        self.recibe = recibe #Instancia de la clase persona
        self.msg = random.choice(datos().mensajes) #STR
        self.time = self.getTime(time)

    def __str__(self):
        return f'Enviado por {self.envia} a {self.recibe} a las {self.time}: "{self.msg}."'
    def getEnvia(self) -> Persona:
        return self.envia
    
    def getRecibe(self) -> Persona:
        return self.recibe
    
    def getMsg(self) -> str:
        return self.msg
    
    def getTime(self, minuto) -> str:
        if minuto <60:
            return f'00:{minuto}'
        else:
            hora = minuto // 60
            minutos = minuto % 60
            if minutos <10:
                minutos = f'0{minutos}'
            return f'{hora}:{minutos}'