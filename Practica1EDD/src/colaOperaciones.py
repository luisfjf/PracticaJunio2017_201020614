# Para la elaboracion de esta lista se tomo de referencia el contenido del siguiente video
# https://www.youtube.com/watch?v=c27dIMT9kLE

from nodoCola import NodoCola

class ColaOperaciones:
    #Metodo constructor
    def __init__(self):
        self.primero = None
    #Metodo para verificar si la cola esta vacia   
    def esta_vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    #Metodo para encolar 
    def encolar(self,operacion):
        nodoNuevo = NodoCola(operacion)
        if self.esta_vacia():
            self.primero = nodoNuevo
        else:
            aux = self.primero
            while aux:                              
                if aux.siguiente == None:                    
                    aux.siguiente = nodoNuevo
                    break
                
                aux = aux.siguiente                    

    #Metodo para desencolar
    def desencolar(self):
        if self.esta_vacia():
            print 'La cola se encuentra vacia'
        else:
            nodoAux = self.primero
            if self.primero.siguiente == None:
                self.primero = None
            else:
                self.primero = self.primero.siguiente
            return nodoAux
                
    def mostrar_cola(self):
        if self.esta_vacia():
            print 'La cola se encuentra vacia'
        else:
            aux = self.primero
            indice = 0
            while aux:
                print "indice ", indice, ": ", aux.operacion
                indice = indice + 1
                aux = aux.siguiente
                