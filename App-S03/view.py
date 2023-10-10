"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * along withthis program.If not, see <http://www.gnu.org/licenses/>.
 """
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
import threading

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def new_controller():
    """
    Se crea una instancia del controlador
    
    """
    print("\n==============================Menú de Estructuras de Datos==============================\nAntes de empezar escoja la Estrcutura de Datos en que desea cargar su información\n")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")
    print("3- DOUBLE_LINKED")
    consulta_EDD = input('Seleccione la Estructura de Datos en la que desea cargar sus datos: ')
    match consulta_EDD:
        case "1":
            consulta_EDD = "ARRAY_LIST"
        case "2":
            consulta_EDD = "SINGLE_LINKED"
        case "3":
            consulta_EDD = "DOUBLE_LINKED"
            
    control = controller.new_controller(consulta_EDD)
    return control

# MENÚS

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Últimos N partidos de un equipo según su condición")
    print("3- Primeros N goles anotados por un jugador")
    print("4- Partidos que disputó un equipo  durante un periodo específico")
    print("5- Partidos relacionados con un torneo durante un periodo específico")
    print("6- Anotaciones de un jugador durante un periodo específico")
    print("7- Clasificar los N mejores equipos de un torneo en un period específico")
    print("8- Clasificar los N mejores anotadores  en partidos ofciales dentro de un periodo específcio")
    print("9- Comparar el desempño histórico de dos selecciones en torneos oficiales")
    print("10- Cambiar algoritmo de ordenamiento ")
    print("0- Salir")
    
def print_consulta_size():
    print("\nMenú de tamaños")
    print("1- small")
    print("2- 5pct")
    print("3- 10pct")
    print("4- 20pct")
    print("5- 30pct")
    print("6- 50pct")
    print("7- 80pct")
    print("8- large")


def print_consulta_alg(control):
    print("\n==============================Menú de Algoritmos de Ordenamiento==============================\n")
    print("1- Insertion")
    print("2- Merge")
    print("3- Quick")
    print("4- Selection")
    print("5- Shell")

    consulta_alg_ord = input("Ingrese Valor: ")

    tiempo = controller.sort_tiempo(control, consulta_alg_ord)

    print("\nEl tiempo fue: " + str(round(tiempo,2)) + " m/s\n")

def load_data(control, consulta_size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    match consulta_size:
        case "1":
            consulta_size = "small"
        case "2":
            consulta_size = "5pct"
        case "3":
            consulta_size = "10pct"
        case "4":
            consulta_size = "20pct"
        case "5":
            consulta_size = "30pct"
        case "6":
            consulta_size = "50pct" 
        case "7":
            consulta_size = "80pct"
        case "8":
            consulta_size = "large"
        
           
    controller.load_data(control, consulta_size)
    
def print_data(control):
    """
    Función que imprime los primeros 3 y últimos 3 elementos ordenados por fecha
    """
    load_data(control, consulta_size)
    for data_type in ["results", "goalscorers", "shootouts"]:
        if data_type in control:
            data = lt.iterator(control[data_type])
            sorted_elements = sorted(data, key=lambda x: x['date'])
            tamaño = lt.size(control[data_type])
            if tamaño >= 6:
                primeros_3 = sorted_elements[:3]
                ultimos_3 = sorted_elements[-3:]
            else:
                primeros_3 = sorted_elements
                ultimos_3 = []

            print(f"{data_type.capitalize()} count: {tamaño}")

            if primeros_3:
                print(f"Primeros 3 {data_type}:")
                print(tabulate(primeros_3, headers="keys", tablefmt="grid", showindex=False))

            if ultimos_3:
                print(f"Últimos  3 {data_type}:")
                print(tabulate(ultimos_3, headers="keys", tablefmt="grid", showindex=False))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    n = int(input("\nIngrese el número de partidos: "))
    n_equipo = input("Ingrese el nombre del Equipo: ").capitalize()
    condicion = input("Condición del equipo: ").lower()


    partidos, resultado, dt = controller.req_1(n, n_equipo, condicion, control, valor_ord)
    
    print("\n======================= Req No. 1 Inputs =======================\n"+"Numero partidos: "+str(n)
          +"\nNombre Equipo: "+ n_equipo.title() +"\nCondición Equipo: "+ condicion.title() 
          + "\n\n======================= Req No. 1 Results =======================" + "\nEl numero de partidos encontrados es: " + str(partidos) + "\n")
    
    print("El tiempo de ejecución del requerimiento es:", dt )
    print(tabulate(lt.iterator(resultado), headers="keys", tablefmt="grid", showindex=False))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")
    consulta_jugador = input("\nIngrese el jugador a consultar: ").lower()
    consulta_goles = int(input("Ingrese el número de goles a consultar: "))
    
    num_goles, goles, dt = controller.req_2(control, consulta_jugador, consulta_goles, valor_ord)
    
    print(f"\n======================= Req No. 2 Inputs ======================= \nNumero goles: {num_goles}"
          +"\nNombre Jugador: "+ consulta_jugador
          + "\n\n======================= Req No. 2 Results =======================" + "\nEl numero de goles encontrados es: " + str(num_goles) + "\n")
    print("El tiempo de ejecución del requerimiento es:",dt )
    print(tabulate(lt.iterator(goles), headers="keys", tablefmt="grid", showindex=False))
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    
    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    consulta_equipo = input("\nIngrese el equipo a consultar: ").capitalize()
    consulta_fecha_i = input("Ingrese la fecha de inicio para la búsqueda en el formato AAAA-MM-DD: ")
    consulta_fecha_f = input("Ingrese la fecha final para la búsqueda en el formato AAAA-MM-DD: ")

    
    num_partidos, num_partidos_L, num_partidos_V, datos, dt = controller.req_3(control, consulta_equipo, consulta_fecha_i, consulta_fecha_f, valor_ord)

    print(f"\n====================================== Req No. 3 Inputs ======================================\n"
      f"Nombre equipo: {consulta_equipo.title()}\n"
      f"Fecha de Inicio: {consulta_fecha_i}\n"
      f"Fecha Final: {consulta_fecha_f}\n"
      f"====================================== Req No. 3 Results ======================================\n"
      f"El número total de partidos disputados encontrados es: {num_partidos}\n"
      f"El número de partidos disputados como local de {consulta_equipo.title()} es: {num_partidos_L}\n"
      f"El número de partidos disputados como visitante de {consulta_equipo.title()} es: {num_partidos_V}\n")
    print("El tiempo de ejecución del requerimiento es:", dt )
    print(tabulate(lt.iterator(datos), headers="keys", tablefmt="grid", showindex=False))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
        
    """


    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    consulta_torneo = input("\nIngrese el torneo a consultar: ")
    consulta_fecha_i = input("Ingrese la fecha de inicio para la búsqueda en el formato AAAA-MM-DD: ")
    consulta_fecha_f = input("Ingrese la fecha final para la búsqueda en el formato AAAA-MM-DD: ")


    num_partidos, num_paises, num_ciudades, num_partidosxpenales, datos, dt = controller.req_4(control, consulta_torneo, consulta_fecha_i, consulta_fecha_f, valor_ord)
    
    print(f"\n====================================== Req No. 4 Inputs ======================================\n"
      f"Nombre del torneo: {consulta_torneo.title()}\n"
      f"Fecha de Inicio: {consulta_fecha_i}\n"
      f"Fecha Final: {consulta_fecha_f}\n"
      f"====================================== Req No. 4 Results ======================================\n"
      f"El número total de 1partidos relevantes encontrados es: {num_partidos}\n"
      f"El número de paises involucrados en el torneo {consulta_torneo.title()} es: {num_paises}\n"
      f"El número de ciudades involucradas en el torneo {consulta_torneo.title()} es: {num_ciudades}\n"
      f"El número de partidos decididos desde punto pernal en el torneo {consulta_torneo.title()} es: {num_partidosxpenales}\n")
    
    print("El tiempo de ejecución del requerimiento es:", dt )
    print(tabulate(lt.iterator(datos), headers="keys", tablefmt="grid", showindex=False))
    
    
