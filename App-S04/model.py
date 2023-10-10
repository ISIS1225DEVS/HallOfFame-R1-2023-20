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
from datetime import date
from tabulate import tabulate
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


def new_Catalog(list_type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'goalscorers': None,
               'results': None,
               'shootouts': None}

    catalog['goalscorers'] = lt.newList(list_type,
                                cmpfunction= compareGoalscorersDate)
    catalog['results'] = lt.newList(list_type,
                                cmpfunction=compareResults)
    catalog['shootouts'] = lt.newList(list_type,
                                cmpfunction=compareShootouts)
    return catalog


# Funciones para agregar informacion al modelo

def add_goalscorer(catalog,goal):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    goalscorers = new_goalscorer(goal['date'], goal['home_team'],goal['away_team'], goal['team'],goal['scorer'], goal['minute'],
                        goal['own_goal'], goal['penalty'])
    lt.addLast(catalog['goalscorers'], goalscorers)
    return catalog

def add_results(catalog,res):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    results = new_results(res['date'], res['home_team'],res['away_team'], res['home_score'],res['away_score'], res['tournament'],
                        res['city'], res['country'],res['neutral'])
    lt.addLast(catalog['results'], results)
    return catalog
    
def add_shootouts(catalog,shoot):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    shootouts = new_shootouts(shoot['date'], shoot['home_team'],shoot['away_team'], shoot['winner'])
    lt.addLast(catalog['shootouts'], shootouts)
    return catalog

# Funciones para creacion de datos

def new_goalscorer(date,home,away,team,scorer,minute,own,penalty):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    goalscorer = {'date': '', 'home_team': '','away_team': '', 'team': '','scorer': '', 'minute': '','own_goal': '', 'penalty': ''}
    goalscorer['date'] = date 
    goalscorer['home_team'] = home
    goalscorer['away_team'] = away
    goalscorer['team'] = team
    goalscorer['scorer'] = scorer
    goalscorer['minute'] = minute
    goalscorer['own_goal'] = own
    goalscorer['penalty'] = penalty
    return goalscorer

def new_results(date,team,away,home,scorer,tournament,city,country,neutral):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    res = {'date' : '','home_team': '','away_team': '', 'home_score': '','away_score': '', 'tournament': '',
           'city': '', 'country': '', 'neutral': ''}
    res['date'] = date 
    res['home_team'] = team
    res['away_team'] = away
    res['home_score'] = home
    res['away_score'] = scorer
    res['tournament'] = tournament
    res['city'] = city
    res['country'] = country
    res['neutral'] = neutral
    return res

def new_shootouts(date,team,away,winner):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    shoot = {'date' : '','home_team': '','away_team': '', 'winner': ''}
    shoot['date'] = date
    shoot['home_team'] = team
    shoot['away_team'] = away
    shoot['winner'] = winner
    return shoot

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    return data_structs[id]

def get_sublist_data(data, pos, numelem):
    return lt.subList(data, pos, numelem) 

def get_sublist(catalog, pos, numelem, id):
    data = catalog[id]
    return lt.subList(data, pos, numelem) 

def goalscorersSize(catalog):
    return lt.size(catalog['goalscorers'])


def resultsSize(catalog):
    return lt.size(catalog['results'])


def shootoutsSize(catalog):
    return lt.size(catalog['shootouts'])

def req_1(catalog, num_matches, team_name, team_condition):
    """
    ARGS: catalog con información de resultados ya ordenada por fechas de más reciente a más vieja, número de partidos
    a consultar, nombre del equipo de interés, condición del equipo en el partido.
    RET: LISTA ENCADENADA de la cantidad deseada de partidos
    """
    results = catalog['results']
    results_size = lt.size(results)
    team_matches = lt.newList('ARRAY_LIST')
    total_matches = 0
    for result_index in range(1, results_size + 1):
        match = lt.getElement(results, result_index)
        if team_condition == 'HOME':
            if match['home_team'] == team_name:
                total_matches += 1
                lt.addLast(team_matches, match)
        elif team_condition == 'AWAY':
            if match['away_team'] == team_name:
                total_matches += 1
                lt.addLast(team_matches, match)
        else:
            if (match['home_team'] == team_name) or (match['away_team'] == team_name):
                total_matches += 1
                lt.addLast(team_matches, match)
        if total_matches == num_matches:
            break
    return team_matches, total_matches

def req_2(control,nombre,numero,list_type,algorithm):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    goles = lt.newList(list_type,compareGoalscorersDate)
    for goal in lt.iterator(control['model']['goalscorers']):
        if goal['scorer'] == nombre:
            lt.addLast(goles,goal)
    sortByCriteria(goles,algorithm,compareGoalscorersDateInv)
    
    if numero >= lt.size(goles):
        return goles,lt.size(goles)
    else:
        return lt.subList(goles,1,numero),lt.size(goles)
        

