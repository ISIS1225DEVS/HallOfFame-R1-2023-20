"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Alg1oritmos
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

from tabulate import tabulate
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
#from tabulate import tabulate
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
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Ejecutar opcion 9")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    santiago = controller.load_results(control, "football/results-utf8-small.csv")
    maria = controller.load_goalscorers(control, "football/goalscorers-utf8-small.csv")
    ian = controller.load_shootouts(control, "football/shootouts-utf8-small.csv")
    return santiago , maria, ian

def load_list_results(control):
    santiago = controller.load_results(control, "football/results-utf8-small.csv")
    santiago_list = controller.list_results(santiago)

    return santiago_list

def load_list_goalscorers(control):
    maria = controller.load_goalscorers(control, "football/goalscorers-utf8-small.csv")
    maria_list = controller.list_goalscorers(maria)
    
    return maria_list

def load_list_shootouts(control):
    ian = controller.load_shootouts(control, "football/shootouts-utf8-small.csv" ) 
    ian_list = controller.list_shootouts(ian)

    return ian_list

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,n_partidos, equipo, condicion):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    results, deltatime =controller.req_1(control,n_partidos, equipo, condicion) 
    if len(results) > 6:
        tablita = results[:3] + results[-3:]
        results_1 = tabulate(tablita,headers="keys",tablefmt = 'grid')
    else:
        results_1 = tabulate(results,headers="keys",tablefmt = 'grid')
    print("Selecting "+ str(len(results)) + "Matches...")
    print(results_1, "Tiempo de ejecuacion: " + str(round(deltatime,2)))

