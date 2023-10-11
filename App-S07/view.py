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
import threading
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_lista):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_lista)
    return control
    

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
    print("10- Elegir algoritmo de ordenamiento")
    print("0- Salir")


def load_data(control, tamaño):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    results, goal_scorers, shootouts = controller.load_data(control, tamaño)
    return results, goal_scorers, shootouts


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass


def print_req_1(rta):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    if lt.size(rta)> 6:
        print_first_last_3(rta)
    else:
        print(tabulate(rta["elements"], headers="keys",tablefmt="grid"))
    


def print_req_2(final_scorer_goals, size_list, number_goals, name_player, total_goals):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    if size_list > 6:
        if total_goals < int(number_goals):
            print("\nLas 3 primeras y 3 ultimas anotaciones de los primeros " + str(total_goals) + " goles de " + name_player + " son: ")
            print_first_last_3(final_scorer_goals)
        else:
            print("\nLas 3 primeras y 3 ultimas anotaciones de los primeros " + number_goals + " goles de " + name_player + " son: ")
            print_first_last_3(final_scorer_goals)   
    else:
        if total_goals < int(number_goals):
            print("\nLos primeros " + str(total_goals) + " goles de " + name_player + " son: ")
            print(tabulate(final_scorer_goals["elements"], headers="keys",tablefmt="grid"))
        else: 
            print("\nLos primeros " + number_goals + " goles de " + name_player + " son: ")
            print(tabulate(final_scorer_goals["elements"], headers="keys",tablefmt="grid"))


def print_req_3(sorted_date, size_list2, team_name, inicial_date, final_date):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    if size_list2 > 6:
        print("\nLos 3 ultimos y 3 primeros partidos disputados por " + team_name + " entre " + inicial_date + " y " + final_date + " son:")
        print_first_last_3(sorted_date)
    else:
        print("\nLos partidos disputados por " + team_name + " entre " + inicial_date + " y " + final_date + " son:")
        print(tabulate(sorted_date["elements"], headers="keys",tablefmt="grid"))


def print_req_4(rta):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    if lt.size(rta)> 6:
        print_first_last_3(rta)
    else:
        print(tabulate(rta["elements"], headers="keys",tablefmt="grid"))


def print_req_5(scorer_data):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    if lt.size(scorer_data)> 6:
        print_first_last_3(scorer_data)
    else:
        print(tabulate(scorer_data["elements"], headers="keys",tablefmt="grid"))


def print_req_6(rta):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    if lt.size(rta)> 6:
        print_first_last_3(rta)
    else:
        print(tabulate(rta["elements"], headers="keys",tablefmt="grid"))


def print_req_7(data_top_scorers, size_list3, top_scorers, total_anotadores):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    if size_list3 > 6:
        if total_anotadores < int(top_scorers):
            print("\nLos 3 primeros y 3 ultimos goleadores del ranking " + str(total_anotadores) + " de goleadores oficiales son:")
            print_first_last_3(data_top_scorers)
        else:
            print("\nLos 3 primeros y 3 ultimos goleadores del ranking " + top_scorers + " de goleadores oficiales son:")
            print_first_last_3(data_top_scorers) 
    else:
        if total_anotadores < int(top_scorers):
            print("\nEl ranking " + str(total_anotadores) + " de goleadores oficiales son:")
            print(tabulate(data_top_scorers["elements"], headers="keys",tablefmt="grid"))
        else:
            print("\nEl ranking " + top_scorers + " de goleadores oficiales son:")
            print(tabulate(data_top_scorers["elements"], headers="keys",tablefmt="grid"))


def print_req_8(lista):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    if lt.size(lista)> 6:
        print_first_last_3(lista)
    else:
        print(tabulate(lista["elements"], headers="keys",tablefmt="grid"))

def print_first_last_3 (lista):
    """
        Funcion que imprime los primeros y ultimos 3 datos de una lista
    """
    rta = []
    sublista_1 = lt.subList(lista, 1, 3)
    sublista_2 = lt.subList(lista, lt.size(lista)-2, 3)
    for i in lt.iterator(sublista_1):
        rta.append(i)
    for i in lt.iterator(sublista_2):
        rta.append(i)
    print(tabulate(rta, headers="keys",tablefmt="grid"))