def compare_dates(match):
    """
    Función auxiliar para comparar las fechas de los partidos.
    """
    return date.fromisoformat(match['date'])

def find_shootouts_in_dates(catalog, team_name, start_date, end_date, startpos=1):
    date_start = date.fromisoformat(start_date)
    date_end = date.fromisoformat(end_date)
    team_shootouts = lt.newList('ARRAY_LIST')
    shootouts = catalog['shootouts']
    shootout_size = lt.size(shootouts)
    final_index = shootout_size + 1
    for shootout_index in range(startpos, shootout_size + 1):
        shootout = lt.getElement(shootouts, shootout_index)
        shootout_date = date.fromisoformat(shootout['date'])
        if ((shootout['home_team'] == team_name) or (shootout['away_team'] == team_name)) and (date_start <= shootout_date) and (shootout_date <= date_end):
            lt.addLast(team_shootouts, shootout)
        if shootout_date > date_end:
            final_index = shootout_index
            break
    if lt.size(team_shootouts) == 0:
        return None
    else:
        return team_shootouts, final_index
    
def find_scorers_in_dates(catalog, team_name, start_date, end_date, startpos=1):
    date_start = date.fromisoformat(start_date)
    date_end = date.fromisoformat(end_date)
    team_scorers = lt.newList('ARRAY_LIST')
    scorers = catalog['goalscorers']
    scorers_size = lt.size(scorers)
    final_index = scorers_size + 1
    for scorers_index in range(startpos, scorers_size + 1):
        scorer = lt.getElement(scorers, scorers_index)
        scorer_date = date.fromisoformat(scorer['date'])
        if (scorer['team'] == team_name) and (date_start <= scorer_date) and (scorer_date <= date_end):
            lt.addLast(team_scorers, scorer)
        if scorer_date > date_end:
            final_index = scorers_index
            break
    if lt.size(team_scorers) == 0:
        return None
    else:
        return team_scorers, final_index
    
def find_results_in_dates(catalog, team_name, start_date, end_date, startpos=1):
    date_start = date.fromisoformat(start_date)
    date_end = date.fromisoformat(end_date)
    team_results = lt.newList('ARRAY_LIST')
    results = catalog['results']
    results_size = lt.size(results)
    final_index = results_size + 1
    for result_index in range(startpos, results_size + 1):
        result = lt.getElement(results, result_index)
        result_date = date.fromisoformat(result['date'])
        if ((result['home_team'] == team_name) or (result['away_team'] == team_name)) and (date_start <= result_date) and (result_date <= date_end):
            lt.addLast(team_results, result)
        if result_date > date_end:
            final_index = result_index
            break
    if lt.size(team_results) == 0:
        return None
    else:
        return team_results, final_index
    

def req_3(catalog, team_name, start_date, end_date):
    """
    Función que soluciona el requerimiento 3
    """
    results = catalog.get('results')  
    if results is None:
        return None  

    results_size = lt.size(results)
    team_home_matches = lt.newList('ARRAY_LIST')
    team_away_matches = lt.newList('ARRAY_LIST')
    total_home_matches = 0
    total_away_matches = 0

    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)

    for result_index in range(1, results_size + 1):
        match = lt.getElement(results, result_index)
        match_date = date.fromisoformat(match['date'])

        if start_date <= match_date <= end_date:
            if match['home_team'] == team_name:
                total_home_matches += 1
                lt.addLast(team_home_matches, match)
            elif match['away_team'] == team_name:
                total_away_matches += 1
                lt.addLast(team_away_matches, match)

    def custom_sort(match1, match2):
         return match1['date'] - match2['date']

    sa.sort(team_home_matches, custom_sort)
    sa.sort(team_away_matches, custom_sort)

    return team_home_matches, team_away_matches, total_home_matches, total_away_matches


def req_4(catalog, tournament_name, start, end):
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    tournament_matches = lt.newList('ARRAY_LIST')
    cities = lt.newList('ARRAY_LIST')
    countries = lt.newList('ARRAY_LIST')
    results = catalog['results']
    shootouts = catalog['shootouts']
    shootout_start_index = 1
    total_shootouts = 0
    total_countries = 0
    total_cities = 0
    total_matches = 0 
    winner = ['']
    
    for result_index in range(1, lt.size(results) + 1):
        result = lt.getElement(results, result_index)
        match_date = date.fromisoformat(result['date'])
        if (start_date <= match_date) and (end_date >= match_date):
            if result['tournament'] == tournament_name:
                total_matches += 1
                if result['home_score'] == result['away_score']:
                    for shootout_index in range(shootout_start_index, lt.size(shootouts) + 1):
                        shootout = lt.getElement(shootouts, shootout_index)
                        if date.fromisoformat(shootout['date']) == match_date and shootout['home_team'] == result['home_team']:
                            winner[0] = shootout['winner']
                            shootout_start_index = shootout_index
                            total_shootouts += 1
                            break
                else: 
                    winner[0] = 'Unknown'
                tournament_match = new_match(result, winner[0])
                if lt.size(tournament_matches) == 0:
                    lt.addFirst(tournament_matches, tournament_match)
                    lt.addFirst(countries, tournament_match['country'])
                    lt.addFirst(cities, tournament_match['city'])
                else:
                    lt.addLast(tournament_matches, tournament_match)
                    if lt.isPresent(cities, tournament_match['city']) == 0:
                        lt.addFirst(cities, tournament_match['city'])
                        total_cities += 1
                    if lt.isPresent(countries, tournament_match['country']) == 0:
                        lt.addFirst(countries, tournament_match['country'])
                        total_countries += 1          
    if total_matches == 0:
        return None, None, None, None, None
    tournament_matches = merg.sort(tournament_matches, compare_tournament_matches)
    return tournament_matches, total_matches, total_shootouts, total_countries, total_cities

