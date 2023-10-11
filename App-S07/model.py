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
from datetime import datetime as dt
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from tabulate import tabulate 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo_lista):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data = {"results": None, "goal_scorers": None, "shootouts": None}
    data["results"] = lt.newList(tipo_lista)
    data["goal_scorers"] = lt.newList(tipo_lista)
    data["shootouts"] = lt.newList(tipo_lista)
    return data


# Funciones para agregar informacion al modelo

def add_results(data, result):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data['results'], result)
    return data

def add_goal_scoreres(data, score):
    lt.addLast(data["goal_scorers"], score)
    return data

def add_shootouts( data, shoot):
    lt.addLast(data["shootouts"], shoot)
    return data



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


def result_size(data):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data['results'])

    pass
def goal_scorers_size (data):
    return lt.size(data['goal_scorers'])

def shootouts_size (data):
    return lt.size(data['shootouts'])


def req_1(data, numero_partidos, equipo, condicion_equipo):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    resultados = data["results"]
    total_de_partidos = 0
    rta = lt.newList("ARRAY_LIST")
    for r in lt.iterator(resultados):
        if condicion_equipo == "Local":
            if equipo == r["home_team"]:
                total_de_partidos += 1
                diccionario ={"date": r["date"], "home_team":r["home_team"], "away_team": r["away_team"],
                              "home_score": r["home_score"], "away_score": r["away_score"], "country": r["country"], 
                              "city": r["city"], "tournament": r["tournament"]}
                lt.addLast(rta, diccionario)
        elif condicion_equipo == "Visitante":
             if equipo == r["away_team"]:
                total_de_partidos += 1
                diccionario ={"date": r["date"], "home_team":r["home_team"], "away_team": r["away_team"],
                              "home_score": r["home_score"], "away_score": r["away_score"], "country": r["country"], 
                              "city": r["city"], "tournament": r["tournament"]}
                lt.addLast(rta, diccionario)
        elif condicion_equipo == "indiferent": 
            if equipo == r["home_team"] or equipo == r["away_team"]:
                total_de_partidos += 1
                diccionario ={"date": r["date"], "home_team":r["home_team"], "away_team": r["away_team"],
                              "home_score": r["home_score"], "away_score": r["away_score"], "country": r["country"], 
                              "city": r["city"], "tournament": r["tournament"]}
                lt.addLast(rta, diccionario)
    if lt.size(rta) > int(numero_partidos):
        rta = lt.subList(rta, 1, int(numero_partidos))
    return total_de_partidos, rta


def req_2(data, number_goals, name_player):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    goals = data["goal_scorers"]
    scorer_goals = lt.newList("ARRAY_LIST")
    total_goals = 0
    final_scorer_goals = lt.newList("ARRAY_LIST")

    for goal in lt.iterator(goals):
        if goal["scorer"] == name_player:
            lt.addLast(scorer_goals, goal)
            total_goals += 1

    sorted_date_minute = sa.sort(scorer_goals, cmp_elementos_by_fecha_y_minuto2)

    i = 1
    while i <= lt.size(sorted_date_minute) and i <= int(number_goals):
        element = lt.getElement(sorted_date_minute, i)
        lt.addLast(final_scorer_goals, element)
        i += 1

    size_list = lt.size(final_scorer_goals)

    return final_scorer_goals, size_list, total_goals


