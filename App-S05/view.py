"""
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
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import threading

import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    
    control=controller.new_controller()
    #TODO: Realizar la carga de datos
    return control 
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    
default_limit = 1000
def menu_cycle():

    """
    Menu principal
    """
    working = True
    # configurando si usa algoritmos recursivos
    rec = True

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- seleccionar el tipo de algoritmo de ordenamiento iterativo")
    print("0- Salir")
    
def print_results_tabla(lista,req7):
    largo=lt.size(lista)
    if largo<6:
        keys=lt.getElement(lista,0).keys()
        listaprint={}
        for n in keys:
            i=1
            listacorta=[]
            while i<=largo:
                listas=lt.getElement(lista,i)
                listacorta.append(listas[n])
                i+=1
            listaprint[n]=listacorta
    else: 
        pritres=lt.subList(lista,1,3)
        largo=lt.size(lista)
        for i in range(largo-2,largo+1):
            valor=lt.getElement(lista,i)
            lt.addLast(pritres,valor)
            
        keys=lt.getElement(pritres,0).keys()
        listaprint={}
        for n in keys:
                i=1
                lista=[]
                while i<7:
                    listas=lt.getElement(pritres,i)
                    if type(listas[n])==dict and req7==False:
                        dic=[listas[n]]
                        tabla_formateada = tabulate(dic, headers="keys", tablefmt="grid")
                        lista.append(tabla_formateada)
                    elif type(listas[n])==dict and req7==True:
                        tabla_datos = [[key, value] for key, value in listas[n].items()]
                        tabla_formateada=tabulate(tabla_datos, headers="keys", tablefmt="grid")

    
                        lista.append(tabla_formateada)
                    else:   
                        lista.append(listas[n])
                    i+=1
                listaprint[n]=lista
                
    tabla=tabulate(listaprint, headers="keys", tablefmt='grid')
    print(tabla)
            


def load_data(control):
    archivo = input('''Archivo a cargar
    small
    5pct
    10pct
    20pct
    30pct
    50pct
    80pct
    large 
Escribir archivo: ''')
    sizeresultados,sizepenales,sizegoleadores,sizetotal,catalog,resultados_sorted,goleadores_sorted,penales_sorted=controller.load_data(control,archivo)
    print(f"El numero de resultados cargados son:{sizeresultados}")
    print_results_tabla(resultados_sorted,False)
    print(f"El numero de penales cargados son:{sizepenales} ")
    print_results_tabla(penales_sorted,False)
    print(f"El numero de goleadores cargados son:{sizegoleadores}")
    print_results_tabla(goleadores_sorted,False)
    print(f"El total de datos cargados es:{sizetotal}")
    return catalog
    

# Datos para la tabla externa

         
   


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    equipo=input("Que equipo desea consultar: ")
    npartidos=int(input("Cuantos partidos quiere ver? "))
    
    print("1.Local")
    print("2.Visitante")
    print("3.indiferente")
    condicion=input("Que condicion del equipo quiere ver? ")
    if int(condicion)==1:
        condicion="local"
    elif int(condicion)==2:
        condicion="visitante"
    elif int(condicion)==3:
        condicion="indiferente"
    partidos,tamano,deltatime=controller.req_1(catalog,equipo,condicion,npartidos)
    print(f"Se encontaron {tamano} partidos de {equipo} jugando de {condicion} en un tiempo de {deltatime} [m/s]")
    print_results_tabla(partidos,False)
    
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    jugador=input("Que jugador desea consultar: ")
    ngoles=int(input("Cuantos goles quiere ver? "))
    goles,tamano,tiempo=controller.req_2(catalog,ngoles,jugador)
    print(f"El jugador {jugador} metio {tamano} goles. Se encontraron los datos en {tiempo} ms")
    print_results_tabla(goles,False)
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    equipo=input("Que equipo desea consultar: ")
    year1=input("Desde cuando quiere consultar (Y-M-D)? ")
    year2=input("Hasta cuando quiere consultar (Y-M-D)? ")
    sublista,total,visitantes,locales,deltatime=controller.req_3(catalog,equipo,year1,year2)
    print(f"{equipo} jugó {total} partidos de los cuales {visitantes} fueron visitantes y {locales} fueron locales" )
    print(f"El requerimiento tardó {deltatime}")
    print_results_tabla(sublista,False)
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    torneo = input('Que torneo desea consultar: ')
    fecha1 = input('Desde cuando quiere consultar (Y-M-D)?: ')
    fecha2 = input("Hasta cuando quiere consultar (Y-M-D): ")
    totPart, totPais, totCit, totPen, lista, deltatime = controller.req_4(catalog,torneo,fecha1,fecha2)
    print('============== Resultados Req No.4 ==============')
    print(f'''{torneo} Partidos totales: {totPart} 
{torneo} Paises totales: {totPais} 
{torneo} Ciudades totales: {totCit} 
{torneo} penales totales: {totPen}''')
    print(f'El requerimiento tardó {deltatime} ms')
    print_results_tabla(lista, False)
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    nombre_jugador = input("Ingrese el nombre del jugador a consultar: ").capitalize()
    fecha_inicio = input("Ingrese la fecha de inicio: ")
    fecha_final = input("Ingrese la fecha final: ")

    # Llamar a la función req5 del controlador
    num_anotaciones, num_torneos, num_penales, num_autogoles, datos = controller.req_5(catalog, nombre_jugador, fecha_inicio, fecha_final)

    # Imprimir resultados
    print(f"Nombre Jugador: {nombre_jugador}")
    print(f"Fecha de Inicio: {fecha_inicio}")
    print(f"Fecha Final: {fecha_final}")
    print(f"El número de goles anotados es: {num_anotaciones}")
    print(f"El número de torneos en los que anotó {nombre_jugador} es: {num_torneos}")
    print(f"El número de penales anotados por {nombre_jugador} es: {num_penales}")
    print(f"El número de autogoles anotados por {nombre_jugador} es: {num_autogoles}")

    # Imprimir datos en forma de tabla
    from tabulate import tabulate
    print(tabulate(datos, headers="keys", tablefmt="grid", showindex=False))



def print_req_6(control):
    torneo=input("Que torneo desea consultar: ")
    year1=input("Desde cuando quiere consultar (Y-M-D)? ")
    year2=input("Hasta cuando quiere consultar (Y-M-D)? ")
    nequipos=int(input("Cuantos equipos quiere ver? "))
    lista,cantidadpartidos,ciudadescan,paisescan,ciudadmasjugada,deltatime=controller.req_6(torneo,year1,year2,nequipos,catalog)
    print(f"Durante el {torneo} entre los años´{year1} y {year2}:")
    print(f"Se jugaron {cantidadpartidos} partidos en {ciudadescan} ciudades distribuidas en {paisescan} paises")
    print(f"La ciudad en la que mas se jugo fue {ciudadmasjugada}")
    print(f"El requerimiento tardo {deltatime}")
    print_results_tabla(lista,False)

    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    year1=input("Desde cuando quiere consultar (Y-M-D)? ")
    year2=input("Hasta cuando quiere consultar (Y-M-D)? ")
    nequipos=int(input("Cuantos jugadores quiere ver? "))
    jugadoresdata,cantidadjugadores,totalauto,totalpenale,totalgoles,cantidadpartidos,deltatime=controller.req_7(year1,year2,nequipos,catalog)
    print(f"Entre el {year1} y el {year2} se jugaron {cantidadpartidos} partidos en los cuales anotaron {cantidadjugadores}")
    print(f'Se anotaron un total de {totalgoles} goles de los cuales {totalpenale} fueron por penales y {totalauto} fueron autogoles')
    print(f'El tiempo de carga fue de {deltatime} ms')
    print_results_tabla(jugadoresdata,True)
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
def print_lab4(catalog,carga,tipo,doc):
    cargalab4,time,size=controller.lab4(catalog,carga,tipo,doc)
    print(f"Se ordenaron {size} resultados en {time} ms usando {carga} en  {tipo}")
    print_results_tabla(cargalab4,False)

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:            
            
            catalog=load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
        elif int(inputs) == 10:
            print("1.small (1%)")
            print("2.5%")
            print("3.10%")
            print("4.20%")
            print("5.30%")
            print("6.50%")
            print("7.80%")
            print("8.large(100%)")
            archivo=input("Elije el archivo a cargar")
            if int(archivo)==1:
                doc=0.01
            elif int(archivo)==2:
                doc=0.05
            elif int(archivo)==3:
                doc=0.1
            elif int(archivo)==4:
                doc=0.2
            elif int(archivo)==5:
                doc=0.3
            elif int(archivo)==6:
                doc=0.5
            elif int(archivo)==7:
                doc=0.8
            elif int(archivo)==8:
                doc=1
            else:
                print("Opción errónea, vuelva a elegir.")                       
            print("1.Array_list")
            print("2.Linked_list")
            inputs=input("Elije el tipo de estructura:")

            if int(inputs)==1:
                tipo='ARRAY_LIST'
                print("1.Selection")
                print("2.Insertion")
                print("3.Shell")
                print("4.Merge")
                print("5.Quick")
                inputs=input("Como desea cargar los datos :")
            
                if int(inputs)==1:
                    carga="Selection"
                elif int(inputs)==2:
                    carga="Insertion"
                elif int(inputs)==3:
                    carga="Shell"
                elif int(inputs)==4:
                    carga="Merge"
                elif int(inputs)==5:
                    carga="Quick"
                else:
                    print("Opción errónea, vuelva a elegir.")

            elif int(inputs)==2:
                tipo='SINGLE_LINKED'
                print("1.Selection")
                print("2.Insertion")
                print("3.Shell")
                inputs=input("Como desea cargar los datos :")
            
                if int(inputs)==1:
                    carga="Selection"
                elif int(inputs)==2:
                    carga="Insertion"
                elif int(inputs)==3:
                    carga="Shell"
                else:
                    print("Opción errónea, vuelva a elegir.")
            else:
                print("opcion no valida")
            print_lab4(catalog,carga,tipo,doc)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