def new_match(result, winner):
    match = {'date' : '','tournament' : '', 'country' : '', 'city' : '', 'home_team' : '' , 'away_team' : '' ,
             'home_score' : '', 'away_score' : '', 'winner' : ''}
    match['date'] = result['date']
    match['tournament'] = result['tournament']
    match['country'] = result['country']
    match['city'] = result['city']
    match['home_team'] = result['home_team']
    match['away_team'] = result['away_team']
    match['home_score'] = result['home_score']
    match['away_score'] = result['away_score']
    match['winner'] = winner
    return match
def compare_tournament_matches(t1, t2):
    if (compareByDate(t1, t2) == 0) and(type(compareByDate(t1, t2)) == type(0)):
        if (compareByCountry(t1, t2)  == 0) and (type(compareByCountry(t1, t2)) == type(0)):
            return compareByCity(t1, t2)
        else:
            return compareByCountry(t1, t2)
    else:
        return compareByDate(t1, t2)
        
def req_5(control,player,fechain,fechafin,list_type,algorithm):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    date1 = date.fromisoformat(fechain)
    date2 = date.fromisoformat(fechafin)
    penal = 0
    auto = 0 
    encuentros = lt.newList(list_type,cmpfunction=compareResults)
    torneos = lt.newList(list_type)
    goles = lt.newList(list_type,cmpfunction= compareGoalscorersDate)
    #conteo de goles autogoles y penales 
    for goal in lt.iterator(control['model']['goalscorers']):
        fecha = date.fromisoformat(goal['date']) 
        if (goal['scorer'] == player) and (date1 <= fecha) and (date2 >= fecha):
            lt.addLast(goles,goal)
            if goal['penalty'] == True:
                penal += 1
            if goal['own_goal'] == True:
                auto += 1
    if lt.size(goles) == 0:
        return None
    
    sortByCriteria(goles,algorithm,compareGoalscorersDate)
    
    for goal in lt.iterator(goles):
        for resultado in lt.iterator(control['model']['results']):
            if goal['date'] == resultado['date']:
                if (goal['home_team'] == resultado['home_team']) and (goal['away_team'] == resultado['away_team']):
                    if lt.isPresent(encuentros,resultado) == 0: 
                        lt.addLast(encuentros,resultado)
    
    for encuentro in lt.iterator(encuentros):
        if lt.isPresent(torneos,encuentro['tournament']) == 0:
            lt.addLast(torneos,encuentro['tournament'])
    if lt.isPresent(torneos,'Friendly') != 0:
        lt.removeLast(torneos)
        
    
    return (penal,auto,encuentros,torneos,goles)

def req_6(catalog, tournament_name, start_date, end_date, num_teams):
    """
    Función que soluciona el requerimiento 6
    """
    results = catalog['results']
    shootouts = catalog['shootouts']

    filtered_results = []
    for result in results:
        result_date = date.fromisoformat(result['date'])
        if result['tournament'] == tournament_name and start_date <= result_date <= end_date:
            filtered_results.append(result)

    teams_stats = {}
    for result in filtered_results:
        home_team = result['home_team']
        away_team = result['away_team']
        home_score = int(result['home_score'])
        away_score = int(result['away_score'])

        if home_team not in teams_stats:
            teams_stats[home_team] = {'points': 0, 'goals_diff': 0, 'goals_scored': 0, 'matches_played': 0,
                                      'penalty_points': 0, 'auto_goal_points': 0, 'victories': 0, 'draws': 0, 'defeats': 0,
                                      'top_scorer': {'name': 'Unknown', 'total_goals': 0, 'matches_with_goals': 0, 'avg_minutes_per_goal': 0}}
        teams_stats[home_team]['matches_played'] += 1
        teams_stats[home_team]['goals_scored'] += home_score
        teams_stats[home_team]['goals_diff'] += (home_score - away_score)
        
    top_teams = []
    for _ in range(num_teams):
        max_points = -1
        top_team = None
        for team_name, stats in teams_stats.items():
            if stats['points'] > max_points and team_name not in top_teams:
                max_points = stats['points']
                top_team = team_name
        if top_team is not None:
            top_teams.append(top_team)
            
    results_dict = {team_name: teams_stats[team_name] for team_name in top_teams}
    return results_dict


