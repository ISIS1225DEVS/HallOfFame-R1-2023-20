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

from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(listType):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {"goalscorers": None,
               "results": None,
               "shootouts ": None}
    catalog["goalscorers"] = lt.newList(listType)
    catalog["results"] = lt.newList(listType)
    catalog["shootouts"] = lt.newList(listType)
    catalog["goalscorers"] = sort_por_fecha_mayor(catalog["goalscorers"])
    catalog["results"] = sort_por_fecha_mayor(catalog["results"])
    catalog["shootouts"] = sort_por_fecha_mayor(catalog["shootouts"])
    return catalog

# Funciones para agregar informacion al modelo

def add_scorers(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["goalscorers"], data)
    return data_structs

def add_results(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["results"], data)
    return data_structs

def add_shootouts(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["shootouts"], data)
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


def data_size_scorers(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["goalscorers"])

def data_size_results(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["results"])

def data_size_shootouts(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["shootouts"])

def sublist(data_structs, filetype):
    sublist = get3main(data_structs, filetype)
    return sublist

def get3(lista):
    sublist = lt.newList("ARRAY_LIST")
    for x in range(0,3):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    for x in range((lt.size(lista)-3),(lt.size(lista))):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    return sublist 

def get3main(data_structs, filetype):
    sublist = lt.newList("ARRAY_LIST")
    lista = data_structs[filetype]
    for x in range(0,3):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    for x in range((lt.size(lista)-3),(lt.size(lista))):
        element = lt.getElement(data_structs[filetype], x)
        lt.addLast(sublist, element)
    return sublist


def req_1_model(catalog, number, team, condition):
    """
    Función que soluciona el requerimiento 1
    """
    lista_results = catalog["results"]
    lista_partidos = lt.newList("ARRAY_LIST")
    for result in lt.iterator(lista_results):
        
        if condition == "home":
            if result["home_team"] == team:
                lt.addLast(lista_partidos,result)
        
        elif condition == "visitor":
            if result["away_team"] == team:
                lt.addLast(lista_partidos,result)
        
        elif condition == "neutral":
            if result["neutral"] == True:
                if result["away_team"] == team or result["home_team"] == team:
                 lt.addLast(lista_partidos,result)
    
    lista_por_fechas = sort_por_fecha_mayor(lista_partidos)
    if lt.size(lista_por_fechas) < number:
        return get3(lista_por_fechas)
    sublist = lt.subList(lista_por_fechas, 1, number)
    
    return get3(sublist)

def req_2_model(catalog, numero_goles, nombre_jugador):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    lista_goalscorers= catalog["goalscorers"]
    lista_jugador = lt.newList("ARRAY_LIST")
    for player in lt.iterator(lista_goalscorers):
        if player["scorer"] == nombre_jugador:
            lt.addLast(lista_jugador, player)
    
    lista_por_fechas = sort_por_fecha_menor(lista_jugador)
    if lt.size(lista_por_fechas) < numero_goles:
        return get3(lista_por_fechas)
    sublist = lt.subList(lista_por_fechas, 1, numero_goles)
    
    return sublist

