
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
import sys, os

lista = ListaUsuarios()
# Main definition - constants
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
    print "\n0. Quit"
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
        print "Las credenciales no coinciden\n"
        ejecutar_menu('9')
        return    
    
    ejecutar_menu('4')
    
    return

# Menu usuarios
def menu_usuario():
    
    print "1. Leer archivo"
    print "2. Resolver operaciones"
    print "3. Operar la matriz"
    print "4. Mostrar Cola"
    print "5. Cerrar Sesion"
    
    opcion = raw_input(" >>  ")
    if opcion == '1':
        opcion = '21'
    if opcion == '5':
        opcion = '9'
    ejecutar_menu(opcion)
 
    return

# Leer archivo XML
# Para esta funcion se tomo de referencia este sitio
# http://www.lawebdelprogramador.com/codigo/Python/3073-Como-leer-un-valor-y-un-atributo-de-un-XML.html
def leer_archivo():
    """
    # La mas sencilla e intuitiva
matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(None)"""
    
    mixml="""<archivo>
        <matriz>
            <x>2</x>
            <y>3</y>
        </matriz>
        <operaciones>
            <operacion>
                2 8+4*7-
            </operacion>
            <operacion>
                2 6 +
            </operacion>
            <operacion>
                2 6 -
            </operacion>              
        </operaciones>
    </archivo>"""    
    xmldoc = minidom.parseString(mixml)
    itemlist = xmldoc.getElementsByTagName("matriz")
    for i in itemlist:
        
        print (i.firstChild.nodeValue)  
    
    itemlist = xmldoc.getElementsByTagName("operacion")
    for i in itemlist:
        print (i.firstChild.nodeValue)      
        
    return
    
# Ver los usuarios registros
def ver_usuarios():
    lista.recorrer()
    ejecutar_menu('9')
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
    '0': salir,
}

# =======================
#      PROGRAMA PRINCIPAL
# =======================

if __name__ == "__main__":
    # Launch main menu
    menu_principal()