def req_3(data, team_name, inicial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    matches = data["results"]
    range_team_matches = lt.newList("ARRAY_LIST")
    goals = data["goal_scorers"]
    range_goals_team = lt.newList("ARRAY_LIST")
    total_team_matches = 0
    total_home_team = 0
    total_away_team = 0

    for match in lt.iterator(matches):
        date = match["date"]
        if (match["home_team"] == team_name or match["away_team"] == team_name) and rango_by_fecha(date, inicial_date, final_date) == True:
            lt.addLast(range_team_matches, match)
            total_team_matches += 1
            if match["home_team"] == team_name:
                total_home_team += 1
            elif match["away_team"] == team_name:
                total_away_team += 1

    for goal in lt.iterator(goals):
        date2 = goal["date"]
        if (goal["home_team"] == team_name or goal["away_team"] == team_name) and rango_by_fecha(date2, inicial_date, final_date) == True:
            lt.addLast(range_goals_team, goal)

    complete_team_matches = find_type_goals(range_team_matches, range_goals_team)
    sorted_date = sa.sort(complete_team_matches, cmp_partidos_by_fecha)
    size_list = lt.size(sorted_date)

    return sorted_date, size_list, total_team_matches, total_home_team, total_away_team


def req_4(data, torneo, lim_inf, lim_sup):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    partidos_torneo = 0
    paises = lt.newList("ARRAY_LIST")
    ciudades = lt.newList()
    resultados = data["results"]
    partidos_penales = data["shootouts"]
    penales = 0
    rta = lt.newList("ARRAY_LIST")
    for r in lt.iterator(resultados):
        winner = "Unknown"
        if r["tournament"] == torneo: 
            for s in lt.iterator(partidos_penales):
                if r["home_team"] == s["home_team"] and r["away_team"] == s["away_team"]:
                    penales += 1
                    winner = s["winner"]
            fecha = r["date"]        
            if rango_by_fecha(fecha, lim_inf, lim_sup) == True:
                diccionario = {"date": r["date"], "tournament": r["tournament"], 
                                   "country": r["country"], "city": r["city"], 
                                   "home_team":r["home_team"], "away_team": r["away_team"],
                                   "home_score": r["home_score"], "away_score": r["away_score"],
                                   "winner" : winner}
                partidos_torneo +=1
                lt.addLast(rta, diccionario)
                if lt.isPresent(paises, r["country"]) == 0:
                    lt.addLast(paises, r["country"])
                if lt.isPresent(ciudades, r["city"]) == 0: 
                    lt.addLast(ciudades, r["city"])
                 
    return partidos_torneo, lt.size(paises), lt.size(ciudades), penales, rta


def req_5(data, name, lim_inf, lim_sup):
    """
    Función que soluciona el requerimiento 5
    """
    anotaciones = 0
    torneos = lt.newList("ARRAY_LIST")
    penales = 0
    autogoles = 0
    rta = lt.newList("ARRAY_LIST")
    current_date = ((dt.strptime(lim_sup,"%Y-%m-%d")).date()).toordinal()
    top_date = ((dt.strptime(lim_inf,"%Y-%m-%d")).date()).toordinal()
    i = 1
    while current_date >= top_date:
        elemento = lt.getElement(data["goal_scorers"], i)
        if elemento["scorer"] == name:
             rango= rango_by_fecha( elemento["date"], lim_inf, lim_sup)
             if rango:
                 tournament, home_score, away_score = find_results(data["results"],elemento["date"], elemento["home_team"], elemento["away_team"])
                 dict_scorer= {
                     "date":  elemento["date"],
                     "minute":  elemento["minute"],
                     "home_team":  elemento["home_team"],
                     "away_team":  elemento["away_team"],
                     "team":  elemento["team"],
                     "home_score": home_score,
                     "away_score": away_score,
                     "tournament": tournament,
                     "penalty":  elemento["penalty"],
                     "own_goal":  elemento["own_goal"]          
                    }
                 lt.addLast(rta, dict_scorer)
                
                 if dict_scorer["penalty"] == True:
                     penales += 1
                 if dict_scorer["own_goal"] == True:
                     autogoles += 1
                 if lt.isPresent(torneos, dict_scorer["tournament"]) == 0:
                     lt.addLast(torneos, dict_scorer["tournament"])
                 anotaciones += 1
        i += 1
        current_date = ((dt.strptime( elemento["date"],"%Y-%m-%d")).date()).toordinal()
        rta_final = sa.sort(rta, cmp_elementos_by_fecha_y_minuto)
    return anotaciones, lt.size(torneos), penales, autogoles, rta_final


def req_6(data, numero_equipos, torneo, lim_inf, lim_sup):

    current_date = ((dt.strptime(lim_sup,"%Y-%m-%d")).date()).toordinal()
    top_date = ((dt.strptime(lim_inf,"%Y-%m-%d")).date()).toordinal()
    resultados = data["results"]
    partidos_torneo = lt.newList("ARRAY_LIST")
    paises = lt.newList("ARRAY_LIST")
    ciudades = lt.newList("ARRAY_LIST")
    ciudades_mas_partidos = {}
    maximo = 0
    scorers = data["goal_scorers"]
    scorers_2 = lt.newList("ARRAY_LIST")
    teams = lt.newList("ARRAY_LIST")
    rta = lt.newList("ARRAY_LIST")
    i = 1

    while current_date >= top_date:
        r = lt.getElement(data["results"], i)
        if r["tournament"] == torneo:
            fecha = r["date"]
            if rango_by_fecha(fecha, lim_inf, lim_sup) == True:
                lt.addLast(partidos_torneo, r)
                if lt.isPresent(paises, r["country"]) == 0:
                    lt.addLast(paises, r["country"])
                if lt.isPresent(ciudades, r["city"]) == 0: 
                    lt.addLast(ciudades, r["city"])
                if r["city"]  not in ciudades_mas_partidos:
                    ciudades_mas_partidos[r["city"]] = 1
                else: 
                    ciudades_mas_partidos[r["city"]] +=1 

                if ciudades_mas_partidos[r["city"]] > maximo:
                    maximo = ciudades_mas_partidos[r["city"]]
                if ciudades_mas_partidos[r["city"]] == maximo:
                    ciudad = r["city"]

                lt.addLast(teams, r["home_team"])


        current_date = ((dt.strptime( r["date"],"%Y-%m-%d")).date()).toordinal()
        i += 1

    scorers = find_goal_scorers_2(data["goal_scorers"], partidos_torneo)
    teams_final = find_teams(scorers, teams)

    for equipo in lt.iterator(teams_final):
        puntos = 0
        diferencia = 0
        victorias = 0
        empates = 0
        derrotas = 0
        favor = 0
        contra = 0
        autogoles = 0
        penales = 0
        maximo = 0
        jugador = "Unknown"
        matches = 0
        for partido in lt.iterator(partidos_torneo):
                
                if partido["away_team"]== equipo or partido["home_team"]== equipo:
                    matches += 1
                    punto, victoria, empate, derrota = calcular_puntos_victorias_empates_derrotas(partido, equipo)
                    puntos += punto
                    victorias += victoria
                    empates += empate
                    derrotas += derrota 
                    favor_1, contra_1, diferencia_1 = diferencia_goles(partido, equipo)
                    favor += favor_1
                    contra += contra_1
                    diferencia += diferencia_1
        autogoles, penales, jugador = find_best_player_own_goals_penalties_req_6(scorers, equipo)

        dict_equipo = {
            "team" : equipo,
            "total_points" : puntos,
            "goal_difference" : diferencia,
            "penalty_points" : penales,
            "matches" : matches,
            "own_goal_points" : autogoles,
            "wins" : victorias,
            "draws" : empates,
            "losses" : derrotas,
            "goals_for" : favor,
            "goals_against" : contra,
            "top_scorer" : tabulate(jugador["elements"], headers="keys",tablefmt="grid")
        }

        lt.addLast(rta, dict_equipo)
    
    respuesta_final = sa.sort(rta, cmp_total_point)
    if lt.size(rta) > int(numero_equipos):
        respuesta_final = lt.subList(rta, 1, int(numero_equipos))
    return lt.size(teams_final), lt.size(partidos_torneo), lt.size(paises), lt.size(ciudades), ciudad, respuesta_final


def find_teams(goal_scorers, teams):
    teams_final = lt.newList("ARRAY_LIST")
    for team in lt.iterator(teams):
        for s in lt.iterator(goal_scorers):
            if lt.isPresent(teams_final, s["team"]) == 0:
                        lt.addLast(teams_final, s["team"])

    return teams_final

def req_7(data, top_scorers, inicial_date, final_date):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    tournaments = data["results"]
    goals_players = data["goal_scorers"]
    range_ofical_matches = lt.newList("ARRAY_LIST")
    range_date_goals = lt.newList("ARRAY_LIST")

    for oficial in lt.iterator(tournaments):
        date = oficial["date"]
        if oficial["tournament"] != "Friendly" and rango_by_fecha(date, inicial_date, final_date) == True:
            lt.addLast(range_ofical_matches, oficial)

    for player in lt.iterator(goals_players):
        date2 = player["date"]
        if rango_by_fecha(date2, inicial_date, final_date) == True:
            lt.addLast(range_date_goals, player)

    info_completa_players = lt.newList("ARRAY_LIST")

    for match in lt.iterator(range_ofical_matches):
        for goles in lt.iterator(range_date_goals):
            resultado = "Unknown"
            if (match["date"] == goles["date"]) and (match["home_team"] == goles["home_team"]) and  (match["away_team"] == goles["away_team"]):
                if goles["team"] == match["home_team"] and int(match["home_score"]) > int(match["away_score"]):
                    resultado = "Victoria"
                elif goles["team"] == match["home_team"] and int(match["home_score"]) == int(match["away_score"]):
                    resultado = "Empate"
                elif goles["team"] == match["home_team"] and int(match["home_score"]) < int(match["away_score"]):
                    resultado = "Derrota"
                elif goles["team"] == match["away_team"] and int(match["away_score"]) > int(match["home_score"]):
                    resultado = "Victoria"
                elif goles["team"] == match["away_team"] and int(match["home_score"]) == int(match["away_score"]):
                    resultado = "Empate"
                elif goles["team"] == match["away_team"] and int(match["home_score"]) < int(match["away_score"]):
                    resultado = "Derrota"
                
                info_completa_goles = {
                                        "scorer": goles["scorer"],
                                        "minute": goles["minute"],
                                        "penalty": goles["penalty"],
                                        "own_goal": goles["own_goal"],
                                        "tournament": match["tournament"],
                                        "date": match["date"],
                                        "home_team": match["home_team"],
                                        "away_team": match["away_team"],
                                        "home_score": match["home_score"],
                                        "away_score": match["away_score"],
                                        "resultado": resultado,
                                      }
                
                lt.addLast(info_completa_players, info_completa_goles)

    partidos = set()
    torneos_tot = set()
    total_anota = set()
    total_goles_anotadores = lt.size(info_completa_players)
    total_penaltys = 0
    total_autogoles = 0

    for infor in lt.iterator(info_completa_players):
        total_anota.add(infor["scorer"])
        partidos.add((infor["date"], infor["home_team"], infor["away_team"]))
        torneos_tot.add(infor["tournament"])
        if infor["penalty"] == "True":
            total_penaltys += 1
        if infor["own_goal"] == "True":
            total_autogoles += 1

    total_partidos = len(partidos)
    total_torneos = len(torneos_tot)
    total_anotadores = len(total_anota)
    
    sorted_info_completa_players = sa.sort(info_completa_players, cmp_elementos_by_fecha_y_minuto2)
    lista_jugadores = lt.newList("ARRAY_LIST")
    dict_jugadores = {}

    i = 1             
    while i <= lt.size(sorted_info_completa_players):
        element = lt.getElement(sorted_info_completa_players, i)
        jug = element["scorer"]

        if jug in dict_jugadores:
            lt.addLast(dict_jugadores[jug], element)
        if jug not in dict_jugadores:
            list_jug = lt.newList("ARRAY_LIST")
            lt.addLast(list_jug, element)
            dict_jugadores[jug] = list_jug
        i += 1

    for jug, goles_jug in dict_jugadores.items():
        lt.addLast(lista_jugadores, goles_jug)

    lista_info_goleadores = lt.newList("ARRAY_LIST")

    for sub_list in lt.iterator(lista_jugadores):
        
        last_goals = {
                        "date": None,
                        "tournament": None,
                        "home_team": None,
                        "away_team": None,
                        "home_score": None,
                        "away_score": None,
                        "minute": None,
                        "penalty": None,
                        "own_goal": None
                     }
        
        info_player ={ 
                        "scorer": None,
                        "puntaje": 0,
                        "total_goals": 0,
                        "penalty_goals": 0,
                        "autogoles": 0,
                        "avg_time [min]": 0,
                        "torneos_totales": 0,
                        "goals_wins": 0,
                        "goals_deal": 0,
                        "goals_losses": 0,
                        "last_goal": None
                      }
        
        torneos = set()
        total_minutes = 0

        for golesitos in lt.iterator(sub_list):

            info_player["total_goals"] += 1
            info_player["puntaje"] +=1

            if golesitos["scorer"] != "":
                info_player["scorer"] = golesitos["scorer"]

            if golesitos["tournament"] != "":
                torneos.add(golesitos["tournament"])

            if golesitos["minute"] != "":
                total_minutes += float(golesitos["minute"])

            if golesitos["penalty"] == "True":
                info_player["penalty_goals"] += 1
                info_player["puntaje"] +=1
                
            if golesitos["own_goal"] == "True":
                info_player["autogoles"] += 1
                info_player["puntaje"] -=1

            if golesitos["resultado"] == "Victoria":
                info_player["goals_wins"] += 1

            if golesitos["resultado"] == "Empate":
                info_player["goals_deal"] += 1

            if golesitos["resultado"] == "Derrota":
                info_player["goals_losses"] += 1

            last_goals["date"] = golesitos["date"]
            last_goals["tournament"] = golesitos["tournament"]
            last_goals["home_team"] = golesitos["home_team"]
            last_goals["away_team"] = golesitos["away_team"]
            last_goals["home_score"] = golesitos["home_score"]
            last_goals["away_score"] = golesitos["away_score"]
            last_goals["minute"] = golesitos["minute"]
            last_goals["penalty"] = golesitos["penalty"]
            last_goals["own_goal"] = golesitos["own_goal"]

        info_player["avg_time [min]"] = total_minutes / info_player["total_goals"] 
        info_player["torneos_totales"] = len(torneos)
        info_player["last_goal"] = last_goals
        lt.addLast(lista_info_goleadores, info_player)

    sorted_info_goleadores = sa.sort(lista_info_goleadores, cmp_jugadores_by_puntaje)
    data_top_scorers = lt.newList("ARRAY_LIST")
    
    for scorer in lt.iterator(sorted_info_goleadores):
        lista = [scorer["last_goal"]] 
        scorer["last_goal"] = tabulate(lista, headers = "keys", tablefmt="grid")

    i = 1
    while i <= lt.size(sorted_info_goleadores) and i <= int(top_scorers):
        element = lt.getElement(sorted_info_goleadores, i)
        lt.addLast(data_top_scorers, element)
        i += 1

    size_list = lt.size(data_top_scorers)

    return data_top_scorers, size_list, total_anotadores, total_partidos, total_torneos, total_goles_anotadores, total_penaltys, total_autogoles

def req_8(data, team1, team2, lim_inf, lim_sup):
    """
    Función que soluciona el requerimiento 8
    """
    current_date = ((dt.strptime(lim_sup,"%Y-%m-%d")).date()).toordinal()
    top_date = ((dt.strptime(lim_inf,"%Y-%m-%d")).date()).toordinal()
    partidos_1 = lt.newList("ARRAY_LIST")
    partidos_2 = lt.newList("ARRAY_LIST")
    ultimo_1 = lt.newList("ARRAY_LIST")
    ultimo_2 = lt.newList("ARRAY_LIST")
    años_1 = lt.newList("ARRAY_LIST")
    años_2 = lt.newList("ARRAY_LIST")
    local_1 = 0
    local_2 = 0
    visitante_1 = 0
    visitante_2 = 0
    victorias_1 = 0
    derrotas_1 = 0
    empates = 0
    victorias_2 = 0
    derrotas_2= 0
    encuentros = lt.newList("ARRAY_LIST")
    ultimo_partido_1_2 = lt.newList("ARRAY_LIST")
    

    i = 1
    while current_date >= top_date:

        elemento = lt.getElement(data["results"], i)
        if elemento["tournament"] != "Friendly":
            home_team1 = elemento["home_team"] == team1
            home_team2 = elemento["home_team"] == team2
            away_team1 = elemento["away_team"] == team1
            away_team2 = elemento["away_team"] == team2

            rango= rango_by_fecha(elemento["date"], lim_inf, lim_sup)

            if (home_team1 or away_team1) and rango:
                if home_team1:
                    local_1 += 1
                else:
                    visitante_1 += 1
              
                lt.addLast(partidos_1, elemento)

                año = (elemento["date"].split("-"))[0]
                if lt.isPresent(años_1, año) == 0:
                    lt.addLast(años_1, año)

            
            if (home_team2 or away_team2) and rango:
                if home_team2:
                    local_2 += 1
                else:
                    visitante_2 += 1
                
                lt.addLast(partidos_2, elemento)

                año = (elemento["date"].split("-"))[0]
                if lt.isPresent(años_2, año) == 0:
                    lt.addLast(años_2, año)

            if home_team1 and away_team2:

                if int(elemento["home_score"]) > int(elemento["away_score"]):
                    victorias_1 += 1
                    derrotas_2 += 1

                elif int(elemento["home_score"]) < int(elemento["away_score"]):  
                    victorias_2 += 1
                    derrotas_1 += 1
                
                else:
                    empates += 1

                lt.addLast(encuentros, elemento)

            elif home_team2 and away_team1:

                if int(elemento["home_score"]) > int(elemento["away_score"]):
                    victorias_2 += 1
                    derrotas_1 += 1

                elif int(elemento["home_score"]) < int(elemento["away_score"]):  
                    victorias_1 += 1
                    derrotas_2 += 1
                
                else:
                    empates += 1
                
                lt.addLast(encuentros, elemento)

        current_date = ((dt.strptime(elemento["date"],"%Y-%m-%d")).date()).toordinal()
        i += 1
    
    ultimo_partido1 = lt.firstElement(partidos_1)
    del ultimo_partido1["neutral"]
    lt.addFirst(ultimo_1, ultimo_partido1)
    years_1 = int(lt.firstElement(años_1)) - int(lt.lastElement(años_1))
    oldest_match_1 = lt.lastElement(partidos_1)["date"]

    ultimo_partido2 = lt.firstElement(partidos_2)
    del ultimo_partido2["neutral"]
    lt.addFirst(ultimo_2, ultimo_partido2)
    years_2 = int(lt.firstElement(años_2)) - int(lt.lastElement(años_2))
    oldest_match_2 = lt.lastElement(partidos_2)["date"]

    ultimo_1_2 = lt.firstElement(encuentros)
    if len(ultimo_1_2)>8:
        del ultimo_1_2["neutral"]
    lt.addFirst(ultimo_partido_1_2, ultimo_1_2)
    anotaciones_ultimo = find_goal_scorers(data["goal_scorers"], ultimo_1_2)
    

    estadisticas_1 = estadisticas_anuales(partidos_1, años_1, team1, data["goal_scorers"])
    estadisticas_2 = estadisticas_anuales(partidos_2, años_2, team2, data["goal_scorers"])
    
    return years_1, lt.size(partidos_1), local_1, visitante_1, oldest_match_1, ultimo_1, estadisticas_1, years_2, lt.size(partidos_2), local_2, visitante_2, oldest_match_2, ultimo_2, estadisticas_2, lt.size(encuentros), victorias_1, derrotas_1, victorias_2, derrotas_2, empates, ultimo_partido_1_2, anotaciones_ultimo



def estadisticas_anuales(partidos, años, team, goal_scorers):

    estadisticas = lt.newList("ARRAY_LIST")

    for año in lt.iterator(años):
        partidos_año = 0
        puntos = 0
        diferencia = 0
        victorias = 0
        empates = 0
        derrotas = 0
        favor = 0
        contra = 0
        for partido in lt.iterator(partidos):
            if año in partido["date"]:
                partidos_año += 1
                punto, victoria, empate, derrota = calcular_puntos_victorias_empates_derrotas(partido, team)
                puntos += punto
                victorias += victoria
                empates += empate
                derrotas += derrota 
                favor_1, contra_1, diferencia_1 = diferencia_goles(partido, team)
                favor += favor_1
                contra += contra_1
                diferencia += diferencia_1
        autogoles, penales, jugador = find_best_player_own_goals_penalties(goal_scorers, team, año)

        dict_año = {
            "year" : año,
            "matches" : partidos_año,
            "total_points" : puntos,
            "goal_difference" : diferencia,
            "penalties" : penales,
            "own_goal" : autogoles,
            "wins" : victorias,
            "draws" : empates,
            "losses" : derrotas,
            "goals_for" : favor,
            "goals_against" : contra,
            "top_scorer" : tabulate(jugador["elements"], headers="keys",tablefmt="grid")
        }
        lt.addLast(estadisticas, dict_año)

    return estadisticas 
    
def calcular_puntos_victorias_empates_derrotas(partido, team):
    """Funcion que calcula las victorias, derrotas o empates de 
    un equipo, a la vez que calcula sus puntos por cada una de estas"""
    puntos = 0
    victoria = 0
    derrota = 0
    empate = 0

    if ((int(partido["away_score"]) > int(partido["home_score"])) and partido["away_team"] == team) or ((int(partido["home_score"]) > int(partido["away_score"])) and partido["home_team"] == team):
        puntos = 3
        victoria = 1
    elif int(partido["away_score"]) == int(partido["home_score"]):
        puntos = 1
        empate = 1
    else:
        derrota = 1
    return puntos, victoria, empate, derrota

def diferencia_goles (partido, team):
    """Funcion que calcula los goles a favor y en contra de un equipo,
    con los cuales cacula la diferencia"""

    if partido["home_team"]== team:
        favor = int(partido["home_score"])
        contra = int(partido["away_score"])
    else:
        favor = int(partido["away_score"])
        contra = int(partido["home_score"])
    diferencia = favor - contra
    return favor, contra, diferencia
 
def find_best_player_own_goals_penalties(goal_scorers, team, año):

    autogoles = 0
    penales = 0
    goleadores = {}
    rta = lt.newList("ARRAY_LIST")

    for jugador in lt.iterator(goal_scorers):
        if(año in jugador["date"]) and (jugador["away_team"] == team or jugador["home_team"] == team):

            if jugador["own_goal"] == "True" and jugador["team"] == team:
                autogoles += 1
            if jugador["penalty"] == "True"  and jugador["team"] == team:
                penales += 1
        
            if jugador["own_goal"] != "True":

                if jugador["scorer"] not in goleadores:
                    goleadores[jugador["scorer"]] = {}
                    goleadores[jugador["scorer"]]["goles"] = 1
                    goleadores[jugador["scorer"]]["partidos"] = [jugador["date"]]
                    goleadores[jugador["scorer"]]["minutos"] = float(jugador["minute"])
                    
                else:
                    goleadores[jugador["scorer"]]["goles"] += 1
                    if jugador["date"] not in goleadores[jugador["scorer"]]["partidos"]:
                        goleadores[jugador["scorer"]]["partidos"].append(jugador["date"])
                    goleadores[jugador["scorer"]]["minutos"] += float(jugador["minute"])

    if len(goleadores) > 1:
        mayor = -1
        for scorer, data in goleadores.items():
            if data["goles"] > mayor:
                mayor = data["goles"]
                top = scorer
        

        for scorer, data in goleadores.items():
            if (data["goles"] == mayor) and (scorer == top):
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)
    
    else:
        for scorer, data in goleadores.items():
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)

    return autogoles, penales, rta 

