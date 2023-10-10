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
import threading
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_Controller(list_type):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_Controller(list_type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1 : Listar los últimos N partidos de un equipo según su condición  ")
    print("3- Ejecutar Requerimiento 2 : Listar los primeros N goles anotados por un jugador")
    print("4- Ejecutar Requerimiento 3 : Consultar los partidos que disputó un equipo durante un periodo especifico ")
    print("5- Ejecutar Requerimiento 4 : Consultar los partidos relacionados con un torneo durante un periodo especifico ")
    print("6- Ejecutar Requerimiento 5 : Consultar las anotaciones de un jugador durante un periodo especifico ")
    print("7- Ejecutar Requerimiento 6 : Clasificar los N mejores equipos de un torneo en un periodo especifico ")
    print("8- Ejecutar Requerimiento 7 : Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo especifico ")
    print("9- Ejecutar Requerimiento 8 : Comparar el desempeño histórico de dos selecciones en torneos oficiales ")
    print("10- Cambiar tipo de algoritmos (recursivos o iterativos)")
    print("0- Salir")
    
def new_table(data, headers, tablefmt):
    table = tabulate(data, headers, tablefmt)
    return table

"""
funciones que dan a elegir al usuario tanto el tipo de dato usado en las listas como el tamaño del archivo de carga 
selecciona listas diferentes a ARRAY_LIST genera un problema en la impresión de los datos
"""

def sel_algorithm():
    print('Seleccione el algoritmo a utilizar para ordenar:')
    print('Presione 0 si desea usar Insertion Sort')
    print('Presione 1 si desea usar Shell sort')
    print('Presione 2 si desea usar Selection sort')
    print('Presione 3 si desea usar Quick sort')
    print('Presione 4 si desea usar Merge sort')
    algorithm = int(input('Seleccione una opción para continuar\n'))
    if algorithm not in (0, 1, 2, 3, 4):
        print('Seleccione una opción correcta')
        return sel_algorithm()
    return algorithm

def selED():
    print('Selecciona el tipo de estructura de dato: ')
    print('Presione 0 si desea usar SINGLE_LINKED')
    print('Presione 1 si desea usar DOUBLE_LINKED')
    print('Presione 2 si desea usar ARRAY_LIST')
    
    inputs = input('Seleccione una opción para continuar\n')
    if inputs == '0':
        return 'SINGLE_LINKED'
    elif inputs == '1':
        return 'DOUBLE_LINKED'
    elif inputs == '2':
        return 'ARRAY_LIST'
    else:
        print('Opción no valida, vuelva a escribir')
        selED()   
        
def selTam():
    print('Selecciona el tamaño del archivo goalscorer: ')
    print('Presione 0 si desea usar 5-pct')
    print('Presione 1 si desea usar 10-pct')
    print('Presione 2 si desea usar 20-pct')
    print('Presione 3 si desea usar 30-pct')
    print('Presione 4 si desea usar 50-pct')
    print('Presione 5 si desea usar 80-pct')
    print('Presione 6 si desea usar -large')
    print('Presione 7 si desea usar -small')
    goalscorers_file_size = int(input('Seleccione una opción para continuar\n')) 
    print('Selecciona el tamaño del archivo results: ')
    print('Presione 0 si desea usar 5-pct')
    print('Presione 1 si desea usar 10-pct')
    print('Presione 2 si desea usar 20-pct')
    print('Presione 3 si desea usar 30-pct')
    print('Presione 4 si desea usar 50-pct')
    print('Presione 5 si desea usar 80-pct')
    print('Presione 6 si desea usar -large')
    print('Presione 7 si desea usar -small')
    results_file_size = int(input('Seleccione una opción para continuar\n'))
    print('Selecciona el tamaño del archivo shootouts: ')
    print('Presione 0 si desea usar 5-pct')
    print('Presione 1 si desea usar 10-pct')
    print('Presione 2 si desea usar 20-pct')
    print('Presione 3 si desea usar 30-pct')
    print('Presione 4 si desea usar 50-pct')
    print('Presione 5 si desea usar 80-pct')
    print('Presione 6 si desea usar -large')
    print('Presione 7 si desea usar -small')
    shootouts_file_size = int(input('Seleccione una opción para continuar\n')) 
    file_sizes = [goalscorers_file_size, shootouts_file_size, results_file_size]
    for index in range(0,3):
        if file_sizes[index] == 0:
            file_sizes[index] = "-5pct"
        elif file_sizes[index] == 1:
            file_sizes[index] = "-10pct"
        elif file_sizes[index] == 2:
            file_sizes[index] = "-20pct"
        elif file_sizes[index] == 3:
            file_sizes[index] = "-30pct"
        elif file_sizes[index] == 4:
            file_sizes[index] = "-50pct"
        elif file_sizes[index] == 5:
            file_sizes[index] = "-80pct"
        elif file_sizes[index] == 6:
            file_sizes[index] = "-large"
        elif file_sizes[index] == 7:
            file_sizes[index] = "-small"
        else:
            print("Seleccione opciones correctas")
            return selTam()
    return file_sizes
    
def load_data(control, sizes, algorithm):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    goalscorers, results, shootouts, goal_small_list, result_small_list, shoot_small_list, time1, time2, time3 = controller.load_data(control, sizes, algorithm)
    return goalscorers, results, shootouts, goal_small_list, result_small_list, shoot_small_list, time1, time2, time3

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
    team_name = input('Por favor escriba el nombre del equipo a consultar: ')
    num_matches = int(input('Por favor digite el número de partidos a consultar: '))
    print('Por favor seleccione la condición de el equipo en los partidos a consultar: ')
    print('[1] para partidos HOME')
    print('[2] para partidos AWAY')
    print('[3] para todos los partidos jugados')
    team_condition = int(input('Digite el número seleccionado: '))
    if team_condition == 1:
        team_condition = 'HOME'
    elif team_condition == 2:
        team_condition = 'AWAY'
    elif team_condition == 3:
        team_condition == 'ANY'
    else: 
        print('Seleccione una opción correcta')
        print_req_1(control)
    games_list, total_games, total_time = controller.req_1(control, num_matches, team_name, team_condition)
    if type(games_list) == type(None):
        print('Unknown')
    else:
        print("====================================REQ 1===================================")
        games_list_table = new_table(games_list, 'keys', 'grid')
        print (games_list_table)
        print('Se encontraron ' + str(total_games)+ ' partidos.')
        print('Se demoró ' + str(f"{total_time: .3f}") + ' milisegundos.')

def print_req_2(res):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    print('El jugador tiene un total de ' + str(res[1]) + ' goles. ')
    if lt.size(res[0]) <= 6:
        tabla = controller.makeTable2(res[0])
    else:
        n = lt.size(res[0])
        lista1 = lt.subList(res[0],1,3)
        lista2 = lt.subList(res[0],n-2,3)
        for i in lt.iterator(lista2):
            lt.addLast(lista1,i)
        tabla = controller.makeTable2(lista1)
        
    print(tabulate(tabla))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    team_name = input("Ingrese el nombre del equipo: ")
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    result = controller.req_3(control, team_name, start_date, end_date)

    team_home_matches, team_away_matches, total_home_matches, total_away_matches = result

    if team_home_matches is None:
        print("No hay resultados disponibles para el equipo y el período de tiempo especificados.")
        return

    print(f"Total de partidos en casa para el equipo: {total_home_matches}")
    print(f"Total de partidos fuera de casa para el equipo: {total_away_matches}")
    
    print("\nPartidos en casa:")
    for match in lt.iterator(team_home_matches):
        print(f"Fecha: {match['date']}, Equipo Local: {match['home_team']}, Equipo Visitante: {match['away_team']}")
    
    print("\nPartidos fuera de casa:")
    for match in lt.iterator(team_away_matches):
        print(f"Fecha: {match['date']}, Equipo Local: {match['home_team']}, Equipo Visitante: {match['away_team']}")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    tournament_name = input('Por favor escriba el nombre del torneo que quiere consultar: ')
    start = input('Por favor escriba la fecha de inicio de consulta en formato YYYY-MM-DD: ')
    end = input('por favor escriba la fecha final de consulta en formato YYYY-MM-DD: ')
    print("====================================REQ 4===================================")
    print('Torneo a consultar: ' + tournament_name)
    print('Fecha inicio: ' + start)
    print('Fecha fin: ' + end)
    tournament_matches, total_matches, total_shootouts, total_countries, total_cities, tiempo_total = controller.req_4(control, tournament_name, start, end)
    if tournament_matches == None:
        print('Unknown')
    else:
        tournament_games_table = new_table(tournament_matches, 'keys', 'grid')
        print('Total matches: ' +str(total_matches))
        print('Total shootouts: ' + str(total_shootouts))
        print('Total cities: ' + str(total_cities))
        print('Total countries: ' + str(total_countries))
        print(tournament_games_table)
        print('Se demoró: ' + str(f"{tiempo_total: .3f}") + ' milisegundos')


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola.
    """
    tournament_name = input("Ingrese el nombre del torneo: ")
    start_date = input("Ingrese la fecha de inicio (en formato 'YYYY-MM-DD'): ")
    end_date = input("Ingrese la fecha de fin (en formato 'YYYY-MM-DD'): ")
    
    print(f"Resultado del Requerimiento 6 para el torneo '{tournament_name}' en el período del {start_date} al {end_date}:")



def print_req_7(res,n):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print('Total de anotadores en partidos oficiales: ' + str(lt.size(res[0])))
    print('Total de partidos oficiales: ' + str(lt.size(res[1])))
    print('Total de goles anotados en partidos oficiales: '+ str(lt.size(res[2])))
    print('Total de torneos oficiales: ' + str(lt.size(res[3])))
    print('Total de goles de penal anotados en partidos oficiales: '+ str(res[4]))
    print('Total de autogoles anotados en partidos oficiales: '+ str(res[5]))
    
    if n >= lt.size(res[0]):
        tabla = controller.makeTable(res[0])
    else:
        tabla = controller.makeTable(lt.subList(res[0],1,n))
        
    print(tabulate(tabla,maxcolwidths=[9,9,9,9,9,9,9,9,9,9,None],tablefmt="grid"))

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    first_team = input('Por favor escriba el nombre del primer equipo: ')
    second_team = input('Por favor escriba el nombre del segundo equipo: ')
    start = input('Por favor escriba la fecha de inicio en YYYY-MM-DD: ')
    end = input('Por favor escriba la fecha final en YYYY-MM-DD: ')
    print("====================================REQ 8===================================")
    first_team_last_match, first_team_yearly_stats, second_team_last_match, second_team_yearly_stats = controller.req_8(control, first_team, second_team, start, end)
    first_last_match_table = new_table(first_team_last_match, 'keys', 'grid')
    second_last_match_table = new_table(second_team_last_match, 'keys', 'grid')
    first_yearly_table = new_table(first_team_yearly_stats, 'keys', 'grid')
    second_yearly_table = new_table(second_team_yearly_stats, 'keys', 'grid')
    print(first_last_match_table)
    print(second_last_match_table)
    print(first_yearly_table)
    print(second_yearly_table)



# Se crea el controlador asociado a la vista
list_type = selED()
sizes = selTam()
algorithm = sel_algorithm()
control = new_Controller(list_type)

bool_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

def main_cycle():
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            goalscorers_size, results_size, shootouts_size, goalscorers_small_list, results_small_list, shootouts_small_list, time1, time2, time3 = load_data(control, sizes, algorithm)
          
            results_table = new_table(results_small_list, 'keys', 'grid')
            goalscorers_table = new_table(goalscorers_small_list, 'keys', 'grid')
            shootouts_table = new_table(shootouts_small_list, 'keys', 'grid')
            
            print('Goalscorers cargados: ' + str(goalscorers_size))
            print(goalscorers_table)
            print('Resultados cargados: ' + str(results_size))
            print(results_table)
            print('Shootouts cargados: ' + str(shootouts_size))
            print(shootouts_table)
            
            tiempo_t = time1 + time2 + time3
            time1 = f"{time1:.3f}"
            time2 = f"{time2:.3f}"
            time3 = f"{time3:.3f}"
            time = f"{tiempo_t:.3f}"
            
            print('Se demoró ' + str(time1) + ' ordenando los jugadores.')
            print('Se demoró ' + str(time2) + ' ordenando los resultados.')
            print('Se demoró ' + str(time3) + ' ordenando los penales.')
            
            print('El tiempo total es ' + str(time))
                
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            nombre = input('Ingrese el nombre del jugador a consultar: ')
            numero = int(input('ingrese el numero de goles a consultar: '))
            res, tiempo_total = controller.req_2(control,nombre,numero,list_type,algorithm)
            print('Se demoró: ' + str(f"{tiempo_total: .3f}") + ' milisegundos')
            print_req_2(res)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            player = input('Escriba el nombre del jugador. ')
            fechasin = input('Ingrese la fecha inicial en formato AAAA-MM-DD: ')
            fechasfin = input('Ingrese la fecha final en formato AAAA-MM-DD: ') 
            res,tiempo_total = controller.req_5(control,player,fechasin,fechasfin,list_type,algorithm)
            print('Se demoró: ' + str(f"{tiempo_total: .3f}") + ' milisegundos')

            if res == None:
                 print('No se encontraron goles en el rango de fechas solicitadas.')
                 return None
            else:
                print('El jugador ' + player + ' anotó ' + str(lt.size(res[4])) + ' goles en el periodo de tiempo solicitado. ')
                print('El total de autogoles es ' + str(res[1])) 
                print('El total de goles de penales es ' + str(res[0]))
                print('El total de torneos donde el jugador anotó goles es ' + str(lt.size(res[3])))
                
                results_table = controller.getUpDown(res[2],res[4])   
               
                print(tabulate(results_table,headers ="firstrow"))
                
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            fechasin = input('Ingrese la fecha inicial en formato AAAA-MM-DD: ')
            fechasfin = input('Ingrese la fecha final en formato AAAA-MM-DD: ')  
            n = int(input('Ingrese el número de jugadores a consultar: '))
            res,tiempo_total = controller.req_7(control,fechasin,fechasfin,list_type,algorithm)
            print('Se demoró: ' + str(f"{tiempo_total: .3f}") + ' milisegundos')

            if res == None:
                print('No se encontraron goles en el rango de fechas solicitadas.')
                return None
            
            print_req_7(res,n)

        elif int(inputs) == 9:
            print_req_8(control)
            
        elif int(inputs) == 10:
            rec = input("Usar algoritmos recursivos? (S/N): ")
            if rec in bool_lt_opt:
                rec = True
            else:
                rec = False

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=main_cycle)
    thread.start()