# Se crea el controlador asociado a la vista
#control = new_controller()
# main del reto
default_limit = 1000
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
            lista = input("Ingrese el tipo de lista que desea utilizar: \na) Array list (si desea utilizar un arreglo)\nb) Single linked (si desea usar una lista enlazada)\n")
            if lista == "a":
                lista = "ARRAY_LIST"
            elif lista == "b":
                lista = "SINGLE_LINKED"
            else:
                lista = "Entrada no valida"
                print(lista)
            control = new_controller(lista)
            
            tamaño = input ("Ingrese el tamaño del archivo que desea utilizar: \na) small\nb) 5pct\nc) 10pct\nd) 20pct\ne) 30pct\nf) 50pct\ng) 80pct\nh) large\n")
            if tamaño == "a":
                tamaño = "small"
            elif tamaño == "b":
                tamaño = "5pct"
            elif tamaño == "c":
                tamaño = "10pct"
            elif tamaño == "d":
                tamaño = "20pct"
            elif tamaño == "e":
                tamaño = "30pct"
            elif tamaño == "f":
                tamaño = "50pct"
            elif tamaño == "g":
                tamaño = "80pct"
            elif tamaño == "h":
                tamaño = "large"
            else:
                tamaño = "Entrada no valida"
                print(tamaño)

            if tamaño != "Entrada no valida":
                print("Cargando información de los archivos ....\n")
                re, go, sho = load_data(control, tamaño)
                print('Match result count: ' + str(re))
                print('goal scorers count: ' + str(go))
                print('shootout-penalty definition count: ' + str(sho))

                print("\n\nResults")
                print_first_last_3(control["model"]["results"])

                print("\n\nScorers")
                print_first_last_3(control["model"]["goal_scorers"])
        
                print("\n\nShoots")
                print_first_last_3(control["model"]["shootouts"])
            
        elif int(inputs) == 2:
            numero_partidos = input("Ingrese el numero de partidos que quiere buscar: ")
            equipo = input("Ingrese el nombre del equipo: ")
            condicion_equipo = input("Ingrese la condición del equipo: ")
            total_partidos, rta, time = controller.req_1(control["model"], numero_partidos, equipo, condicion_equipo)
            print("total matches found: ", str(total_partidos))
            print_req_1(rta)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))


        elif int(inputs) == 3:
            name_player = input("Ingrese el nombre completo del jugador: ")
            number_goals = input("Ingrese el numero de goles que desea consultar: ")
            final_scorer_goals, size_list, total_goals, time = controller.req_2(control["model"], number_goals, name_player)
            print("\nEl total de goles anotados por " + name_player + " es: \n" + str(total_goals) + " goles")
            print_req_2(final_scorer_goals, size_list, number_goals, name_player, total_goals)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))

        elif int(inputs) == 4:
            team_name = input("Ingrese el nombre completo del equipo: ")
            inicial_date = input("Ingrese la fecha inicial del periodo: ")
            final_date = input("Ingrese la fecha final del periodo: ")
            sorted_date, size_list2, total_team_matches, total_home_team, total_away_team, time = controller.req_3(control["model"], team_name, inicial_date, final_date)
            print("\nEl total de partidos disputados por " + team_name + " entre " + inicial_date + " y " + final_date + " es: \n" + str(total_team_matches) + " partidos")
            print("\nEl numero de partidos disputados como local es: \n" + str(total_home_team) + " partidos")
            print("\nEl numero de partidos disputados como visitante es: \n" + str(total_away_team) + " partidos")
            print_req_3(sorted_date, size_list2, team_name, inicial_date, final_date)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))

        elif int(inputs) == 5:
            torneo = input("Ingrese el nombre del torneo: ")
            limite_inferior = input("Ingrese la fecha en la que inicia el rango: ")
            limite_superior = input("Ingrese la fecha en la que termina el rango: ")
            partidos_torneo, paises, ciudades, penales, rta, time = controller.req_4(control["model"], torneo, limite_inferior, limite_superior)
            print(torneo + " Total matches: " + str(partidos_torneo))
            print(torneo + " Total countries: " + str(paises))
            print(torneo + " Total cities: " + str(ciudades))
            print(torneo + " Total shootout: " + str(penales))
            print_req_4(rta)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))


        elif int(inputs) == 6:
            scorer = input("Ingrese el nombre del jugador: ")
            limite_inferior = input("Ingrese la fecha en la que inicia el rango: ")
            limite_superior = input("Ingrese la fecha en la que termina el rango: ")
            anotaciones, torneos, penales, autogoles, scorer_data, time = controller.req_5(control["model"], scorer, limite_inferior, limite_superior)
            print(scorer + " Total goals: " + str(anotaciones))
            print(scorer + " Total tournaments: " + str(torneos))
            print(scorer + " Total penalties: " + str(penales) )
            print(scorer + " Total autogoals: " + str(autogoles))
            print_req_5(scorer_data)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))

        elif int(inputs) == 7:
            numero_equipos = input("Ingrese el top: ")
            torneo = input("Ingrese el nombre del torneo: ")
            limite_inferior = input("Ingrese la fecha en la que inicia el rango: ")
            limite_superior = input("Ingrese la fecha en la que termina el rango: ")
            teams, partidos_torneo, paises, ciudades, ciudad, rta, time = controller.req_6(control["model"], numero_equipos, torneo, limite_inferior, limite_superior)
            print(torneo + " Total teams: " + str(teams))
            print(torneo + " Total matches: " + str(partidos_torneo))
            print(torneo + " Total countries: " + str(paises))
            print(torneo + " Total cities: " + str(ciudades))
            print(torneo + " City with most matches: " + str(ciudad))
            print_req_6(rta)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))

        elif int(inputs) == 8:
            top_scorers = input("Ingrese top ranking jugadores que desea consultar: ")
            inicial_date2 = input("Ingrese la fecha inicial del periodo: ")
            final_date2 = input("Ingrese la fecha final del periodo: ")
            data_top_scorers, size_list3, total_anotadores, total_partidos1, total_torneos, total_goles_anotadores, total_penaltys, total_autogoles, time2 = controller.req_7(control["model"], top_scorers, inicial_date2, final_date2)
            print("\nEl top ranking de goleadores es " + top_scorers + " jugadores")
            print("Fecha inicial del periodo: " + inicial_date2)
            print("Fecha final del periodo: " + final_date2)
            print("\nAnotadores torneos oficiales: " + str(total_anotadores))
            print("Partidos torneos oficiales: " + str(total_partidos1))
            print("torneos oficiales: " + str(total_torneos))
            print("Goles totales de torneos oficiales: " + str(total_goles_anotadores))
            print("Goles por penal de torneos oficiales: " + str(total_penaltys))
            print("Autogoles en torneos oficiales: " + str(total_autogoles))
            print_req_7(data_top_scorers, size_list3, top_scorers, total_anotadores)
            delta_time2 = f"{time2:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time2))
        
        elif int(inputs) == 9:
            team1 = input("Team 1 name: ")
            team2 = input("Team 2 name: ")
            limite_inferior = input("Ingrese la fecha en la que inicia el rango: ")
            limite_superior = input("Ingrese la fecha en la que termina el rango: ")
            years_1, partidos_1, local_1, visitante_1, oldest_match_1, ultimo_1, estadisticas_1, years_2, partidos_2, local_2, visitante_2, oldest_match_2, ultimo_2, estadisticas_2, encuentros, victorias_1, derrotas_1, victorias_2, derrotas_2, empates, ultimo_partido_1_2, anotaciones_ultimo, time  = controller.req_8(control["model"], team1, team2, limite_inferior, limite_superior)
            
            print("\n\n" + team1 + " Statistics")
            print("\nYears: " + str(years_1))
            print("Total matches: " + str(partidos_1))
            print("Total home matches: " + str(local_1))
            print("Total away matches: " + str(visitante_1))
            print("Oldest match date: " + oldest_match_1)
            print("\n\n Newest match data")
            print_req_8(ultimo_1)
            print("\n\n Yearly statistics")
            print_req_8(estadisticas_1)

            print("\n\n" + team2 + " Statistics")
            print("\nYears: " + str(years_2))
            print("Total matches: " + str(partidos_2))
            print("Total home matches: " + str(local_2))
            print("Total away matches: " + str(visitante_2))
            print("Oldest match date: " + oldest_match_2)
            print("\n\n Newest match data")
            print_req_8(ultimo_2)
            print("\n\n Yearly statistics")
            print_req_8(estadisticas_2)

            print("\n\n" + team1 + " vs " + team2 + " Statistics")
            print("\nTotal matches: " + str(encuentros))
            print("Total wins for " + team1 + ": " + str(victorias_1))
            print("Total losses for " + team1 + ": " + str(derrotas_1))
            print("Total wins for " + team2 + ": " + str(victorias_2))
            print("Total losses for " + team2 + ": " + str(derrotas_2))
            print("Total draws: " + str(empates))
            print("\n\n Newest match data")
            print_req_8(ultimo_partido_1_2)
            print("\n\n Match scorers")
            print_req_8(anotaciones_ultimo)
            delta_time = f"{time:.3}"
            print("El tiempo para ejecutar el requerimiento fue de: " + str(delta_time))

        elif int(inputs) == 10:
            sortings = ["se", "ins", "sa", "merg", "quk"]
            tipo = int( input ("Ingrese el tipo de ordenamiento que desea utilizar: \n 1) Selection\n 2) Insertion\n 3) Shell\n 4) Merge Sort\n 5) Quick Sort\n"))
            if tipo == 1:
                tipo = "se"
            elif tipo == 2:
                tipo = "ins"
            elif tipo == 3:
                tipo = "sa"
            elif tipo == 4:
                tipo = "merg"
            elif tipo == 5:
                tipo = "quk"
            else:
                tipo = "Opcion no valida"
                print(tipo)
            if tipo != "Opcion no valida": 
                time_r, time_g, time_s, results, goal_scorers, shootouts = controller.sort_data(tipo, control["model"])
                delta_time_1 = f"{time_r:.3}"
                delta_time_2 = f"{time_g:.3}"
                delta_time_3 = f"{time_s:.3}"
                control["model"]["results"]= results 
                control["model"]["goal_scorers"]= goal_scorers 
                control["model"]["shootouts"]= shootouts 
                print("\n\nSORTED RESULTS")
                print("Para " +str(lt.size(results)) +" datos el delta de tiempo es: "+str(delta_time_1)+" [ms]")
                print_first_last_3(results)

                print("\n\nSORTED GOAL SCORERS")
                print("Para " +str(lt.size(goal_scorers)) +" datos el delta de tiempo es: "+str(delta_time_2)+" [ms]")
                print_first_last_3(goal_scorers)

                print("\n\nSORTED SHOOTOUTS")
                print("Para " +str(lt.size(shootouts)) +" datos el delta de tiempo es: "+str(delta_time_3)+" [ms]")
                print_first_last_3(shootouts)


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