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
from datetime import date
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
    
    data = {'matches': None, 'goal_scorers':None, 'shootouts':None}

    data['matches'] = lt.newList('ARRAY_LIST',cmpfunction=compare)
    data['goal_scorers'] = lt.newList('ARRAY_LIST',cmpfunction=compare)
    data['shootouts'] = lt.newList('ARRAY_LIST',cmpfunction=compare)

    return data

def modificar_listas(data):
    # Función que modifica el tipo de representación de la lista para cargar el catálogo
    data['matches'] = lt.newList("SINGLE_LINKED",cmpfunction=compare)
    data['goal_scorers'] = lt.newList("SINGLE_LINKED",cmpfunction=compare)
    data['shootouts'] = lt.newList("SINGLE_LINKED",cmpfunction=compare)

    return data

# Funciones para agregar informacion al modelo


def add_match(data, match):
    lt.addLast(data['matches'], match)


def matchesSize(data):
    return lt.size(data['matches'])

def add_goalscorer(data, goalscorer):
    lt.addLast(data["goal_scorers"], goalscorer)

def goalScorersSize(data):
    return lt.size(data["goal_scorers"])


def add_shootouts(data, shootout):
    lt.addLast(data['shootouts'], shootout)

def shootoutsSize(data):
    return lt.size(data["shootouts"])


def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    if len(data)==10:
        add_match(data_structs,data)
    elif len(data)==9:
        add_goalscorer(data_structs,data)
    elif len(data)==5:
        add_shootouts(data_structs,data)

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
    matches_size = matchesSize(data_structs)
    goalScorers_size = goalScorersSize(data_structs)
    shootouts_size = shootoutsSize(data_structs)
    return (matches_size, goalScorers_size, shootouts_size)