def find_type_goals(range_team_matches, range_goals_team):
    
    data_team_matches = lt.newList("ARRAY_LIST")
    data_match = {}
    
    for match in lt.iterator(range_team_matches):
        match_info = (match['date'], match['home_team'], match['away_team'])
        data_match[match_info] = {
                                    "date" : match["date"],
                                    "home_score" : match["home_score"],
                                    "away_score" : match["away_score"],
                                    "home_team" : match["home_team"],
                                    "away_team" : match["away_team"],
                                    "city" : match["city"],
                                    "country" : match["country"],
                                    "tournament" : match["tournament"],                                
                                    "penalty" : "Unknown",
                                    "own_goal" : "Unknown"
                                 } 

    for goal in lt.iterator(range_goals_team):
        match_info2 = (goal['date'], goal['home_team'], goal['away_team']) 

        if match_info2 in data_match:   
            if goal["penalty"] == "True":
                data_match[match_info2]["penalty"] = "True"

            if data_match[match_info2]["penalty"] != "True" and goal["penalty"] == "False":
                data_match[match_info2]["penalty"] = "False"

            if goal["own_goal"] == "True":
                data_match[match_info2]["own_goal"] = "True"

            if data_match[match_info2]["own_goal"] != "True" and goal["own_goal"] == "False":
                data_match[match_info2]["own_goal"] = "False" 
        
    for info in data_match.values():
        lt.addLast(data_team_matches, info)

    return data_team_matches