def req_7(control,fechain,fechafin,list_type,algorithm):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    date1 = date.fromisoformat(fechain)
    date2 = date.fromisoformat(fechafin)
    penal = 0
    auto = 0 
    encuentros = lt.newList(list_type,cmpfunction=compareResults)
    torneos = lt.newList(list_type)
    goles = lt.newList(list_type,cmpfunction= compareGoalscorersDate)
    jugadores = lt.newList(list_type,cmpfunction=compareJugadorByName)
    for goal in lt.iterator(control['model']['goalscorers']):
        fecha = date.fromisoformat(goal['date']) 
        if (date1 <= fecha) and (date2 >= fecha):
            torneo = 'Desconocido'
            for resultado in lt.iterator(control['model']['results']):
                if goal['date'] == resultado['date']:
                    if (goal['home_team'] == resultado['home_team']) and (goal['away_team'] == resultado['away_team']):
                        torneo = resultado['tournament']
                        if torneo != 'Friendly':
                            if lt.isPresent(encuentros,resultado) == 0: 
                                lt.addLast(encuentros,resultado)  
                            if lt.isPresent(torneos,torneo) == 0: 
                                lt.addLast(torneos,torneo)      
            if torneo != 'Friendly':
                lt.addLast(goles,goal)
                if goal['penalty'] == 'True':
                    penal += 1
                if goal['own_goal'] == 'True':
                    auto += 1
    
    if lt.size(goles) == 0:
        return None
    
    for goal in lt.iterator(goles):
        if lt.isPresent(jugadores,goal['scorer']) == 0: 
            player = newPLayer()
            player['name'] = goal['scorer'] 
            player['goles'] = 1
            if goal['penalty'] == 'True':
                player['penalty'] += 1 
            if goal['own_goal'] == 'True':
                player['autogoles'] += 1 
            if goal['minute'] != '':
                player['promedio'] = float(goal['minute'])
            player['ultimo_gol'] = goal 
            
            
            for encuentro in lt.iterator(encuentros):
                if encuentro['date'] == goal['date']:
                    if (encuentro['home_team'] == goal['home_team']) and (encuentro['away_team'] == goal['away_team']):
                        lt.addLast(player['torneos'],encuentro['tournament'])
                        winner = ganador(encuentro['home_team'],encuentro['away_team'],
                                         int(encuentro['home_score']),int(encuentro['away_score']))
                        if winner == 'empate':
                            player['goles_empate'] += 1
                        elif winner == goal['team']:
                            player['goles_victoria'] +=1
                        else:
                            player['goles_derrota'] += 1
            lt.addLast(jugadores,player)
            
        else:
            pos = lt.isPresent(jugadores,goal['scorer'])
            player = lt.getElement(jugadores,pos)
            player['goles'] += 1
            if goal['penalty'] == 'True':
                player['penalty'] += 1 
            if goal['own_goal'] == 'True':
                player['autogoles'] += 1 
            if goal['minute'] != '':
                player['promedio'] = float(goal['minute']) + player['promedio']
            date3 = date.fromisoformat(goal['date'])
            date4 = date.fromisoformat(player['ultimo_gol']['date']) 
            if date3 > date4:
                player['ultimo_gol'] = goal 
            elif date3 == date4:
                if goal['minute'] != " " and player['ultimo_gol']['minute'] != " ":
                    if float(goal['minute']) > float(player['ultimo_gol']['minute']):
                        player['ultimo_gol'] = goal     
              
            for encuentro in lt.iterator(encuentros):
                if encuentro['date'] == goal['date']:
                    if (encuentro['home_team'] == goal['home_team']) and (encuentro['away_team'] == goal['away_team']):
                        if lt.isPresent(player['torneos'],encuentro['tournament']) == 0:
                            lt.addLast(player['torneos'],encuentro['tournament'])
                        winner = ganador(encuentro['home_team'],encuentro['away_team'],
                                         int(encuentro['home_score']),int(encuentro['away_score']))
                        if winner == 'empate':
                            player['goles_empate'] += 1
                        elif winner == goal['team']:
                            player['goles_victoria'] +=1
                        else:
                            player['goles_derrota'] += 1        
            #lt.changeInfo(jugadores,pos,player)
    for player in lt.iterator(jugadores):
        player['puntaje'] = player['goles'] + player['penalty'] - player['autogoles']
        player['promedio'] = round(player['promedio'] / player['goles'],2)
    
        for encuentro in lt.iterator(encuentros):
            if encuentro['date'] == player['ultimo_gol']['date']:
                if (encuentro['home_team'] == player['ultimo_gol']['home_team']) and (encuentro['away_team'] == player['ultimo_gol']['away_team']):
                    player['ultimo_partido'] = encuentro
          
    sortByCriteria(jugadores,algorithm,comparePlayerByPuntaje)
    
    return(jugadores,encuentros,goles,torneos,penal,auto)
            