def req_3_model(catalog, team_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista_results = catalog["results"]
    lista_goalscorers = catalog["goalscorers"]
    lista_partidos = lt.newList("ARRAY_LIST")
    home_games = 0
    away_games = 0
    for result in lt.iterator(lista_results):
        if result["home_team"] == team_name:
                if result["date"] >= initial_date and result["date"] <= final_date:
                    
                    for scorer in lt.iterator(lista_goalscorers):
                        if scorer["home_team"] == result["home_team"] and scorer["date"] == result["date"] and scorer["away_team"] == result["away_team"]:
                            result["own_goal"] = scorer["own_goal"]
                            result["penalty"] = scorer["penalty"]
                        
                    lt.addLast(lista_partidos, result)
                    home_games +=1
        
        elif result["away_team"] == team_name:
            
               if result["date"] >= initial_date and result["date"] <= final_date:
                    for scorer in lt.iterator(lista_goalscorers):
                        if scorer["home_team"] == result["home_team"] and scorer["date"]==result["date"] and scorer["away_team" ]== result["away_team"]:
                            result["own_goal"] = scorer["own_goal"]
                            result["penalty"] = scorer["penalty"]
                    lt.addLast(lista_partidos, result)
                    away_games +=1
    
    total_games = home_games + away_games
    lista_por_fechas = sort_por_fecha_menor(lista_partidos)
    return get3(lista_por_fechas), total_games,home_games, away_games



def req_4_model(catalog, tournament, initial_date, final_date):
    """
    Función que soluciona el requerimiento 4
    """
    answer = lt.newList("ARRAY_LIST")
    country_counter = []
    cities_counter = []
    shootouts_counter = 0
    
    initial_date = datetime.strptime(initial_date, "%Y-%m-%d").date()
    final_date = datetime.strptime(final_date, "%Y-%m-%d").date()
    
    for result in lt.iterator(catalog["results"]):
        if result["tournament"] == tournament and initial_date <= result["date"] <= final_date:
            result["winner"] = "Unknown" 
            for shootout in lt.iterator(catalog["shootouts"]):
                if result["date"] == shootout["date"] and result["home_team"] == shootout["home_team"]:
                    result["winner"] = shootout["winner"]
                    shootouts_counter+=1
            if result["country"] not in country_counter:
                country_counter.append(result["country"])
            if result["city"] not in cities_counter:
                cities_counter.append(result["city"])
            del result["neutral"]
            lt.addLast(answer, result)
    answer = sort_por_fecha_mayor(answer)
            
    return lt.size(answer), len(country_counter), len(cities_counter), shootouts_counter, get3(answer)

def req_5(data_structs, nombre, fecha1, fecha2):
    nueva_lista = lt.newList("ARRAY_LIST")
    data = lt.iterator(data_structs["goalscorers"])
    data2= lt.iterator(data_structs["results"])

    nombre_jug = nombre
    fecha_inicial = datetime.strptime(fecha1, "%Y-%m-%d").date()
    fecha_final = datetime.strptime(fecha2, "%Y-%m-%d").date()
    goles = 0
    autogol = 0
    penalti = 0
    torneos = 0
    torneos_rep=""
    

    for scorer in data:
        

        if scorer["date"] >= fecha_inicial and scorer["date"] <= fecha_final and scorer["scorer"] == nombre_jug:
            goles +=1
            scorer["home_score"] = "Desconocido"
                            
            scorer["away_score"] = "Desconocido"
                            
            scorer["tournament"] = "Desconocido"
            for result in data2:
                if scorer["home_team"] == result["home_team"] and scorer["date"] == result["date"] and scorer["away_team"] == result["away_team"]:
                            
                    
                            scorer["home_score"] = result["home_score"]
                            scorer["away_score"] = result["away_score"]
                            scorer["tournament"] = result["tournament"]
                            
                                
                            if scorer["tournament"] != torneos_rep:
                                torneos_rep == scorer["tournament"]
                                torneos +=1
            del scorer["scorer"]
                

            lt.addLast(nueva_lista, scorer)

            if scorer["own_goal"] == "True":
                autogol += 1
            if scorer["penalty"] == "True":
                penalti += 1

    lista_por_fechas = sort_por_fecha_mayor(nueva_lista)
    return goles, torneos, penalti, autogol , get3(lista_por_fechas)


def req_6_model(data_structs, n, tournament_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 6
    """
    teams_information = lt.newList("ARRAY_LIST")

    initial_date = datetime.strptime(initial_date, "%Y-%m-%d").date()
    final_date = datetime.strptime(final_date, "%Y-%m-%d").date()
    
    unique_teams = set()
    unique_cities = set()
    unique_countries = set()

    for result in lt.iterator(data_structs["results"]):
        if tournament_name == result["tournament"] and initial_date < result["date"] < final_date:
            team1 = result["home_team"]
            team2 = result["away_team"]
            date = result["date"]
            score1 = int(result["home_score"])
            score2 = int(result["away_score"])
            
            found_team1 = False
            for team_info in lt.iterator(teams_information):
                if team_info["name"] == team1:
                    addinfo(data_structs, teams_information, team1, date, score1, score2)
                    found_team1 = True
                    break
            
            if not found_team1:
                newinfo(data_structs, teams_information, team1, date, score1, score2)
                unique_teams.add(team1)

            found_team2 = False
            for team_info in lt.iterator(teams_information):
                if team_info["name"] == team2:
                    addinfo(data_structs, teams_information, team2, date, score2, score1)
                    found_team2 = True
                    break
            
            if not found_team2:
                newinfo(data_structs, teams_information, team2, date, score2, score1)
                unique_teams.add(team2)
            
            unique_cities.add(result["city"])
            unique_countries.add(result["country"])
    
    num_teams = len(unique_teams)
    num_cities = len(unique_cities)
    num_countries = len(unique_countries)

    for team_info in lt.iterator(teams_information):
        team_name = team_info["name"]
        team_goalscorers = []

        for scorer in lt.iterator(data_structs["goalscorers"]):
            if scorer["team"] == team_name:
                minute_str = scorer["minute"]
                if minute_str:
                    minute = float(minute_str)
                else:
                    minute = 0.0

                scorer_info = {
                    "player_name": scorer["scorer"],
                    "total_goals": 1, 
                    "total_matches_with_goals": 1,  
                    "average_time_to_score": minute
                }
                team_goalscorers.append(scorer_info)

        if team_goalscorers:
            top_scorer = max(team_goalscorers, key=lambda x: x["total_goals"])
            team_info["top scorer"] = top_scorer

        for scorer_info in team_goalscorers:
            top_scorer_name = team_info["top scorer"]["player_name"]
            if scorer_info["player_name"] == top_scorer_name:
                team_info["top scorer"]["total_goals"] += scorer_info["total_goals"]
                team_info["top scorer"]["total_matches_with_goals"] += scorer_info["total_matches_with_goals"]
                team_info["top scorer"]["average_time_to_score"] = (
                    team_info["top scorer"]["average_time_to_score"] +
                    scorer_info["average_time_to_score"]) / team_info["top scorer"]["total_matches_with_goals"]
    
    teams_information = sort_por_points(teams_information)

    return teams_information, num_cities, num_countries, num_teams
             
    
def newinfo(data_structs, teams_information, team1, date, score1, score2 ):
    team_info = {"name": team1,
                "total points": total_points(score1, score2),
                "goal difference": goal_difference(score1, score2),
                "matches play": 1,
                "shootout_points":shootout_point(data_structs, date, team1),
                "own_goals_points": owngoals(data_structs, date, team1),
                "wins": wins(score1, score2),
                "draws": draws(score1, score2),
                "losses": losses(score1, score2),
                "goals_for": goals_for(score1),
                "goals_against": goals_against(score2),
                "top scorer": top_scorer(data_structs, date, team1)}
    lt.addLast(teams_information, team_info)
      
def addinfo(data_structs, teams_information, team1, date, score1, score2):
    team_exists = False 

    for team in lt.iterator(teams_information):
        if team["name"] == team1:
            team_exists = True  
            team["total points"] += total_points(score1, score2)
            team["goal difference"] += goal_difference(score1, score2)
            team["matches play"] += 1
            team["shootout_points"] += shootout_point(data_structs, date, team1)
            team["own_goals_points"] += owngoals(data_structs, date, team1)
            team["wins"] += wins(score1, score2)
            team["draws"] += draws(score1, score2)
            team["losses"] += losses(score1, score2)
            team["goals_for"] += goals_for(score1)
            team["goals_against"] += goals_against(score2)
            team["top scorer"] = top_scorer(data_structs, date, team1)

    if not team_exists:
        new_team_info = {
            "name": team1,
            "total points": total_points(score1, score2),
            "goal difference": goal_difference(score1, score2),
            "matches play": 1,
            "shootout_points": shootout_point(data_structs, date, team1),
            "own_goals_points": owngoals(data_structs, date, team1),
            "wins": wins(score1, score2),
            "draws": draws(score1, score2),
            "losses": losses(score1, score2),
            "goals_for": goals_for(score1),
            "goals_against": goals_against(score2),
            "top scorer": top_scorer(data_structs, date, team1)
        }
        lt.addLast(teams_information, new_team_info)

    
def total_points(score1, score2):
    if score1 > score2:
        points = 3
    elif score1 < score2:
        points = 0
    else:
        points = 1 
    return points

def goal_difference(score1, score2):
    return score1-score2

def shootout_point(catalog, date, team):
    for shootout in lt.iterator(catalog["shootouts"]):
        if shootout["date"] == date and (shootout["home_team"] == team or shootout["away_team"] == team )and shootout["winner"] == team:
            return 0
        else:
            return 1

def owngoals(catalog, date, team):
    for scorer in lt.iterator(catalog["goalscorers"]):
        if date == scorer["date"] and (team == scorer["home_team"] or team == scorer["away_team"]):
            if scorer["own_goal"]==True:
                return 1 
            
    return 0  
            
def wins(score1, score2):
    if score1 > score2:
        return 1 
    else: 
        return 0 
         
def draws(score1, score2):
    if score1 == score2:
        return 1
    else: 
        return 0  
         
def losses(score1, score2):
    if score1 < score2:
        return 1  
    else: 
        return 0 

def goals_for( score):
    return score

def goals_against(score):
    return score

def top_scorer(catalog, date, team):
    for scorer in lt.iterator(catalog["goalscorers"]):
        if scorer["date"] == date and (scorer["home_team"] == team or scorer["away_team"] == team):
            return scorer["scorer"]


def total_points(penalty, own_goal):
    if penalty == "False" and  own_goal == "False":
        
        
        
        return 1
    elif penalty == "True" and  own_goal == "False":
        
        
        return 1
    elif penalty == "False" and  own_goal == "True":
        return -1
        


def sort_total_points(total1 , total2):
    total_p1 = total1["total_points"]
    total_p2 = total2["total_points"]
    
    return total_p2 < total_p1

def sort_total_points_f(ranking_jugadores):
    newlist = merg.sort(ranking_jugadores, sort_total_points)
    return newlist
    

def req_7(data_structs , num_jugadores , fecha1 , fecha2 ):
    """
    Función que soluciona el requerimiento 7
    
    """
    ranking_jugadores = lt.newList("ARRAY_LIST")
    probar = []
    fecha_inicial = datetime.strptime(fecha1, "%Y-%m-%d").date()
    fecha_final = datetime.strptime(fecha2, "%Y-%m-%d").date()
    
    data = lt.iterator(data_structs["goalscorers"])
    data2 = lt.iterator(data_structs["results"])
    data3 = lt.iterator(data_structs["shootouts"])
    
    tournament = 0
    torneos_rep = ""
    goles_winner = 0
    goles_losses = 0
    goles_draws = 0
    dicts = {}
    total_players = 0
    
    
    player_total_points = {}
    
    home_match = ""
    away_match = ""
    cantidad_match = 0
    
    nombre = ""
    goles = 0
    
    total_goles = 0
    autogoles = 0
    goles_list = {}
    own_goals_list = {}
    for scorer in data:
        
        if scorer["date"] >= fecha_inicial and scorer["date"] <= fecha_final:
            goles +=1
            resultado = 0
            if scorer["scorer"] != nombre:
                nombre = scorer["scorer"]

                total_players +=1
            if scorer["penalty"] == "True":
               total_goles +=1
            if scorer["own_goal"] == "True":
                autogoles +=1
            
            if scorer["penalty"] == "False" and  scorer["own_goal"] == "False":
                
                
                resultado = 1

            elif scorer["penalty"] == "True" and  scorer["own_goal"] == "False":
                
                resultado = 1

            elif scorer["penalty"] == "False" and  scorer["own_goal"] == "True":
                
                resultado = -1

            player_name = scorer["scorer"]
            if player_name not in player_total_points:
                
                player_total_points[player_name] = 0
            player_total_points[player_name] += resultado
            
            player_name2 = scorer["scorer"]
            if player_name2 not in goles_list:
                goles_list[player_name2] = 0
            goles_list[player_name2] += 1    

            if scorer["home_team"] != home_match and scorer["away_team"] != away_match:
                home_match = scorer["home_team"]
                away_match = scorer["away_team"]
                cantidad_match +=1
  
            for result in data2:
                if result["tournament"] != "Friendly":
                    if scorer["home_team"] == result["home_team"] and scorer["date"] == result["date"] and scorer["away_team"] == result["away_team"]:
                
                    
                        scorer["tournament"] = result["tournament"]
                        if scorer["tournament"] != torneos_rep:
                                    torneos_rep = scorer["tournament"]
                                    tournament +=1
            
            for shoot in data3:
                if scorer["home_team"] == shoot["home_team"] and scorer["date"] == shoot["date"] and scorer["away_team"] == shoot["away_team"]:
                    scorer["winner"] = shoot["winner"]
                            
                    if scorer["winner"] == scorer["team"]:
                        goles_winner +=1
                            
                    elif scorer["winner"] != scorer["team"]:
                        goles_losses +=1
                    else:
                        goles_draws+=1
                        
                if scorer["scorer"] not in dicts:
                    
                    
                            
                    dicts = {"name": scorer["scorer"],
                             
                                "total_points":  player_total_points[player_name],
                                "total_goals" : goles_list[player_name2],
                                "penalty_goals" : scorer["penalty"],
                                "own_goal" : scorer["own_goal"],
                                "avg_time" : scorer["minute"],
                                "total_tournaments" : tournament,
                                "scored_in_wins": goles_winner, 
                                "scored_in_losses": goles_losses,
                                "scored_in_draws":goles_draws , 
                                "last_goal" : scorer }
                    
                            
                    lt.addLast(ranking_jugadores ,dicts)
                    break
                
                
                            
        

                            
        ranking_jugadores = sort_total_points_f(ranking_jugadores)
        

    return total_players , cantidad_match , goles , total_goles , autogoles , get3(ranking_jugadores)


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass




# Funciones utilizadas para comparar elementos dentro de una lista

def compareratings(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
# Funciones utilizadas para organizar una lista 
def sort_por_fecha_mayor(lista_partidos):
    """ 
    Filtramos la lista por fecha de mayor a menor.
    """
    newlist = merg.sort(lista_partidos, cmp_date_mayor_to_minor)
    return newlist

def sort_por_fecha_menor(lista_partidos):
    """ 
    Filtramos la lista por fecha de menor a mayor.
    """
    newlist = merg.sort(lista_partidos, cmp_date_minor_to_mayor)
    return newlist

def cmp_date_mayor_to_minor(match1,match2):
    date1 = match1["date"]
    date2 = match2["date"] 
    
    return date1 > date2

def cmp_date_minor_to_mayor(match1,match2):
    date1 = match1["date"]
    date2 = match2["date"] 
    
    return date1 < date2

def cmp_date_match(match1, match2):
    
    date1 = match1["date"]
    date2 = match2["date"]
    country1 = match1["country"]
    country2 = match2["country"]
    
    if date1 == date2:
        return country1 < country2
    return date1 < date2

def sort(data_structs, sort_type):
    partidos = data_structs["results"]
    sorted_list = sort_type.sort(partidos, cmp_date_match)
    return sorted_list

def sort_por_points(lista_partidos):
    """ 
    Filtramos la lista por fecha de menor a mayor.
    """
    newlist = merg.sort(lista_partidos, cmp_points)
    return newlist

def cmp_points(point1, point2):
    point1 = point1["total points"]
    point2 = point2["total points"]