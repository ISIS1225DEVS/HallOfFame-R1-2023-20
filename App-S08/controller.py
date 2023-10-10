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
import datetime
from DISClib.ADT import list as lt

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos

    data = control['model']
    start_time_matches = get_time()
    match = loadMatchResults(data)
    end_time_matches = get_time()
    start_time_scorers = get_time()
    goalscorers = loadGoalScorers(data)
    end_time_scorers = get_time()
    start_time_shootouts = get_time()
    shootouts = loadShootouts(data)
    end_time_shootouts = get_time()

    deltaTime_matches = delta_time(start_time_matches, end_time_matches)
    deltaTime_scorers = delta_time(start_time_scorers, end_time_scorers)
    deltaTime_shootouts = delta_time(start_time_shootouts, end_time_shootouts)

    sort(control)

    return match, goalscorers, shootouts, deltaTime_matches, deltaTime_scorers, deltaTime_shootouts


def loadMatchResults(data):

    resultsFile = cf.data_dir + 'football/results-utf8-large.csv'
    input_file = csv.DictReader(open(resultsFile, encoding='utf-8'))
    i=1
    for match in input_file:
        match['id'] = i
        i+=1
        if match['date'] == '' or match['date'] == ' ' or match['date'] == None:
            match['date'] == 'Unknown'
        else:
            match['date']=datetime.datetime.strptime(match['date'], '%Y-%m-%d')
        if match['home_team'] == '' or match['home_team'] == ' ' or match['home_team'] == None:
            match['home_team'] = 'Unknown'
        if match['away_team'] == ''or match['away_team'] == ' ' or match['away_team'] == None:
            match['away_team'] = 'Unknown'
        if match['home_score'] == '' or match['home_score'] == ' ' or match['home_score'] == None:
            match['home_score'] = -1
        else:
            match['home_score'] = int(match['home_score'])
        if match['away_score'] == '' or match['away_score'] == ' ' or match['away_score'] == None:
            match['away_score'] = -1
        else:
            match['away_score'] = int(match['away_score'])
        if match['tournament'] == '' or match['tournament'] == ' ' or match['tournament'] == None:
            match['tournament'] = 'Unknown'
        if match['city'] == '' or match['city'] == ' ' or match['city'] == None:
            match['city'] = 'Unknown'
        if match['country'] == '' or match['country'] == ' ' or match['country'] == None:
            match['country'] = 'Unknown'
        if match['neutral'] == '' or match['neutral'] == ' ' or match['neutral'] == None:
            match['neutral'] = 'Unknown'
        model.add_data(data, match)
    return model.data_size(data)[0]

def loadGoalScorers(data):

    goalscorersFile = cf.data_dir + "football/goalscorers-utf8-large.csv"
    input_file = csv.DictReader(open(goalscorersFile, encoding= "utf-8"))
    i=1
    for goalscorer in input_file:
        goalscorer['id']=i
        i+=1
        if goalscorer['date'] == '' or goalscorer['date'] == ' ' or goalscorer['date'] == None:
            goalscorer['date'] = 'Unknown'
        else:
            goalscorer['date']=datetime.datetime.strptime(goalscorer['date'], '%Y-%m-%d')
        if goalscorer['minute'] == '' or goalscorer['minute'] == ' ' or goalscorer['minute'] == None:
            goalscorer['minute'] = 200
        else:
            goalscorer['minute'] = float(goalscorer['minute'])
        if goalscorer['home_team'] == '' or goalscorer['home_team'] == ' ' or goalscorer['home_team'] == None:
            goalscorer['home_team'] = 'Unknown'
        if goalscorer['away_team'] == '' or goalscorer['away_team'] == ' ' or goalscorer['away_team'] == None:
            goalscorer['away_team'] = 'Unknown'
        if goalscorer['team'] == '' or goalscorer['team'] == ' ' or goalscorer['team'] == None:
            goalscorer['team'] = 'Unknown'
        if goalscorer['scorer'] == '' or goalscorer['scorer'] == ' ' or goalscorer['scorer'] == None:
            goalscorer['scorer'] = 'Unknown'
        else:
            goalscorer['scorer'] = goalscorer['scorer'].lower()
        if goalscorer['own_goal'] == '' or goalscorer['own_goal'] == ' ' or goalscorer['own_goal'] == None:
            goalscorer['own_goal'] = 'Unknown'
        if goalscorer['penalty'] == '' or goalscorer['penalty'] == ' ' or goalscorer['penalty'] == None:
            goalscorer['penalty'] = 'Unknown'
        model.add_data(data, goalscorer)
    return model.data_size(data)[1]