def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    
    pass

def determine_years_for_statistic(date1, date2):
    start_date = date.fromisoformat(date1)
    end_date = date.fromisoformat(date2)
    if start_date == end_date:
        return None
    ranges = lt.newList('ARRAY_LIST')
    start_year = start_date.year
    end_year = end_date.year 
    range_year = start_year
    while range_year <= end_year:
        print(range_year)
        date_range = ['','']
        date_range[0] = str(range_year) + '-01-01'
        date_range[1] = str(range_year) + '-12-31'
        print(date_range)
        lt.addFirst(ranges, date_range)
        range_year += 1
    return ranges

def determine_yearly_statistics(catalog, date_ranges, team_name):
    """
    ARGS: Lista con rango de años a consultar en tupla de str en iso (inicio, fin)
    """
    yearly_stats = lt.newList('ARRAY_LIST')
    shootout_start_index = 1
    result_start_index = 1
    scorer_start_index = 1
    for date_range in lt.iterator(date_ranges):
        start_date = date_range[0]
        end_date = date_range[1]
        result_list, res_index = find_results_in_dates(catalog, team_name, start_date, end_date, result_start_index)
        shootout_list, shoot_index = find_shootouts_in_dates(catalog, team_name, start_date, end_date, shootout_start_index)
        scorer_list, score_index = find_scorers_in_dates(catalog, team_name, start_date, end_date, scorer_start_index)
        shootout_start_index = shoot_index
        result_start_index = res_index
        scorer_start_index = score_index
        year_stat = new_year_stat(result_list, shootout_list, scorer_list, start_date, team_name)
        lt.addLast(yearly_stats, year_stat)
    if lt.size(yearly_stats) == 0:
        return None
    else:
        return yearly_stats

def new_year_stat(result_list, shootout_list, scorer_list, start_date, team_name):
    """
    ARGS: una lista no vacía de RESULTS y una lista no vacía de SHOOTOUTS del 
    equipo y dentro de los rangos de fecha del año
    """
    year_stat = {'year' : '', 'total_matches' : '', 'total_points': '',
                 'goal_difference' : '', 'shootout_points' : '', 'own_goal_points' : '',
                 'total_victories' : '', 'total_ties' : '', 'total_defeats' : '',
                 'goals_made' : '', 'goals_conceded' : '', 'top_scorer': ''}
    match_date = date.fromisoformat(start_date)
    players = lt.newList('ARRAY_LIST')
    year = match_date.year
    total_matches = 0
    total_points = 0
    goal_diff = 0
    shoot_points = 0
    own_goal_points = 0
    victories = 0
    ties = 0
    defeats = 0
    goals_made = 0
    goals_conceded = 0
    home_playing = False
    for result in lt.iterator(result_list):
        total_matches += 1
        if result['home_team'] == team_name:
            home_playing = True
        else:
            home_playing = False
        home_score = result['home_score']
        away_score = result['away_score']
        if home_score == away_score:
            ties += 1
        if home_playing:
            goals_made += home_score
            goals_conceded += away_score
            if home_score > away_score:
                victories += 1
            else:
                defeats += 1
        else:
            goals_made += away_score
            goals_conceded += home_score
            if home_score < away_score:
                victories += 1
            else:
                defeats += 1
    for shootout in lt.iterator(shootout_list):
        if shootout['winner'] == team_name:
            shoot_points += 3
    
    for scorer in lt.iterator(scorer_list):
        players_size = lt.size(players)
        match_was_listed = False
        player_was_listed = False
        player_name = scorer['scorer']
        player_goals = 1
        player_own_goals = 0
        player_own = scorer['own_goal']
        player_match = (scorer['home_team'], scorer['away_team'])
        player_minute = scorer['minute']
        if player_own:
            player_own_goals = 1
            own_goal_points += 1
        if players_size == 0:
            player = newPLayer()
            player['name'] = player_name
            player['goles'] = player_goals
            player['autogoles'] += player_own_goals
            player['torneos'] = lt.addFirst(player['torneos'], player_match)
            player['puntaje'] = player_minute
            lt.addFirst(players, player)
        else:
            for listed_player in lt.iterator(players):
                if player_name == listed_player['name']:
                    player_was_listed = True
                    player['goles'] += player_goals
                    player['autogoles'] += player_own_goals
                    for listed_match in lt.iterator(player['torneos']):
                        if player_match == listed_match:
                            match_was_listed = True
                    if match_was_listed == False:
                        player['torneos'] = lt.addFirst(player['torneos'], player_match)
                    player['puntaje'] += player_minute
                if player_was_listed == False:
                    player = newPLayer()
                    player['name'] = player_name
                    player['goles'] = player_goals
                    player['autogoles'] += player_own_goals
                    player['torneos'] = lt.addLast(player['torneos'], player_match)
                    player['puntaje'] = player_minute
                    lt.addFirst(players, player)
    
    players = merg.sort(players, sort_players)
    best_player = lt.firstElement(players)
    best_scorer = {'name': '', 'total_goals' : '', 'total_matches' : '', 'avg_time' : ''}
    best_scorer['avg_time'] = best_player['puntaje'] // (best_player['goles'] - best_player['autogoles'])
    best_scorer['name'] = best_player['name']
    best_scorer['total_goals'] = best_player['goles'] - best_player['autogoles']
    best_scorer['total_matches'] = lt.size(best_player['torneos'])
    goal_diff = goals_made - goals_conceded
    total_points = shoot_points + ties +( 3 * victories)
    
    best_scorer_table = tabulate.table(best_scorer, 'keys', 'grid')
    
    year_stat['year'] = year
    year_stat['goal_difference'] = goal_diff
    year_stat['goals_conceded'] = goals_conceded
    year_stat['goals_made'] = goals_made
    year_stat['own_goal_points'] = own_goal_points
    year_stat['shootout_points'] = shoot_points
    year_stat['total_defeats'] = defeats
    year_stat['total_matches'] = total_matches
    year_stat['total_points'] = total_points
    year_stat['total_ties'] = ties
    year_stat['total_victories'] = victories
    year_stat['top_scorer'] = best_scorer_table
    
    return year_stat
    
