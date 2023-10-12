﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import threading
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from tabulate import tabulate
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*1000000)
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar datos")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Representación de los datos")
    print("0- Salir")


def load_data(control,filegoalscorers, fileresults, fileshootouts):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    goal_scores, results, shootouts = controller.load_data(control, filegoalscorers,fileresults,fileshootouts)
    return goal_scores, results, shootouts


def print_data(control,id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,nom,condicion, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    res,lista, tamano,respuestas= controller.req_1(control, nom, condicion, num)
    print("El total de resultados encontrados es: "+ str(tamano))
    print("Para los "+str(num)+" seleccionados")
    print(res)
    print(lista)
    delta_time = f"{respuestas:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control,nombre, num):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    res,lista, tamano,respuestas= controller.req_2(control, nombre, num)
    print("El total de resultados encontrados es: "+ str(tamano))
    print("Para los "+str(num)+" seleccionados")
    print(res)
    print(lista)
    delta_time = f"{respuestas:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,nomb,f_i,f_f):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    res,lista,tamano,home,visitante,respuestas=controller.req_3(control,nomb,f_i,f_f)
    print("El total de partidos de "+str(nomb)+" es de: "+ str(tamano))
    print("El total de partidos de "+str(nomb)+" como local es de: "+ str(home))
    print("El total de partidos de "+str(nomb)+" como visitante es de: "+ str(visitante))
    print(res)
    print(lista)
    delta_time = f"{respuestas:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, nombreTorneo, fechaIni, fechaFin):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    x=controller.req_4(control, nombreTorneo, fechaIni, fechaFin)
    print("El total de partidos de "+str(nombreTorneo)+" es de: "+str(x[1]))
    print("El total de paises de "+str(nombreTorneo)+" es de: "+str(x[2]))
    print("El total de ciudades de "+str(nombreTorneo)+" es de: "+str(x[3]))
    print("El total de penales de "+str(nombreTorneo)+" es de: "+str(x[4]))
    delta_time = f"{x[5]:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")
    i=1
    while i<4:
        print(lt.getElement(x[0],i ), '\n')
        
        i+=1
    j=lt.size(x[0])-2
    while j<lt.size(x[0])+1:
        print(lt.getElement(x[0], j),'\n')
        j+=1
    
    #print('Encontrando ultimo el partido numero: '+ str(x[1]-z) + ' es: ', lt.getElement(x[0], x[1]-z))
    

def print_req_5(control, nombre_jugador, fecha_inicio, fecha_final):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    respuesta,resultado,goles,torneo,penaltis,autogoles,respuestas = controller.req_5(control,nombre_jugador, fecha_inicio, fecha_final)
    print("Cantidad total de goles hechos por " + nombre_jugador + " "+ str(goles))
    print("Cantidad total de torneos jugados por " + nombre_jugador + " " + str(torneo))
    print("Cantidad total de goles marcados por penalti de " + nombre_jugador +" " + str(penaltis))
    print("Cantidad total de autogoles marcados por " + nombre_jugador + " " +   str(autogoles))
    
    print(respuesta)
    print(resultado)
    delta_time = f"{respuestas:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")

def print_req_6(control,torneo,f_i,f_f,top):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    res,sublista,equipos,partidos,paises,ciudades,moda,respuestas=controller.req_6(control,torneo,f_i,f_f,top)
    print("El total de equipos involucrados en el torneo es de: "+ str(equipos) )
    print("El total de partidos disputas en el torneo es de "+str(partidos))
    print("El total de paises involucrados en el torneo es de "+str(paises))
    print("El total de ciudades involucradas en el torneo es de : "+str(ciudades))
    print("La ciudad donde más partidos se disputaron es en: "+str (moda))
    print(res)
    print(sublista)
    delta_time = f"{respuestas:.3f}"
    print( "tiempo:", str(delta_time), "[ms]")
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control,fechaIni,fechaFin,top):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    res, resultado, anotadores,partidos,torneos,goles,penales, auto,= controller.req_7(control, fechaIni, fechaFin,top)
    
    print('La fecha inicial es', fechaIni)
    print('La fecha final es ', fechaFin)
    
    print('Total de jugadores:', anotadores)
    print('Total de partidos:', partidos)
    print('Total de torneos:', torneos)
    print('Total de goles:', goles)
    print('Total de penales', penales)
    print('Total de autogoles', auto)
    print(res)
    print(resultado)

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def funcion_seleccionadora ():
    inputs= int(input("ingrese 1 si quiere que la estructura de datos sea un ARRAY_LIST o 2 si desea que la estructura de datos sea un SINGLE_LIST "))
    formato ="SINGLE_LINKED"
    if inputs == 1:
        formato= "ARRAY_LIST"
    return formato
