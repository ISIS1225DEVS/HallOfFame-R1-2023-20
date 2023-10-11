"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tipo_lista):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(tipo_lista)
    return control
    pass

# Funciones para la carga de datos

def load_data(control, tamaño):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    data = control['model']
    results = loadResults(data, tamaño)
    goal_scorers = loadscorers(data, tamaño)
    shootouts = loadshootouts(data, tamaño)
    return results, goal_scorers, shootouts 


def loadResults (data, tamaño):
    resultsfile = cf.data_dir + "football/results-utf8-"+ tamaño +".csv"
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    for result in input_file:
        model.add_results(data, result)
    return model.result_size(data)

def loadscorers (data, tamaño): 
    scoresfile = cf.data_dir + "football/goalscorers-utf8-"+ tamaño +".csv"
    input_file = csv.DictReader(open(scoresfile, encoding='utf-8'))
    for score in input_file:
        model.add_goal_scoreres(data, score)
    return model.goal_scorers_size(data)

def loadshootouts (data, tamaño):
    shootsfile = cf.data_dir + "football/shootouts-utf8-"+ tamaño +".csv"
    input_file = csv.DictReader (open(shootsfile, encoding="utf8"))
    for shoot in input_file:
        model.add_shootouts(data, shoot)
    return model.shootouts_size(data)
    
def sort_data (sorting, control):
    start = get_time()
    sorted_results = model.sort_results(sorting, control["results"])
    end = get_time()
    time_r = delta_time(start, end)

    start = get_time()
    sorted_goal_scorers = model.sort_scorers(sorting, control["goal_scorers"])
    end = get_time()
    time_g = delta_time(start, end)

    start = get_time()
    sorted_shootouts = model.sort_shootouts(sorting, control["shootouts"])
    end = get_time()
    time_s = delta_time(start, end)
    
    return time_r, time_g, time_s, sorted_results, sorted_goal_scorers, sorted_shootouts




# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, numero_partidos, equipo, condicion_equipo):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start = get_time()
    total_partidos, rta = model.req_1(control, numero_partidos, equipo, condicion_equipo)
    end = get_time()
    time = delta_time(start, end)
    return total_partidos, rta, time 


def req_2(control, number_goals, name_player):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start = get_time()
    final_scorer_goals, size_list, total_goals = model.req_2(control, number_goals, name_player)
    end = get_time()
    time = delta_time(start, end)
    return final_scorer_goals, size_list, total_goals, time


def req_3(control, team_name, inicial_date, final_date):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start = get_time()
    sorted_date, size_list, total_team_matches, total_home_team, total_away_team = model.req_3(control, team_name, inicial_date, final_date)
    end = get_time()
    time = delta_time(start, end)
    return sorted_date, size_list, total_team_matches, total_home_team, total_away_team, time


def req_4(control, torneo, lim_inf, lim_sup):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start = get_time()
    partidos_torneo, paises, ciudades, penales, rta  = model.req_4(control,torneo, lim_inf, lim_sup)
    end = get_time()
    time = delta_time(start, end)
    return partidos_torneo, paises, ciudades, penales, rta, time


def req_5(control, scorer, lim_inf, lim_sup):
    """
    Retorna el resultado del requerimiento 5
    """
    start = get_time()
    anotaciones, torneos, penales, autogoles, scorer_data = model.req_5(control, scorer, lim_inf, lim_sup)
    end = get_time()
    time = delta_time(start, end)
    return anotaciones, torneos, penales, autogoles, scorer_data, time

def req_6(control, numero_equipos, torneo, lim_inf, lim_sup):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start = get_time()
    teams, partidos_torneo, paises, ciudades, ciudad, rta= model.req_6(control,numero_equipos, torneo, lim_inf, lim_sup )
    end = get_time()
    time = delta_time(start, end)
    return teams, partidos_torneo, paises, ciudades, ciudad, rta, time


def req_7(control, top_scorers, inicial_date, final_date):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start = get_time()
    data_top_scorers, size_list, total_anotadores, total_partidos, total_torneos, total_goles_anotadores, total_penaltys, total_autogoles = model.req_7(control, top_scorers, inicial_date, final_date)
    end = get_time()
    time = delta_time(start, end)
    return data_top_scorers, size_list, total_anotadores, total_partidos, total_torneos, total_goles_anotadores, total_penaltys, total_autogoles, time


def req_8(control, team1, team2, lim_inf, lim_sup):
    """
    Retorna el resultado del requerimiento 8
    """
    start = get_time()
    years_1, partidos_1, local_1, visitante_1, oldest_match_1, ultimo_1, estadisticas_1, years_2, partidos_2, local_2, visitante_2, oldest_match_2, ultimo_2, estadisticas_2, encuentros, victorias_1, derrotas_1, victorias_2, derrotas_2, empates, ultimo_partido_1_2, anotaciones_ultimo = model.req_8(control, team1, team2, lim_inf, lim_sup)
    end = get_time()
    time = delta_time(start, end)
    return years_1, partidos_1, local_1, visitante_1, oldest_match_1, ultimo_1, estadisticas_1, years_2, partidos_2, local_2, visitante_2, oldest_match_2, ultimo_2, estadisticas_2, encuentros, victorias_1, derrotas_1, victorias_2, derrotas_2, empates, ultimo_partido_1_2, anotaciones_ultimo, time

# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