def sort_players(player1, player2):
    if player1['goles'] > player2['goles']:
        return True
    elif player1['goles'] < player2['goles']:
        return False
    else:
        if lt.size(player1['torneos']) < lt.size(player2['torneos']):
            return True
        elif lt.size(player1['torneos']) > lt.size(player2['torneos']):
            return False
        else:
            if (player1['puntaje'] / player1['goles']) < (player2['puntaje'] / player2['goles']):
                return True
            elif (player1['puntaje'] / player1['goles']) < (player2['puntaje'] / player2['goles']):
                return False
            else:
                return 0

def ganador(equipo1,equipo2,goles1,goles2):
    """
    Recibe el marcador de un partido y devuelve el equipo ganador. En caso de empate, devuelve "empate".
    """
    if goles1 == goles2:
        return "empate"
    elif goles1 > goles2:
        return equipo1
    else:
        return equipo2
    
def newPLayer():
    player ={ 
             'name' : None,
             'goles' : 0,
             'autogoles' : 0,
             'penalty' : 0,
             'puntaje' : 0,
             'promedio' : 0,
             'goles_victoria' : 0,
             'goles_derrota' : 0, 
             'goles_empate' : 0,
             'ultimo_gol' : None,
             'ultimo_partido': None,
             'torneos' : lt.newList()
             }
    return player 
    
def makeTable(jugadores):
    tabla = [['NOMBRE','PUNTAJE','GOLES','AUTOGOLES','PENALES', 'PROMEDIO\n MINUTOS','GOLES\nVICTORIA','GOLES\nEMPATE','GOLES\nDERROTA','TORNEOS','ULTIMO GOL']]
    for jugador in lt.iterator(jugadores):
        fila = [jugador['name'],jugador['puntaje'],jugador['goles'],jugador['autogoles'],jugador['penalty'],
                jugador['promedio'],jugador['goles_victoria'],jugador['goles_empate'],jugador['goles_derrota'],
                lt.size(jugador['torneos']),tabulate(last_goal(jugador),headers='firstrow',maxcolwidths=[8,9,9,9,None,None,None,9,9,9])]
        tabla.append(fila)
       
    return tabla
    
def makeTable2(goles):
    tabla = [['FECHA','EQUIPO\nLOCAL','EQUIPO\nVISITANTE','EQUIPO','MINUTO','AUTOGOL','PENAL']]
    for gol in lt.iterator(goles):
        fila = [gol['date'],gol['home_team'],gol['away_team'],gol['team'],gol['minute'],gol['own_goal'],gol['penalty']]
        tabla.append(fila)
        
    return tabla    
    
def last_goal(player):
    goal=[['fecha','local','visitante','equipo','minuto','autogol','penalty','gol\nlocal','gol\nvisitante','torneo'],
            [player['ultimo_gol']['date'],player['ultimo_gol']['home_team'],player['ultimo_gol']['away_team'],player['ultimo_gol']['team']
            ,player['ultimo_gol']['minute'],player['ultimo_gol']['own_goal'],player['ultimo_gol']['penalty'],'desconocido','desconocido',
            'desconocido']]
   
    if player['ultimo_partido'] != None:
        goal[1][7] = player['ultimo_partido']['home_score']
        goal[1][8] = player['ultimo_partido']['away_score']
        goal[1][9] = player['ultimo_partido']['tournament']
       
    return goal
    
