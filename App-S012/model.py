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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    fifa = {'results':None,
            'goalscorers':None,
            'shootouts':None    
    }
    
    fifa['results'] = lt.newList('ARRAY_LIST')
    fifa['goalscorers'] = lt.newList('ARRAY_LIST')
    fifa['shootouts'] = lt.newList('ARRAY_LIST')
    #TODO 4.5 Modificar el uso del TAD lista (p.30.) 

    return fifa



# Funciones para agregar informacion al modelo

def add_data_results(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de results
    """
    
    lt.addLast(data_structs['model']['results'], data)
    
    return data_structs

def add_data_goalscorers(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de goalscorers
    """
    lt.addLast(data_structs['model']['goalscorers'], data)
    
    return data_structs

def add_data_shootouts(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de shootouts
    """
    lt.addLast(data_structs['model']['shootouts'], data)
    
    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, n_partidos, equipo, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    results = sort_req1(data_structs)
    size = results["size"]
    i = 1
    lista = []
    while len(lista) <= n_partidos and i < size:
        actual = lt.getElement(results, i)
        if condicion == "Local":
            if actual["home_team"] == equipo:
                lista.append(actual)
        elif condicion == "Visitante":
            if actual["away_team"] == equipo:
                lista.append(actual)
        elif condicion == "Indiferente":
            if actual["home_team"] == equipo or actual["away_team"] == equipo:
                lista.append(actual)
        i += 1
    return lista




def req_2(data_structs, n_goles, jugador):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    goalscorers = sort_req2(data_structs)
    size = goalscorers["size"]
    i = 1
    lista = []
    
    while len(lista) <= n_goles and i < size:
        actual = lt.getElement(goalscorers, i)
        if jugador == actual["scorer"]:
            lista.append(actual)
        i += 1
    return lista





def req_3(data_structs, equipo, fecha_i, fecha_f ):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista = []
    results = sort_req3_results(data_structs)
    i = 1
    size = results["size"]

    while i < size:
        actual = lt.getElement(results, i)
        if actual["date"] >= fecha_i and actual["date"] <= fecha_f:
            if actual["home_team"] == equipo or actual["away_team"] == equipo:
                actual.pop("neutral")
                j = 1
                goalscorers = sort_req3_goalscorers(data_structs)
                size_2 = goalscorers["size"]
                encontro = False
                while j < size_2:
                    actual_2 = lt.getElement(goalscorers, j)
                    
                    if actual["date"] == actual_2["date"]:
                       
                        actual["penalty"] = actual_2["penalty"] 
                        actual["own_goal"] = actual_2["own_goal"]
                        encontro = True
                        lista.append(actual)
                        
                    j += 1
                    
                if encontro == False:
                        
                    actual["penalty"] = "unknown" 
                    actual["own_goal"] = True
                    lista.append(actual)
   
                
        i += 1
    local = 0
    visitante = 0
    for partido in lista:
        if partido["home_team"] == equipo:
            local += 1
        elif partido["away_team"] == equipo:
            visitante += 1
    return lista, local, visitante



def req_4(data_structs,torneo,fecha_i,fecha_f):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    results = sort_req1(data_structs)
    size = results["size"]
    lista = []
    i = 1
    centinela = True
    while centinela and i < size:
        actual = lt.getElement(results,i)
        fecha = actual["date"]
        if actual["tournament"] == torneo:
            if fecha_i <= fecha and fecha <= fecha_f:
                if "neutral" in actual:
                    actual.pop("neutral")
                if actual["home_score"] == actual["away_score"]:
                    size_s = lt.size(data_structs["shootouts"])
                    shootouts = lt.subList(data_structs["shootouts"],1,size_s)
                    j = 1
                    bandera = True
                    while j < size_s and bandera:
                        penales = lt.getElement(shootouts,j)
                        if penales["date"] == fecha and actual["home_team"] == penales["home_team"]:
                            actual["winner"] = penales["winner"]
                            bandera = False
                        j += 1
                else:
                    actual["winner"] = "Unknown"
                lista.append(actual)
            elif fecha < fecha_i:
                centinela = False
        i += 1
    paises = []
    ciudades = []
    penales = 0
    for partido in lista:
        if partido["home_team"] not in paises:
            paises.append(partido["home_team"])
        if partido["away_team"] not in paises:
            paises.append(partido["away_team"])
        if partido["city"] not in ciudades:
            ciudades.append(partido["city"])
        #if partido["winner"] != "Unknown":
           # penales += 1
    
    return lista, len(paises), len(ciudades), penales        
            


def req_5(data_structs, nom_player, fecha_i, fecha_f):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    goalscorers = sort_req5(data_structs)
    results = sort_req1(data_structs)
    sizeg = goalscorers["size"]
    sizer = results["size"]
    lista = []
    i = 1
    while i < sizeg:
        actual = lt.getElement(goalscorers, i)
        if actual["date"] >= fecha_i and actual["date"] <= fecha_f:
            if actual["scorer"] == nom_player:
                j = 1
                while j < sizer:
                    data = lt.getElement(results, j)
                    if data["date"] == actual["date"]:
                        if data["home_team"] == actual["home_team"]:
                            actual["tournament"] = data["tournament"]            
                            lista.append(actual)
                    j += 1        
        i +=1
    torneos = []
    penales = 0
    autogoles = 0
    for goles in lista:
        if goles["tournament"] not in torneos:
            torneos.append(goles["tournament"])
        if goles["penalty"] != "False":
            penales += 1
        elif goles["own_goal"] != "False":
            autogoles += 1
        
    return lista, len(torneos), penales, autogoles
    


def req_6(data_structs,n_equipos,torneo,fecha_i,fecha_f):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    mejores = lt.newList('ARRAY_LIST')
    paises = {}
    results = sort_req1(data_structs)
    goalscorers = sort_req2(data_structs)
    size = results["size"]
    size_goals = goalscorers["size"]
    jugadores = {}
    i = 1
    poderoso = True
    partidos = 0
    ciudades = {}
    while i < size and poderoso:
        data = lt.getElement(results,i)
        fecha = data["date"]
        pais_1 = data["home_team"]
        pais_2 = data["away_team"]
        if torneo == data["tournament"]:
            if fecha >= fecha_i and fecha <= fecha_f:
                partidos += 1
                if data["city"] not in ciudades:
                    ciudades[data["city"]] = 1
                else:
                    ciudades[data["city"]] += 1
                if pais_1 not in paises:
                    paises[pais_1] = {"team":None,
                    "points": 0,
                    "dif_goles": 0,
                    "Matches_played": 0,
                    "Goles x penal": 0,
                    "Autogoles": 0,
                    "Victorias": 0,
                    "Empates":0,
                    "Derrotas":0,
                    "Goles":0,
                    "Goles Recibidos":0,
                    "Top Scorer": {"Nombre":None,
                                    "Goles":0,
                                    "Scored Matches": 0,
                                    "Promedio":0}}
                    paises[pais_1]["team"] = pais_1
                if pais_2 not in paises:
                    paises[pais_2] = {"team":None,
                    "points": 0,
                    "dif_goles": 0,
                    "Matches_played": 0,
                    "Goles x penal": 0,
                    "Autogoles": 0,
                    "Victorias": 0,
                    "Empates":0,
                    "Derrotas":0,
                    "Goles":0,
                    "Goles Recibidos":0,
                    "Top Scorer": {"Nombre":None,
                                    "Goles":0,
                                    "Scored Matches": 0,
                                    "Promedio":0}}
                    paises[pais_2]["team"] = pais_2
                if float(data["home_score"]) > float(data["away_score"]):
                    paises[pais_1]["points"] += 3
                    paises[pais_1]["Victorias"] += 1
                    paises[pais_1]["Matches_played"] += 1
                    paises[pais_1]["Goles"] += float(data["home_score"])
                    paises[pais_1]["Goles Recibidos"] += float(data["away_score"])
      
                    paises[pais_2]["Derrotas"] += 1
                    paises[pais_2]["Matches_played"] += 1
                    paises[pais_2]["Goles"] += float(data["away_score"])
                    paises[pais_2]["Goles Recibidos"] += int(data["home_score"])
                    j = 1
                    centinela = True
                    bandera = True
                    while centinela and j < size_goals:
                        actual = lt.getElement(goalscorers, j)
                        if fecha == actual["date"]:
                            if pais_1 == actual["home_team"]:
                                if actual["own_goal"]:
                                    paises[actual["team"]]["Autogoles"] += 1
                                if actual["penalty"]:
                                    paises[actual["team"]]["Goles x penal"] += 1
                                if actual["scorer"] not in jugadores:
                                    jugadores[actual["scorer"]] = {"pais":actual["team"],
                                                                "goles":0,
                                                                "Scored Matches":0,
                                                                "promedio":0}
                                jugadores[actual["scorer"]]["goles"] += 1
                                jugadores[actual["scorer"]]["promedio"] += float(actual["minute"])
                                if bandera:
                                    jugadores[actual["scorer"]]["Scored Matches"] += 1
                                    bandera = False
                        elif fecha < actual["date"]:
                            centinela = False
                        j += 1
                    
                elif int(data["home_score"]) < int(data["away_score"]):
                    paises[pais_2]["points"] += 3
                    paises[pais_2]["Victorias"] += 1
                    paises[pais_2]["Matches_played"] += 1
                    paises[pais_2]["Goles"] += int(data["away_score"])
                    paises[pais_2]["Goles Recibidos"] += int(data["home_score"])
    
                    paises[pais_1]["Derrotas"] += 1
                    paises[pais_1]["Matches_played"] += 1
                    paises[pais_1]["Goles"] += int(data["home_score"])
                    paises[pais_1]["Goles Recibidos"] += int(data["away_score"])
                    j = 1
                    centinela = True
                    bandera = True
                    while centinela and j < size_goals:
                        actual = lt.getElement(goalscorers, j)
                        if fecha == actual["date"]:
                            if pais_1 == actual["home_team"]:
                                if actual["own_goal"]:
                                    paises[actual["team"]]["Autogoles"] += 1
                                if actual["penalty"]:
                                    paises[actual["team"]]["Goles x penal"] += 1
                                if actual["scorer"] not in jugadores:
                                    jugadores[actual["scorer"]] = {"pais":actual["team"],
                                                                "goles":0,
                                                                "Scored Matches":0,
                                                                "promedio":0}
                                jugadores[actual["scorer"]]["goles"] += 1
                                jugadores[actual["scorer"]]["promedio"] += float(actual["minute"])
                                if bandera:
                                    jugadores[actual["scorer"]]["Scored Matches"] += 1
                                    bandera = False
                        elif fecha < actual["date"]:
                            centinela = False
                        j += 1
                else: 
                    paises[pais_2]["points"] += 1
                    paises[pais_2]["Empates"] += 1
                    paises[pais_2]["Matches_played"] += 1
                    paises[pais_2]["Goles"] += int(data["away_score"])
                    paises[pais_2]["Goles Recibidos"] += int(data["home_score"])
    
                    paises[pais_1]["points"] += 1
                    paises[pais_1]["Empates"] += 1
                    paises[pais_1]["Matches_played"] += 1
                    paises[pais_1]["Goles"] += int(data["home_score"])
                    paises[pais_1]["Goles Recibidos"] += int(data["away_score"])
                    j = 1
                    centinela = True
                    bandera = True
                    while centinela and j < size_goals:
                        actual = lt.getElement(goalscorers, j)
                        if fecha == actual["date"]:
                            if pais_1 == actual["home_team"]:
                                if actual["own_goal"]:
                                    paises[actual["team"]]["Autogoles"] += 1
                                if actual["penalty"]:
                                    paises[actual["team"]]["Goles x penal"] += 1
                                if actual["scorer"] not in jugadores:
                                    jugadores[actual["scorer"]] = {"pais":actual["team"],
                                                                "goles":0,
                                                                "Scored Matches":0,
                                                                "promedio":0
                                                                }
                                jugadores[actual["scorer"]]["goles"] += 1
                                jugadores[actual["scorer"]]["promedio"] += float(actual["minute"])
                                if bandera:
                                    jugadores[actual["scorer"]]["Scored Matches"] += 1
                                    bandera = False
                        elif fecha < actual["date"]:
                            centinela = False
                        j += 1
        elif fecha < fecha_i:
            poderoso = False
        i += 1
            
    for jugador in jugadores:
        actual = jugadores[jugador]
        promedio = actual["promedio"]/actual["goles"]
        actual["promedio"] = promedio
    for pais in paises:
        actual = paises[pais]
        actual["dif_goles"] = actual["Goles"] - actual["Goles Recibidos"]   
        mejor = {"pais":None,
                 "goles":0,
                "Scored Matches":0,
                "promedio":0
                            }
        max_g = 0
        nombre = None
        for jugador in jugadores:
            jug_act = jugadores[jugador]
            if jug_act["pais"] == pais:
                if max_g < jug_act["goles"]:
                    max_g = jug_act["goles"]
                    mejor = jug_act
                    nombre = jugador
        paises[pais]["Top Scorer"] = {"Nombre":nombre,
                                    "Goles":mejor["goles"],
                                    "Scored Matches": mejor["Scored Matches"],
                                    "Promedio":mejor["promedio"]}
        lt.addLast(mejores,actual)
    mejores = sort_req_6(mejores)
    mejores = lt.subList(mejores,1,n_equipos)
    max_c = 0
    mejor = None
    for ciudad in ciudades:
        actual = ciudades[ciudad]
        if actual > max_c:
            max_c = actual
            mejor = ciudad
    return mejores, partidos, len(ciudades), mejor
    
                    


def req_7(data_structs,n_jugadores,fecha_i,fecha_f):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    mejores = lt.newList('ARRAY_LIST')
    results = sort_req1(data_structs)
    goalscorers = sort_req2(data_structs)
    size = results["size"]
    size_goals = goalscorers["size"]
    jugadores = {}
    i = 1
    poderoso = True
    partidos = 0
    while i < size and poderoso:
        data = lt.getElement(results,i)
        fecha = data["date"]
        pais_1 = data["home_team"]
        if fecha >= fecha_i and fecha <= fecha_f:
            if data["tournament"] != "Friendly":
                partidos += 1
                j = 1
                centinela = True
                bandera = True
                while centinela and j < size_goals:
                    actual = lt.getElement(goalscorers, j)
                    jugador = actual["scorer"]
                    if fecha == actual["date"]:
                        if pais_1 == actual["home_team"]:
                            if jugador not in jugadores:
                                jugadores[jugador] = {"nombre":jugador,
                                                      "total_points":0,
                                                      "total_goals":0,
                                                      "penalty_goals":0,
                                                      "own_goals":0,
                                                      "avg_time(min)":0,
                                                      "total_tournaments":[],
                                                      "scored_in_wins":0,
                                                      "scored_in_losses":0,
                                                      "scored_in_draws":0,
                                                      "last_goal":{"date":None,
                                                                   "tournament":None,
                                                                   "home_team":None,
                                                                   "away_team":None,
                                                                   "home_score":0,
                                                                   "away_score":0,
                                                                   "minute":0,
                                                                   "penalty":"Unknown",
                                                                   "own_goal":"Unknown"}}
                            if actual["penalty"]:
                                jugadores[jugador]["total_points"] += 2
                                jugadores[jugador]["penalty_goals"] += 1
                            else: 
                                jugadores[jugador]["total_points"] += 1
                            jugadores[jugador]["total_goals"] += 1
                            if actual["own_goal"]:
                                jugadores[jugador]["total_points"] -= 1
                                jugadores[jugador]["own_goals"] += 1
                            if actual["minute"] != None:
                                jugadores[jugador]["avg_time(min)"] += float(actual["minute"])
                            if data["tournament"] not in jugadores[jugador]["total_tournaments"]:
                                jugadores[jugador]["total_tournaments"].append(data["tournament"])
                            if actual["team"] == data["home_team"]:
                                if int(data["home_score"]) > int(data["away_score"]):
                                    jugadores[jugador]["scored_in_wins"] += 1
                                elif int(data["home_score"]) < int(data["away_score"]):
                                    jugadores[jugador]["scored_in_losses"] += 1
                            
                            if actual["team"] == data["away_team"]:
                                if int(data["away_score"]) > int(data["home_score"]):
                                    jugadores[jugador]["scored_in_wins"] += 1
                                elif int(data["home_score"]) > int(data["away_score"]):
                                    jugadores[jugador]["scored_in_losses"] += 1
                            else:
                                jugadores[jugador]["scored_in_draws"] += 1
                            if bandera:
                                last = jugadores[jugador]["last_goal"]
                                last["date"] = fecha
                                last["tournament"] = data["tournament"]
                                last["home_team"] = pais_1
                                last["away_team"] = actual["away_team"]
                                last["home_score"] = data["home_score"]
                                last["away_score"] = data["away_score"]
                                last["minute"] = actual["minute"]
                                last["penalty"] = actual["penalty"]
                                last["own_goal"] = actual["own_goal"]
                            lt.addLast(mejores,jugadores[jugador])
                    j += 1
        i += 1
    mejores = sort_req_7(mejores)
    total_players = lt.size(mejores)
    goles = 0
    penaltis = 0
    autogoles = 0
    for jugador in lt.iterator(mejores):
        goles += jugador["total_goals"]
        penaltis += jugador["penalty_goals"]
        autogoles += jugador["own_goals"]
    mejores = lt.subList(mejores,1,n_jugadores)
    return mejores, total_players, partidos, goles, penaltis, autogoles                     
                                
                            
                                    
                


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def sort_req_6(paises):
    
    sorted_list = sa.sort(paises, points_comparison)
    return sorted_list
    
def points_comparison(pais_1,pais_2):
    resultado = pais_1["points"] > pais_2["points"]
    return resultado
# Funciones utilizadas para comparar elementos dentro de una lista

def sort_req_7(mejores):
    sorted_list = sa.sort(mejores,points_comparison_2)
    return sorted_list
    
def points_comparison_2(jugador_1,jugador_2):
    resultado = jugador_1["total_points"] > jugador_2["total_points"]
    return resultado

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def date_comparison(results1, results2):
    
    resultado = results1['date']>results2['date']
    
    return resultado


def sort_req1(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    size = lt.size(data_structs["results"])
    sub_list = lt.subList(data_structs['results'],1,size)
    sorted_list = sa.sort(sub_list, date_comparison)
    return sorted_list




def sort_req2(data_structs):
    size = lt.size(data_structs["goalscorers"])
    sub_list = lt.subList(data_structs['goalscorers'],1,size)
    sorted_list = sa.sort(sub_list, minute_comparison)
    return sorted_list

        
def minute_comparison(goalscorers1, goalscorers2):

    fecha = False
    if (goalscorers1['date']<goalscorers2['date']):
        fecha = True
    elif (goalscorers1['date']==goalscorers2['date']):
        if goalscorers1['minute'] < goalscorers2['minute']:
            fecha = True
    return fecha

def comparison_req3(goalscorers1, goalscorers2):
    
    goal = goalscorers1['date']<goalscorers2['date']
    
    return goal

def sort_req3_goalscorers(data_structs):
    size = lt.size(data_structs["goalscorers"])
    sub_list = lt.subList(data_structs['goalscorers'],1,size)
    sorted_list = sa.sort(sub_list, comparison_req3)
    return sorted_list

def sort_req3_results(data_structs):
    size = lt.size(data_structs["results"])
    sub_list = lt.subList(data_structs['results'],1,size)
    sorted_list = sa.sort(sub_list, comparison_req3)
    return sorted_list



def sort_req5(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    size = lt.size(data_structs["goalscorers"])
    sub_list = lt.subList(data_structs['goalscorers'],1,size)
    sorted_list = sa.sort(sub_list, minute_comparison_de_mayor_a_menor)
    return sorted_list

def minute_comparison_de_mayor_a_menor(goalscorers1, goalscorers2):

    fecha = False
    if (goalscorers1['date'] > goalscorers2['date']):
        fecha = True
    elif (goalscorers1['date']==goalscorers2['date']):
        if goalscorers1['minute'] > goalscorers2['minute']:
            fecha = True
    return fecha


def cmp_partidos_by_fecha_y_pais(results1, results2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelva falso (False).
    Args:
        Resultado1: información del primer registro de resultados FIFA que incluye
        “date” y el “country”
        Resultado2: información del segundo registro de resultados FIFA que incluye
        “date” y el “country”
    """
    fecha = False
    if (results1['date']<results2['date']):
        fecha = True
    elif (results1['date']==results2['date']):
        if results1['country'] < results2['country']:
            fecha = True
    return fecha

def sort_fifa_shell(data_structs, size):
    sub_list = lt.subList(data_structs['results'],1,size)
    sorted_list = sa.sort(sub_list, cmp_partidos_by_fecha_y_pais)
    return sorted_list

def sort_fifa_selec(data_structs, size):
    sub_list = lt.subList(data_structs['results'],1,size)
    sorted_list = se.sort(sub_list, cmp_partidos_by_fecha_y_pais)
    return sorted_list

def sort_fifa_inser(data_structs, size):
    sub_list = lt.subList(data_structs['results'],1,size)
    sorted_list = ins.sort(sub_list, cmp_partidos_by_fecha_y_pais)
    return sorted_list
