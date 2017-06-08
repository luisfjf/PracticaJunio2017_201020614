class NodoUsuario:
    
    def __init__(self,nombre,pwd):
        self.nombre = nombre
        self.pwd = pwd
        self.siguiente = None
        self.anterior = None