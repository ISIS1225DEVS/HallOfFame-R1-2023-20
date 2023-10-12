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


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos
def load_data(control):
    fifa = control['model']
    results = load_results(fifa)
    goalscorers = load_goalscorers(fifa)
    shootouts = load_shootouts(fifa)
    
    return results, goalscorers, shootouts

def load_results(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    results_file = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))
    for result in input_file:
        model.add_data_results(control, result)
    return control 

def load_goalscorers(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    goalscorers_file = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))
    for goal in input_file:
        model.add_data_goalscorers(control, goal)
    return control 

def load_shootouts(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    shootouts_file = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))
    for outs in input_file:
        model.add_data_shootouts(control, outs)
    return control 


# Funciones de ordenamiento

def list_results(control):
    results = control['model']['results']['elements']
    lista_results = []  
    headers = ['date','home_team','away_team','home_score','away_score','tournament','city','country','neutral']
    lista_results.append(headers)
    for result in results:
        new_line = []
        for llave in result:
            new_line.append(result[llave])
        lista_results.append(new_line)
    lista_results.sort(reverse=True)
    return lista_results

def list_goalscorers(control):
    goalscorers = control['model']['goalscorers']['elements']
    lista_goals = []  
    headers = ['date','home_team','away_team','team','scorer','minute','own_goal','penalty']
    lista_goals.append(headers)
    for goal in goalscorers:
        new_line = []
        for llave in goal:
            new_line.append(goal[llave])
        lista_goals.append(new_line)
    lista_goals.sort(reverse=True)
    return lista_goals
              
def list_shootouts(control):
    shootouts = control['model']['shootouts']['elements']
    lista_shootouts = []
    headers = ['date', 'home_team', 'away_team', 'winner']
    lista_shootouts.append(headers)
    for outs in shootouts:
        new_line = []
        for llave in outs:
            new_line.append(outs[llave])
        lista_shootouts.append(new_line)
    lista_shootouts.sort(reverse=True)
    return lista_shootouts
        
def sort(control, size, ordenamiento):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    if ordenamiento == "3":
        sorted_list = model.sort_fifa_shell(control['model'],size)
    elif ordenamiento == "1":
        sorted_list = model.sort_fifa_selec(control['model'],size)
    elif ordenamiento == "2":
        sorted_list = model.sort_fifa_inser(control['model'],size)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    #TODO: Llamar la función del modelo para ordenar los datos
    return deltatime, sorted_list


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,n_partidos, equipo, condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    results = model.req_1(control["model"],n_partidos, equipo, condicion)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return results, deltatime


def req_2(control, n_goles, jugador):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    goalscorers = model.req_2(control["model"], n_goles, jugador)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return goalscorers, deltatime

def req_3(control, equipo, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    resultado, local, visitante = model.req_3(control["model"], equipo, fecha_i, fecha_f)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return resultado,local, visitante, deltatime


def req_4(control,torneo,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    tournament, paises, ciudades, penales = model.req_4(control["model"],torneo,fecha_i,fecha_f)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return tournament, paises, ciudades, penales, deltatime


def req_5(control,nom_player, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    results, torneos, penales, autogoles = model.req_5(control["model"],nom_player, fecha_i, fecha_f)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return results, torneos, penales, autogoles, deltatime

def req_6(control,n_equipos,torneo,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    paises, partidos, ciudades, mejor = model.req_6(control["model"],n_equipos,torneo,fecha_i,fecha_f)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return paises["elements"],partidos, ciudades, mejor, deltatime


def req_7(control,n_jugadores,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    mejores, total_players, partidos, goles, penaltis, autogoles  = model.req_7(control["model"],n_jugadores,fecha_i,fecha_f)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return mejores["elements"], total_players, partidos, goles, penaltis, autogoles, deltatime


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