def loadShootouts(data):

    shootoutsFile = cf.data_dir + "football/shootouts-utf8-large.csv"
    input_file = csv.DictReader(open(shootoutsFile, encoding= "utf-8"))
    i=1
    for shootout in input_file:
        shootout['id']=i
        i+=1
        if shootout['date'] == '' or shootout['date'] == ' ' or shootout['date'] == None:
            shootout['date'] = 'Unknown'
        else:
            shootout['date']=datetime.datetime.strptime(shootout['date'], '%Y-%m-%d')
        if shootout['home_team'] == '' or shootout['home_team'] == ' ' or shootout['home_team'] == None:
            shootout['home_team'] = 'Unknown'
        else:
            shootout['home_team'] = shootout['home_team'].lower()
        if shootout['away_team'] == '' or shootout['away_team'] == ' ' or shootout['away_team'] == None:
            shootout['away_team'] = 'Unknown'
        else:
            shootout['away_team'] = shootout['away_team'].lower()
        if shootout['winner'] == '' or shootout['winner'] == ' ' or shootout['winner'] == None:
            shootout['winner'] = 'Unknown'
        model.add_data(data, shootout)
    return model.data_size(data)[2]

def modificar_listas(control):
    #Función que le indica al model que modifique la reprsentación de las listas de los catálogos a "SINGLE_LINKED"
    model.modificar_listas(control['model'])

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    control['model'] = model.sort(control['model'])
    i=1
    for match in lt.iterator(control['model']['matches']):
        match['id']=i
        i += 1
    
    j=1
    for goal_scorer in lt.iterator(control['model']['goal_scorers']):
        goal_scorer['id'] = j
        j +=1
    
    k=1
    for shootout in lt.iterator(control['model']['shootouts']):
        shootout['id'] = k
        k += 1


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, partidos, equipo, condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    data_structs = control['model']
    start_time = get_time()
    respuesta, size = model.req_1(data_structs,partidos, equipo, condicion)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    igualdad = True
    if size != int(partidos):
        igualdad = False
    return respuesta, size, igualdad, deltaTime


def req_2(control, nombreJugador, numeroGoles):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    data_structs = control['model']
    start_time = get_time()
    respuesta, size = model.req_2(data_structs, nombreJugador, numeroGoles)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    vacio = False

    if size == 0:
        vacio = True

    return respuesta, size, vacio, deltaTime


def req_3(control, nombre_equipo, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
  
    vacio = False
    data_structs = control['model']
    fecha_inicial = datetime.datetime.strptime(fecha_i,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fecha_f,'%Y-%m-%d')
    start_time = get_time()
    respuesta, numeroPartidos, localmatch, visitantematch = model.req_3(data_structs,nombre_equipo,fecha_inicial,fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    if numeroPartidos == 0:
        vacio = True
    return respuesta, numeroPartidos, localmatch, visitantematch, vacio, deltaTime



def req_4(control, nombre_torneo, fecha_inic, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4

    data_structs = control['model']
    fecha_inicial = datetime.datetime.strptime(fecha_inic,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fecha_fin,'%Y-%m-%d')
    start_time = get_time()
    partidos, paises, ciudades, penalties, torneo, vacio = model.req_4(data_structs,nombre_torneo,fecha_inicial,fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return partidos, paises, ciudades, penalties, torneo, vacio, deltaTime


def req_5(control,nombre,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    vacio = False
    data_structs = control['model']
    fecha_inicial = datetime.datetime.strptime(fecha_i,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fecha_f,'%Y-%m-%d')
    start_time = get_time()
    respuesta, anotaciones, torneos, penaltis, autogoles = model.req_5(data_structs,nombre,fecha_inicial,fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    if anotaciones == 0:
        vacio = True
    return respuesta, anotaciones, torneos, penaltis, autogoles, vacio, deltaTime

def req_6(control, cantidad_partidos, torneo, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    vacio = False
    data_structs = control['model']
    cantidad_p = int(cantidad_partidos)
    tournament = torneo.lower()
    fecha_inicial = datetime.datetime.strptime(fecha_i,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fecha_f,'%Y-%m-%d')
    start_time = get_time()
    respuesta, equipos, partidos, paises, ciudades, max_ciudad = model.req_6(data_structs, cantidad_p, tournament,fecha_inicial, fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    if respuesta == 0:
        vacio = True
    return respuesta, equipos, partidos, paises, ciudades, max_ciudad, vacio, deltaTime


def req_7(control, numeroJugadores, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    
    vacio = False
    data_structs = control['model']
    fecha_inicial = datetime.datetime.strptime(fecha_i,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fecha_f,'%Y-%m-%d')
    start_time = get_time()
    anotadoresTotales, partidosUnicos, torneosUnicos, GolesTotales, Penales, Autogol, respuestaFinal = model.req_7(data_structs, numeroJugadores, fecha_inicial, fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)

    if respuestaFinal == 0:
        vacio = True
    return anotadoresTotales, partidosUnicos, torneosUnicos, GolesTotales, Penales, Autogol, respuestaFinal, vacio, deltaTime



def req_8(control, team1, team2, fechaInicio, fechaFin):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    data_structs = control["model"]
    fecha_inicial = datetime.datetime.strptime(fechaInicio,'%Y-%m-%d')
    fecha_final = datetime.datetime.strptime(fechaFin,'%Y-%m-%d')

    start_time = get_time()
    datos1, datos2, est1, est2, comun = model.req_8(data_structs, team1, team2, fecha_inicial, fecha_final)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)

    return datos1, datos2, est1, est2, comun, deltaTime


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

def sortMatches(control,size,orden):

    start_time = get_time()
    sort_list=model.sortMatches(control["model"],size,orden)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return deltaTime, sort_list