def find_best_player_own_goals_penalties_req_6(goal_scorers, team):

    """Funcion que calcula los autogoles, los penales y busca el mejor
    jugador a partir de un equipo y una isto filtrada de goal scorers"""

    autogoles = 0
    penales = 0
    goleadores = {}
    rta = lt.newList("ARRAY_LIST")

    for jugador in lt.iterator(goal_scorers):
        if jugador["away_team"] == team or jugador["home_team"] == team:

            if jugador["own_goal"] == "True" and jugador["team"] == team:
                autogoles += 1
            if jugador["penalty"] == "True"  and jugador["team"] == team:
                penales += 1
        
            if jugador["own_goal"] != "True":

                if jugador["scorer"] not in goleadores:
                    goleadores[jugador["scorer"]] = {}
                    goleadores[jugador["scorer"]]["goles"] = 1
                    goleadores[jugador["scorer"]]["partidos"] = [jugador["date"]]
                    goleadores[jugador["scorer"]]["minutos"] = float(jugador["minute"])
                    
                else:
                    goleadores[jugador["scorer"]]["goles"] += 1
                    if jugador["date"] not in goleadores[jugador["scorer"]]["partidos"]:
                        goleadores[jugador["scorer"]]["partidos"].append(jugador["date"])
                    goleadores[jugador["scorer"]]["minutos"] += float(jugador["minute"])

    if len(goleadores) > 1:
        mayor = -1
        for scorer, data in goleadores.items():
            if data["goles"] > mayor:
                mayor = data["goles"]
                top = scorer
        

        for scorer, data in goleadores.items():
            if (data["goles"] == mayor) and (scorer == top):
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)
    
    else:
        for scorer, data in goleadores.items():
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)

    return autogoles, penales, rta 

