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
import datetime 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
# En model.py
def new_data_structs(tipo_lista):
    data = {
        'goalscore': None,
        'results': None,
        'shootouts': None,
    }
    if tipo_lista == "ARRAY_LIST":
        data['goalscore'] = lt.newList('ARRAY_LIST')
        data['results'] = lt.newList('ARRAY_LIST')
        data['shootouts'] = lt.newList('ARRAY_LIST')
    elif tipo_lista == "SINGLE_LINKED":
        data['goalscore'] = lt.newList('SINGLE_LINKED')
        data['results'] = lt.newList('SINGLE_LINKED')
        data['shootouts'] = lt.newList('SINGLE_LINKED')  
    return data
#limpiar las

        
def add_goalscorers1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de goleadores
    """
    lt.addLast(data_structs['goalscore'], data)

def add_results1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de resultados de partidos
    """
    lt.addLast(data_structs['results'], data)

def add_shootouts1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de definiciones de partidos desde el punto penal
    """
    lt.addLast(data_structs['shootouts'], data)


# ...

# Funciones de comparación
def cmp_date_and_minute(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')

    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        # Si las fechas son iguales, ordenar por minuto en que se anotó el gol

        minute1 = data1['minute']
        minute2 = data2['minute']
        
        # Comprobar si los minutos no son cadenas vacías antes de convertir a flotante
        if minute1 and minute2:
            if float(minute1) < float(minute2):
                return False
            else:
                return True

 

def cmp_date(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')

    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    
def cmp_fecha_país_mayor_menor(data1, data2):
    # Ordenar primero por fecha, luego por puntaje local y puntaje visitante
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        if (data1['home_team']) < ((data2['home_team'])):
            return False
        elif (data1['home_team']) > (data2['home_team']):
            return True
        else:
            return False

def compare_shootouts(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        # Si las fechas son iguales, comparar los nombres de los equipos sin importar mayúsculas y minúsculas
        team1 = data1['home_team'].lower()
        team2 = data2['home_team'].lower()
        if team1 < team2:
            return False
        elif team1 > team2:
            return True
        else:
            ateam1 = data1['away_team'].lower()
            ateam2 = data2['away_team'].lower()
            return False if ateam1 < ateam2 else True if ateam1 > ateam2 else False




def cmp_partidos_by_fecha_y_pais(resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelve falso (False).
    Args:
    resultado1: información del primer registro de resultados FIFA que incluye
    “date” y el “country”
    resultado2: información del segundo registro de resultados FIFA que incluye
    “date” y el “country”
    """
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(resultado1['date'], date_format)
    date2 = datetime.datetime.strptime(resultado2['date'], date_format)

    if date1 != date2:
        return date1 < date2
    else:
        # Si las fechas son iguales, ordenar por nombre de país
        country1 = resultado1['home_team']
        country2 = resultado2['home_team']
        return country1 < country2