def getUpDown(encuentros,goles):
    table = [['DATE','MINUTE','HOME TEAM','AWAY TEAM','PLAYER TEAM','HOME SCORE','AWAY SCORE','TOURNAMENT','PENALTY', 'OWN GOAL']]
    if lt.size(goles) <= 6:
        for goal in lt.iterator(goles):
            torneo = 'Desconocido'
            goal_local = 'Desconocido'
            goal_visitante = 'Desconocido'
            for encuentro in lt.iterator(encuentros):
                if (goal['date'] == encuentro['date']) and (goal['home_team'] == encuentro['home_team']) and (goal['away_team'] == encuentro['away_team']):
                  torneo = encuentro['tournament']  
                  goal_local = encuentro['home_score'] 
                  goal_visitante =encuentro['away_score']  
            table.append([goal['date'],goal['minute'],goal['home_team'],goal['away_team'],goal['team'],goal_local,goal_visitante,
                          torneo,goal['penalty'],goal['own_goal']])
    else:
        for goal in lt.iterator(lt.subList(goles,1,3)):
            torneo = 'Desconocido'
            goal_local = 'Desconocido'
            goal_visitante = 'Desconocido'
            for encuentro in lt.iterator(encuentros):
                if (goal['date'] == encuentro['date']) and (goal['home_team'] == encuentro['home_team']) and (goal['away_team'] == encuentro['away_team']):
                  torneo = encuentro['tournament']  
                  goal_local = encuentro['home_score'] 
                  goal_visitante =encuentro['away_score']  
            table.append([goal['date'],goal['minute'],goal['home_team'],goal['away_team'],goal['team'],goal_local,goal_visitante,
                          torneo,goal['penalty'],goal['own_goal']])
        
        r = lt.size(goles)
        for goal in lt.iterator(lt.subList(goles,r-2,3)):
            torneo = 'Desconocido'
            goal_local = 'Desconocido'
            goal_visitante = 'Desconocido'
            for encuentro in lt.iterator(encuentros):
                if (goal['date'] == encuentro['date']) and (goal['home_team'] == encuentro['home_team']) and (goal['away_team'] == encuentro['away_team']):
                  torneo = encuentro['tournament']  
                  goal_local = encuentro['home_score'] 
                  goal_visitante =encuentro['away_score']  
            table.append([goal['date'],goal['minute'],goal['home_team'],goal['away_team'],goal['team'],goal_local,goal_visitante,
                          torneo,goal['penalty'],goal['own_goal']])
        
    return table 

# Funciones utilizadas para comparar elementos dentro de una lista

def compareGoalscorersDateInv(goal1,goal2):
    """
    Función encargada de comparar dos datos
    """
    if (compareByDate(goal1, goal2) == 0) and (type(compareByDate(goal1,goal2)) == type(0)):
        return compareByMin(goal1,goal2)
    else:
        return not(compareByDate(goal1, goal2))
    
def compareGoalscorersDate(goal1,goal2):
    """
    Función encargada de comparar dos datos
    """
    if (compareByDate(goal1, goal2) == 0) and (type(compareByDate(goal1,goal2)) == type(0)):
        if (compareByMin(goal1, goal2) == 0) and (type(compareByMin(goal1,goal2)) == type(0)):
            return compareByPlayerName(goal1, goal2) 
        else:
            return compareByMin(goal1,goal2)
    else:
        return compareByDate(goal1, goal2)
    
def compareTournamentByCountry(tour1,tour2):
    if (compareByDate(tour1, tour2) == 0) and (type(compareByDate(tour1,tour2)) == type(0)):
        return compareByCountry(tour1, tour2)   
    else:
        return compareByDate(tour1, tour2)
    
def compareByMin(goal1,goal2):
    if goal1['minute'] < goal2['minute']:
        return True
    elif goal1['minute'] > goal2['minute']:
        return False
    else:
        return 0
        
def compareResults(res1,res2):
    """
    Función encargada de comparar dos datos por fecha
    """
    if (compareByDate(res1, res2) == 0) and (type(compareByDate(res1, res2,)) == type(0)):
        return compareByScoreboard(res1, res2)
    else:
        return compareByDate(res1, res2)
    
def compareByScoreboard(res1, res2):
    """
    Función encargada de comparar dos datos por marcador de equipos involucrados 
    
    si res1 tiene menor puntaje en algún caso: return True
    si res2 tiene mayor puntaje en algún caso: return False
    si tienen el mismo puntaje return 0
    """
    if res1['home_score'] < res2['home_score']:
        return True
    elif res1['home_score'] > res2['home_score']:
        return False
    else:
        if res1['away_score'] < res2['away_score']:
            return True
        elif res1['away_score'] > res2['away_score']:
            return False
        else:
            return 0
        
def compareByPlayerName(goal1,goal2):
    if goal1['scorer'] < goal2['scorer']:
        return True
    elif goal1['scorer'] > goal2['scorer']:
        return False
    else:
        return 0
    