def find_goal_scorers(goal_scorers, partido):

    rta_final = lt.newList("ARRAY_LIST")

    for anotacion in lt.iterator(goal_scorers):

        if (anotacion["date"] == partido["date"]) and (anotacion["home_team"] == partido["home_team"]) and (anotacion["away_team"] == partido["away_team"]):

            scorer = anotacion["scorer"]
            team = anotacion["team"]
            minute = anotacion["minute"]
            own_goal = anotacion["own_goal"]
            penalty = anotacion["penalty"]

            rta = {"date" : partido["date"],
                    "home_team" : partido["home_team"],
                    "away_team" : partido["away_team"],
                    "scorer" : scorer,
                    "team" : team,
                    "minute" : minute,
                    "penalty" : penalty,
                    "own_goal" : own_goal
                        }
            lt.addLast(rta_final, rta)

    if lt.size(rta_final) == 0:

            rta = {"date" : partido["date"],
                    "home_team" : partido["home_team"],
                    "away_team" : partido["away_team"],
                    "scorer" : "Unknown",
                    "team" : "Unknown",
                    "minute" :"Unknown",
                    "penalty" : "Unknown",
                    "own_goal" : "Unknown"
                        }
            lt.addLast(rta_final, rta)
    
    else:
        rta_final = sa.sort(rta_final, cmp_anotaciones_by_minuto)
            
    return rta_final 

