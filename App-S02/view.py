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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime


assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(list_type):
    """
        Se crea una instancia del controlador """
    
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos

    control = controller.new_controller(list_type)
    
    
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los últimos N partidos de un equipo según su condición ")
    print("3- Listar los primeros N goles anotados por un jugador ")
    print("4- Consultar los partidos que disputó un equipo durante un periodo especifico")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo especifico ")
    print("6- Consultar las anotaciones de un jugador durante un periodo especifico ")
    print("7- Clasificar los N mejores equipos de un torneo en un periodo especifico ")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo especifico ")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales ")
    print("10 - Ordenar resultados (Lab4)")
    print("0- Salir")

def archivo()->str:
    input_file_size = int(input("Seleccione el tamaño del archivo: \n 1-5% \n 2-10% \n 3-20% \n 4-30% \n 5-50% \n 6-80% \n 7-large \n 8-small \n"))
    tamanio = ""
    if input_file_size == 1:
        tamanio = "-5pct.csv"
    elif input_file_size == 2:
        tamanio = "-10pct.csv"
    elif input_file_size == 3:
        tamanio = "-20pct.csv"
    elif input_file_size == 4:
        tamanio = "-30pct.csv"
    elif input_file_size == 5:
        tamanio = "-50pct.csv"
    elif input_file_size == 6:
        tamanio = "-80pct.csv"
    elif input_file_size == 7:
        tamanio = "-large.csv"
    elif input_file_size == 8:
        tamanio = "-small.csv"
    return tamanio

def tipo_lista():
    input_list_type = int(input("Seleccione el tipo de lista:\n1- Array List \n2-Single Linked List\n "))   
    if input_list_type == 1:
        list_type = "ARRAY_LIST"
    elif input_list_type == 2:
        list_type = "SINGLE_LINKED"
    return list_type

def load_data_view(control, tamanio):
    """
    Carga los datos
    """
    goalscorers = "goalscorers-utf8"+tamanio
    results = "results-utf8"+tamanio 
    shootouts = "shootouts-utf8"+tamanio

    controller.load_data(control, goalscorers, results, shootouts)

    sublist_goalscorers = controller.loadsublist(control, "goalscorers")
    sublist_results = controller.loadsublist(control, "results")
    sublist_shootouts = controller.loadsublist(control, "shootouts")

    print(tabulate(lt.iterator(sublist_goalscorers), headers="keys", tablefmt="grid"))
    print(tabulate(lt.iterator(sublist_results), headers="keys", tablefmt="grid"))
    print(tabulate(lt.iterator(sublist_shootouts), headers="keys", tablefmt="grid"))
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    numero_partidos = int(input("Ingrese el número de partidos a revisar: "))
    team = input("Ingrese la selección(Inglés): ")
    condicion_equipo = int(input("Ingrese la condición del partido 1 para local, 2 para visitante y 3 para neutral: "))
    if condicion_equipo == 1:
        condicion = "home"
    elif condicion_equipo == 2:
        condicion = "visitor"
    elif condicion_equipo == 3:
        condicion = "neutral"
    result, execution_time = controller.req_1_controller(control, numero_partidos, team, condicion)
    print("============= REQ No. 1 Results ============")
    print(f"Execution time: {execution_time} seconds.")
    print(tabulate(lt.iterator(result), headers="keys", tablefmt="grid"))
    return result, execution_time

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    numero_goles = int(input("Ingrese el número de goles: "))
    nombre_jugador = input("Ingres el nombre del jugador que desea buscar: ")
    result, execution_time = controller.req_2_controller(control, numero_goles, nombre_jugador)
    print("============= REQ No. 2 Results ============")
    print(f"Execution time: {execution_time} seconds.")

    print(tabulate(lt.iterator(result), headers="keys", tablefmt="grid"))
    return result

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    team_name = input("Ingrese la selección(Inglés): ")
    initial_date = datetime.strptime(input("Ingrese la fecha inicial(YYYY-mm-dd): "),"%Y-%m-%d").date()
    final_date = datetime.strptime(input("Ingrese la fecha final(YYYY-mm-dd): "),"%Y-%m-%d").date()
    result, execution_time  = controller.req_3_controller(control, team_name, initial_date, final_date)
    get3_result, total_games,total_home,total_away = result
    print("============= REQ No. 3 Results ============")
    print(team_name+ "Total games: "+str(total_games))
    print(team_name+ "Total home games: "+str(total_home))
    print(team_name+ "Total away games: "+str(total_away))
    print(f"Execution time: {execution_time} seconds.")

    print(tabulate(lt.iterator(get3_result), headers="keys", tablefmt="grid"))

    return result
    
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("===============   Req No. 4 Inputs  ===============")

    tournament_name = input("Ingrese el nombre del torneo: ")
    initial_date = input("Ingrese la fecha inicial(YYYY-mm-dd): ")
    final_date = input("Ingrese la fecha final(YYYY-mm-dd): ")
    result, time = controller.req_4_controller(control, tournament_name, initial_date , final_date)
    partidos, paises, ciudades, shootouts, lista = result
    print("===============   Req No. 4 Answers  ===============")

    print("Total games "+ str(partidos))
    print("Total countries "+str(paises))
    print("Total cities "+ str(ciudades))
    print("Total shootouts "+str(shootouts))
    print("Total time "+str(time))
    print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("===============   Req No. 5 Inputs  ===============")
    nombre = input("Player name: ")
    fecha1 = input("Start Date: ")
    fecha2 = input("End date: ")
    
    
    result , execution_time = controller.req_5(control , nombre , fecha1 , fecha2  )
    goals, torneos , penalties, autogoals,  data = result
    print("===============   Req No. 5 Results  ===============")
    print(f"Execution Time: {execution_time} seconds")

    print(nombre +" " + f"goales: {goals}")
    print(nombre +" " + f"torneos: {torneos}")
    print(nombre +" " +f"penaltis: {penalties}")
    print(nombre +" " + f"autogoles: {autogoals}")


    print(tabulate(lt.iterator(data) , headers="keys" , tablefmt = "grid"))
    
    
    return result


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    print("===============   Req No. 6 Inputs  ===============")

    tournament_name = input("Ingrese el nombre del torneo: ")
    initial_date = input("Ingrese la fecha inicial(YYYY-mm-dd): ")
    final_date = input("Ingrese la fecha final(YYYY-mm-dd): ")
    
    print("===============   Req No. 6 Answers  ===============")

    result, time  = (controller.req_6_controller(control, 3, tournament_name, initial_date,final_date))
    teams_information, num_cities, num_countries, num_teams = result
    print("Total games "+ str(num_teams))
    print("Total countries "+str(num_countries))
    print("Total cities "+ str(num_cities))
    print("Total time "+str(time))
    print(tabulate(lt.iterator(teams_information),headers="keys", tablefmt="fancy_grid"))


