from colaOperaciones import ColaOperaciones

global matriz
global matrizTranspuesta
matriz = []
matrizTranspuesta = []

class NodoUsuario:
    
    def __init__(self,nombre,pwd):
        self.nombre = nombre
        self.pwd = pwd
        self.cola = ColaOperaciones()
        self.matriz = matriz
        self.matrizTranspuesta = matrizTranspuesta
        self.filas = 0
        self.columnas = 0
        self.siguiente = None
        self.anterior = None
        
    def asignar_cola(self,cola):
        self.cola = cola
        
    def obtener_cola(self):
        return self.cola
        
    def asignar_fila_columna(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        
    def asignar_matriz(self,matriz):
        self.matriz = matriz
        
    def asignar_matriz_transpuesta(self,matrizTranspuesta):
        self.matrizTranspuesta = matrizTranspuesta             
        
    def asignar_valor_matriz(self,posX,posY,valor):
        self.matriz[int(posX)][int(posY)] = valor
        return
    
    def operar_matriz_transpuesta(self):
        for i in xrange(int(self.filas)):
                for j in xrange(int(self.columnas)):
                        self.matrizTranspuesta[j][i] = self.matriz[i][j]
        print 'Se realizo la transpuesta de la matriz\n'
        
    def mostrar_matriz_original(self):
        for i in xrange(int(self.filas)):
            for j in xrange(int(self.columnas)):
                print '{:4}'.format(self.matriz[i][j]),
            print        
            
    def mostrar_matriz_transpuesta(self):
        
        for i in xrange(int(self.columnas)):
            for j in xrange(int(self.filas)):
                print '{:4}'.format(self.matrizTranspuesta[i][j]),
            print        
              