def find_goal_scorers_2(goal_scorers, partidos):

    rta = lt.newList("ARRAY_LIST")

    for partido in lt.iterator(partidos):
        for anotacion in lt.iterator(goal_scorers):
            if (anotacion["date"] == partido["date"]) and (anotacion["home_team"] == partido["home_team"]) and (anotacion["away_team"] == partido["away_team"]):
                lt.addFirst(rta, anotacion)

    return rta

def cmp_total_point(points_1, points_2):
    rta = False
    puntos_1 = points_1["total_points"]
    puntos_2 = points_2["total_points"]
    diferencia_1 = points_1["goal_difference"]
    diferencia_2 = points_2["goal_difference"] 
    penal_1 = points_1["penalty_points"]
    penal_2 = points_2["penalty_points"]
    if puntos_1 > puntos_2:
        rta = True
    elif puntos_1== puntos_2:
        if diferencia_1 > diferencia_2:
            rta = True
        elif diferencia_1 == diferencia_2:
            if penal_1 > penal_2:
                rta = True
    return rta 

def cmp_partidos_by_fecha_y_pais(resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelva falso (False).
    Args:
        Resultado1: información del primer registro de resultados FIFA que incluye 
        “date” y el “country” 
        impuesto2: información del segundo registro de resultados FIFA que incluye 
        “date" y el "country" 
    """
    rta = False
    fecha_1 = ((dt.strptime(resultado1["date"],"%Y-%m-%d")).date()).toordinal()
    fecha_2 = ((dt.strptime(resultado2["date"],"%Y-%m-%d")).date()).toordinal()
    pais_1 = resultado1["country"]
    pais_2 = resultado2["country"] 
    if fecha_1 > fecha_2:
        rta = True
    elif fecha_1== fecha_2:
        if pais_1 < pais_2:
            rta = True
    return rta 

def cmp_jugadores_by_puntaje(resultado1, resultado2):
    rta = False
    puntaje_1 = resultado1["puntaje"]    
    puntaje_2 = resultado2["puntaje"]
    goles_totales1 = resultado1["total_goals"]
    goles_totales2 = resultado2["total_goals"]
    if puntaje_1 > puntaje_2:
        rta = True
    elif puntaje_1 == puntaje_2:
        if goles_totales1 > goles_totales2:
            rta = True
    return rta

def cmp_partidos_by_fecha(resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es mayor que en el resultado2,
    de lo contrario devuelva falso (False).
    Args:
        Resultado1: información del primer registro de resultados FIFA que incluye 
        “date” 
        impuesto2: información del segundo registro de resultados FIFA que incluye 
        “date" 
    """
    rta = False
    fecha_1 = ((dt.strptime(resultado1["date"],"%Y-%m-%d")).date()).toordinal()
    fecha_2 = ((dt.strptime(resultado2["date"],"%Y-%m-%d")).date()).toordinal()
    if fecha_1 > fecha_2:
        rta = True
    return rta 
                
def sort_results (sorting, resuts):
    if sorting == "sa":
        sorted_list = sa.sort(resuts, cmp_partidos_by_fecha_y_pais)
    elif sorting == "se":
        sorted_list = se.sort(resuts, cmp_partidos_by_fecha_y_pais)
    elif sorting == "ins":
        sorted_list = ins.sort(resuts, cmp_partidos_by_fecha_y_pais)
    elif sorting == "merg":
        sorted_list = merg.sort(resuts, cmp_partidos_by_fecha_y_pais)
    elif sorting == "quk":
        sorted_list = quk.sort(resuts, cmp_partidos_by_fecha_y_pais)
    return sorted_list 

def cmp_elementos_by_fecha_y_minuto(resultado1, resultado2):
    """
    
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el minuto de la anotacion,
    de lo contrario devuelva falso (False).
    Args:
        Resultado1: información del primer registro de resultados FIFA que incluye 
        “date” y el “minute"
        impuesto2: información del segundo registro de resultados FIFA que incluye 
        “date" y el "minute" 
    """

    rta = False
    fecha_1 = ((dt.strptime(resultado1["date"],"%Y-%m-%d")).date()).toordinal()
    fecha_2 = ((dt.strptime(resultado2["date"],"%Y-%m-%d")).date()).toordinal()
    minute_1 = resultado1["minute"]
    minute_2 = resultado2["minute"]
    
    if fecha_1 > fecha_2:
            rta = True
    elif fecha_1 == fecha_2:
        if minute_1 < minute_2:
            rta = True
    return rta 

def cmp_elementos_by_fecha_y_minuto2(resultado1, resultado2):
    """
    
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el minuto de la anotacion,
    de lo contrario devuelva falso (False).
    Args:
        Resultado1: información del primer registro de resultados FIFA que incluye 
        “date” y el “minute"
        impuesto2: información del segundo registro de resultados FIFA que incluye 
        “date" y el "minute" 
    """

    rta = False
    fecha_1 = ((dt.strptime(resultado1["date"],"%Y-%m-%d")).date()).toordinal()
    fecha_2 = ((dt.strptime(resultado2["date"],"%Y-%m-%d")).date()).toordinal()
    minute_1 = resultado1["minute"]
    minute_2 = resultado2["minute"]
    
    if fecha_1 < fecha_2:
            rta = True
    elif fecha_1 == fecha_2:
        if minute_1 < minute_2:
            rta = True
    return rta 

def cmp_anotaciones_by_minuto(elemento1, elemento2):
    minuto1 = elemento1["minute"]
    minuto2 = elemento2["minute"]
    rta = False

    if minuto1 < minuto2:
        rta = True
    return rta 

def sort_scorers (sorting, goal_scorers):
    
    if sorting == "sa":
        sorted_list = sa.sort(goal_scorers, cmp_elementos_by_fecha_y_minuto)
    elif sorting == "se":
        sorted_list = se.sort(goal_scorers, cmp_elementos_by_fecha_y_minuto)
    elif sorting == "ins":
        sorted_list = ins.sort(goal_scorers, cmp_elementos_by_fecha_y_minuto)
    elif sorting == "merg":
        sorted_list = merg.sort(goal_scorers, cmp_elementos_by_fecha_y_minuto)
    elif sorting == "quk":
        sorted_list = quk.sort(goal_scorers, cmp_elementos_by_fecha_y_minuto)
    return sorted_list 

def cmp_anotaciones_by_fecha_Y_equipo (resultado1, resultado2):

    rta = False
    fecha_1 = ((dt.strptime(resultado1["date"],"%Y-%m-%d")).date()).toordinal()
    fecha_2 = ((dt.strptime(resultado2["date"],"%Y-%m-%d")).date()).toordinal()
    home_team_1 = resultado1["home_team"]
    home_team_2 = resultado2["home_team"] 
    away_team_1 = resultado1["away_team"]
    away_team_2 = resultado2["away_team"]

    if fecha_1 > fecha_2:
        rta = True
    elif fecha_1 == fecha_2:
        if home_team_1 < home_team_2:
            rta = True
        elif home_team_1 == home_team_2:
            if away_team_1 < away_team_2:
                rta = True
    return rta 

def sort_shootouts (sorting, shootouts):
    if sorting == "sa":
        sorted_list = sa.sort(shootouts, cmp_anotaciones_by_fecha_Y_equipo)
    elif sorting == "se":
        sorted_list = se.sort(shootouts, cmp_anotaciones_by_fecha_Y_equipo)
    elif sorting == "ins":
        sorted_list = ins.sort(shootouts, cmp_anotaciones_by_fecha_Y_equipo)
    elif sorting == "merg":
        sorted_list = merg.sort(shootouts, cmp_anotaciones_by_fecha_Y_equipo)
    elif sorting == "quk":
        sorted_list = quk.sort(shootouts, cmp_anotaciones_by_fecha_Y_equipo)
    return sorted_list

def rango_by_fecha(fecha, limite_inferior, limite_superior):
    """
    Devuelve verdadero (True) si la fecha esta dentro del rango estipulado.
    Args:
        Fecha: fecha a comparar
        limite_inferior: fecha en la que incia el rango.
        imite_superior: fecha en la que termina el rango. 
    """
    rta = False
    fecha = ((dt.strptime(fecha,"%Y-%m-%d")).date()).toordinal()
    limite_inferior = ((dt.strptime(limite_inferior,"%Y-%m-%d")).date()).toordinal()
    limite_superior = ((dt.strptime(limite_superior,"%Y-%m-%d")).date()).toordinal()
    if (fecha >= limite_inferior) and (fecha <= limite_superior):
        rta = True
    return rta 

def find_results (results, date, home_team, away_team):
    """
    Busca los datos de results requeridos para completar el requerimiento 
    Args:
        results: lista de resultados
        date, home_team, away_team: son los datos requeridos para comparar y determinar si
        los resultados corresponden a esa fecha
    """
    tournament = "Unknown"
    home_score = "Unknown"
    away_score = "Unknown"

    for r in lt.iterator(results):

        if (r["date"] == date) and (r["home_team"] == home_team) and (r["away_team"] == away_team):
             tournament = r["tournament"]
             home_score = r["home_score"]
             away_score = r["away_score"]

    return tournament, home_score, away_score 