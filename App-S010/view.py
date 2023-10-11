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
import traceback
from prettytable import PrettyTable, ALL
import threading


default_limit = 1000
sys.setrecursionlimit(default_limit*100)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_lista="ARRAY_LIST"):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_lista)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los partidos de un equipo")
    print("3- Listar los primeros goles anotados por un jugador")
    print("4- Consultar los partidos que disputo un equipo en un periodo de tiempo")
    print("5- Consultar los partidos en un torneo durante un periodo de tiempo")
    print("6- Consultar anotaciones de un jugador en un periodo de tiempo")
    print("7- Clasificar los mejores equipos de un torneo en un periodo")
    print("8- Clasificar los mejores anotadores en partidos oficiales en un periodo")
    print("9- Seleccionar el tipo de lista y el tipo de ordenamiento")
    print("10- Cambiar tipo de algoritmos (recursivos o iterativos)")
    print("0- Salir")
#pretty table
def printSimpleTable(tableList, keys):
    """
    Función encargada de mostrar los datos en tablas
    """
    table = PrettyTable()
    table.max_width = 20
    table.hrules =ALL
    table.field_names = keys
    lines = []
    for element in lt.iterator(tableList):
        line = []
        for key in keys:
            stringE = str(element[key])
            if len(stringE) > 20:
                stringE = stringE[:20]
            line.append(stringE)
        lines.append(line)
    table.add_rows(lines)
    print(table)
def load_data_s_r(control, sample_option):
    """
    Carga los datos desde las funciones de carga de datos y devuelve las listas.
    """

    goal_score_count = controller.loadGoalscorers1(control, sample_option)
    result_count = controller.loadResults1(control, sample_option)
    shootout_count = controller.loadShootouts1(control, sample_option)
    
    return goal_score_count, result_count, shootout_count
def sortData(control, ordenamiento):
    time = controller.sortData(control, ordenamiento)
    return time
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass
# req 2
def print_first_n_goals_by_player(total_goals, player_goals):
    """Muestra los goles del jugador usando printSimpleTable

    Args:
        total_goals (int): Total de goles
        player_goals (int): Total de goles por jugador
    """
    
    print(f"Total de goles anotados por el jugador: {total_goals}\n")
    print("Detalles de los goles:")
    
    if total_goals > 0:
        keys = ['date', 'home_team', 'away_team', 'scorer', 'minute', 'penalty', 'own_goal']

        

        if total_goals > 6:
            player_goals = controller.sixdata(player_goals)
         
        printSimpleTable(player_goals,keys)
         
    else:
        print("No se encontraron goles para el jugador especificado.")



def print_games_over_a_period_of_time(total_games, total_home_games, total_away_games, games_played):
    """ Función que imprime los partidos, en un periodo de tiempo específico

    Args:
        total_games (int): Número total de partidos
        total_home_games (int): Número de partidos jugados como local
        total_away_games (int): Número de partidos jugados como visitante
    """
    print(f"\nTotal de partidos jugados por el equipo: {total_games}")
    print(f"Total de partidos jugados por el equipo como local: {total_home_games}")
    print(f"Total de partidos jugados por el equipo como visitante: {total_away_games}")     
    print("Detalles de los goles:")
    
    if total_games > 0:
        keys = ['date','home_team','away_team','country','city','tournament', 'penalty','own_goal']

        

        if total_games > 6:
            games_played = controller.sixdata(games_played)
         
        printSimpleTable(games_played,keys)
         
    else:
        print("No se encontraron goles para el jugador especificado.")

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4


#req 5
def print_annotations_over_a_period_of_time(total_goals, total_tournaments, penalties, own_goals, player_goals):
    """ Función que imprime las anotaciones, en un periodo de tiempo específico

    Args:
        total_goals (int): Número total de goles 
        total_tournaments (int): Número de torneos en los que se hicieron los goles
        penalties (int): Número de goles que fueron hechos en penalties
        own_goals (int): Número de goles que fueron autogol
        player_goals (list): Lista de los goles del jugador.
    """
    print(f"\nTotal de goles anotados por el jugador: {total_goals}")
    print(f"Total de torneos: {total_tournaments}")
    print(f"Total de penalties: {penalties}")   
    print(f"Total de autogoles: {own_goals}")   
    print("Detalles de los goles:")
    
    if total_goals > 0:
        keys = ['date', 'home_team', 'away_team', 'scorer', 'minute', 'penalty', 'own_goal', 'tournament']

        

        if total_goals > 6:
            player_goals = controller.sixdata(player_goals)
         
        printSimpleTable(player_goals,keys)
         
    else:
        print("No se encontraron goles para el jugador especificado.")