def compareJugadorByName(nombre,player):
    if nombre < player['name']:
        return True
    elif nombre > player['name']:
        return False
    else:
        return 0
    
def compareByDate(element1, element2):
    """
    Función recibe dos elementos que compara por sus fechas. si elem1 < elem2, true. si elem1 > elem2, false. 
    si == entones 0
    """
    date1 = date.fromisoformat(element1['date'])
    date2 = date.fromisoformat(element2['date'])
    if date1 > date2:
        return True
    elif date1 < date2:
        return False
    else:
        return 0
    
def compareByCountry(c1,c2):
    if c1['country'] < c2['country']:
        return True
    elif c1['country'] > c2['country']:
        return False
    else:
        return 0
    
def compareByCity(c1,c2):
    if c1['city'] < c2['city']:
        return True
    elif c1['city'] > c2['city']:
        return False
    else:
        return 0
        
def compareShootouts(shoot1,shoot2):
    if (compareByDate(shoot1, shoot2) == 0) and (type(compareByDate(shoot1, shoot2,)) == type(0)):
        return compareByShoot(shoot1, shoot2)
    else:
        return compareByDate(shoot1, shoot2)
    
    
def compareByShoot(shoot1,shoot2):
     if shoot1['home_team'] < shoot2['home_team']:
            return True
     elif shoot1['home_team'] > shoot2['home_team']:
            return False
     else:
        if shoot1['away_team'] < shoot2['away_team']:
            return True
        elif shoot1['away_team'] > shoot2['away_team']:
                return False
        else:
            return 0
    
def comparePlayerByPuntaje(player1,player2):
    if player1['puntaje'] > player2['puntaje']:
        return True
    elif player1['puntaje'] < player2['puntaje']:
        return False
    else:
        return 0 
    
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

def sortByCriteria(lista, algorithm, cmp):
    """
    Función encargada de ordenar la lista usando el algoritmo seleccionado por el usuario y el criterio de ordenamiento cmp.
    """
    #TODO: Crear función de ordenamiento
  
    if algorithm == 0:
        #insertion
        lista = ins.sort(lista, cmp)
    elif algorithm == 1:
        #shell
        lista = sa.sort(lista, cmp)
    elif algorithm == 2:
        #selection
        lista = se.sort(lista, cmp)
    elif algorithm == 3:
        #quick
        lista = quk.sort(lista, cmp)
    elif algorithm == 4:
        #merge
        lista = merg.sort(lista, cmp)
    else:
        lista = quk.sort(lista, cmp)
       

def sortGoalscorers(catalog, algorithm):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
  
    if algorithm == 0:
        #insertion
        catalog['goalscorers'] = ins.sort(catalog['goalscorers'], compareGoalscorersDate)
    elif algorithm == 1:
        #shell
        catalog['goalscorers'] = sa.sort(catalog['goalscorers'], compareGoalscorersDate)
    elif algorithm == 2:
        #selection
        catalog['goalscorers'] = se.sort(catalog['goalscorers'], compareGoalscorersDate)
    elif algorithm == 3:
        #quick
        catalog['goalscorers'] = quk.sort(catalog['goalscorers'], compareGoalscorersDate)
    elif algorithm == 4:
        #merge
        catalog['goalscorers'] = merg.sort(catalog['goalscorers'], compareGoalscorersDate)
    else:
        catalog['goalscorers'] = quk.sort(catalog['goalscorers'], compareGoalscorersDate)
    
def sortResults(catalog, algorithm):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    
    if algorithm == 0:
        #insertion
        catalog['results'] = ins.sort(catalog['results'], compareResults)
    elif algorithm == 1:
        #shell
        catalog['results'] = sa.sort(catalog['results'], compareResults)
    elif algorithm == 2:
        #selection
        catalog['results'] = se.sort(catalog['results'], compareResults)
    elif algorithm == 3:
        #quick
        catalog['results'] = quk.sort(catalog['results'], compareResults)
    elif algorithm == 4:
        #merge
        catalog['results'] = merg.sort(catalog['results'], compareResults)
    else:
        catalog['results'] = quk.sort(catalog['results'], compareResults)
   
            
def sortShootouts(catalog, algorithm):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    if algorithm == 0:
        #insertion
        catalog['shootouts'] = ins.sort(catalog['shootouts'], compareShootouts)
    elif algorithm == 1:
        #shell
        catalog['shootouts'] = sa.sort(catalog['shootouts'], compareShootouts)
    elif algorithm == 2:
        #selection
        catalog['shootouts'] = se.sort(catalog['shootouts'], compareShootouts)
    elif algorithm == 3:
        #quick
        catalog['shootouts'] = quk.sort(catalog['shootouts'], compareShootouts)
    elif algorithm == 4:
        #merge
        catalog['shootouts'] = merg.sort(catalog['shootouts'], compareShootouts)
    else:
        catalog['shootouts'] = quk.sort(catalog['shootouts'], compareShootouts)
    