def print_req_2(control, n_goles, jugador):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    goalscorers, deltatime = controller.req_2(control, n_goles, jugador) 
    if len(goalscorers) > 6:
        tabla = goalscorers[:3] + goalscorers[-3:]
        goalscorers_1 = tabulate(tabla, headers ="keys", tablefmt = "grid")
    else:
        goalscorers_1 = tabulate(goalscorers, headers ="keys", tablefmt = "grid")
    print("Selectings"+ str(len(goalscorers)) + "scorers...")    
    print(goalscorers_1, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_3(control, equipo, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    req_3,local, visitante, deltatime = controller.req_3(control, equipo, fecha_i, fecha_f)
    if len(req_3) > 6:
        resultado = req_3[:3] + req_3[-3:]
        resp = tabulate(resultado, headers = "keys", tablefmt = "grid")
    else:
        resp = tabulate(req_3, headers = "keys", tablefmt = "grid")
    print(equipo + "total matches: " + str(len(req_3)))
    print(equipo + "total home games: " + str(local))
    print(equipo + "total away games: " + str(visitante ))
    print(resp, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_4(control,torneo,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    tournament, paises, ciudades, penales, deltatime = controller.req_4(control,torneo,fecha_i,fecha_f)
    if len(tournament) > 6:
        reducida = tournament[:3] + tournament[-3:]
        tournament_p = tabulate(reducida, headers ="keys", tablefmt = "grid")
    else:
        tournament_p = tabulate(tournament, headers ="keys", tablefmt = "grid")
    print(torneo + "Total matches: " + str(len(tournament)))
    print(torneo + "Total countries: " + str(paises))
    print(torneo + "Total cities: " + str(ciudades))
    print(torneo + "Total shootouts: " + str(penales))
    print(tournament_p, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_5(control,nom_player, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    results, torneos, penales, autogoles, deltatime =controller.req_5(control,nom_player, fecha_i, fecha_f) 
    if len(results) > 6:
        tablita = results[:3] + results[-3:]
        results_1 = tabulate(tablita,headers="keys",tablefmt = 'grid')
    else:
       results_1 = tabulate(results,headers="keys",tablefmt = 'grid')
    print(nom_player + "Total goals: " + str(len(results)))
    print(nom_player + "Total tournaments" + str(torneos))
    print(nom_player + "Total penalties" + str(penales))
    print(nom_player + "Total autogoals" + str(autogoles))
    print(results_1, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_6(control,n_equipos,torneo,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    paises, partidos, ciudades, mejor, deltatime = controller.req_6(control,n_equipos,torneo,fecha_i,fecha_f)
    for pais in paises:
        tab = tabulate([pais["Top Scorer"]],headers ="keys", tablefmt = "grid")
        pais["Top Scorer"] = tab
    if len(paises) > 6:
        nueva = paises[:3] + paises[-3:]
        paises_1 = tabulate(nueva, headers ="keys", tablefmt = "grid")
    else:
        paises_1 = tabulate(paises, headers ="keys", tablefmt = "grid")
    print(torneo + "Total teams: " + str(len(paises)))
    print(torneo + "Total matches: " + str(partidos))
    print(torneo + "Total countries: " + str(len(paises)))
    print(torneo + "Total cities: " + str(ciudades))
    print(torneo + "City with most matches: " + mejor)
    print(paises_1, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_7(control,n_jugadores,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    jugadores, total_players, partidos, goles, penaltis, autogoles, deltatime = controller.req_7(control,n_jugadores,fecha_i,fecha_f)
    # for jugador in jugadores:
    #     tab = tabulate([jugador["last_goal"]],headers ="keys", tablefmt = "grid")
    #     jugador["last_goal"] = tab
    if len(jugadores) > 6:
        nueva = jugadores[:3] + jugadores[-3:]
        jugadores_1 = tabulate(nueva, headers ="keys", tablefmt = "grid")
    else:
        jugadores_1 = tabulate(jugadores, headers ="keys", tablefmt = "grid")
    print("Official tournaments total players: " + str(total_players))
    print("Official tournaments total matches: " + str(partidos))
    print("Official tournaments total goals: " + str(goles))
    print("Official tournaments total penalties: " + str(penaltis))
    print("Official tournaments total autogoals: " + str(autogoles))
    print(jugadores_1, "Tiempo de ejecuacion: " + str(round(deltatime,2)))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def print_sort_results(control,size,ordenamiento):
    
    print(controller.sort(control,size,ordenamiento))
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
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            print("-"*40)
            
            data_results = load_list_results(control)
            data_goals = load_list_goalscorers(control)
            data_shootouts = load_list_shootouts(control)

            print("Match result count: " + str(len(data_results)-1))
            print("Goal scorers count: " + str(len(data_goals)-1))
            print("shootout-penalty definition count:" + str(len(data_shootouts)-1))

            
            tabla_res = data_results[:4] + data_results[-3:]
            tabla_gol = data_goals[:4] + data_goals[-3:]
            tabla_shoot = data_shootouts[:4] + data_shootouts[-3:]
            
            tabla_results_1 = tabulate(tabla_res,headers = 'firstrow',tablefmt = 'grid')
            tabla_goals_primeros = tabulate(tabla_gol,headers = 'firstrow',tablefmt = 'grid')
            tabla_shootouts_1 = tabulate(tabla_shoot, headers = 'firstrow', tablefmt = 'grid')
            
            print("-"*40)
            print("="*45)
            print("============ FIFA RECORDS REPORT ============")
            print("="*45)
            print("Printing results for the first 3 and last 3 records on file.")
            print("\n ---- MATCH RESULTS ----")
            print("    Total match results: " + str(len(data_results)-1))
            print("Results struct has more than 6 records...")
            print(tabla_results_1)
            print ("---- GOAL SCORERS ----")
            print("     Total goal scorers: " + str(len(data_goals)-1))
            print("Goal scorers struct has more than 6 records...")
            print(tabla_goals_primeros)
            print("---- SHOOTOUTS ----")
            print("     Total shootouts: " + str(len(data_shootouts)-1))
            print("Shootouts struct has more than 6 records...")
            print (tabla_shootouts_1)
            
            
            
        elif int(inputs) == 2:
            n_partidos = int(input("Ingrese el numero de partidos que quiere consultar: "))
            equipo = input("Ingrese el equipo que quiere consultar: ")
            condicion = input("Ingrese la condicion del equipo consultado Local, Visitante, o Indiferente: ")
            print_req_1(control, n_partidos, equipo, condicion)

        elif int(inputs) == 3:
            n_goles = int(input("ingrese el numero de goles que quiere consultar: "))
            jugador = input("ingrese el nombre completo del jugador: ")
            print_req_2(control, n_goles, jugador)

        elif int(inputs) == 4:
            equipo = input("Ingrese el equipo que quiere consultar: ")
            fecha_i = input("Ingrese la fecha inicial del periodo a consultar: ")
            fecha_f = input("Ingrese la fecha final del periodo a consultar: ")

            print_req_3(control, equipo, fecha_i, fecha_f)

        elif int(inputs) == 5:
            torneo = input("Indique el nombre del torneo que quiere consultar: ")
            fecha_i = input("Ingrese la fecha inicial del periodo a consultar: ")
            fecha_f = input("Ingrese la fecha final del periodo a consultar:")
            print_req_4(control,torneo,fecha_i,fecha_f)
            

        elif int(inputs) == 6:
            nom_player = input("ingrese el nombre del anotador: ")
            fecha_i = input("ingrese la fecha del periodo inicial a consultar: ")
            fecha_f = input("ingrese la fecha del periodo final a consultar: ")

            print_req_5(control, nom_player, fecha_i, fecha_f)

        elif int(inputs) == 7:
            n_equipos = int(input("Ingrese el numero de equipos que quiere consultar: "))
            torneo = input("Ingrese el nombre del torneo que quiere consultar: ")
            fecha_i = input("Ingrese la fecha inicial del periodo a consultar: ")
            fecha_f = input("Ingrese la fecha final del periodo a consultar: ")
            print_req_6(control,n_equipos,torneo,fecha_i,fecha_f)

        elif int(inputs) == 8:
            n_jugadores = int(input("Ingrese el numero de jugadores que quiere consultar: "))
            fecha_i = input("Ingrese la fecha inicial del periodo a consultar: ")
            fecha_f = input("Ingrese la fecha final del periodo a consultar: ")
            print_req_7(control, n_jugadores, fecha_i, fecha_f)

        elif int(inputs) == 9:
            print_req_8(control)
            
        elif int(inputs) == 10:
            size = int(input("Indique el tamaño de la muestra: "))
            ordenamiento = input("Escriba 1 para Selection, 2 para Insertion o 3 para Shell, para indicar el tipo de ordenamiento: ")
            result = controller.sort(control,size, ordenamiento)
            delta_time = f"{result[0]:.3f}"
            sorted_list = result[1]
            
            print_sort_results(control,size,ordenamiento)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
