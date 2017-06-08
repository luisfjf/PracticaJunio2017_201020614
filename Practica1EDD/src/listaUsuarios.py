# Para la elaboracion de esta lista se tomo de referencia el contenido del siguiente video
# https://www.youtube.com/watch?v=c27dIMT9kLE

from nodoUsuario import NodoUsuario

class ListaUsuarios:
    #Metodo constructor
    def __init__(self):
        self.primero = None
        self.ultimo = None
    #Metodo para verificar si la lista esta vacia   
    def esta_vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    #Metodo para agregar un nodo al inicio de la lista   
    def agregar_al_inicio(self,nombre,pwd):
        if self.esta_vacia():
            self.primero = self.ultimo = NodoUsuario(nombre,pwd)
        else:
            aux = NodoUsuario(nombre,pwd)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
    #Metodo para recorrer   
    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.nombre)
            aux = aux.siguiente
            if aux == self.primero:
                break
                
    #Metodo para buscar  
    def buscar(self,nombre):
        aux = self.primero
        while aux:
            if aux.nombre == nombre:
                return True
            aux = aux.siguiente
            if aux == self.primero:
                break                
        
    #Metodo para validar credenciales
    def validar_credenciales(self,nombre,pwd):
        aux = self.primero
        while aux:
            if aux.nombre == nombre:
                if aux.pwd == pwd:
                    return True
                else:
                    return False
            aux = aux.siguiente
            if aux == self.primero:
                break      