def ordenamiento():
    print("1 = insertion")
    print("2 = shell")
    print("3 = selection")
    inputs= int(input("Ingrese el tipo de ordenamiento iterativo: "))
    return inputs



# Se crea el controlador asociado a la vista
control = new_controller()
default_limit = 1000

# main del reto
def menu_cycle():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            final = input ("Escribe el su-fijo del archivo goalscorer (ej: 5pct)")
            fin = input ("Escribe el su-fijo del archivo results (ej: 5pct)")
            fi = input ("Escribe el su-fijo del archivo shootouts (ej: 5pct)")
            filename1 = str("goalscorers-utf8-" + final +".csv")
            filename2 = str("results-utf8-" + fin +".csv")
            filename3 = str("shootouts-utf8-" + fi +".csv")
            
            print("Cargando información de los archivos ....\n")
            
            v1, v2, v3 = load_data(control, filename1, filename2, filename3)
            print("Match results count: "+ str(v2))
            print("Goal scorers count: "+ str(v1))
            print("Shootout-penalty definition count: "+ str(v3))
            
            f1,f2,f3 = controller.get_data(control)
            print("Goal scorers count: "+ str(v1))
            print(f1)
            print("Match results count: "+ str(v2))
            print (f2)
            print("Shootout-penalty definition count: "+ str(v3))
            print(f3)
            
        elif int(inputs) == 2:
            num, nombre, condicion = "desconocido","desconocido","desconocido"
            nombre= input("Ingrese el nombre del equipo: \n ")
            num=int(input("Ingrese la cantidad de ultimos partidos que quiere consultar: \n "))
            condicion= input("Ingrese la condición del equipo en los partidos consultados (Local, Visitante, o Indiferente):\n  ")
            print_req_1(control,nombre,condicion,num)

        elif int(inputs) == 3:
            num, nombre = "desconocido","desconocido"
            nombre=input("Ingrese el nombre del jugador que desea consultar: \n ")
            num=int(input("Ingrese la cantidad de goles que desea consultar: \n "))
            print_req_2(control,nombre,num)
            

        elif int(inputs) == 4:
            nomb,f_i,f_f="desconocido","desconocido","desconocido"
            nomb=input("Ingrese el nombre del equipo: \n ")
            f_i=input("Ingrese la fecha de inicio del rango :\n ")
            f_f=input("Ingrese la fecha final del rango : \n ")
            print_req_3(control,nomb,f_i,f_f)

        elif int(inputs) == 5:
            nombreTorneo = input('Digite el nombre del torneo que desea consultar: \n')
            fechaIni = input ('Digite una fecha inicial del periodo a consultar: \n')
            fechaFin = input('Digite una fecha final del periodo a consultar: \n')
            print_req_4(control, nombreTorneo, fechaIni, fechaFin)
            
 

        elif int(inputs) == 6:
            nombre= input ("ingrese el nombre del deportista:\n ")
            f_i=input("Ingrese la fecha de inicio del rango :\n ")
            f_f=input("Ingrese la fecha final del rango : \n ")
            print_req_5(control,nombre,f_i,f_f)

        elif int(inputs) == 7:
            torneo = input('Digite el nombre del torneo que desea consultar: \n')
            f_i = input ('Digite una fecha inicial del periodo a consultar: \n')
            f_f = input('Digite una fecha final del periodo a consultar: \n')
            top= int(input("Ingrese número del Top de equipos que desea consultar: \n"))
            print_req_6(control, torneo, f_i, f_f,top)

        elif int(inputs) == 8:
            numDeJugadores = int(input('Ingrese el numero de jugadores'))
            fechaIni = input('Digite una fecha inicial a consultar')
            fechaFin = input('Digite una fecha final a consultar')
            print_req_7(control,fechaIni,fechaFin,numDeJugadores)

        elif int(inputs) == 9:
            print_req_8(control)
        elif int(inputs)==10:
            funcion_seleccion=funcion_seleccionadora()
            numero= int(input("ingrese franja de datos: "))
            lista = controller.sublista(control, numero)
            if lista ==1:
                print("La cantidad se sale del rango")
            else: 
                orden = ordenamiento()
                results= controller.sort(lista, orden)
                result = f"{results:.3f}"
                print("Para", numero , "elementos, delta tiempo:", str(result), "[ms]\n")
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
if __name__ == "__main__":
    # TODO modificar main para reserar memoria (parte 2)
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()