def print_consultar_anotaciones_jugador_periodo(torneo_nombre, total_equipos, total_encuentros, total_paises, total_ciudades, ciudad_mas_partidos, equipos_clasificados):
    print(f"\n{torneo_nombre} Total de equipos: {total_equipos}")
    print(f"{torneo_nombre} Total de encuentros: {total_encuentros}")
    print(f"{torneo_nombre} Total de paises: {total_paises}")
    print(f"{torneo_nombre} Total de ciudades: {total_ciudades}") 
    print(f"{torneo_nombre} Ciudad con más partidos: {ciudad_mas_partidos}") 
    print("Detalles de los goles:")

    if total_encuentros > 0:
        keys = ['nombre_equipo', 'total_puntos', 'diferencia_goles', 'partidos_disputados', 'puntos_penal', 'puntos_autogol', 'victorias', 'derrotas', 'empates', 'goles_obtenidos', 'goles_recibidos', 'max_goleador']

        if total_encuentros > 6:
            equipos_clasificados = controller.sixdata(equipos_clasificados)

        # Crear una tabla para los equipos clasificados
        equipos_table = PrettyTable()
        equipos_table.field_names = keys
        equipos_table.horizontal_char = '-'
        equipos_table.hrules =ALL
        equipos_table.field_names = keys
        # Recorrer los equipos clasificados y agregarlos a la tabla
        for equipo in lt.iterator(equipos_clasificados):
            max_goleador_data = equipo['max_goleador']  # Obtener los datos del máximo goleador
            max_goleador_table = PrettyTable()  # Crear una tabla para el máximo goleador
            max_goleador_keys = ['nombre_jugador', 'goles_anotados', 'partidos_anotados', 'promedio_tiempo']
            
            # Agregar los datos del máximo goleador a la tabla del máximo goleador
            max_goleador_table.field_names = max_goleador_keys
            max_goleador_table.add_row([max_goleador_data.get(key, '') for key in max_goleador_keys])
            
            # Agregar una fila en la tabla de equipos con la tabla del máximo goleador
            equipo_data = [equipo[key] if key != 'max_goleador' else str(max_goleador_table) for key in keys]
            equipos_table.add_row(equipo_data)
            
        # Imprimir la tabla de equipos clasificados
        print(equipos_table)
    else:
        print("No se encontraron goles para el jugador especificado.")


 #REQ 7   


def print_clasificar_anotadores(total_anotadores, total_partidos, total_torneos, total_goles, total_goles_penal, total_autogoles, lista_anotadores):
    print("Clasificación de los mejores anotadores:")
    print(f"Total de anotadores encontrados: {total_anotadores}")
    print(f"Total de partidos en que participaron los anotadores: {total_partidos}")
    print(f"Total de torneos en que participaron los anotadores: {total_torneos}")
    print(f"Total de goles anotados durante el período: {total_goles}")
    print(f"Total de goles por penal anotados durante el período: {total_goles_penal}")
    print(f"Total de autogoles anotados durante el período: {total_autogoles}")

    if total_anotadores > 0:
        keys = [
                        'scorer',
                        'total_points',
                        'total_goals',
                        'penalty_goals',
                        'own_goals',
                        'avg_time (min)',
                        'total_tournaments',
                        'scored_in_wins',
                        'scored_in_loses',
                        'scored_in_draws',
                        'last_goal' 
        ]

        if  total_anotadores > 6:
            lista_anotadores = controller.sixdata(lista_anotadores)

        # Crear una tabla para los equipos clasificados
        equipos_table = PrettyTable()
        equipos_table.field_names = keys
        equipos_table.horizontal_char = '-'
        equipos_table.hrules =ALL
        equipos_table.field_names = keys
        # Recorrer los equipos clasificados y agregarlos a la tabla

        for equipo in lt.iterator(lista_anotadores):
            last_goal_data = equipo['last_goal']  
            last_goal_table = PrettyTable()  # Crear una tabla para el máximo goleador
            last_goal_keys = ['date',
                        'tournament',
                       'home_team',
                       'away_team',
                        'home_score',
                        'away_score',
                        'minute',
                        'penalty',
                        'own_goal']
            
            # Agregar los datos del máximo goleador a la tabla del máximo goleador
            last_goal_table.field_names = last_goal_keys
            last_goal_table.add_row([last_goal_data.get(key, '') for key in last_goal_keys])
            
            # Agregar una fila en la tabla de equipos con la tabla del máximo goleador
            equipo_data = [equipo[key] if key != 'last_goal' else str(last_goal_table) for key in keys]
            equipos_table.add_row(equipo_data)
            
        # Imprimir la tabla de equipos clasificados
        print(equipos_table)
    else:
        print("No se encontraron goles para el jugador especificado.")


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista

bool_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")
control = new_controller()

def menu_cycle():

    """
    Menu principal
    """
    working = True
    # configurando si usa algoritmos recursivos
    rec = True
    #ciclo del menu
    control = new_controller()
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
                        
            tipo_lista = "ARRAY_LIST"
            sample_option = input("Selecciona el tamaño de muestra (-5pct, -20pct, -30pct, -50pct, -large): ")
            load_data_s_r(control, sample_option)
 

            print(f"Tamaño de muestra seleccionado: {len(sample_option)}")
            print('Match result count: ' + str(lt.size(control['model']['results'])))
            print('Goal scorers count: ' + str(lt.size(control['model']['goalscore'])))
            print('shootout-penalty definition count: ' + str(lt.size(control['model']['shootouts'])))
            #--------------------MATCH RESULTS ----------------------
            print("--------------------MATCH RESULTS --------------------")
            sixResults =controller.sixdata(control['model']['results'])
            printSimpleTable(sixResults, ['date','home_team','away_team','home_score','away_score','country','city','tournament'])
           # -----------GOAL SCORES-----------------------------
            print("-------------------GOAL SCORES-----------------------------")
            sixgoals = controller.sixdata(control['model']['goalscore'])
            printSimpleTable(sixgoals,['date','home_team','away_team','scorer','team','minute','penalty','own_goal'])
            # ------------------- SHOOTOUS----------------------------------------------------------------
            print("----------------------SHOOTOUS-----------------------------")
            sixshoots = controller.sixdata(control['model']['shootouts'])
            printSimpleTable(sixshoots,['date','home_team','away_team','winner'])


        elif int(inputs) == 2:
            print("========================== Req No. 1 Inputs ===============")
            number_matchs =int( input("Ingrese el numero de partidos: "))
            name_team = input("Ingrese el nombre del Equipo: ")
            condition_team = input("Ingrese la condicion del equipo (local, visitante o indiferente): ")
            print("========================= Req No.1 Results ==================")
            total_matchs, time = controller.sortName(control['model']['results'], name_team, condition_team, number_matchs)
            printSimpleTable(total_matchs,['date','home_team','away_team','country','city','home_score','away_score'])
            print(" delta tiempo fue:", str(time))

        elif int(inputs) == 3:
            print("========================== Req No. 2 Inputs ===============")
            player_name = input("Ingrese el nombre del jugador: ")
            n = int(input("Ingrese el número de goles a mostrar: "))
            print("========================= Req No.2 Results ==================")
            time, total_goals, player_goals = controller.get_first_n_goals_by_player(control, player_name, n, recursive=rec)

            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_first_n_goals_by_player(total_goals, player_goals)


                

        elif int(inputs) == 4:
            print("========================== Req No. 3 Inputs ===============")
            team_name = input("Ingrese el nombre del equipo: ")
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD):")
            fecha_fin = input("ingrese la fecha de fin (YYYY-MM-DD):")
            print("========================= Req No.3 Results ==================")
            time, total_games, total_home_games, total_away_games, games_played = controller.consulta_partidos_equipo_periodo(control, team_name,
                                                                                                          fecha_inicio, fecha_fin)
            print("Delta de tiempo fue:", str(time))
            print_games_over_a_period_of_time(total_games, total_home_games, total_away_games, games_played)

        elif int(inputs) == 5:
            """PConsultar los partidos relacionados
             con un torneo durante un
            periodo especifico."""
            name_tournament = input(" Ingrese el nombre del Torneo: ")
            start_date = input("Ingrese la fecha de inicio del periodo a consultar (YYYY-MM-DD): ")
            end_date = input("Ingrese la fecha de final del periodo a consultar (YYYY-MM-DD): ")
            matchs,total_coutries, total_cities, size , sizematches,time= controller.queryMatchsbyPeriod(name_tournament, start_date, end_date ,control['model']['shootouts'], control['model']['results'])
            print("========================== Req No. 4 Inputs ===============")
            print(f"tournament name : {name_tournament}")
            print(f"Start date: {start_date}")
            print(f"End date: {end_date}")
            print("========================== Req No. 4 Inputs ===============")
            print(f"{name_tournament} total matches: ",sizematches)
            print(f"{name_tournament} total countries: ",total_coutries)
            print(f"{name_tournament} total cities: ",total_cities)
            if size >= 6:
                print("\n the Tournament results has more than 6 records")
            else:
                print("\n the Tournament results has more than 6 records")
            printSimpleTable(matchs,['date','tournament','country','city','home_team','away_team','home_score','away_score','winner'])
            print("Delta de tiempo fue:", str(time))

        elif int(inputs) == 6:
            print("========================== Req No. 5 Inputs ===============")
            player_name = input("Ingrese el nombre del jugador: ")
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            
            print("========================= Req No.5 Results ==================")
            time, total_goals, total_tournaments, penalties, own_goals, player_goals = controller.consultar_anotaciones_jugador_periodo(
            control, player_name, fecha_inicio, fecha_fin, recursive=rec)

            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_annotations_over_a_period_of_time(total_goals, total_tournaments, penalties, own_goals, player_goals)

        elif int(inputs) == 7:
            print("========================== Req No. 6 Inputs ===============")
            torneo_nombre = input("Ingrese el nombre del torneo: ")
            N = int(input("Ingrese el número de partidos"))
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            
            print("========================= Req No.6 Results ==================")
            time, total_equipos, total_encuentros, total_paises, total_ciudades, ciudad_mas_partidos, equipos_clasificados= controller.consultar_mejores_equipos(
           control, N, torneo_nombre, fecha_inicio, fecha_fin)
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_consultar_anotaciones_jugador_periodo(torneo_nombre, total_equipos, total_encuentros, total_paises, total_ciudades, ciudad_mas_partidos, equipos_clasificados)


        elif int(inputs) == 8:
            print("========================== Req No. 7 Inputs ===============")
           
            N = int(input("Ingrese el número de partidos"))
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            
            print("========================= Req No.7 Results ==================")
            time, total_anotadores, total_partidos, total_torneos, total_goles, total_goles_penal,  total_autogoles, lista_anotadores= controller.clasificar_anotadores(
           control, N, fecha_inicio, fecha_fin)
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_clasificar_anotadores( total_anotadores, total_partidos, total_torneos, total_goles, total_goles_penal,  total_autogoles, lista_anotadores)



        elif int(inputs) == 9:
            tipo_lista = input("Qué tipo de lista deseas [ARRAY_LIST] o [SINGLE_LINKED]: ")
            if tipo_lista.upper() == "ARRAY_LIST" or tipo_lista.upper() == "SINGLE_LINKED":
             control = new_controller(tipo_lista)
             print(f"Los datos se han cargado como {tipo_lista}")
            else:
                print("Tipo de lista no válido. Se utilizará ARRAY_LIST por defecto.")
                control = new_controller("ARRAY_LIST")
            print(f"Tipo de lista actual: {tipo_lista}")
            load_data_s_r(control, sample_option)
            print("Seleccione el tipo de algoritmo de ordenamiento (Selection, Insertion o Shell):")
            ordenamiento = input().lower()
            a = sortData(control, ordenamiento )
            delta_time = f"{a}"
            
            print("Para", sample_option, "elementos, delta tiempo:", str(delta_time))
            #------------------------PRINT DATOS ORDENADOS---------------------
            print(f"Tamaño de muestra seleccionado: {lt.size(control['model']['results'])}")
            print('Match result count: ' + str(lt.size(control['model']['results'])))
            print('Goal scorers count: ' + str(lt.size(control['model']['goalscore'])))
            print('shootout-penalty definition count: ' + str(lt.size(control['model']['shootouts'])))
            #--------------------MATCH RESULTS ----------------------
            print("--------------------MATCH RESULTS --------------------")
            sixResults =controller.sixdata(control['model']['results'])
            printSimpleTable(sixResults, ['date','home_team','away_team','home_score','away_score','country','city','tournament'])
           # -----------GOAL SCORES-----------------------------

        elif int(inputs) == 10:
            # TODO modificar opcion 10 del menu en el lab 5 (parte 2)
            # configurar si usa algoritmos recursivos
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

if __name__ == "__main__":

    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