def cmp_partidos_by_fecha(resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2
    """
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(resultado1['date'], date_format)
    date2 = datetime.datetime.strptime(resultado2['date'], date_format)

    if date1 != date2:
        return date1 < date2
       
def compare_home(data1, data2):
    team1 = data1['home_team'].lower()
    team2 = data2['home_team'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False
def compare_away(data1, data2):
    team1 = data1['away_team'].lower()
    team2 = data2['away_team'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False
#req 6
def cmp_total_p(equipo1, equipo2):
    """
    Compara dos equipos por su criterio compuesto de estadísticas.
    """
    if equipo1['total_puntos'] > equipo2['total_puntos']:
        return True
    elif equipo1['total_puntos'] < equipo2['total_puntos']:
        return False
    else:
        if equipo1['diferencia_goles'] > equipo2['diferencia_goles']:
            return True
        elif equipo1['diferencia_goles'] < equipo2['diferencia_goles']:
            return False
        else:
            if equipo1['puntos_penal'] > equipo2['puntos_penal']:
                return True
            elif equipo1['puntos_penal'] < equipo2['puntos_penal']:
                return False
            else:
                if equipo1['partidos_disputados'] < equipo2['partidos_disputados']:
                    return True
                elif equipo1['partidos_disputados'] > equipo2['partidos_disputados']:
                    return False
                else:
                    if equipo1['puntos_autogol'] < equipo2['puntos_autogol']:
                        return True
                    elif equipo1['puntos_autogol'] > equipo2['puntos_autogol']:
                        return False
                    else:
                        return True
def comparar_anotadores(anotador1, anotador2):
    # Obtener los valores relevantes para la comparación de cada anotador
    puntos1 = anotador1['total_points']
    total_goles1 = anotador1['total_points'] - anotador1['penalty_goals'] - anotador1['own_goals']
    goles_penal1 = anotador1['penalty_goals']
    autogoles1 = anotador1['own_goals']
    tiempo_promedio1 = anotador1['avg_time (min)']

    puntos2 = anotador2['total_points']
    total_goles2 = anotador2['total_points'] - anotador2['penalty_goals'] - anotador2['own_goals']
    goles_penal2 = anotador2['penalty_goals']
    autogoles2 = anotador2['own_goals']
    tiempo_promedio2 = anotador2['avg_time (min)']

    # Comparar según el criterio compuesto
    if puntos1 > puntos2:
        return True
    elif puntos1 < puntos2:
        return False
    else:
        if total_goles1 > total_goles2:
            return True
        elif total_goles1 < total_goles2:
            return False
        else:
            if goles_penal1 > goles_penal2:
                return True
            elif goles_penal1 < goles_penal2:
                return False
            else:
                if autogoles1 < autogoles2:
                    return True
                elif autogoles1 > autogoles2:
                    return False
                else:
                    if tiempo_promedio1 < tiempo_promedio2:
                        return True
                    elif tiempo_promedio1 > tiempo_promedio2:
                        return False
                    else:
                        return False  # Igualdad en todos los criterios
#req1

def compare_country(data1, data2):
    team1 = data1['country'].lower()
    team2 = data2['country'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False
#req1
def compare_countryMoretoLess(data1, data2):
    team1 = data1['country'].lower()
    team2 = data2['country'].lower()
    if team1 > team2:
        return True
    elif team1 < team2:
        return False

def sortName(data,name_team, condition_team, number_matchs):
    e =0
    total_indices = []
    if condition_team.lower() == "local":
        f ="home_team"
        indices, NameSort= searchname(data,name_team, condition_team, number_matchs,f)
        total_indices = indices
    
    elif condition_team.lower() == "visitante":
        f ="away_team"
        indices, NameSort= searchname(data,name_team, condition_team, number_matchs,f)
        total_indices = indices


    else:
        e =1
        f ="home_team"
        indices1, NameSort1= searchname(data,name_team, condition_team, number_matchs,f)
        z ="away_team"
        indices2, NameSort2= searchname(data,name_team, condition_team, number_matchs, z)      
    if e==1:
        total_teams = lt.newList('ARRAY_LIST')
        answerSort = lt.newList('ARRAY_LIST')
        for i in indices1:
            element= lt.getElement(NameSort1,i+1)
            lt.addFirst(total_teams,element)
        for i in indices2:
            element= lt.getElement(NameSort2,i+1)
            lt.addFirst(total_teams,element)
        answer= sa.sort(total_teams, compare_shootouts)
        answerSort = getFirstNum(number_matchs,answer)
        return answerSort

    else:
        total_teams = lt.newList('ARRAY_LIST')
        answerSort = lt.newList('ARRAY_LIST')
        for i in total_indices:
            element= lt.getElement(NameSort,i+1)
            lt.addFirst(total_teams,element)
        answer= sa.sort(total_teams, compare_shootouts)
        answerSort = getFirstNum(number_matchs,answer)
        return answerSort
 

def searchname(data,name_team, condition_team, number_matchs,f):
        NameSort = lt.newList('ARRAY_LIST')
        newList = []
        if f=='home_team':
            NameSort = sa.sort(data, compare_home)
        else:
            NameSort = sa.sort(data, compare_away)
        for name in lt.iterator(NameSort):
            
            name_value = name[f].lower()
            newList.append(name_value)
        
        i = 0
        work = True
        indices = []
        izquierda = 0
        derecha = len(newList) - 1
        x = newList
        while izquierda <= derecha and work:
            medio = (izquierda + derecha) // 2  # Encontramos el índice medio de la lista
            r = newList[medio]
            z = name_team.lower()
            if newList[medio] == name_team.lower():
                indices.append(medio)  # Hemos encontrado el elemento y agregamos su índice a la lista
                # Buscamos más ocurrencias hacia la izquierda
                i = medio - 1
                while i >= 0 and newList[i] == name_team.lower():
                    indices.append(i)
                    i -= 1
                # Buscamos más ocurrencias hacia la derecha
                j = medio + 1
                while j < len(newList) and newList[j] == name_team.lower():
                    indices.append(j)
                    j += 1
                work = False

            elif newList[medio] < name_team.lower():
                izquierda = medio + 1  # El elemento está en la mitad derecha
            else:
                derecha = medio - 1  # El elemento está en la mitad izquierda
        return indices, NameSort

#req 2
def get_first_n_goals_by_player(catalog, player_name, n,  recursive=True):
    if recursive:
        return recurs_get_first_n_goals_by_player(catalog, player_name, n)
    else:
        return iter_get_first_n_goals_by_player(catalog, player_name, n)
#Iterativa
def iter_get_first_n_goals_by_player(data_structs, player_name, n):
    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    sa.sort(data_structs["goalscore"], cmp_fecha_país_mayor_menor)
    # Recorremos la lista de goles y seleccionamos los que coincidan con el jugador
    for goal in lt.iterator(data_structs['goalscore']):
        if goal['scorer'].lower() == player_name.lower():
            lt.addLast(player_goals, goal)
            total_goals += 1
            if total_goals == n:
                break
    return total_goals, player_goals
#Recursiva
def recurs_get_first_n_goals_by_player(data_structs, player_name, n):
    def recursive_goals(goals, player_goals, total_goals, index):
        if index >= lt.size(goals) or total_goals >= n:
            return total_goals, player_goals
        
        goal = lt.getElement(goals, index)
        if goal['scorer'].lower() == player_name.lower():
            lt.addLast(player_goals, goal)
            total_goals += 1
        
        return recursive_goals(goals, player_goals, total_goals, index + 1)
    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    sa.sort(data_structs["goalscore"], cmp_fecha_país_mayor_menor )
    goals = data_structs['goalscore']

    return recursive_goals(goals, player_goals, total_goals, 0)

#Requerimiento 3
def iter_consultar_partidos_equipo_periodo(data_structs, team_name, fecha_inicio, fecha_fin):
    
    games_played = lt.newList("ARRAY_LIST")
    
    
    sa.sort(data_structs["results"], cmp_date)
    total_games = 0
    total_home_games = 0
    total_away_games = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')

    for partido in lt.iterator(data_structs["results"]):
        goal_date = datetime.datetime.strptime(partido['date'], '%Y-%m-%d')
        if fecha_inicio <= goal_date <= fecha_fin and (partido["home_team"].lower() == team_name.lower() or partido["away_team"].lower() == team_name.lower()):
            total_games += 1
            penalty = buscar_penaltis(data_structs["goalscore"],partido['date'], partido['home_team'], partido['away_team'])
            own_goal = buscar_autogoles(data_structs["goalscore"],partido['date'], partido['home_team'], partido['away_team'])
            if partido["home_team"].lower() == team_name.lower():
                total_home_games += 1
            if partido["away_team"].lower() == team_name.lower():
                total_away_games += 1
            
            partido["penalty"] = penalty 
            partido["own_goal"] = own_goal
            lt.addLast(games_played, partido)
    return total_games , total_home_games, total_away_games, games_played

def buscar_penaltis(results, game_date, home_team, away_team):
    """
    Busca si hubo penaltis en la lista de goles según la fecha y los equipos.
    """
    for result in lt.iterator(results):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        penalty = False
        if result_date == datetime.datetime.strptime(game_date, '%Y-%m-%d') and result['home_team'] == home_team and result['away_team'] == away_team:
            if result['penalty'] == True:
                penalty = True
            return penalty
    return 'Desconocido'

def buscar_autogoles(results, game_date, home_team, away_team):
    """
    Busca si hubo autogoles en la lista de goles según la fecha y los equipos.
    """
    for result in lt.iterator(results):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        own_goal = False
        if result_date == datetime.datetime.strptime(game_date, '%Y-%m-%d') and result['home_team'] == home_team and result['away_team'] == away_team:
            if result['own_goal'] == True:
                own_goal = True
            return own_goal
    return 'Desconocido'

#req4
def queryMatchsbyPeriod(name_tournament, start_date, end_date,shootouts, results):
    """
    Función que soluciona el requerimiento 4
    """
    newarray = lt.newList('ARRAY_LIST')
    goals =sa.sort(shootouts,compare_home)
    total_paises = set()
    total_ciudades = set()
    sa.sort(shootouts,compare_away)
    start_date= datetime.datetime.strptime(start_date,"%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    r = lt.newList('ARRAY_LIST')
    for i in lt.iterator(results):
        date = datetime.datetime.strptime(i['date'],"%Y-%m-%d")
        if date<= end_date and date>= start_date and i['tournament']== name_tournament:
            country = i['country']
            city = i['city']
            total_paises.add(country)
            total_ciudades.add(city)
            if i['home_score'] == i['away_score']:
                winner = buscar_ganador(shootouts, date, i['home_team'], i ['away_team'])
            else:
                winner = 'Unknown'
            i['winner'] = winner
            lt.addLast(newarray, i)




        
        


    size = lt.size(newarray)
    return newarray, len(total_paises), len(total_ciudades),size
def buscar_ganador(shootouts,date, home_team, away_team):
    winner = 'Unkown'
    for i in lt.iterator(shootouts):
        datei = datetime.datetime.strptime(i['date'],"%Y-%m-%d")
        if date == datei and i['home_team'] == home_team and i['away_team'] == away_team:
            return i['winner']



def sortmatchAlphabet(data):
   
    sa.sort(data, cmp_fecha_país_mayor_menor)
    return data

def lenght(data):
    return lt.size(data)
    






def sortmatchAlphabet(data):
   
    sa.sort(data, cmp_fecha_país_mayor_menor)
    return data

def lenght(data):
    return lt.size(data)

#search name binary
def searchnameBinary(data, goal, key, goal2, key2):
    low, high = 0 , lt.size(data)
    x =-1
    while low<= high:
        mid = (low + high) // 2
        f=lt.getElement(data,mid)[key].lower()
        if lt.getElement(data,mid)[key].lower()  ==goal.lower() :
            if lt.getElement(data,mid)[key2].lower() == goal2.lower():
                x = mid
                return x
            else:
                work =True
                while work:
                     #buscamos en la izquierda mas ocurrencias
                    if lt.getElement(data,mid)[key].lower()  ==goal.lower():
                        mid-=1
                    else:
                        work = False
                        x = mid+1
                    #buscamos mas iteraciones a la izquierda
                working = True
                while working:
                    if lt.getElement(data,x)[key].lower()  ==goal.lower():
                        if lt.getElement(data,x)[key2].lower() == goal2.lower():
                            return x
                    if lt.getElement(data,x)[key].lower()  ==goal.lower():
                            x+=1
                    else:
                        working = False

        elif lt.getElement(data,mid)[key].lower() <goal.lower():
            #and lt.getElement(data,mid)[key2].lower() == goal2.lower()s
            #(lt.getElement(data,mid)[key].lower() == goal.lower() and  lt.getElement(data,mid)[key2].lower() <goal2.lower()):
            #partido["local"] < local or (partido["local"] == local and partido["visitante"] < visitante):
            low = mid+1
            
        else:
            high= mid-1

    return  x




#Req 5
def consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin, recursive = True):
    if recursive:
        return rec_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin)
    else:
        return iter_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin)
    
#Iterativa
def iter_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin):
    """
    Consulta las anotaciones de un jugador en un período de tiempo.
    Devuelve una lista de goles del jugador en ese período.
    """
    player_goals = lt.newList('ARRAY_LIST')

    # Ordena la lista de goles por fecha y minuto
    sa.sort(data_structs['goalscore'], cmp_date_and_minute)

    total_goals = 0
    total_tournaments = set()
    penalties = 0
    own_goals = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    for goal in lt.iterator(data_structs['goalscore']):
        goal_date = datetime.datetime.strptime(goal['date'], '%Y-%m-%d')
        if fecha_inicio <= goal_date <= fecha_fin and goal['scorer'].lower() == jugador_nombre.lower():
            total_goals += 1
            # Obtener el nombre del torneo desde la lista de resultados
            tournament = buscar_torneo(data_structs['results'], goal['date'], goal['home_team'], goal['away_team'])
            if tournament:
                total_tournaments.add(tournament)
            if goal['penalty'] == 'True':
                penalties += 1
            if goal['own_goal'] == 'True':
                own_goals += 1

            # Incluir el nombre del torneo en el gol
            goal['tournament'] = tournament
            lt.addLast(player_goals, goal)

    return total_goals, len(total_tournaments), penalties, own_goals, player_goals


#Recursiva 
def rec_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin):
    def recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, index):
        if index >= lt.size(goals):
            return total_goals, len(total_tournaments), penalties, own_goals, player_goals
        
        goal = lt.getElement(goals, index)
        goal_date = datetime.datetime.strptime(goal['date'], '%Y-%m-%d')

        if fecha_inicio <= goal_date <= fecha_fin and goal['scorer'].lower() == jugador_nombre.lower():
            total_goals += 1
            # Obtener el nombre del torneo desde la lista de resultados
            tournament = buscar_torneo(data_structs['results'], goal['date'], goal['home_team'], goal['away_team'])
            if tournament:
                total_tournaments.add(tournament)
            if goal['penalty'] == 'True':
                penalties += 1
            if goal['own_goal'] == 'True':
                own_goals += 1

            # Incluir el nombre del torneo en el gol
            goal['tournament'] = tournament
            lt.addLast(player_goals, goal)
        
        return recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, index + 1)

    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    total_tournaments = set()
    penalties = 0
    own_goals = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    sa.sort(data_structs["goalscore"], cmp_date_and_minute)
    goals = data_structs['goalscore']

    return recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, 0)
def buscar_torneo(results, goal_date, home_team, away_team):
    """
    Busca el nombre del torneo en la lista de resultados según la fecha y los equipos.
    """
    for result in lt.iterator(results):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        if result_date == datetime.datetime.strptime(goal_date, '%Y-%m-%d') and result['home_team'] == home_team and result['away_team'] == away_team:
            return result['tournament']
    return 'Desconocido'

#Req 6







def consultar_mejores_equipos(data_structs, N, torneo_nombre, fecha_inicio, fecha_fin):
    """ 
    Calcula El total de equipos,
    el total de encuentros disputados, 
    el total de países,
    el total de ciudades, 
    el nombre de la ciudad donde más partidos se han disputado,
    el listado de los equipos que conforman el torneo

    """
    # Filtrar los datos por torneo y período de tiempo
    tournament_results = filtrar_por_torneo(data_structs['results'], torneo_nombre)
    filtered_results = filtrar_por_periodo(tournament_results, fecha_inicio, fecha_fin)
    
    # Crear un diccionario para almacenar las estadísticas de cada equipo
    team_stats = {}
    
    for result in lt.iterator(filtered_results):
        home_team = result['home_team']
        away_team = result['away_team']
        home_score = float(result['home_score'])
        away_score = float(result['away_score'])
        
        # Actualizar estadísticas de los equipos
        actualizar_estadisticas_equipo(team_stats, home_team, home_score, away_score, data_structs['goalscore'])
        actualizar_estadisticas_equipo(team_stats, away_team, away_score, home_score, data_structs['goalscore'])
    
    
    list_team = lt.newList('ARRAY_LIST')
    for a in team_stats.values():
        lt.addLast(list_team, a)

    list_team = sa.sort(list_team, cmp_total_p)
    list_team = lt.subList(list_team, 1, N)


    
    # Obtener información adicional
    total_equipos = obtener_total_equipos(filtered_results)
    total_encuentros = lt.size(filtered_results)
    total_paises = obtener_total_paises(filtered_results)
    total_ciudades = obtener_total_ciudades(filtered_results)
    ciudad_mas_partidos = obtener_ciudad_mas_partidos(filtered_results)
    
    # Limitar la lista de equipos clasificados a los primeros N
    
    
    return total_equipos, total_encuentros, total_paises, total_ciudades, ciudad_mas_partidos, list_team

def filtrar_por_torneo(results, torneo_nombre):
    """
    Filtra los resultados por nombre de torneo.
    """
    filtered_results = lt.newList('ARRAY_LIST')
    for result in lt.iterator(results):
        if torneo_nombre in result['tournament']:
            lt.addLast(filtered_results, result)
    return filtered_results

def filtrar_por_periodo(results, fecha_inicio, fecha_fin):
    """
    Filtra los resultados por período de tiempo.
    """
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    filtered_results = lt.newList('ARRAY_LIST')
    for result in lt.iterator(results):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        if fecha_inicio <= result_date <= fecha_fin:
            lt.addLast(filtered_results, result)
    return filtered_results
def obtener_estadisticas_equipo(team_stats, team_name):
    """
    Obtiene las estadísticas de un equipo del diccionario de estadísticas de equipos.
    Si no existe, crea un registro para el equipo.
    """
    if team_name in team_stats:
        return team_stats[team_name]
    
    # Si el equipo no existe en el diccionario, lo crea.
    new_team_stats = {
        'nombre_equipo': team_name,
        'total_puntos': 0,
        'diferencia_goles': 0,
        'partidos_disputados': 0,
        'puntos_penal':0,
        'puntos_autogol':0,
        'victorias':0,
        'derrotas': 0,
        'empates': 0,
        'goles_obtenidos':0,
        'goles_recibidos':0,
        'max_goleador': None
    }
    team_stats[team_name] = new_team_stats
    return new_team_stats


def actualizar_estadisticas_equipo(team_stats, team_name, goles_a_favor, goles_en_contra, data_structs):
    """
    Actualiza las estadísticas de un equipo en función de los goles a favor y en contra.
    """
    equipo = obtener_estadisticas_equipo(team_stats, team_name)
    
    # Realiza los cálculos de estadísticas
    equipo['total_puntos'] += calcular_puntos(goles_a_favor, goles_en_contra)
    equipo['diferencia_goles'] += goles_a_favor - goles_en_contra
    equipo['partidos_disputados'] += 1
    equipo['puntos_penal'] += goles_a_favor
    for goal in lt.iterator(data_structs):
        if goal['own_goal']==True:
            equipo['puntos_autogol'] += 1
    
    
    if goles_a_favor > goles_en_contra:
        equipo['victorias'] += 1
    elif goles_a_favor < goles_en_contra:
        equipo['derrotas'] += 1
    else:
        equipo['empates'] += 1
    
    equipo['goles_obtenidos'] += goles_a_favor
    equipo['goles_recibidos'] += goles_en_contra
    
    # Actualiza el máximo goleador
    
    actualizar_max_goleador(equipo, goles_a_favor, goles_en_contra, data_structs)

def calcular_puntos(goles_a_favor, goles_en_contra):
    """
    Calcula los puntos de un partido según los goles a favor y en contra.
    """
    if goles_a_favor > goles_en_contra:
        return 3
    elif goles_a_favor == goles_en_contra:
        return 1
    else:
        return 0



def calcular_puntos_autogol(goalscore):
    """
    Calcula los puntos recibidos por autogol.
    """

    autogol = 0  # Utilizamos un conjunto para evitar duplicados
    for goal in lt.iterator(goalscore):
        if goal['own_goal']:
            autogol +=1

    return autogol
def obtener_max_goleador(data_structs, equipo_nombre):
    """
    Obtiene la información del máximo goleador de un equipo.
    """
    max_goleador_equipo = {}
    max_goles = 0
    
    for gol in lt.iterator(data_structs):
 
        equipo_local = gol['home_team']
        equipo_visitante = gol['away_team']
        equipo_anotador = gol['team']
        jugador_anotador = gol['scorer']
        if gol['minute']:
            minuto = float(gol['minute'])


        if equipo_nombre == equipo_local or equipo_nombre == equipo_visitante:
            if equipo_nombre == equipo_anotador:
                if jugador_anotador != '' :
                    if jugador_anotador not in max_goleador_equipo:
                        max_goleador_equipo[jugador_anotador] = {'goles_anotados': 1, 'partidos_anotados': 1, 'promedio_tiempo': minuto}
                    else:
                        max_goleador_equipo[jugador_anotador]['goles_anotados'] += 1
                        max_goleador_equipo[jugador_anotador]['partidos_anotados'] += 1
                        max_goleador_equipo[jugador_anotador]['promedio_tiempo'] += minuto
                        max_goleador_equipo[jugador_anotador]['promedio_tiempo'] /= max_goleador_equipo[jugador_anotador]['partidos_anotados']
                        
                    if max_goleador_equipo[jugador_anotador]['goles_anotados'] > max_goles:
                        max_goles = max_goleador_equipo[jugador_anotador]['goles_anotados']
                        max_goleador = jugador_anotador
                        partidos_anotados = max_goleador_equipo[jugador_anotador]['partidos_anotados']
                        promedio_tiempo = max_goleador_equipo[jugador_anotador]['promedio_tiempo']
    return {'nombre_jugador': max_goleador, 'goles_anotados': max_goles, 'partidos_anotados':partidos_anotados, 'promedio_tiempo': promedio_tiempo} if max_goles > 0 else None

def actualizar_max_goleador(equipo, goles_a_favor, goles_en_contra, data_structs):
    """
    Actualiza al máximo goleador del equipo.
    """
    max_goleador_data = obtener_max_goleador(data_structs, equipo['nombre_equipo'])
    
    if max_goleador_data:
        equipo['max_goleador'] = {
            'nombre_jugador': max_goleador_data['nombre_jugador'],
            'goles_anotados': max_goleador_data['goles_anotados'],
            'partidos_anotados': max_goleador_data['partidos_anotados'],
            'promedio_tiempo': max_goleador_data['promedio_tiempo'] 
        }
    else:
        equipo['max_goleador'] = None

def obtener_total_equipos(results):
    """
    Obtiene el total de países involucrados en los resultados.
    """
    paises = set()  # Utilizamos un conjunto para evitar duplicados
    for result in lt.iterator(results):
         paises.add(result['home_team'])
         paises.add(result['away_team'])

    return len(paises)

def obtener_total_paises(results):
    """
    Obtiene el total de países involucrados en los resultados.
    """
    paises = set()  # Utilizamos un conjunto para evitar duplicados
    for result in lt.iterator(results):
        paises.add(result['country'])

    return len(paises)

def obtener_total_ciudades(results):
    """
    Obtiene el total de ciudades involucradas en los resultados.
    """
    ciudades = set()  # Utilizamos un conjunto para evitar duplicados
    for result in lt.iterator(results):
        ciudades.add(result['city'])

    return len(ciudades)

def obtener_ciudad_mas_partidos(results):
    """
    Obtiene la ciudad donde se han disputado más partidos.
    """
    ciudades_partidos = {}  # Diccionario para realizar un seguimiento de la cantidad de partidos por ciudad
    for result in lt.iterator(results):
        ciudad = result['city']
        if ciudad in ciudades_partidos:
            ciudades_partidos[ciudad] += 1
        else:
            ciudades_partidos[ciudad] = 1
    
    # Encuentra la ciudad con más partidos
    ciudad_mas_partidos = max(ciudades_partidos, key=ciudades_partidos.get)
    
    return ciudad_mas_partidos

#####REQ 7

                


def clasificar_anotadores(data_structs, N, fecha_ini, fecha_fin):
    lista_anotadores = lt.newList('ARRAY_LIST')
    fecha_inicio = datetime.datetime.strptime(fecha_ini, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    partidos_anotadores = {}
    total_anotadores = set()
    total_t = set()
    total_goles = 0
    total_goles_penal = 0
    total_autogoles = 0
    scorer_data = {}

    for result in lt.iterator(data_structs['results']):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        if fecha_inicio <= result_date <= fecha_fin and result['tournament'] != 'Friendly':
            partido_unique_key = (result['date'], result['home_team'], result['away_team'])
            winner = result['home_team'] if result['home_score'] > result['away_score'] else result['away_team'] if result['home_score'] < result['away_score'] else 'tie'

            if result['tournament']:
                total_t.add(result['tournament'])

            for scorer in lt.iterator(data_structs['goalscore']):
                jugador = scorer['scorer']
                if jugador not in scorer_data:
                    scorer_data[jugador] = {
                        'scorer': jugador,
                        'total_points': 0,
                        'total_goals': 0,
                        'penalty_goals': 0,
                        'own_goals': 0,
                        'avg_time (min)': 0,
                        'total_tournaments': 0,
                        'scored_in_wins': 0,
                        'scored_in_loses': 0,
                        'scored_in_draws': 0,
                        'last_goal': None,
                        'total_games': 0
                    }

                if result['date'] == scorer['date'] and (result['home_team'] == scorer['home_team'] or result['away_team'] == scorer['away_team']):
                    total_anotadores.add(jugador)
                    if jugador not in partidos_anotadores:
                        partidos_anotadores[jugador] = set()
                    if partido_unique_key not in partidos_anotadores[jugador]:
                        partidos_anotadores[jugador].add(partido_unique_key)
                        scorer_data[jugador]['total_goals'] += 1
                        total_goles += 1

                    scorer_data[jugador]['total_points'] += 1

                    if scorer['penalty'] == 'True':
                        scorer_data[jugador]['penalty_goals'] += 1
                        scorer_data[jugador]['total_points'] += 1
                        total_goles_penal += 1
                    if scorer['own_goal'] == 'True':
                        scorer_data[jugador]['own_goals'] += 1
                        scorer_data[jugador]['total_points'] -= 1
                        total_autogoles += 1
                    if scorer['minute']:
                        minuto = float(scorer['minute'])
                        a = scorer_data[jugador]
                        if 'avg_time (min)' not in a:
                            a['avg_time (min)'] = minuto
                            a['total_games'] = 1
                        else:
                            a['avg_time (min)'] = (a['avg_time (min)'] * a['total_games'] + minuto) / (a['total_games'] + 1)
                            a['total_games'] += 1

                    if winner == 'tie':
                        scorer_data[jugador]['scored_in_draws'] += 1
                    elif winner == jugador:
                        scorer_data[jugador]['scored_in_wins'] += 1
                    else:
                        scorer_data[jugador]['scored_in_loses'] += 1

                    scorer_data[jugador]['last_goal'] = {
                        'date': result['date'],
                        'tournament': result['tournament'],
                        'home_team': result['home_team'],
                        'away_team': result['away_team'],
                        'home_score': result['home_score'],
                        'away_score': result['away_score'],
                        'minute': scorer['minute'],
                        'penalty': scorer['penalty'],
                        'own_goal': scorer['own_goal']
                    }

    for a in scorer_data.values():
        lt.addLast(lista_anotadores, a)

    lista_anotadores = merg.sort(lista_anotadores, comparar_anotadores)
    lista_anotadores = lt.subList(lista_anotadores, 1, N)

    return len(total_anotadores), len(partidos_anotadores), len(total_t), total_goles, total_goles_penal, total_autogoles, lista_anotadores






                    
        
        
    




def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass




    
# Funciones de ordenamiento

def sort(data, ordenamiento):
    # Ordenar las listas usando los criterios de comparación definidos
    if ordenamiento == "Shell".lower():
        #sa.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        sa.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #sa.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)
    elif ordenamiento == "Selection".lower():
        #se.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        se.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #se.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)    
    elif ordenamiento == "Insertion".lower():
        #ins.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        ins.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #ins.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)    
       

# Funciones de ordenamiento

def getFirstNum(number, tablelist):
    if number <= lt.size(tablelist):
        firsts = lt.newList('ARRAY_LIST')
        for element in range(1, number+1):
            d = lt.getElement(tablelist, element)
            lt.addLast(firsts, d)
        return firsts
    else:
        return tablelist
def getLastNum(number, tablelist):
    if number <= lt.size(tablelist):
        last = lt.newList('ARRAY_LIST')
        for element in range(0,number):
            d = lt.getElement(tablelist, lt.size(tablelist)-element)
            lt.addFirst(last, d)
        return last
    else:
        return tablelist

def listFusion(list1, list2):
    listfusion = lt.newList('ARRAY_LIST')
    for element in lt.iterator(list1):
        lt.addLast(listfusion, element)
    for element in lt.iterator(list2):
        lt.addLast(listfusion, element)
    return listfusion

def getnameTeam(tableList,name):
    nameTeam = lt.newList('ARRAY_LIST')
    x =lt.compareElements(tableList, name, element)
    for element in lt.iterator(tableList['home_team']):
        if name == element:
            nameTeam.addLast(element)

