from Cola import cola
class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.amigos = []
    
    def __str__(self):
        return f'Soy {self.nombre}, identificado con {self.id}. Tengo {self.edad} años.'
    
    def getId(self) -> int:
        return self.id
    
    def getNombre(self) -> str:
        return self.nombre
    
    def getEdad(self) -> int:
        return self.edad
    
    def getAmigos(self) -> list:
        return self.amigos