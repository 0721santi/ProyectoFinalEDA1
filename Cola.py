from Nodo import nodo
class cola:

  def __init__(self):
    self.primero = None
    self.ultimo = None
    self.size = 0

  def insert(self, dato):
    #Se asigna un método insert para una cola de prioridad
    n = nodo(dato)
    if self.size == 0:
      self.primero = self.ultimo = n
    else:
      aux = self.primero
      v = False
      #Se inserta prioritariamente si el estado del paciente es menor
      if (len(self.primero.dato[1]) < len(dato[1])) or (len(self.primero.dato[1])==len(dato[1]) and len(dato)>2 and dato[2]<self.primero.dato[2]):
        n.siguiente = self.primero
        self.primero = n
        v = True
      while aux.siguiente and not v:
        if (len(aux.siguiente.dato[1]) < len(dato[1])) or (len(aux.siguiente.dato[1])==len(dato[1]) and len(dato)>2 and dato[2]<aux.siguiente.dato[2]):
          n.siguiente = aux.siguiente
          aux.siguiente = n
          v = True
          break
        aux = aux.siguiente
      if not v:
        self.ultimo.siguiente = n
        self.ultimo = n
    self.size += 1

  def eliminar(self):
    if self.size == 0:
      return False
    else:
      x = self.primero.dato
      self.primero = self.primero.siguiente
      self.size -= 1
    return x

  def imprimir(self):
    aux = self.primero
    while aux.siguiente != None:
      print(f'{aux.dato[0]}-{len(aux.dato[1])}')
      print()
      aux = aux.siguiente
    print(f'{aux.dato[0]}-{len(aux.dato[1])}', end='-')