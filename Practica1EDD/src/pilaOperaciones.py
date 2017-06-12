# Para la elaboracion de esta lista se tomo de referencia la siguiente pagina
# http://librosweb.es/libro/algoritmos_python/capitulo_17/pilas.html

from nodoPila import NodoPila

class PilaOperaciones:
    #Metodo constructor
    def __init__(self):
        self.tope = None
    #Metodo para verificar si la pila esta vacia   
    def esta_vacia(self):
        return self.tope==None
    #Metodo para apilar
    def apilar(self,operacion):
        nodoNuevo = NodoPila(operacion,self.tope)
        self.tope = nodoNuevo

    #Metodo para desapilar
    def desapilar(self):
        if self.esta_vacia():
            print 'La pila se encuentra vacia'
        else:
            Nodo = self.tope
            self.tope = self.tope.siguiente
            return Nodo.operacion
                
    def mostrar_pila(self):
        if self.esta_vacia():
            print 'La pila se encuentra vacia'
        else:
            aux = self.tope
            indice = 0
            while aux:
                print aux.operacion
                indice = indice + 1
                aux = aux.siguiente                
                