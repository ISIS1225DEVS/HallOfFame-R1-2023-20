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
import model
import time
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_Controller(list_type):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_Catalog(list_type)
    return control


# Funciones para la carga de datos

def load_data(control, sizes, algorithm):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog = control['model']
    goalscorers_size, tiempo_total1 = loadGoalscorers(catalog, sizes, algorithm)
    results_size, tiempo_total2 = loadResults(catalog, sizes, algorithm)
    shootouts_size, tiempo_total3 = loadShootouts(catalog, sizes, algorithm)
    top_bottom_goalscorers = get_sublist_top_and_bottom(catalog, 3, goalscorers_size, 'goalscorers')
    top_bottom_results = get_sublist_top_and_bottom(catalog, 3, results_size, 'results')
    top_bottom_shootouts = get_sublist_top_and_bottom(catalog, 3, shootouts_size, 'shootouts')
    return goalscorers_size, results_size, shootouts_size, top_bottom_goalscorers, top_bottom_results, top_bottom_shootouts, tiempo_total1, tiempo_total2,tiempo_total3

def loadGoalscorers(catalog, sizes, algorithm):
    size = sizes[0]
    goalscorers_file = cf.data_dir + 'football/goalscorers-utf8'+size+'.csv'
    input_file = csv.DictReader(open(goalscorers_file, encoding='utf-8'))
    for tag in input_file:
        model.add_goalscorer(catalog, tag)
    tiempo_inicial = get_time()
    sortGoalscorers(catalog, algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return model.goalscorersSize(catalog), tiempo_total

def loadResults(catalog, sizes, algorithm):
    size = sizes[2]
    results_file = cf.data_dir + 'football/results-utf8'+size+'.csv'
    input_file = csv.DictReader(open(results_file, encoding='utf-8'))
    for tag in input_file:
        model.add_results(catalog, tag)
    tiempo_inicial = get_time()
    sortResults(catalog, algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return model.resultsSize(catalog), tiempo_total

def loadShootouts(catalog, sizes, algorithm):
    size = sizes[1]
    shootouts_file = cf.data_dir + 'football/shootouts-utf8'+size+'.csv'
    input_file = csv.DictReader(open(shootouts_file, encoding='utf-8'))
    for tag in input_file:
        model.add_shootouts(catalog, tag)
    tiempo_inicial = get_time()
    sortShootouts(catalog, algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return model.shootoutsSize(catalog), tiempo_total

def get_sublist_top_and_bottom(catalog, numElem, size, id):
    top_list = get_sublist(catalog, 1, numElem, id)
    bottom_list = get_sublist(catalog, size - (numElem - 1), numElem, id)
    return top_list['elements'] + bottom_list['elements']

# Funciones de ordenamiento

def sortGoalscorers(catalog,algorithm):
    """
    llama función de ordenamiento de goalscorers en el model
    """
    return model.sortGoalscorers(catalog,algorithm)
 
def sortResults(catalog, algorithm):
    """
    llama función de ordenamiento de results en el model
    """
    return model.sortResults(catalog, algorithm)
    
def sortShootouts(catalog, algorithm):
    """
    llama función de ordenamiento de shootouts en el model
    """
    return model.sortShootouts(catalog, algorithm)

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control, id)
    return data

def get_sublist(catalog, pos, numelem, id):
    return model.get_sublist(catalog, pos, numelem, id)

def getUpDown(encuentros,goles):
    return model.getUpDown(encuentros,goles)

def makeTable(jugadores):
    return model.makeTable(jugadores)

def makeTable2(goles):
    return model.makeTable2(goles)

def req_1(control, num_matches, team_name, team_condition):
    """
    Retorna el resultado del requerimiento 1
    """
    tiempo_inicio = get_time()
    team_matches, total_matches = model.req_1(control['model'], num_matches, team_name, team_condition)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicio, tiempo_final)
    if total_matches == 0:
        return None
    if total_matches > 6:
        matches = get_sublist_6elements(team_matches, total_matches)
        return matches, total_matches, tiempo_total
    else:
        matches = team_matches['elements']
        return matches, total_matches, tiempo_total
    


def req_2(control,nombre,numero,list_type,algorithm):
    """
    Retorna el resultado del requerimiento 2
    """
    tiempo_inicio = get_time()
    res = model.req_2(control,nombre,numero,list_type,algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicio, tiempo_final)

    return res,tiempo_total

def req_3(control, team_name, start_date, end_date):
    """
    Retorna el resultado del requerimiento 3
    """
    return model.req_3(control['model'], team_name, start_date, end_date)



def req_4(control, tournament_name, start, end):
    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicio = get_time()
    tournament_matches, total_matches, total_shootouts, total_countries, total_cities = model.req_4(control['model'], tournament_name, start, end)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicio, tiempo_final)
    if tournament_matches == None:
        return tournament_matches, total_matches, total_shootouts, total_countries, total_cities, tiempo_total
    if total_matches > 6:
       top6 = get_sublist_6elements(tournament_matches, total_matches)
       return top6, total_matches, total_shootouts, total_countries, total_cities, tiempo_total
    return tournament_matches['elements'], total_matches, total_shootouts, total_countries, total_cities, tiempo_total

        
def get_sublist_6elements(data, size):
        top = model.get_sublist_data(data, 1, 3)
        bottom = model.get_sublist_data(data, size - 4, 3)
        return top['elements'] + bottom['elements']

def req_5(control,player,fechain,fechafin,list_type,algorithm):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    tiempo_inicio = get_time()
    salida = model.req_5(control,player,fechain,fechafin,list_type,algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicio, tiempo_final)
    return salida,tiempo_total

def req_6(control):
    """
    Retorna el resultado del requerimiento 6.
    """
    catalog = control['catalog']
    tournament_name = control['tournament_name']
    start_date = control['start_date']
    end_date = control['end_date']
    num_teams = control['num_teams']
    result = req_6(catalog, tournament_name, start_date, end_date, num_teams)

    return result


def req_7(control,fechain,fechafin,list_type,algorithm):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    tiempo_inicio = get_time()
    salida = model.req_7(control,fechain,fechafin,list_type,algorithm)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicio, tiempo_final)
    return salida,tiempo_total

def req_8(control, first_team, second_team, start, end):
    """
    ARGS: Control, nombre primer equipo, nombre segundo equipo, fecha inicio, fecha fin en ISO
    RET: 
    - partido más reciente de primer equipo
    - información relevante para primer equipo
        listado de estadísticas
        jugador con más anotaciones en el año
    - partido más reciente de segundo equipo
    - lista de información relevante para segundo equipo
    - información de comparación entre dos equipos
    - listado de anotaciones en encuentro más reciente
    """
    # TODO: Modificar el requerimiento 8
    
    first_team_last_match = model.req_1(control['model'], 1, first_team, 'BOTH')
    second_team_last_match = model.req_1(control['model'], 1, second_team, 'BOTH')
    date_ranges = model.determine_years_for_statistic(start, end)
    print(date_ranges)
    first_team_yearly_stats = model.determine_yearly_statistics(control['model'], date_ranges, first_team)
    print(first_team_yearly_stats)
    second_team_yearly_stats = model.determine_yearly_statistics(control['model'], date_ranges, second_team)
    print(second_team_yearly_stats)
    
    return first_team_last_match, first_team_yearly_stats['elements'], second_team_last_match, second_team_yearly_stats['elements']



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