def req_1(data_structs, partidos, equipo, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    respuesta = lt.newList('SINGLE_LINKED',cmpfunction=compare)
    size = lt.size(respuesta)
    matches = data_structs['matches']
    i=1
    if condicion == '3':
        while size < int(partidos) and i < data_size(data_structs)[0]:
            elemento = lt.getElement(matches,i)
            if elemento['home_team'] == equipo or elemento['away_team'] == equipo:
                lt.addLast(respuesta,elemento)
            size = lt.size(respuesta)
            i+=1
    elif condicion == '1':
        while size < int(partidos) and i < data_size(data_structs)[0]:
            elemento = lt.getElement(matches,i)
            if elemento['home_team'] == equipo:
                lt.addLast(respuesta, elemento)
            size = lt.size(respuesta)
            i+=1
    else:
        while size < int(partidos) and i < data_size(data_structs)[0]:
            elemento = lt.getElement(matches,i)
            if elemento['away_team'] == equipo:
                lt.addLast(respuesta, elemento)
            size = lt.size(respuesta)
            i+=1
    return respuesta, size


def req_2(data_structs, nombreJugador, numeroGoles):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    goal_scorers = data_structs['goal_scorers']

    results = lt.newList('SINGLE_LINKED',cmpfunction=compare)
    filtered = lt.newList('SINGLE_LINKED',cmpfunction=compare)

    for i in range(1,lt.size(goal_scorers)+1):

        goleador = lt.getElement(goal_scorers,i)
        jugadorActual = goleador['scorer']
        anotaciones = {}

        if jugadorActual.lower() == nombreJugador.lower():
            anotaciones['id'] = i
            anotaciones['date'] = goleador['date']
            anotaciones['home_team'] = goleador['home_team']
            anotaciones['away_team'] = goleador['away_team']
            anotaciones['team'] = goleador['team']
            anotaciones['minute'] = goleador['minute']
            anotaciones['penalty'] = goleador['penalty']
            anotaciones['own_goal'] = goleador['own_goal']
            lt.addLast(results,anotaciones)

    resultsSorted = merg.sort(results, sort_goleadores)
    
    for j in range(1, lt.size(resultsSorted)+1):
        lt.addLast(filtered,lt.getElement(resultsSorted,j))

    if lt.size(filtered) > int(numeroGoles):
        lt.subList(filtered,1,int(numeroGoles))

    return filtered, lt.size(results)


def req_3(data_structs,nombre_equipo,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    matches = data_structs['matches']
    goal_scorers = data_structs['goal_scorers']

    results = lt.newList('SINGLE_LINKED',cmpfunction=compare)

    sub_match = lt.newList('ARRAY_LIST',cmpfunction=compare)
    sub_goal_scorers = lt.newList('ARRAY_LIST',cmpfunction=compare)

    localmatch = 0
    visitantematch = 0

    for match in lt.iterator(matches):

        homeTeam = match['home_team']
        awayTeam = match['away_team']

        if match['date'] != 'Unknown':
            if match['date'] >= fecha_inicial and match['date'] <= fecha_final:
                if homeTeam.lower() == nombre_equipo.lower() or awayTeam.lower() == nombre_equipo.lower():
                    if homeTeam.lower() == nombre_equipo.lower():
                        localmatch += 1
                    elif awayTeam.lower() == nombre_equipo.lower():
                        visitantematch += 1
                    lt.addLast(sub_match, match)

    for goles in lt.iterator(goal_scorers):

        homeTeam = goles['home_team']
        awayTeam = goles['away_team']

        if goles['date'] != 'Unknown':
            if homeTeam.lower() == nombre_equipo.lower() or awayTeam.lower() == nombre_equipo.lower():
                if goles['date'] >= fecha_inicial and goles['date'] <= fecha_final :
                    lt.addLast(sub_goal_scorers, goles)

    for i in range(1,lt.size(sub_match)+1):
        partido = lt.getElement(sub_match,i)
        
        dictPorPartido = {
        'id': i,
        'date': partido['date'],
        'home_score': partido['home_score'],
        'away_score': partido['away_score'],
        'home_team': partido['home_team'],
        'away_team': partido['away_team'],
        'country': partido['country'],
        'city': partido['city'],
        'tournament': partido['tournament'],
        'penalty': 0,
        'own_goal': 0 
    }
        
        for j in range(1, lt.size(sub_goal_scorers) + 1):
            goles = lt.getElement(sub_goal_scorers, j)
            if partido['date'] == goles['date'] and partido['home_team'] == goles['home_team'] and partido['away_team'] == goles['away_team']:
                if goles['penalty'] == 'True':
                    dictPorPartido['penalty'] += 1
                if goles['own_goal'] == 'True':
                    dictPorPartido['own_goal'] += 1

        lt.addLast(results,dictPorPartido)

    return results, lt.size(sub_match), localmatch, visitantematch




def req_4(data_structs, nombre_torneo, fecha_inic, fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    matches = data_structs['matches']
    shootouts = data_structs['shootouts']
    torneo = lt.newList('SINGLE_LINKED', cmpfunction=compare)
    ciudades = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    paises = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    for match in lt.iterator(matches):
        if match['date'] != 'Unknown':
            if match['date'] >= fecha_inic and match['date'] <= fecha_fin:
                if match['tournament'] == nombre_torneo:
                    lt.addLast(torneo, match)

                    if lt.isPresent(ciudades, match['city'])==0:
                        lt.addLast(ciudades, match['city'])
        
                    if lt.isPresent(paises, match['country'])==0:
                        lt.addLast(paises, match['country'])
                    
    vacio = False
    torneo_ord = None
    penalties = 0
    if lt.size(torneo) == 0:
        vacio = True
    else:
        for match in lt.iterator(torneo):
            fecha_match, home_team_match, away_team_match = match['date'], match['home_team'], match['away_team']
            match['penal'] = False
            match['winner'] = 'Unknown'
            del match['neutral']
            for shootout in lt.iterator(shootouts):
                if fecha_match == shootout['date'] and home_team_match.lower() == shootout['home_team'].lower() and away_team_match.lower() == shootout['away_team'].lower():
                    penalties += 1
                    match['penal'] = True
                    match['winner'] = shootout['winner']
       
        torneo_ord = merg.sort(torneo, cmp_partidos_by_fecha_pais_ciudad)

    conteo_partidos = lt.size(torneo)
    conteo_ciudades = lt.size(ciudades)
    conteo_paises = lt.size(paises)
        
    return conteo_partidos, conteo_paises, conteo_ciudades, penalties, torneo_ord, vacio


def req_5(data_structs, nombre, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    matches = data_structs['matches']
    goal_scorers = data_structs['goal_scorers']
    jugador = lt.newList('SINGLE_LINKED',cmpfunction=compare)
    sub_match = lt.newList('ARRAY_LIST',cmpfunction=compare)
    sub_goal_scorers = lt.newList('ARRAY_LIST',cmpfunction=compare)
    results = lt.newList('ARRAY_LIST',cmpfunction=compare)
    goles = lt.newList('ARRAY_LIST',cmpfunction=compare)
    tournaments = lt.newList('ARRAY_LIST',cmpfunction=compare_1)
    penaltis = 0
    autogoles = 0

    for match in lt.iterator(matches):
        if match['date'] != 'Unknown':
            if match['date'] >= fecha_inicial and match['date'] <= fecha_final:
                lt.addLast(sub_match, match)
    
    for goal_scorer in lt.iterator(goal_scorers):
        if goal_scorer['date'] != 'Unknown':
            if goal_scorer['date'] >= fecha_inicial and goal_scorer['date'] <= fecha_final:
                lt.addLast(sub_goal_scorers, goal_scorer)
    
    for goal_scorer in lt.iterator(sub_goal_scorers):
        if goal_scorer['scorer'] == nombre.lower():
            lt.addLast(goles,goal_scorer)

    for goal_scorer in lt.iterator(goles):
        encontro = False
        i = 1
        while not encontro and i < lt.size(sub_match):
            elemento = lt.getElement(sub_match,i)
            if elemento['date'] == goal_scorer['date'] and elemento['home_team'] == goal_scorer['home_team'] and elemento['away_team'] == goal_scorer['away_team']:
                lt.addLast(results,elemento)
                encontro = True
                if lt.isPresent(tournaments,elemento['tournament']) == 0:
                    lt.addLast(tournaments,elemento['tournament'])
            i += 1
        if goal_scorer['penalty'] == 'True':
            penaltis +=1
        if goal_scorer['own_goal'] == 'True':
            autogoles += 1 
    
    if lt.size(goles) !=0:
        for i in range(1,lt.size(goles)+1):
            anotacion = {}
            partido = lt.getElement(results,i)
            anotador = lt.getElement(goles,i)
            anotacion['id'] = i
            anotacion['date'] = anotador['date']
            anotacion['minute'] = anotador['minute']
            anotacion['home_team'] = anotador['home_team']
            anotacion['away_team'] = anotador['away_team']
            anotacion['team'] = anotador['team']
            anotacion['home_score'] = partido['home_score']
            anotacion['away_score'] = partido['away_score']
            anotacion['torunament'] = partido['tournament']
            anotacion['penalty'] = anotador['penalty']
            anotacion['own_goal'] = anotador['own_goal']
            lt.addLast(jugador,anotacion)

    return jugador, lt.size(jugador), lt.size(tournaments), penaltis, autogoles

def req_6(data_structs, cantidad_equipos, torneo, fecha_inicial, fecha_final ):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    matches = data_structs['matches']
    sub_matches = lt.newList('ARRAY_LIST', cmpfunction=compare)
    sub_goal_scorers = lt.newList('ARRAY_LIST', cmpfunction=compare)
    goal_scorers = data_structs['goal_scorers']
    equipos = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    equipos_id = lt.newList('SINGLE_LINKED', cmpfunction=compare)
    paises = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    ciudades = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    ciudades_id = lt.newList('SINGLE_LINKED', cmpfunction=compare)
    partidos_torneo = 0

    for goal_scorer in lt.iterator(goal_scorers):
        if goal_scorer['date'] != 'Unknown':
            if goal_scorer['date'] >= fecha_inicial and goal_scorer['date'] <= fecha_final:
                lt.addLast(sub_goal_scorers,goal_scorer)

    i = 1
    j = 1
    for match in lt.iterator(matches):
        if match['date'] != 'Unknown':
            if match['date'] >= fecha_inicial and match['date'] <= fecha_final and match['tournament'].lower() == torneo:
                partidos_torneo += 1
                match_copy = match.copy()
                match_copy['goles'] = lt.newList('SINGLE_LINKED',cmpfunction=compare)
                for goal_scorer in lt.iterator(sub_goal_scorers):
                    if goal_scorer['date'] != 'Unknown':
                        if goal_scorer['date'] == match_copy['date'] and goal_scorer['home_team'] == match_copy['home_team'] and goal_scorer['away_team'] == match_copy['away_team']:
                            lt.addLast(match_copy['goles'],goal_scorer)
                #lt.addLast(sub_matches, match)
                if match['home_team'] != 'Unknown':
                    if lt.isPresent(equipos,match['home_team']) == 0:
                        equipo = {'id':i, 'equipo':match['home_team'],
                                  'diferencia de goles':0, 
                                  'partidos':0, 
                                  'puntos':0, 
                                  'penales':0,
                                  'autogoles':0,
                                  'victorias':0,
                                  'empates':0, 
                                  'derrotas':0,
                                  'anotados':0, 
                                  'recibidos':0,
                                  'jugador':{'jugador':None,
                                             'anotaciones':None, 
                                             'partidos en los que anotó':None,
                                             'promedio':None}, 
                                  'resultados': lt.newList('SINGLE_LINKED',cmpfunction=compare)}
                        lt.addLast(equipos, match['home_team'])
                        lt.addLast(equipos_id,equipo)
                        lt.addLast(equipo['resultados'],match_copy)
                        if match['home_score'] != 'Unknown':
                            equipo['diferencia de goles'] += match['home_score']
                            equipo['anotados'] += match['home_score']
                        if match['away_score'] != 'Unknwon':
                            equipo['diferencia de goles'] -= match['away_score']
                            equipo['recibidos'] += match['away_score']
                        equipo['partidos'] += 1
                        if match['home_score'] != 'Unknown' and match['away_score'] != 'Unknown':
                            equipo['puntos'] += puntos(match['home_score'],match['away_score'])[0]
                            if puntos(match['home_score'],match['away_score'])[1] == 1:
                                equipo['victorias'] += 1
                            elif puntos(match['home_score'],match['away_score'])[1] == 0:
                                equipo['empates'] += 1
                            else:
                                equipo['derrotas'] += 1 
                        i += 1
                    else:
                        pos = lt.isPresent(equipos,match['home_team'])
                        team = lt.getElement(equipos_id,pos)
                        lt.addLast(team['resultados'],match_copy)
                        if match['home_score'] != 'Unknown':
                            team['diferencia de goles'] += match['home_score']
                            team['anotados'] += match['home_score']
                        if match['away_score'] != 'Unknown':
                            team['diferencia de goles'] -= match['away_score']
                            team['recibidos'] += match['away_score']
                        team['partidos'] += 1
                        if match['home_score'] != 'Unknow' and match['away_score'] != 'Unknown':
                            team['puntos'] += puntos(match['home_score'],match['away_score'])[0]
                            if puntos(match['home_score'],match['away_score'])[1] == 1:
                                team['victorias'] += 1
                            elif puntos(match['home_score'],match['away_score'])[1] == 0:
                                team['empates'] += 1
                            else:
                                team['derrotas'] += 1 
                if match['away_team'] != 'Unknown':
                    if lt.isPresent(equipos,match['away_team']) == 0:
                        equipo = {'id':i, 
                                  'equipo':match['away_team'],
                                  'diferencia de goles':0, 
                                  'partidos':0, 'puntos':0, 
                                  'penales':0,'autogoles':0,
                                  'victorias':0, 'empates':0, 
                                  'derrotas':0,'anotados':0, 
                                  'recibidos':0,
                                  'jugador':{'jugador':None, 
                                             'anotaciones':None, 
                                             'partidos en los que anotó':None,
                                             'promedio':None}, 
                                  'resultados': lt.newList('SINGLE_LINKED',cmpfunction=compare)}
                        lt.addLast(equipos, match['away_team']) 
                        lt.addLast(equipos_id, equipo)
                        lt.addLast(equipo['resultados'],match_copy)
                        if match['away_score'] != 'Unknown':
                            equipo['diferencia de goles'] += match['away_score']
                            equipo['anotados'] += match['away_score']
                        if match['home_score'] != 'Unknown':
                            equipo['diferencia de goles'] -= match['home_score']
                            equipo['recibidos'] += match['home_score']
                        equipo['partidos'] += 1
                        if match['away_score'] != 'Unknown' and match['home_score'] != 'Unknown':
                            equipo['puntos'] += puntos(match['away_score'],match['home_score'])[0]
                            if puntos(match['away_score'],match['home_score'])[1] == 1:
                                equipo['victorias'] += 1
                            elif puntos(match['away_score'],match['home_score'])[1] == 0:
                                equipo['empates'] += 1
                            else:
                                equipo['derrotas'] += 1 
                        i += 1
                    else:
                        pos = lt.isPresent(equipos,match['away_team'])
                        team = lt.getElement(equipos_id,pos)
                        lt.addLast(team['resultados'],match_copy)
                        if match['away_score'] != 'Unknown':
                            team['diferencia de goles'] += match['away_score']
                            team['anotados'] += match['away_score']
                        if match['home_score'] != 'Unknown':
                            team['diferencia de goles'] -= match['home_score']
                            team['recibidos'] += match['home_score']
                        team['partidos'] += 1
                        if match['away_score'] != 'Unknown' and match['home_score'] != 'Unknown':
                            team['puntos'] += puntos(match['away_score'],match['home_score'])[0]
                            if puntos(match['away_score'],match['home_score'])[1] == 1:
                                team['victorias'] += 1
                            elif puntos(match['away_score'],match['home_score'])[1] == 0:
                                team['empates'] += 1
                            else:
                                team['derrotas'] += 1 
            if match['tournament'].lower() == torneo:
                if lt.isPresent(sub_matches, match) == 0:
                    lt.addLast(sub_matches, match)
                if match['country'] != 'Unknown':
                    if lt.isPresent(paises, match['country']) == 0:
                        lt.addLast(paises, match['country'])
                if match['city'] != 'Unknown':
                    if lt.isPresent(ciudades,match['city']) == 0:
                        ciudad = {'id':j, 'ciudad':match['city'], 'cantidad':0}
                        lt.addLast(ciudades,match['city'])
                        lt.addLast(ciudades_id,ciudad)
                        ciudad['cantidad'] += 1
                        j += 1
                    else:
                        pos = lt.isPresent(ciudades,match['city'])
                        city = lt.getElement(ciudades_id,pos)
                        city['cantidad'] += 1
    sort_equipos(equipos_id)
    if not lt.isEmpty(equipos_id):
        k = 1
        for i in range(1,cantidad_equipos+1):
            jugadores_id = lt.newList('SINGLE_LINKED',cmpfunction=compare)
            jugadores = lt.newList('SINGLE_LINKED',cmpfunction=compare_1)
            equipo = lt.getElement(equipos_id,i)
            penaltis = 0
            autogoles = 0
            max_goleador = None
            goles = 0
            partidos_goles = None
            anotaciones = None
            for match in lt.iterator(equipo['resultados']):
                for anotacion in lt.iterator(match['goles']):
                    if anotacion['penalty'] == 'True':
                        penaltis += 1
                    if anotacion['own_goal'] == 'True':
                        autogoles += 1
                    if anotacion['scorer'] != 'Unknown':
                        if lt.isPresent(jugadores, anotacion['scorer']) == 0:
                            jugador = {'id':k,
                                       'nombre':anotacion['scorer'],
                                       'cantidad':1,
                                       'partidos':lt.newList('SINGLE_LINKED',cmpfunction=compare),
                                       'anotaciones':lt.newList('SINGLE_LINKED',cmpfunction=compare)}
                            lt.addLast(jugadores,anotacion['scorer'])
                            lt.addLast(jugador['anotaciones'],anotacion)
                            lt.addLast(jugadores_id,jugador)
                            if lt.isPresent(jugador['partidos'],match) == 0:
                                lt.addLast(jugador['partidos'],match)
                            k += 1
                        else:
                            if anotacion['scorer'] != 'Unknown':
                                pos = lt.isPresent(jugadores,anotacion['scorer'])
                                elemento = lt.getElement(jugadores_id,pos)
                                elemento['cantidad'] += 1
                                lt.addLast(elemento['anotaciones'],anotacion)
                                if lt.isPresent(elemento['partidos'],match) == 0:
                                    lt.addLast(elemento['partidos'],match)
            for jugador in lt.iterator(jugadores_id):
                if jugador['cantidad'] > goles:
                    goles = jugador['cantidad']
                    max_goleador = jugador['nombre']
                    partidos_goles = lt.size(jugador['partidos'])
                    anotaciones = jugador['anotaciones']
            equipo['jugador']['jugador'] = max_goleador
            if goles != 0:
                equipo['jugador']['anotaciones'] = goles
            equipo['jugador']['partidos en los que anotó'] = partidos_goles
            minutos = 0
            if anotaciones is not None:
                for anotacion in lt.iterator(anotaciones):
                    minutos += anotacion['minute']
                equipo['jugador']['promedio'] = (minutos//lt.size(anotaciones))
            equipo['penales'] = penaltis
            equipo['autogoles'] = autogoles
        max_ciudad = 0
        nom_max_ciudad = None
        for ciudad in lt.iterator(ciudades_id):
            if ciudad['cantidad'] > max_ciudad:
                max_ciudad = ciudad['cantidad']
                nom_max_ciudad = ciudad['ciudad']
        r = lt.subList(equipos_id,1,cantidad_equipos), lt.size(sub_matches), partidos_torneo, lt.size(paises),lt.size(ciudades),nom_max_ciudad
    else:
        r = 0, 0, 0, 0, 0, 0
    return r

def puntos(goles_1,goles_2):
    p = 1
    r = 0
    if goles_1 > goles_2:
        p = 3
        r = 1
    elif goles_1 < goles_2:
        p = 0
        r = -1
    return p, r 

def sort_equipos(equipos):
    equipos = merg.sort(equipos,sort_criteria_equipos)
    return equipos

def sort_criteria_equipos(equipo1,equipo2):
    respuesta = False
    if equipo1['puntos'] > equipo2['puntos']:
        respuesta = True
    elif equipo1['puntos'] == equipo2['puntos']:
        if equipo1['diferencia de goles'] > equipo2['diferencia de goles']:
            respuesta = True
        elif equipo1['diferencia de goles'] == equipo2['diferencia de goles']:
            if equipo1['penales'] > equipo2['penales']:
                respuesta = True
            elif equipo1['penales'] == equipo2['penales']:
                if equipo1['partidos'] < equipo2['partidos']:
                    respuesta = True
                elif equipo1['partidos'] == equipo2['partidos']:
                    if equipo1['autogoles'] < equipo2['autogoles']:
                        respuesta = True
    return respuesta

def req_7(data_structs, numeroJugadores, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    matches = data_structs['matches']
    goal_scorers = data_structs['goal_scorers']
    
    sub_matches = lt.newList('ARRAY_LIST', cmpfunction=compare)
    sub_goal_scorers = lt.newList('ARRAY_LIST', cmpfunction=compare)

    respuesta = lt.newList('SINGLE_LINKED', cmpfunction=compare)
    
    torneosUnicos = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    golesTotales = 0
    for match in lt.iterator(matches):
        if match['date'] != 'Unknown':
            if match['date'] >= fecha_inicial and match['date'] <= fecha_final:
                torneo = match['tournament']
                if torneo != "Friendly":
                    lt.addLast(sub_matches, match)
                    if lt.isPresent(torneosUnicos, torneo)==0:
                        lt.addLast(torneosUnicos, torneo)
                    
                    golesTotales += match['home_score'] + match['away_score']

    anotadoresUnicos = {}
    partidosUnicos = lt.newList('SINGLE_LINKED', cmpfunction=compare_1)
    
    contadorPenales = 0
    contadorAutogol = 0
    
    dictRespuesta = {}

    for goal_scorer in lt.iterator(goal_scorers):

        if goal_scorer['date'] != 'Unknown':
            if goal_scorer['date'] >= fecha_inicial and goal_scorer['date'] <= fecha_final:

                torneos = lt.newList('ARRAY_LIST')

                fechas = lt.newList('ARRAY_LIST')
                away_teams = lt.newList('ARRAY_LIST')
                home_teams = lt.newList('ARRAY_LIST')
                minutesA = lt.newList('ARRAY_LIST')
                penalty = lt.newList('ARRAY_LIST')
                own_goal = lt.newList('ARRAY_LIST')
            
                lt.addLast(sub_goal_scorers, goal_scorer)
                lt.addLast(fechas, goal_scorer['date'])
                lt.addLast(away_teams, goal_scorer['away_team'])
                lt.addLast(home_teams, goal_scorer['home_team'])
                lt.addLast(minutesA, goal_scorer['minute'])
                lt.addLast(penalty, goal_scorer['penalty'])
                lt.addLast(own_goal, goal_scorer['own_goal'])

                if goal_scorer['scorer'] not in anotadoresUnicos:

                    anotadoresUnicos[goal_scorer['scorer']] = {'goles': 1, 'penales': 0, 'autogoles': 0, 'minutes': goal_scorer['minute'],
                                                                'fechas': fechas, 'away_teams': away_teams, 'home_teams': home_teams, 
                                                                'torneos': torneos, 'golesVictoria':0, 'golesDerrota':0, 'golesEmpate':0,
                                                                'equipo': goal_scorer['team'], 'minutesArray': minutesA, 'penalty': penalty, 'own_goal': own_goal}
            
                    if goal_scorer['penalty']=='True':
                        anotadoresUnicos[goal_scorer['scorer']]['penales'] = 1
                    if goal_scorer['own_goal']=='True':
                        anotadoresUnicos[goal_scorer['scorer']]['autogoles'] = 1
                    
                else:
                    anotadoresUnicos[goal_scorer['scorer']]['goles'] += 1
                    anotadoresUnicos[goal_scorer['scorer']]['minutes'] += goal_scorer['minute']
                    if goal_scorer['penalty']=='True':
                        anotadoresUnicos[goal_scorer['scorer']]['penales'] += 1
                    if goal_scorer['own_goal']=='True':
                        anotadoresUnicos[goal_scorer['scorer']]['autogoles'] += 1

                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['fechas'], goal_scorer['date'])
                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['away_teams'], goal_scorer['away_team'])
                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['home_teams'], goal_scorer['home_team'])
                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['minutesArray'], goal_scorer['minute'])
                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['penalty'], goal_scorer['penalty'])
                    lt.addLast(anotadoresUnicos[goal_scorer['scorer']]['own_goal'], goal_scorer['own_goal'])

        

                idPartido = str(goal_scorer['date']) + goal_scorer['home_team'] + goal_scorer['away_team']

                if lt.isPresent(partidosUnicos, idPartido)==0:
                    lt.addLast(partidosUnicos, idPartido)

                penalActual = goal_scorer['penalty']
                autogolActual = goal_scorer['own_goal']

                if penalActual == 'True':
                    contadorPenales += 1

                if autogolActual == 'True':
                    contadorAutogol += 1


    resultsByGoal = lt.newList('ARRAY_LIST')

    for partido in lt.iterator(sub_matches):

        i = 0

        lastGoal = {}

        for nombreActual in anotadoresUnicos.keys():

            value = anotadoresUnicos[nombreActual]

            lastMatch = lt.newList('ARRAY_LIST')

            for j in range(lt.size(value['fechas'])):
  
                fecha = lt.getElement(value['fechas'], j)
                home_team = lt.getElement(value['home_teams'], j)
                away_team = lt.getElement(value['away_teams'], j)
                minute = lt.getElement(value['minutesArray'], j)
                home_score = partido['home_score']
                away_score = partido['away_score']
                penalty = lt.getElement(value['penalty'], j)
                own_goal = lt.getElement(value['own_goal'], j)

                if partido['date'] == fecha and partido['home_team'] == home_team and partido['away_team'] == away_team:
                    if lt.isPresent(value['torneos'], partido['tournament'])==0:
                        lt.addLast(value['torneos'], partido['tournament'])

                    equipoJugador = value['equipo']
 
                    if home_score > away_score:
                        if equipoJugador == home_team:
                            anotadoresUnicos[nombreActual]['golesVictoria'] += 1
                        elif equipoJugador == away_team:
                            anotadoresUnicos[nombreActual]['golesDerrota'] += 1

                    elif home_score < away_score:
                        if equipoJugador == home_team:
                            anotadoresUnicos[nombreActual]['golesDerrota'] += 1
                        elif equipoJugador == away_team:
                            anotadoresUnicos[nombreActual]['golesVictoria'] += 1
                    elif home_score == away_score:
                        anotadoresUnicos[nombreActual]['golesEmpate'] += 1

                    
                    if j == 0:
                        lt.addLast(lastMatch, fecha)
                        lt.addLast(lastMatch, partido['tournament'])
                        lt.addLast(lastMatch, home_team)
                        lt.addLast(lastMatch, away_team)
                        lt.addLast(lastMatch, home_score)
                        lt.addLast(lastMatch, away_score)
                        lt.addLast(lastMatch, minute)
                        lt.addLast(lastMatch, penalty)
                        lt.addLast(lastMatch, own_goal)

                        lastGoal[nombreActual] = lastMatch
            
                        lt.addLast(resultsByGoal, lastGoal)

            i += 1

    for anotador in anotadoresUnicos:

        dictPorJugador = {
            'puntajeAnotador': 0,
            'totalGoles': 0,
            'totalGolesPenales': 0,
            'totalAutogoles': 0,
            'tiempoPromedio': 0,
            'totalTorneos': 0,
            'totalAnotacionesVictoria': 0,
            'totalAnotacionesEmpate': 0,
            'totalAnotacionesDerrota': 0,
            'PuntajeSort': 0,
            'ultimoGol': {
                'fecha': 'Unknown',
                'torneo': 'Unknown',
                'home_team': 'Unknown',
                'away_team': 'Unknown',
                'home_score': 'Unknown',
                'away_score': 'Unknown',
                'minute': 'Unknown',
                'penalty': 'Unknown',
                'own_goal': 'Unknown'
            }
        }

        nombreJugador = anotador 
        if nombreJugador not in dictRespuesta:
            
            dictRespuesta[nombreJugador] = dictPorJugador

        dictPorJugador['nombre']= nombreJugador

        dictPorJugador['totalGoles'] = anotadoresUnicos[nombreJugador]['goles']

        dictPorJugador['puntajeAnotador'] = anotadoresUnicos[nombreJugador]['goles'] + anotadoresUnicos[nombreJugador]['penales'] - anotadoresUnicos[nombreJugador]['autogoles']

        dictPorJugador['totalGolesPenales'] = anotadoresUnicos[nombreJugador]['penales']

        dictPorJugador['totalAutogoles'] = anotadoresUnicos[nombreJugador]['autogoles']

        dictPorJugador['tiempoPromedio'] = anotadoresUnicos[nombreJugador]['minutes'] / anotadoresUnicos[nombreJugador]['goles']

        dictPorJugador['totalTorneos'] = lt.size(anotadoresUnicos[nombreJugador]['torneos'])

        dictPorJugador['totalAnotacionesVictoria'] = anotadoresUnicos[nombreJugador]['golesVictoria']

        dictPorJugador['totalAnotacionesEmpate'] = anotadoresUnicos[nombreJugador]['golesEmpate']

        dictPorJugador['totalAnotacionesDerrota'] = anotadoresUnicos[nombreJugador]['golesDerrota']

        dictPorJugador['PuntajeSort'] = anotadoresUnicos[nombreJugador]['goles'] + anotadoresUnicos[nombreJugador]['penales'] - anotadoresUnicos[nombreJugador]['autogoles'] 

        
        for jugador in lt.iterator(resultsByGoal):

            if nombreJugador in jugador.keys():
                dictPorJugador['ultimoGol']['fecha'] = jugador[nombreJugador]['elements'][0]
                dictPorJugador['ultimoGol']['torneo'] = jugador[nombreJugador]['elements'][1]
                dictPorJugador['ultimoGol']['home_team'] = jugador[nombreJugador]['elements'][2]
                dictPorJugador['ultimoGol']['away_team'] = jugador[nombreJugador]['elements'][3]
                dictPorJugador['ultimoGol']['home_score'] = jugador[nombreJugador]['elements'][4]
                dictPorJugador['ultimoGol']['away_score'] = jugador[nombreJugador]['elements'][5]
                dictPorJugador['ultimoGol']['minute'] = jugador[nombreJugador]['elements'][6]
                dictPorJugador['ultimoGol']['penalty'] = jugador[nombreJugador]['elements'][7]
                dictPorJugador['ultimoGol']['own_goal'] = jugador[nombreJugador]['elements'][8]
    
    for i in dictRespuesta:
        lt.addLast(respuesta, dictRespuesta[i])
    
    sorted_respuesta = merg.sort(respuesta, sort_crit)

    numeroJugadores = int(numeroJugadores)
    respuestaFinal = lt.subList(sorted_respuesta, 1, numeroJugadores)
    anotadoresTotales = lt.size(respuesta)
    
    return anotadoresTotales, lt.size(partidosUnicos),lt.size(torneosUnicos), golesTotales, contadorPenales, contadorAutogol, respuestaFinal

def sort_goleadores(a, b):
    if a['date'] < b['date']:
        return True
    elif a['date'] == b['date'] and a['minute'] < b['minute']:
        return True
    return False

def sort_crit(player1, player2):
    puntaje_sort1 = player1['PuntajeSort']
    puntaje_sort2 = player2['PuntajeSort']
    if puntaje_sort1 != puntaje_sort2:
        return puntaje_sort1 > puntaje_sort2
    else:
        tiempo_promedio1 = player1['tiempoPromedio']
        tiempo_promedio2 = player2['tiempoPromedio']
        return tiempo_promedio1 < tiempo_promedio2


def req_8(data_structs, nombre_1, nombre_2, fecha_inic, fecha_fin):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    matches = data_structs["matches"]
    matches = merg.sort(matches,sort_criteria_matches)

    # Primera Parte

    partidosTeam1 = {"local": lt.newList('ARRAY_LIST'), 
                     "visitante": lt.newList('ARRAY_LIST'), 
                     "aniosTotal": lt.newList('ARRAY_LIST', cmpfunction=compare_1)}
    partidosTeam2 = {"local": lt.newList('ARRAY_LIST'),
                     "visitante": lt.newList('ARRAY_LIST'),
                     "aniosTotal": lt.newList('ARRAY_LIST', cmpfunction=compare_1)}

    anios = fecha_fin.year - fecha_inic.year
    
    for match in lt.iterator(matches):
        home, away, torneo, anioFecha = match["home_team"], match["away_team"], match['tournament'], match["date"].year

        if ((home == nombre_1) or (home == nombre_2) or (away == nombre_1) or (away == nombre_2)) and (torneo != 'Friendly'):
            if match['date'] <= fecha_fin and match['date'] >= fecha_inic:
                if home == nombre_1:
                    lt.addLast(partidosTeam1["local"],match)
                    if lt.isPresent(partidosTeam1['aniosTotal'], anioFecha) == 0:
                        lt.addLast(partidosTeam1["aniosTotal"], anioFecha)
                elif away == nombre_1:
                    lt.addLast(partidosTeam1["visitante"],match)
                    if lt.isPresent(partidosTeam1['aniosTotal'], anioFecha) == 0:
                        lt.addLast(partidosTeam1["aniosTotal"], anioFecha)
                elif home == nombre_2:
                    lt.addLast(partidosTeam2["local"],match)
                    if lt.isPresent(partidosTeam2['aniosTotal'], anioFecha) == 0:
                        lt.addLast(partidosTeam2["aniosTotal"], anioFecha)
                elif away == nombre_2:
                    lt.addLast(partidosTeam2["visitante"],match)
                    if lt.isPresent(partidosTeam2['aniosTotal'], anioFecha) == 0:
                        lt.addLast(partidosTeam2["aniosTotal"], anioFecha)

    local_team1, visit_team1 = lt.size(partidosTeam1['local'])+1, lt.size(partidosTeam1['visitante'])  
    total_team1 = local_team1 + visit_team1
    masAntiguo1 = lt.getElement(partidosTeam1['visitante'],lt.size(partidosTeam1['visitante']))['date']
    if lt.getElement(partidosTeam1['local'],lt.size(partidosTeam1['local']))['date'] < masAntiguo1:
        masAntiguo1 = lt.getElement(partidosTeam1['local'],lt.size(partidosTeam1['local']))['date']

    masReciente1_date = lt.getElement(partidosTeam1['visitante'], 1)['date']
    masReciente1 = lt.getElement(partidosTeam1['visitante'], 1)
    if lt.getElement(partidosTeam1['local'],1)['date'] > masReciente1_date:
        masReciente1 = lt.getElement(partidosTeam1['local'], 1)

    local_team2, visit_team2 = lt.size(partidosTeam2['local'])+1, lt.size(partidosTeam2['visitante'])  
    total_team2 = local_team2 + visit_team2
    masAntiguo2 = lt.getElement(partidosTeam2['visitante'],lt.size(partidosTeam2['visitante']))['date']
    if lt.getElement(partidosTeam2['local'],lt.size(partidosTeam2['local']))['date'] < masAntiguo2:
        masAntiguo2 = lt.getElement(partidosTeam2['local'],lt.size(partidosTeam2['local']))['date']

    masReciente2_date = lt.getElement(partidosTeam2['visitante'], 1)['date']
    masReciente2 = lt.getElement(partidosTeam2['visitante'], 1)
    if lt.getElement(partidosTeam2['local'],1)['date'] > masReciente2_date:
        masReciente2 = lt.getElement(partidosTeam2['local'], 1)

    # Estadisticas anuales equipo 1
    estAnuales1 = {}
    for anio in lt.iterator(partidosTeam1['aniosTotal']):
        estAnuales1[lt.getElement(partidosTeam1['aniosTotal'], lt.isPresent(partidosTeam1['aniosTotal'],anio))] = lt.newList('ARRAY_LIST', cmpfunction=compare_1)

    goalscorers = data_structs['goal_scorers']
    shootouts = data_structs['shootouts']

    for anio in lt.iterator(partidosTeam1['aniosTotal']):
        partLocales = partidosTeam1['local']
        puntosTot, goles_marc, goles_recib = 0, 0, 0
        victorias, empates, derrotas = 0, 0, 0
        partidos_anio = 0
        for partLocal in range(lt.size(partLocales)):
            partido = lt.getElement(partLocales, partLocal)

            if partido['date'].year == anio:
                partidos_anio +=1

                goles_marc +=partido['home_score']
                goles_recib +=partido['away_score']

                if partido['home_score'] > partido['away_score']:
                    puntosTot += 3
                    victorias +=1
                elif partido['home_score'] == partido['away_score']:
                    puntosTot +=1
                    empates +=1
                else:
                    derrotas +=1
        
        partVisitantes = partidosTeam1['visitante']
        for partVisit in range(lt.size(partVisitantes)):
            partido = lt.getElement(partVisitantes, partVisit)
            if partido['date'].year == anio:
                partidos_anio +=1

                goles_marc +=partido['away_score']
                goles_recib +=partido['home_score']

                if partido['home_score'] < partido['away_score']:
                    puntosTot += 3
                    victorias += 1
                elif partido['home_score'] == partido['away_score']:
                    puntosTot +=1
                    empates += 1
                else:
                    derrotas += 1

        puntos_penal, autogoles = 0, 0
        mas_anot, goleador, part_jugador, promed = 0, None, lt.newList('ARRAY_LIST'), 0
        mejorJug = {}
        for scored in lt.iterator(goalscorers):
            jugador, goles, part_jug, minutos = scored['scorer'], 0, part_jugador, 0
            if scored['team'] == nombre_1 and scored['date'].year == anio:
                
                # Conteo de autogoles
                if scored['own_goal'] == True or scored['own_goal'] == "True":
                    autogoles += 1
               
                # Conteo penales
                if scored['penalty'] == True or scored['penalty'] == "True":
                    puntos_penal += 1

            # Validación goleador equipo
            for x in lt.iterator(goalscorers):

                if (x['home_team'] == nombre_1 or x['away_team'] == nombre_1) and x['date'].year == anio:
                    if x['scorer'] == jugador:
                        goles += 1
                        minutos += x['minute']
                        if lt.isPresent(part_jug, x['date']) == 0:
                            lt.addLast(part_jug, x['date'])
                                                        
            if goles > mas_anot:
                mas_anot = goles
                goleador = jugador
                part_jugador = part_jug
                promed = minutos/lt.size(part_jugador)

        mejorJug['nombre'] = goleador
        mejorJug['goles'] = mas_anot
        mejorJug['partidos'] = lt.size(part_jugador)
        mejorJug['tiempo_promedio [min]'] = promed

        lt.addLast(estAnuales1[anio], partidos_anio)
        lt.addLast(estAnuales1[anio], puntosTot)
        lt.addLast(estAnuales1[anio], goles_marc-goles_recib)
        lt.addLast(estAnuales1[anio], puntos_penal)
        lt.addLast(estAnuales1[anio], autogoles)
        lt.addLast(estAnuales1[anio], victorias)
        lt.addLast(estAnuales1[anio], empates)
        lt.addLast(estAnuales1[anio], derrotas)
        lt.addLast(estAnuales1[anio], goles_marc)
        lt.addLast(estAnuales1[anio], goles_recib)
        lt.addLast(estAnuales1[anio], mejorJug)

    otrosDatos1 = lt.newList('ARRAY_LIST')
    lt.addLast(otrosDatos1, anios)
    lt.addLast(otrosDatos1, total_team1)
    lt.addLast(otrosDatos1, local_team1)
    lt.addLast(otrosDatos1, visit_team1)
    lt.addLast(otrosDatos1, masAntiguo1)
    lt.addLast(otrosDatos1, masReciente1)

    # Estadisticas anuales equipo 2
    estAnuales2 = {}
    for anio in lt.iterator(partidosTeam2['aniosTotal']):
        estAnuales2[lt.getElement(partidosTeam2['aniosTotal'], lt.isPresent(partidosTeam2['aniosTotal'],anio))] = lt.newList('ARRAY_LIST', cmpfunction=compare_1)

    goalscorers = data_structs['goal_scorers']
    shootouts = data_structs['shootouts']

    for anio in lt.iterator(partidosTeam2['aniosTotal']):
        partLocales = partidosTeam2['local']
        puntosTot, goles_marc, goles_recib = 0, 0, 0
        victorias, empates, derrotas = 0, 0, 0
        partidos_anio = 0
        for partLocal in range(lt.size(partLocales)):
            partido = lt.getElement(partLocales, partLocal)

            if partido['date'].year == anio:
                partidos_anio +=1

                goles_marc +=partido['home_score']
                goles_recib +=partido['away_score']

                if partido['home_score'] > partido['away_score']:
                    puntosTot += 3
                    victorias +=1
                elif partido['home_score'] == partido['away_score']:
                    puntosTot +=1
                    empates +=1
                else:
                    derrotas +=1
        
        partVisitantes = partidosTeam2['visitante']
        for partVisit in range(lt.size(partVisitantes)):
            partido = lt.getElement(partVisitantes, partVisit)
            if partido['date'].year == anio:
                partidos_anio +=1

                goles_marc +=partido['away_score']
                goles_recib +=partido['home_score']

                if partido['home_score'] < partido['away_score']:
                    puntosTot += 3
                    victorias += 1
                elif partido['home_score'] == partido['away_score']:
                    puntosTot += 1
                    empates += 1
                else:
                    derrotas += 1

        puntos_penal, autogoles = 0, 0
        mas_anot, goleador, part_jugador, promed = 0, None, lt.newList('ARRAY_LIST'), 0
        mejorJug = {}
        for scored in lt.iterator(goalscorers):
            jugador, goles, part_jug, minutos = scored['scorer'], 0, part_jugador, 0
            if scored['team'] == nombre_2 and scored['date'].year == anio:
                
                # Conteo de autogoles
                if scored['own_goal'] == True or scored['own_goal'] == "True":
                    autogoles += 1
                
                # Conteo penales
                if scored['penalty'] == True or scored['penalty'] == "True":
                    puntos_penal += 1

            # Validación goleador equipo
            for x in lt.iterator(goalscorers):

                if (x['home_team'] == nombre_2 or x['away_team'] == nombre_2) and x['date'].year == anio:
                    if x['scorer'] == jugador:
                        goles += 1
                        minutos += x['minute']
                        if lt.isPresent(part_jug, x['date']) == 0:
                            lt.addLast(part_jug, x['date'])
                                                        
            if goles > mas_anot:
                mas_anot = goles
                goleador = jugador
                part_jugador = part_jug
                promed = minutos/lt.size(part_jugador)

        mejorJug['nombre'] = goleador
        mejorJug['num_goles'] = mas_anot
        mejorJug['num_partidos'] = lt.size(part_jugador)
        mejorJug['promedio_min'] = promed

        lt.addLast(estAnuales2[anio], partidos_anio)
        lt.addLast(estAnuales2[anio], puntosTot)
        lt.addLast(estAnuales2[anio], goles_marc-goles_recib)
        lt.addLast(estAnuales2[anio], puntos_penal)
        lt.addLast(estAnuales2[anio], autogoles)
        lt.addLast(estAnuales2[anio], victorias)
        lt.addLast(estAnuales2[anio], empates)
        lt.addLast(estAnuales2[anio], derrotas)
        lt.addLast(estAnuales2[anio], goles_marc)
        lt.addLast(estAnuales2[anio], goles_recib)
        lt.addLast(estAnuales2[anio], mejorJug)
    
    otrosDatos2 = lt.newList('ARRAY_LIST')
    lt.addLast(otrosDatos2, anios)
    lt.addLast(otrosDatos2, total_team2)
    lt.addLast(otrosDatos2, local_team2)
    lt.addLast(otrosDatos2, visit_team2)
    lt.addLast(otrosDatos2, masAntiguo2)
    lt.addLast(otrosDatos2, masReciente2)

    
    # Segunda Parte

    enComun = lt.newList('ARRAY_LIST')

    partidos_comunes, num_pComunes = lt.newList('ARRAY_LIST', cmpfunction=compare_1), 0
    vict_team1, vict_team2 = 0, 0
    derro_team1, derro_team2 = 0, 0
    ambos = 0
    for match in lt.iterator(matches):
        home, away, torneo, anioFecha = match["home_team"], match["away_team"], match['tournament'], match["date"].year

        if ((nombre_1 == home and nombre_2 == away) or (nombre_2 == home and nombre_1 == away)) and (match['date'] <= fecha_fin and match['date'] >= fecha_inic):

            num_pComunes += 1
            lt.addLast(partidos_comunes, match)
            if nombre_1 == home and nombre_2 == away:

                if match['home_score'] > match['away_score']:
                    vict_team1 += 1
                    derro_team2 += 1

                elif match['home_score'] < match['away_score']:
                    vict_team2 += 1
                    derro_team1 += 1

                elif match['home_score'] == match['away_score']:
                    ambos += 1

            if nombre_2 == home and nombre_1 == away:

                if match['home_score'] > match['away_score']:
                    vict_team2 += 1
                    derro_team1 += 1

                elif match['home_score'] < match['away_score']:
                    vict_team1 += 1
                    derro_team2 += 1

                elif match['home_score'] == match['away_score']:
                    ambos += 1


    masReciente3_date = lt.getElement(partidos_comunes, 1)['date']
    masReciente3 = lt.getElement(partidos_comunes, 1)
    for i in range(lt.size(partidos_comunes)):
        if lt.getElement(partidos_comunes, i)['date'] > masReciente3_date:
            masReciente3 = lt.getElement(partidos_comunes, i)

    goles_ultimo = lt.newList('ARRAY_LIST')
    ultimo = {}
    for goles in lt.iterator(goalscorers):
        if goles['date'] == masReciente3['date'] and goles['home_team'] == masReciente3['home_team'] and goles['away_team'] == masReciente3['away_team']:
            ultimo = goles
            break
        else:
            ultimo['date'] = masReciente3['date']
            ultimo['home_team'] = masReciente3['home_team']
            ultimo['away_team'] = masReciente3['away_team']
            ultimo['team'] = 'Unknown'
            ultimo['scorer'] = 'Unknown'
            ultimo['minuto'] = 'Unknown'
            ultimo['own_goal'] = 'Unknown'
            ultimo['penalty'] = 'Unknown'

    lt.addLast(goles_ultimo, ultimo)


    lt.addLast(enComun, num_pComunes)
    lt.addLast(enComun, vict_team1)
    lt.addLast(enComun, derro_team1)
    lt.addLast(enComun, vict_team2)
    lt.addLast(enComun, derro_team2)
    lt.addLast(enComun, ambos)
    lt.addLast(enComun, masReciente3)
    lt.addLast(enComun, goles_ultimo)

    return otrosDatos1, otrosDatos2, estAnuales1, estAnuales2, enComun


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    respuesta = 0
    if data_1['id'] > data_2['id']:
        respuesta = 1
    elif data_2['id'] < data_2['id']:
        respuesta = -1
    return respuesta

def compare_1(data_1,data_2):
    respuesta = 0
    if data_1 < data_2:
        respuesta = -1
    elif data_1 > data_2:
        respuesta = 1
    return respuesta
# Funciones de ordenamiento


def sort_criteria_matches(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (dict): Resultado 1 a comparar
        data2 (dict): Resultado 2 a comparar 
    Returns:
        bool: Devuelve True si la fecha del resultado 1 es mayor que la fecha del resultado 2.
        En caso de ser iguales, se devuelve True si el marcador del equipo local del resultado 1 
        es mayor que el marcador del equipo local del resultado 2. Si permanece la igualdad, se
        revisa el marcador del equipo visitante.
    """
    #TODO: Crear función comparadora para ordenar
    respuesta = False
    if data_1['date'] > data_2['date']:
        respuesta = True
    elif data_1['date'] == data_2['date']:
        if data_1['home_score'] > data_2['home_score']:
            respuesta = True
        elif data_1['home_score'] == data_2['home_score']:
            if data_1['away_score'] > data_2['away_score']:
                respuesta = True
    return respuesta

def sort_criteria_goal_scorers(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (dict): Goleador 1 a comparar
        data2 (dict): Goleador 2 a comparar 
    Returns:
        bool: Devuelve True si la fecha de la anotación 1 es mayor que la fecha de la anotación 2.
        En caso de ser iguales, se mira si la anotación 1 fue en un minuto menor a la anotación 2.
        Finalmente, al permanecer la igualdad, se revisa el nombre del jugador.
    """
    #TODO: Crear función comparadora para ordenar
    respuesta = False
    if data_1['date'] > data_2['date']:
        respuesta = True
    elif data_1['date'] == data_2['date']:
        if data_1['minute'] < data_2['minute']:
            respuesta = True
        elif data_1['minute'] == data_2['minute']:
            if data_1['scorer'] < data_2['scorer']:
                respuesta = True
    return respuesta

def sort_criteria_shootouts(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (dict): Penaltis 1 a comparar
        data2 (dict): Penaltis 2 a comparar 
    Returns:
        bool: Devuelve True si la fecha del resultado 1 es mayor que la fecha del resultado 2.
        En caso de ser iguales, se devuelve True si el marcador del equipo local del resultado 1 
        es mayor que el marcador del equipo local del resultado 2. Si permanece la igualdad, se
        revisa el marcador del equipo visitante.
    """
    #TODO: Crear función comparadora para ordenar
    respuesta = False
    if data_1['date'] > data_2['date']:
        respuesta = True
    elif data_1['date'] == data_2['date']:
        if data_1['home_team'] < data_2['home_team']:
            respuesta = True
        elif data_1['home_team'] == data_2['home_team']:
            if data_1['away_team'] < data_2['away_team']:
                respuesta = True
    return respuesta


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    matches = data_structs['matches']
    goal_scorers = data_structs['goal_scorers']
    shootouts = data_structs['shootouts']
    sorted_matches = merg.sort(matches, sort_criteria_matches)
    sorted_goal_scorers = merg.sort(goal_scorers, sort_criteria_goal_scorers)
    sorted_shootouts = merg.sort(shootouts, sort_criteria_shootouts)
    data_structs['matches'] = sorted_matches
    data_structs['goal_scorers'] = sorted_goal_scorers
    data_structs['shootouts'] = sorted_shootouts
    return data_structs

def cmp_partidos_by_fecha_y_pais(resultado1,resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que la fecha del resultado2,
    en caso de ser igual se tiene en cuenta si el nombre de la ciudad en que se disputó el partido
    del resultado1 es menor que la ciudad del resultado 2,
    de lo contrario devuelve falso
    """
    fecha1= resultado1["date"]
    fecha2= resultado2["date"]
    if fecha1<fecha2:
        respuesta=True
    elif fecha1==fecha2:
        if resultado1["country"].lower() < resultado2["country"].lower():
            respuesta=True
        else:
            respuesta=False
    else:
        respuesta=False
    return respuesta

def cmp_partidos_by_fecha_pais_ciudad(resultado1,resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que la fecha del resultado2,
    en caso de ser igual se tiene en cuenta si el nombre de la ciudad en que se disputó el partido
    del resultado1 es menor que la ciudad del resultado 2,
    de lo contrario devuelve falso
    """
    fecha1= resultado1["date"]
    fecha2= resultado2["date"]
    if fecha1>fecha2:
        respuesta=True
    elif fecha1==fecha2:
        if resultado1["country"].lower() < resultado2["country"].lower():
            respuesta=True
        elif resultado1["country"].lower() == resultado2["country"].lower():
            if resultado1["city"].lower() < resultado2["city"].lower():
                respuesta = True
            else:
                respuesta = False
        else:
            respuesta=False
    else:
        respuesta=False
    return respuesta

def sortMatches(data,size, orden):
    if size=="1":
        sub_list=lt.subList(data["matches"],1,2238)
    elif size=="2":
        sub_list=lt.subList(data["matches"],1,8952)
    elif size=="3":
        sub_list=lt.subList(data["matches"],1,13429)
    elif size=="4":
        sub_list=lt.subList(data["matches"],1,22381)
    else:
        sub_list=data["matches"]
    if orden=="1":
        sort_list=se.sort(sub_list,cmp_partidos_by_fecha_y_pais)
    elif orden=="2":
        sort_list=ins.sort(sub_list,cmp_partidos_by_fecha_y_pais)
    elif orden == '3':
        sort_list=sa.sort(sub_list,cmp_partidos_by_fecha_y_pais)
    elif orden == '4':
        sort_list=merg.sort(sub_list, cmp_partidos_by_fecha_y_pais)
    else:
        sort_list=quk.sort(sub_list,cmp_partidos_by_fecha_y_pais)
    return sort_list

def sort_goleadores(a, b):
    if a['date'] < b['date']:
        return True
    elif a['date'] == b['date'] and a['minute'] < b['minute']:
        return True
    return False