def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    
    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    consulta_jugador = input("\nIngrese el jugador a consultar: ").lower()
    consulta_fecha_i = input("Ingrese la fecha de inicio para la búsqueda en el formato AAAA-MM-DD: ")
    consulta_fecha_f = input("Ingrese la fecha final para la búsqueda en el formato AAAA-MM-DD: ")
    
    num_anotaciones, num_torneos, num_penales, num_autogoles, datos,dt = controller.req_5(control, consulta_jugador, consulta_fecha_i, consulta_fecha_f,valor_ord)

    print(f"\n====================================== Req No. 5 Inputs ======================================\n"
      f"Nombre Jugador: {consulta_jugador.title()}\n"
      f"Fecha de Inicio: {consulta_fecha_i}\n"
      f"Fecha Final: {consulta_fecha_f}\n"
      f"====================================== Req No. 5 Results ======================================\n"
      f"El numero de goles encontrados es: {num_anotaciones}\n"
      f"El número de torneos en que anotó {consulta_jugador.title()} es: {num_torneos}\n"
      f"El número de penales anotados por {consulta_jugador.title()} es: {num_penales}\n"
      f"El número de autogoles anotados por {consulta_jugador.title()} es: {num_autogoles}\n")
    
    print("El tiempo de ejecución del requerimiento es:", dt )

    print(tabulate(lt.iterator(datos), headers="keys", tablefmt="grid", showindex=False))
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6

    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    consulta_n_mejores = int(input("\nIngrese el número de equipos a consultar: "))
    consulta_torneo = input("Ingrese el torneo a consultar: ").lower()
    consulta_fecha_i = input("Ingrese la fecha de inicio para la búsqueda en el formato AAAA-MM-DD: ")
    consulta_fecha_f = input("Ingrese la fecha final para la búsqueda en el formato AAAA-MM-DD: ")
    
    num_equipos, num_partidos, num_paises, num_ciudades, ciudad_md, equipos, dt = controller.req_6(control, 
                                                                                 consulta_n_mejores,
                                                                                 consulta_torneo,
                                                                                 consulta_fecha_i, 
                                                                                 consulta_fecha_f,valor_ord)
    
    print(f"\n====================================== Req No. 6 Inputs ======================================\n"
      f"Torneo: {consulta_torneo}\n"
      f"Número de Equipos Consultados: {consulta_n_mejores}\n"
      f"Fecha de Inicio: {consulta_fecha_i}\n"
      f"Fecha Final: {consulta_fecha_f}\n"
      f"====================================== Req No. 6 Results ======================================\n"
      f"El numero de equipos encontrados es: {num_equipos}\n"
      f"El número de partidos del torneo fue: {num_partidos} \n"
      f"El número de ciudades anfitrionas del torneo es: {num_ciudades}\n"
      f"El número de paises involucrados en el torneo es: {num_paises}\n"
      f"Las ciudade en la que más se jugaron partidos en el torneo es: {ciudad_md}\n")

    print("El tiempo de ejecución del requerimiento es:", dt )

    for equipo in lt.iterator(equipos):
        titulos = list(equipo["Jugador Destacado"].keys())
        data = list(equipo["Jugador Destacado"].values())
        equipo["Jugador Destacado"] = tabulate([data],headers=titulos,tablefmt='grid')
    print(tabulate(lt.iterator(equipos), headers="keys", tablefmt="grid", showindex=False))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    print("\nTipo de algortimo ordenamiento\n1. Inserction\n2. Merge\n3. Quick\n4. Selection\n5. Shell")
    valor_ord = input("Ingrese número: ")

    consulta_n_jugadores = int(input("Ingrese el número de jugadores a consultar: "))
    consulta_fecha_i = input("Ingrese la fecha de inicio para la búsqueda en el formato AAAA-MM-DD: ")
    consulta_fecha_f = input("Ingrese la fecha final para la búsqueda en el formato AAAA-MM-DD: ")
    
    num_anotadores, num_partidos,num_torneos, num_anotaciones, goles_penal, autogoles, anotadores, dt = controller.req_7(control, 
                                                                                 consulta_n_jugadores,
                                                                                 consulta_fecha_i, 
                                                                                 consulta_fecha_f,valor_ord)

    print(f"\n====================================== Req No. 7 Inputs ======================================\n"
      f"Número de Equipos Consultados: {consulta_n_jugadores}\n"
      f"Fecha de Inicio: {consulta_fecha_i}\n"
      f"Fecha Final: {consulta_fecha_f}\n"
      f"====================================== Req No. 7 Results ======================================\n"
      f"El numero de jugadores encontrados es: {num_anotadores}\n"
      f"El número de partidos del torneo fue: {num_partidos}\n"
      f"El número de torneos fue: {num_torneos} \n"
      f"El número de goles: {num_anotaciones}\n"
      f"El número de penales: {goles_penal}\n"
      f"El número de autogoles: {autogoles}\n")

    print("El tiempo de ejecución del requerimiento es:", dt )
    
    for anotador in lt.iterator(anotadores):
        titulos = list(anotador["ultimo_gol"].keys())
        data = list(anotador["ultimo_gol"].values())
        anotador["ultimo_gol"] = tabulate([data],headers=titulos,tablefmt='grid')

    print(tabulate(lt.iterator(anotadores), headers="keys", tablefmt="grid", showindex=False))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def algoritmo_ordenamiento(control, consulta_alg_ord):
    controller.sort(control, consulta_alg_ord)


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print_consulta_size()
                consulta_size = input('Seleccione el tamaño de archivos que desea cargar: ')
                
                print("Cargando información de los archivos ....\n")
                print_data(control)    

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
                print_consulta_alg(control)
                # algoritmo_ordenamiento(consulta_alg_ord)
                

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa") 
            else:
                print("Opción errónea, vuelva a elegir.\n")
        
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
                
    sys.exit(0)