
#Aplicacion desarrollada por Luis Jimenez (LJIM)
#Para realizar el menu se tomo de referencia la siguiente web
"""
Referencias

Bggofurther.com. (2017). Create an interactive command-line menu using Python | BG Go Further. [online] Available at: https://www.bggofurther.com/2015/01/create-an-interactive-command-line-menu-using-python/ [Accessed 8 Jun. 2017].
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# practica1edd.py


from xml.dom import minidom
from listaUsuarios import ListaUsuarios
from nodoUsuario import NodoUsuario
from colaOperaciones import ColaOperaciones
from pilaOperaciones import PilaOperaciones
import sys
import os

lista = ListaUsuarios()
cola = ColaOperaciones()
pila = PilaOperaciones()
matriz = []
matrizTranspuesta = []
filas = 0
columnas = 0

menu_acciones  = {}

# Menu Principal
def menu_principal():
    #Dependiendo del S.O. se determina la variable LIMPIAR
    global LIMPIAR 
    LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"

    os.system(LIMPIAR)
    
    print "PRACTICA 1 EDD\n"
    print "Escoga una opcion:"
    print "1. Crear usuario"
    print "2. Ingresar al sistema"
    print "3. Mostrar Usuarios"
    print "\n0. Salir"
    opcion = raw_input(" >>  ")
    ejecutar_menu(opcion)
 
    return

# Ejecuta menu
def ejecutar_menu(opcion):
    os.system(LIMPIAR)
    ch = opcion.lower()
    if ch == '':
        menu_acciones['menu_principal']()
    else:
        try:
            menu_acciones[ch]()
        except KeyError:
            print "Seleccion invalida, por favor intente de nuevo.\n"
            menu_acciones['menu_principal']()
    return

# Crear usuario
def crear_usuario():
    print "Ingrese nombre\n"
    nombre = raw_input(" >>  ")
    
    if lista.buscar(nombre):
        print "El usuario ya existe\n"
        ejecutar_menu('9')
        return    
    
    print "Ingrese password\n"
    pwd = raw_input(" >>  ")
        
    lista.agregar_al_inicio(nombre,pwd)
    ejecutar_menu('9')
    return

# Ingresar al sistema
def ingresar_sistema():
    print "Ingrese nombre\n"
    nombre = raw_input(" >>  ")
    
    print "Ingrese password\n"
    pwd = raw_input(" >>  ")
    
    if lista.validar_credenciales(nombre,pwd) == False:
        print "Las credenciales y/o el usuario no coinciden\n"
        ejecutar_menu('9')
        return    
    #Usuario que ingresa al sistema
    global usuarioActivo 
    usuarioActivo = lista.obtener_usuario(nombre)
    ejecutar_menu('4')
    
    return

# Menu usuarios
def menu_usuario():
    print "BIENVENIDO ", usuarioActivo.nombre
    print ""
    print "1. Leer archivo"
    print "2. Resolver operaciones"
    print "3. Operar la matriz"
    print "4. Mostrar Cola"
    print "5. Cerrar Sesion"
    
    opcion = raw_input(" >>  ")
    if opcion == '1': #1. Leer archivo
        opcion = '21'
    if opcion == '2': #2. Resolver operaciones
        #para resolver operaciones deben existir datos en la cola
        if usuarioActivo.cola.esta_vacia():
            print 'No existen operaciones para este usuario'
            opcion = '4'
        else:
            opcion = '22'
    if opcion== '3':
        #para resolver operaciones deben existir datos en la cola
        if usuarioActivo.cola.esta_vacia():
            print 'No existen operaciones para este usuario'
            opcion = '4'
        else:
            opcion = '23'        
    if opcion == '4': #4. Mostrar Cola
        opcion = '24'        
    if opcion == '5': #5. Cerrar Sesion
        opcion = '9'
    print ""
    ejecutar_menu(opcion)
 
    return

# Menu operaciones
def menu_operaciones():
    print ""
    print "1. Operar Siguiente "
    print "2. Regresar"
    
    opcion = raw_input(" >>  ")
    if opcion == '1':
        if usuarioActivo.cola.esta_vacia():
            print 'No existen operaciones para este usuario'
            opcion = '4'
        else:        
            pila = PilaOperaciones()
            #sacamos un nodo cola
            nodoCola = usuarioActivo.cola.desencolar()
            operacion = nodoCola.operacion
            operaciones = operacion.split()

            for ope in operaciones:
                pila.apilar(ope)
                if ope == '+' or ope == '-'  or ope == '*':
                    operador = pila.desapilar()
                    operando2 = pila.desapilar()
                    operando1 = pila.desapilar()
                    #global resultado
                    resultado = 0

                    ope2 = int(operando2)
                    ope1 = int(operando1)
                    if operador == '+':
                        resultado = ope1 + ope2
                        print "Operacion: ", operando1, " + ", operando2, " = ", resultado
                    if operador == '-':
                        resultado = ope1 - ope2
                        print "Operacion: ", operando1, " - ", operando2, " = ", resultado
                    if operador == '*':
                        resultado = ope1 * ope2
                        print "Operacion: ", operando1, " * ", operando2, " = ", resultado
                    pila.apilar(resultado)

            #print "Valor en pila: ",pila.mostrar_pila()    
            opcion = '22'
    if opcion == '2':
        opcion = '4'
    ejecutar_menu(opcion)
    return


# Menu para operaciones de matrices
def menu_matriz():
    print ""
    print "1. Ingresar dato"
    print "2. Operar transpuesta"
    print "3. Mostrar matriz original"
    print "4. Mostrar matriz transpuesta"
    print "5. Regresar"

    opcion = raw_input(" >>  ")
    print ""
    if opcion == '1': #1. Ingresar dato
        print 'Ingrese coordenada en X: '
        posX = raw_input(" >>  ")
        
        if posX > filas:
            print 'La posicion maxima en X es: ', filas
            opcion = '23'
            ejecutar_menu(opcion)
            return              
    
        print 'Ingrese coordenada en Y: '        
        posY = raw_input(" >>  ")
        
        if posY > columnas:
            print 'La posicion maxima en Y es: ', columnas
            opcion = '23'
            ejecutar_menu(opcion)
            return
        
        print 'Ingrese valor: '        
        valor = raw_input(" >>  ")
        
        #matriz[int(posX)][int(posY)] = valor
        usuarioActivo.asignar_valor_matriz(posX,posY,valor)
        
        opcion = '23'
        ejecutar_menu(opcion)
        return
    
    if opcion == '2': #2. Operar transpuesta
        usuarioActivo.operar_matriz_transpuesta()
        ejecutar_menu('23')
        return
    
    if opcion == '3': #3. Mostrar matriz original 
        mostrar_matriz_original()
        return
    
    if opcion == '4': #4. Mostrar matriz transpuesta
        mostrar_matriz_transpuesta()
        return    
    
    if opcion == '5': 
        opcion = '4'
    ejecutar_menu(opcion)
    return    
    
def read_file(filename):
    filehandle = open(filename)
    archivo = filehandle.read()
    filehandle.close()
    return archivo

def mostrar_matriz_original():
    #Se tomo la referencia del siguiente enlance
    # https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python

    usuarioActivo.mostrar_matriz_original()
    #for i in xrange(int(filas)):
    #    for j in xrange(int(columnas)):
    #        print '{:4}'.format(matriz[i][j]),
    #    print
    
    ejecutar_menu('23')
    return

def mostrar_matriz_transpuesta():
    #Se tomo la referencia del siguiente enlance
    # https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
    usuarioActivo.mostrar_matriz_transpuesta()
    
    ejecutar_menu('23')
    return

# Leer archivo XML
# Para esta funcion se tomo de referencia este sitio
# http://www.lawebdelprogramador.com/codigo/Python/3073-Como-leer-un-valor-y-un-atributo-de-un-XML.html
def leer_archivo():
    print 'Escriba el nombre del archivo de prueba'
    nombre = raw_input(" >>  ")
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    
    filename = os.path.join(fileDir, nombre)
    filename.replace('\\','/')
    
    mixml = read_file(filename)
    
    global matriz
    global matrizTranspuesta
    global filas
    global columnas
    matriz = []
    matrizTranspuesta = []
    cola = ColaOperaciones()
    filas = 0
    columnas = 0
    
    #Si el usuario ya existe se obtiene su cola
    if usuarioActivo.filas == 0:
        cola = ColaOperaciones()
    else:
        cola = usuarioActivo.obtener_cola()
        
    xmldoc = minidom.parseString(mixml)

    itemlist = xmldoc.getElementsByTagName("x")
    for i in itemlist:
        filas = i.firstChild.nodeValue
        
    itemlist = xmldoc.getElementsByTagName("y")
    for i in itemlist:
        columnas = i.firstChild.nodeValue        
   
    # Para Matriz
    for i in range(int(filas)):
        matriz.append([])
        for j in range(int(columnas)):
            matriz[i].append(None)
            
    for i in xrange(int(filas)):
        for j in xrange(int(columnas)):
            matriz[i][j] = 0            
            
    # Para Matriz transpuesta
    for i in range(int(columnas)):
        matrizTranspuesta.append([])
        for j in range(int(filas)):
            matrizTranspuesta[i].append(None)
            
    for i in xrange(int(columnas)):
        for j in xrange(int(filas)):
            matrizTranspuesta[i][j] = 0            

    itemlist = xmldoc.getElementsByTagName("operacion")
    for i in itemlist:
        cola.encolar(i.firstChild.nodeValue)
    #Asignar operaciones al usuario activo        
    usuarioActivo.asignar_cola(cola)
    
    #Si ya existe una matriz, no se sustituye
    if usuarioActivo.filas == 0:
        usuarioActivo.asignar_matriz(matriz)
        usuarioActivo.asignar_matriz_transpuesta(matrizTranspuesta)
        usuarioActivo.asignar_fila_columna(filas,columnas)
    else:
        print 'Ya existe una matriz previamente cargada'
    
    print 'El archivo fue leido con exito\n'    
    ejecutar_menu('4')
    

    return
    
# Ver los usuarios registros
def ver_usuarios():
    lista.recorrer()
    lista.recorrer_atras()
    ejecutar_menu('9')
    return    

# Ver las operaciones pendientes en la cola del usuario
def ver_cola():
    usuarioActivo.cola.mostrar_cola()
    ejecutar_menu('4')
    return

# Regresar al menu principal
def regresar():
    menu_acciones['menu_principal']()

# Salir del programa
def salir():
    sys.exit()

# =======================
#    DEFINICIONES DE MENU
# =======================
menu_acciones = {
    'menu_principal': menu_principal,
    '1': crear_usuario,
    '2': ingresar_sistema,
    '3': ver_usuarios,
    '4': menu_usuario,
    '9': regresar,
    '21': leer_archivo,
    '22': menu_operaciones,
    '23': menu_matriz,
    '24': ver_cola,
    '0': salir,
}

# =======================
#      PROGRAMA PRINCIPAL
# =======================

if __name__ == "__main__":
    # Launch main menu
    menu_principal()