def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    print("===============   Req No. 7 Inputs  ===============")
    num_jugadores = int(input("Numero de jugadores "))
    fecha1 = input("Start Date: ")
    fecha2 = input("End date: ")
    
    result7, execution_time = controller.req_7(control, num_jugadores, fecha1, fecha2)
    total_players, cantidad_match, goles, total_goles, autogoles, ranking_jugadores = result7
    
    print("===============   Req No. 7 Results  ===============")
    print(f"Execution Time: {execution_time} seconds")
    print(f"Official tournaments total players: {total_players}")
    print(f"Official tournaments total matches: {cantidad_match}")
    print(f"Official tournaments total goals: {goles}")
    print(f"Official tournaments total penalties: {total_goles}")
    print(f"Official tournaments total own_goals: {autogoles}")
    
    
    
    
    print(tabulate(lt.iterator(ranking_jugadores) , headers="keys" , tablefmt = "grid"))
    
    
    
    
    
    return result7


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def print_req_9(control):
    
    input_sort_type = int(input("Seleccione el tipo de sort: \n 1-Selection \n 2-Insertion \n 3-Shell \n 4-Merge \n 5-Quick \n"))
    if input_sort_type == 1:
        sort_type = se
    elif input_sort_type == 2:
        sort_type = ins
    elif input_sort_type == 3:
        sort_type = sa
    elif input_sort_type == 4:
        sort_type = merg
    elif input_sort_type == 5:
        sort_type = quk
    
    tiempo, lista= controller.sort(control,sort_type)
    get3 = controller.get3(lista)
    print(tabulate(lt.iterator(get3), headers="keys", tablefmt="grid"))
    print(tiempo)


# Se crea el controlador asociado a la vista

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
        if int(inputs) == 1:
            tipo = tipo_lista()
            control = new_controller(tipo)
            tamanio = archivo()
            print("Cargando información de los archivos ....\n")
            load_data_view(control, tamanio)
            
    
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
            print("Cargando información de los archivos ....\n")
            requerimiento9 = print_req_9(control)
            
       
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
