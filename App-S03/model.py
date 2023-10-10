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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime, timedelta
import bisect as bi
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs(consulta_EDD):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    data_structs = {'goalscorers': None,
                    'results': None,
                    'shootouts': None}

    data_structs['goalscorers'] = lt.newList(consulta_EDD)
    data_structs['results'] = lt.newList(consulta_EDD)
    data_structs['shootouts'] = lt.newList(consulta_EDD)
    return data_structs

# Funciones para agregar informacion al modelo

def add_data(data_structs, archivo, data):
    """
    Función para agregar nuevos elementos de un archivo a la las EEdDD

    Args:
        data_structs (_type_): _description_
        archivo (_type_): _description_
        data (_type_): _description_
    """    
    lt.addLast(data_structs[archivo], data)

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id, sub_id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    for pos in range(1, lt.size(data_structs) + 1):
        element = lt.getElement(data_structs, pos)
        if element[sub_id] == id:
            return element
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(n,n_equipo,condicion,data_structs,valor_ord):
    """
    Función que soluciona el requerimiento 1
    """
    lista = lt.iterator(data_structs["results"])

    partidos_filtrados = lt.newList(datastructure='ARRAY_LIST')
    if condicion == "local":
        for partidos in lista:
            if partidos["home_team"] == n_equipo:
                lt.addLast(partidos_filtrados,partidos)

    if condicion == "visitante":
        for partidos in lista:
            if partidos["away_team"] == n_equipo:
                lt.addLast(partidos_filtrados,partidos)
    else:
        for partidos in lista:
            if partidos["away_team"] == n_equipo or partidos["home_team"]  == n_equipo:
                lt.addLast(partidos_filtrados,partidos)

    partidos_ordenados = sort(partidos_filtrados, valor_ord, criterio_date_min)

    resultado = lt.newList(datastructure='ARRAY_LIST')

    if lt.size(partidos_ordenados) > 6:
        tamano = lt.size(partidos_ordenados)
        resultado = lt.subList(partidos_ordenados,1,3) 
        i = 2
        while i >= 0:
            if n <= tamano:
                valor = lt.getElement(partidos_ordenados,n-i)
                lt.addLast(resultado,valor)
                i = i-1
            else:
                valor = lt.getElement(partidos_ordenados,tamano-i)
                lt.addLast(resultado,valor)
                i = i-1
        return tamano, resultado
    else:
        return lt.size(partidos_ordenados), lt.subList(partidos_ordenados,1,min(n, lt.size(partidos_ordenados)))

    
def req_2(data_structs, jugador, num_gol, valor_ord ):
    """_summary_

    Args:
        data_structs (_type_): _description_
        jugador (_type_): _description_
        num_gol (_type_): _description_

    Returns:
        _type_: _description_
    """    
    lista_anotaciones = lt.iterator(data_structs["goalscorers"])
    
    goles_filtrados = lt.newList(datastructure='ARRAY_LIST')
    for anotacion in lista_anotaciones:
        if anotacion["scorer"].lower() == jugador and anotacion["own_goal"]=="False":
            lt.addLast(goles_filtrados, anotacion)
            
    goles_ordenados = sort(goles_filtrados, valor_ord, criterio_date_min)
    
    
    goles = lt.newList(datastructure='ARRAY_LIST')  
    if lt.size(goles_ordenados) > 6:
        for i in range(1,4):
            if i <= lt.size(goles_ordenados):
                lt.addLast(goles, lt.getElement(goles_ordenados, i))
        for i in range(lt.size(goles_ordenados) - 2, lt.size(goles_ordenados)+1):
            lt.addLast(goles, lt.getElement(goles_ordenados, + 1))
    
    else:
        for i in range(1,min(num_gol, lt.size(goles_ordenados)) + 1):
            lt.addLast(goles, lt.getElement(goles_ordenados, i))
    return lt.size(goles_ordenados), goles

def req_3(data_structs, consulta_equipo, consulta_fecha_i, consulta_fecha_f, valor_ord):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista_resultados = lt.iterator(data_structs["results"])
    lista_anotaciones = lt.iterator(data_structs["goalscorers"])    
    
    n_local = 0 
    n_visitante = 0

    partidos_filtrados = lt.newList('ARRAY_LIST') #filtro datos
    goles_filtrados = lt.newList('ARRAY_LIST')

    for goles in lista_anotaciones:
        if goles["date"] >= consulta_fecha_i and goles["date"] <= consulta_fecha_f and (goles["home_team"] == consulta_equipo or goles["away_team"] == consulta_equipo):
            lt.addLast(goles_filtrados,goles)
    
    for partido in lista_resultados:
        if partido["date"] >= consulta_fecha_i and partido["date"] <= consulta_fecha_f and (partido["home_team"] == consulta_equipo or partido["away_team"] == consulta_equipo):
            lt.addLast(partidos_filtrados,partido)

    respuesta = lt.newList('ARRAY_LIST')

    for datos_partidos in lt.iterator(partidos_filtrados):
        datos_partidos["penalty"] = "Unknown"
        datos_partidos["own_goal"] = "Unknown"

        for datos_goals in lt.iterator(goles_filtrados):
            if all(datos_goals[llave] == datos_partidos[llave] for llave in ["date", "home_team", "away_team"]):
                datos_partidos["penalty"] = datos_goals["penalty"]
                datos_partidos["own_goal"] = datos_goals["own_goal"]

        del datos_partidos["neutral"]

        lt.addLast(respuesta,datos_partidos)
        if datos_partidos["home_team"] == consulta_equipo:
            n_local += 1
        if datos_partidos["away_team"] == consulta_equipo:
            n_visitante += 1              

    respuesta = sort(respuesta, valor_ord, criterio_date_min)

    if lt.size(respuesta) > 6:
        tamano = lt.size(respuesta)
        resultado = lt.subList(respuesta,1,3) 
        i = 2
        while i >= 0:
            valor = lt.getElement(respuesta,tamano-i)
            lt.addLast(resultado,valor)
            i = i-1
        return lt.size(respuesta),n_local,n_visitante, resultado
    else:
        return lt.size(respuesta), n_local,n_visitante, lt.subList(respuesta,1,lt.size(respuesta))

def req_4(data_structs:dict, torneo:str, fecha_i:str, fecha_f:str, valor_ord:str):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    """
    - Tabla 1 (results) : El archivo results-utf8.csv, contiene la información relevante 
        a los resultados del partido. Como se ve en Tabla 1 da fecha del encuentro, 
        los equipos involucrados, el marcador final, el lugar donde
        se llevó a cabo el evento y a que torneo FIFA perteneció la competencia
    - Tabla 3 (shootouts): El archivo shootouts-utf8.csv, contiene la información 
        sobre la definición de penales dentro del partido.
        la Tabla 3 contiene los detalles de la fecha del partido y 
        quien fue el ganador de la definición máxima por penales.""" 
     #borrar
    
    lista_resultados = lt.iterator(data_structs["results"])
    lista_penales = lt.iterator(data_structs["shootouts"])
    
    partidos_relevantes = lt.newList('ARRAY_LIST') #retornar el size
    paises_involucrados = lt.newList('ARRAY_LIST') #retornar el len
    ciudades_involucradas =lt.newList('ARRAY_LIST') #retornar el len
    partidos_penal = lt.newList('ARRAY_LIST') 
    size_partidosp = 0
    partidos_disputados = lt.newList('ARRAY_LIST') 
    
    for resultados in lista_resultados: #Se hace para retornar el size
        if resultados['date'] >= fecha_i and resultados['date'] <= fecha_f:
            if resultados["tournament"] == torneo:
               lt.addLast(partidos_relevantes,resultados)
    
    for involucrados in lt.iterator(partidos_relevantes): # Se hace para retornar el size:    
        if lt.isPresent(paises_involucrados, involucrados["country"]) == 0:
            lt.addLast(paises_involucrados, involucrados["country"])
            
        if lt.isPresent(ciudades_involucradas, involucrados["city"]) == 0:
            lt.addLast(ciudades_involucradas, involucrados["city"])
    
    for resultados in lista_penales: #Se hace para retornar el size
        if resultados['date'] >= fecha_i and resultados['date'] <= fecha_f:
               lt.addLast(partidos_penal,resultados)
               
    for partidos in lt.iterator(partidos_relevantes):
        for partidosp in lt.iterator(partidos_penal): 
            if partidosp["home_team"] == partidos['home_team'] and partidosp['away_team'] == partidos['away_team']:
                size_partidosp += 1
  
    for partidos_r in lt.iterator(partidos_relevantes):
        partidos_r["by_penal"] = "Unknown"
        for partidosp in lt.iterator(partidos_penal):
            if all(partidos_r[llave] == partidosp[llave] for llave in ["date", "home_team", "away_team"]):
                partidos_r["by_penal"] = partidosp["winner"]

        del partidos_r["neutral"]
        # vamos aca 
        lt.addLast(partidos_disputados,partidos_r)              

    partidos_disputados = sort(partidos_disputados,valor_ord, criterio_date_min_inverso)

    if lt.size(partidos_disputados) > 6:
        tamano = lt.size(partidos_disputados)
        partidos_disputados_r = lt.subList(partidos_disputados,1,3) 
        i = 2
        while i >= 0:
            valor = lt.getElement(partidos_disputados,tamano-i)
            lt.addLast(partidos_disputados_r,valor)
            i = i-1
        return lt.size(partidos_disputados),len(paises_involucrados), len(ciudades_involucradas), size_partidosp, partidos_disputados_r
    else:
        return lt.size(partidos_relevantes), len(paises_involucrados), len(ciudades_involucradas), size_partidosp, lt.subList(partidos_disputados,1,lt.size(partidos_disputados))


def req_5(data_structs:dict, jugador:str, fecha_i:str, fecha_f:str,valor_ord): 
    """
    Función que soluciona el requerimiento 4
     
    Args:
        data_structs (dict): Catálogo
        jugador (str): Jugador Consultado
        fecha_i (str): Fecha Inicial Consultada
        fecha_f (str): Fecha Final Consultada

    Returns:
        i_anotaciones (float): Cantidad de goles del jugador en rango de fechas
        i_torneos (float): Cantidad de torneos jugados del jugador en rango de fechas
        i_penales (float): Cantidad de goles por penalty del jugador en rango de fechas
        i_autogoles (float): Cantidad de autogoles del jugador en rango de fechas
        respuestas (ARRAY_LIST): 
    """    
    partidos = lt.iterator(data_structs["results"])
    anotaciones = lt.iterator(data_structs["goalscorers"])
    
    anotaciones_f_jugador = lt.newList('ARRAY_LIST') #Lista Filtrada de Anotaciones por Jugador
    i_anotaciones = 0 #Contador de Anotaciones
    for anotacion in anotaciones:
        if anotacion["scorer"].lower() == jugador and fecha_i <= anotacion["date"] and anotacion["date"] <= fecha_f:
            lt.addLast(anotaciones_f_jugador, anotacion)
            i_anotaciones +=1
     
    partidos_f_fecha = lt.newList('ARRAY_LIST') #Lista Filtrada de Anotaciones por Rango de Fechas
    for partido in partidos:
        if fecha_i <= partido["date"] and partido["date"] <= fecha_f:
            lt.addLast(partidos_f_fecha, partido)
       
    torneos_anotados = lt.newList('ARRAY_LIST') #Estrcutura de Datos que Elimina Elementos Repetidos
    i_penales = 0 #Contador de Penaltys
    i_autogoles = 0 #Contador de Autogoles
    for anotacion_filtrada in lt.iterator(anotaciones_f_jugador):
        for partido_filtrado in lt.iterator(partidos_f_fecha):
            if all(anotacion_filtrada[llave] == partido_filtrado[llave] for llave in ["date", "home_team", "away_team"]):
        
                anotacion_filtrada["tournament"] = partido_filtrado["tournament"]
                anotacion_filtrada["home_score"] = partido_filtrado["home_score"]
                anotacion_filtrada["away_score"] = partido_filtrado["away_score"]
                
                if anotacion_filtrada["penalty"] == "True":
                    i_penales += 1
                if anotacion_filtrada["own_goal"] == "True":
                    i_autogoles += 1
                if lt.isPresent(torneos_anotados, anotacion_filtrada["tournament"]) == 0:
                    lt.addLast(torneos_anotados, anotacion_filtrada["tournament"])
                
    i_torneos = lt.size(torneos_anotados)
    
    ordenados = sort(anotaciones_f_jugador,valor_ord, criterio_date_min)
    
    respuesta = primeros_ultimos_3(ordenados)
              
    return i_anotaciones, i_torneos, i_penales, i_autogoles, respuesta


def req_6(data_structs, num_equipos, torneo, fecha_i, fecha_f,valor_ord):
    """
    Función que soluciona el requerimiento 6
    """
    
    Partidos =  sort(data_structs["results"],valor_ord, criterio_date_min)
    indice_i_p = busq_bin_izq(Partidos, fecha_i)
    indice_f_p = busq_bin_der(Partidos, fecha_f)
    
    Anotaciones = sort(data_structs["goalscorers"],valor_ord, criterio_date_min)
    indice_i_a = busq_bin_izq(Anotaciones, fecha_i)
    indice_f_a = busq_bin_der(Anotaciones, fecha_f)
    
    paises = lt.newList('ARRAY_LIST')
    ciudades = []
    
    partidos_f_fecha_torneo = lt.newList('ARRAY_LIST') #Lista Filtrada de Partidos por Torneo y Rango de Fechas
    for i in range(indice_i_p, indice_f_p + 1): 
        partido = lt.getElement(Partidos, i)
        if partido["tournament"].lower() == torneo:
            lt.addLast(partidos_f_fecha_torneo, partido)
            if lt.isPresent(paises, partido["country"]) == 0:
                lt.addLast(paises, partido["country"])
            ciudades.append(partido["city"])
    ciudades_unicas = set(ciudades)
    
    anotaciones_f_fecha = lt.newList('ARRAY_LIST')
    for i in range(indice_i_a, indice_f_a + 1):
        anotacion = lt.getElement(Anotaciones, i)
        lt.addLast(anotaciones_f_fecha, anotacion)
  
    index_anotacion_filtrada = 1
    while index_anotacion_filtrada < lt.size(anotaciones_f_fecha) + 1:
        anotacion_filtrada = lt.getElement(anotaciones_f_fecha, index_anotacion_filtrada)
        coincidencia = False

        for partido_filtrado in lt.iterator(partidos_f_fecha_torneo):
            if all(anotacion_filtrada[llave] == partido_filtrado[llave] for llave in ["date", "home_team", "away_team"]):
                anotacion_filtrada["tournament"] = partido_filtrado["tournament"]
                coincidencia = True

        if not coincidencia:
            lt.deleteElement(anotaciones_f_fecha, index_anotacion_filtrada)
        else:
            index_anotacion_filtrada += 1

    equipos = lt.newList('ARRAY_LIST')   
    for partido_filtrado in lt.iterator(partidos_f_fecha_torneo):
        local = partido_filtrado["home_team"]
        visitante = partido_filtrado["away_team"]
        marcador_local = int(partido_filtrado["home_score"])
        marcador_visitante = int(partido_filtrado["away_score"])
        
        equipo_local = get_data(equipos, local, "Equipo") 
        if equipo_local == None:
            equipo_local = {
                            "Equipo": local,
                            "Puntos": 0, 
                            "Diferencia_goles": 0, 
                            "Partidos": 0,
                            "Penales": 0, 
                            "Autogoles": 0, 
                            "Victorias": 0, 
                            "Empates": 0, 
                            "Derrotas": 0,
                            "Goles_anotados": 0, 
                            "Goles_recibidos": 0,
                            "Jugador Destacado": {}
                           }
            
            lt.addLast(equipos, equipo_local)
            
        equipo_visitante = get_data(equipos, visitante, "Equipo")
        if equipo_visitante == None:
            equipo_visitante = {
                                "Equipo": visitante,
                                "Puntos": 0, 
                                "Diferencia_goles": 0, 
                                "Partidos": 0,
                                "Penales": 0, 
                                "Autogoles": 0, 
                                "Victorias": 0, 
                                "Empates": 0, 
                                "Derrotas": 0,
                                "Goles_anotados": 0, 
                                "Goles_recibidos": 0, 
                                "Jugador Destacado": {}
                                
                               }
            
            lt.addLast(equipos, equipo_visitante)
    
        equipo_local["Partidos"] += 1
        equipo_visitante["Partidos"] += 1
        equipo_local["Goles_anotados"] += marcador_local
        equipo_local["Goles_recibidos"] += marcador_visitante
        equipo_visitante["Goles_anotados"] += marcador_visitante
        equipo_visitante["Goles_recibidos"] += marcador_local  
        
        if marcador_local > marcador_visitante:
            equipo_local["Victorias"] += 1
            equipo_local["Puntos"] += 3
            equipo_visitante["Derrotas"] += 1
        elif marcador_local < marcador_visitante:
            equipo_visitante["Victorias"] += 1
            equipo_visitante["Puntos"] += 3
            equipo_local["Derrotas"] += 1
        else:
            equipo_local["Empates"] += 1
            equipo_local["Puntos"] += 1
            equipo_visitante["Empates"] += 1
            equipo_visitante["Puntos"] += 1

        equipo_local["Diferencia_goles"] =  equipo_local["Goles_anotados"] -  equipo_local["Goles_recibidos"]
        equipo_visitante["Diferencia_goles"] =  equipo_visitante["Goles_anotados"] -  equipo_visitante["Goles_recibidos"]   
    
    for anotacion_filtrada in lt.iterator(anotaciones_f_fecha):
        equipo_anotacion = anotacion_filtrada["team"] 
        equipo = get_data(equipos, equipo_anotacion, "Equipo")
        
        if anotacion_filtrada["penalty"] == "True":
            equipo["Penales"] += 1  
              
        if anotacion_filtrada["own_goal"] == "True":
            equipo["Autogoles"] += 1 

           
    jugadores_datos = {}
    
    for anotacion_filtrada in lt.iterator(anotaciones_f_fecha):
        team = anotacion_filtrada["team"]
        jugador = anotacion_filtrada["scorer"]
        minuto = float(anotacion_filtrada["minute"])
        
        if team not in jugadores_datos:
            jugadores_datos[team] = {}
        
        if jugador not in jugadores_datos[team]:
            jugadores_datos[team][jugador] = {
                                              "Anotaciones": 0,
                                              "Partidos Anotados": 0,
                                              "Minutos Jugados": 0
                                             }
        
        jugadores_datos[team][jugador]["Anotaciones"] += 1
        jugadores_datos[team][jugador]["Partidos Anotados"] += 1
        jugadores_datos[team][jugador]["Minutos Jugados"] += minuto
        
    for pos in range(1, lt.size(equipos) + 1):
            equipo = lt.getElement(equipos, pos)
            equipo_nombre = equipo["Equipo"]
            if equipo_nombre in jugadores_datos:
                max_goleador = max(jugadores_datos[equipo_nombre], key=lambda x: jugadores_datos[equipo_nombre][x]["Anotaciones"])
                max_goleador_datos = jugadores_datos[equipo_nombre][max_goleador]
                tiempo_promedio = max_goleador_datos["Minutos Jugados"] / max_goleador_datos["Anotaciones"]
                
                equipo["Jugador Destacado"] = {
                                              "Jugador": max_goleador, 
                                              "Anotaciones":max_goleador_datos["Anotaciones"], 
                                              "Partidos Anotados": max_goleador_datos["Partidos Anotados"],
                                              "Promedio Minutos": int(tiempo_promedio), 
                                             }
            
     
    equipos_sort = sort(equipos,valor_ord, criterio_estadisticas)
    
    mejores_equipos = lt.subList(equipos_sort,1,int(num_equipos))
    

    num_equipos = lt.size(equipos)
    num_partidos = lt.size(partidos_f_fecha_torneo)
    num_ciudades = len(ciudades_unicas)
    num_paises = lt.size(paises)
    ciudad_md = max(ciudades, key=lambda x: ciudades.count(x))
    
    resultado = primeros_ultimos_3(mejores_equipos)


    return num_equipos, num_partidos, num_paises, num_ciudades, ciudad_md, resultado

def req_7(data_structs, n_jugadores, fecha_i, fecha_f,valor_ord):
    """
    FunciÃ³n que soluciona el requerimiento 7
    """
    
    # TODO: Realizar el requerimiento 7
    todas_anotaciones = (data_structs["goalscorers"])
    todas_partidos_borrados = (data_structs["results"])
    
    index_partido_filtrada = 1
    #borra los partidos que no coinciden entre results y goalscorers
    while index_partido_filtrada < lt.size(todas_partidos_borrados) + 1:
        partido_filtrada = lt.getElement(todas_partidos_borrados, index_partido_filtrada)
        coincidencia = False

        for anotacion_filtrada in lt.iterator(todas_anotaciones):
            if all(partido_filtrada[llave] == anotacion_filtrada[llave] for llave in ["date", "home_team", "away_team"]):
                anotacion_filtrada["tournament"] = partido_filtrada["tournament"]
                coincidencia = True

        if not coincidencia:
            lt.deleteElement(todas_partidos_borrados, index_partido_filtrada)
        else:
            index_partido_filtrada += 1
    
    todas_partidos_borrados = sort(todas_partidos_borrados,valor_ord,criterio_date_min)

    anotaciones_fechas = lt.newList('ARRAY_LIST') #Lista Filtrada de Anotaciones por Rango de Fechas

    for anotacionn in lt.iterator(todas_anotaciones):
        if fecha_i <= anotacionn["date"] and anotacionn["date"] <= fecha_f:
            lt.addLast(anotaciones_fechas, anotacionn)

    anotaciones_organizadas = sort(anotaciones_fechas,valor_ord,criterio_date_min)

    nombres_partidos = lt.newList("ARRAY_LIST")

    goles = 0
    goles_penales = 0
    goles_autogoles = 0
    informacion_jugadores = lt.newList('ARRAY_LIST')
    nombres_torneos = lt.newList('ARRAY_LIST')

    for partido in lt.iterator(todas_partidos_borrados):
        fecha_partido = partido["date"]

        if fecha_i <= fecha_partido and fecha_partido <= fecha_f and partido["tournament"] != "Friendly":
            #verifica si el resultado cumple los criterios
            nombre_partido = str(partido["date"]) + str(partido["home_team"]) + str(partido["away_team"])
            if lt.isPresent(nombres_partidos, nombre_partido) == 0:
                lt.addLast(nombres_partidos,nombre_partido)
            
            if lt.isPresent(nombres_torneos, partido["tournament"]) == 0:
                lt.addLast(nombres_torneos, partido["tournament"])

            goles = goles + int(partido["home_score"]) + int(partido["away_score"])

            posizq = busq_bin_izq(anotaciones_organizadas,partido["date"])
            posder = busq_bin_der(anotaciones_organizadas,partido["date"])

            #busca los partidos jugaores que hay
            for i in range(posizq,posder+1):
                
                anotacion_encontrada = lt.getElement(anotaciones_organizadas,i)
                nombre_jugador = anotacion_encontrada["scorer"]
                if posizq > 0 and posder > 0:
                    if partido["home_team"] == anotacion_encontrada["home_team"] and partido["away_team"] == anotacion_encontrada["away_team"]:

                        equipo_jug = anotacion_encontrada["team"]

                        jugador = get_data(informacion_jugadores, nombre_jugador, "Nombre")

                        if jugador == None:
                            jugador = {
                                "Nombre": nombre_jugador,
                                "puntos_totales": 0,
                                "goles_totales": 0,
                                "goles_penalty":0,
                                "autogoles":0,
                                "tiempo_promedio":0,
                                "total_torneos":0,
                                "goles_victoria":0,
                                "goles_derrota":0,
                                "goles_empate":0,
                                "ultimo_gol": 0,
                                "fecha_gol":"1000-01-01"
                            }

                            lt.addLast(informacion_jugadores,jugador)
                        
                        lista_torneos = lt.newList('ARRAY_LIST')

                        if partido["home_team"] == equipo_jug:
                            if lt.isPresent(lista_torneos, partido["tournament"]) == 0:
                                lt.addLast(lista_torneos,partido["tournament"])
                            if partido["home_score"] > partido["away_score"]:
                                jugador["goles_victoria"]+=1

                            elif partido["home_score"] < partido["away_score"]:
                                jugador["goles_derrota"]+=1
                            else:
                                jugador["goles_empate"]+=1

                        elif partido["away_team"] == equipo_jug: 
                            if lt.isPresent(lista_torneos, partido["tournament"]) == 0:
                                lt.addLast(lista_torneos,partido["tournament"])

                            if partido["home_score"] < partido["away_score"]:
                                jugador["goles_victoria"]+=1

                            elif partido["home_score"] > partido["away_score"]:
                                jugador["goles_derrota"]+=1
                            else:
                                jugador["goles_empate"]+=1

                        if anotacion_encontrada["own_goal"] == "True":
                            jugador["autogoles"] += 1
                            jugador["puntos_totales"] -= 1
                            goles_autogoles += 1

                        if anotacion_encontrada["penalty"] == "True":
                            jugador["goles_penalty"] += 1
                            jugador["puntos_totales"] += 1
                            goles_penales += 1
                        if jugador["Nombre"] == anotacion_encontrada["scorer"]:
                            if anotacion_encontrada["date"] > jugador["fecha_gol"]:
                                jugador["fecha_gol"] = anotacion_encontrada["date"] 
                                jugador["ultimo_gol"] = anotacion_encontrada

                        jugador["total_torneos"] = lt.size(lista_torneos)
                        jugador["tiempo_promedio"] += float(anotacion_encontrada["minute"])
                        jugador["goles_totales"] = jugador["goles_victoria"] + jugador["goles_derrota"] + jugador["goles_empate"]
                        jugador["puntos_totales"] = jugador["goles_totales"] + jugador["goles_penalty"] - jugador["autogoles"]
    
    ordenada = sort(informacion_jugadores,valor_ord,criterio_anotaciones)
    top_jug = lt.subList(ordenada,1,n_jugadores)
    
    for jug in lt.iterator(informacion_jugadores):
        jug["tiempo_promedio"] = jug["tiempo_promedio"]/jug["goles_totales"]
        
        posizq_ultimo = busq_bin_izq(todas_partidos_borrados,jug["fecha_gol"])
        posder_ultimo = busq_bin_der(todas_partidos_borrados,jug["fecha_gol"])

        del jug["fecha_gol"]
        del jug["ultimo_gol"]["team"]
        del jug["ultimo_gol"]["scorer"]

        jug["ultimo_gol"]["home_score"] = "Unknown"
        jug["ultimo_gol"]["away_score"] = "Unknown"

            #busca los partidos jugaores que hay
        for i in range(posizq_ultimo,posder_ultimo+1):
            partido = lt.getElement(todas_partidos_borrados,i)
    
            if all(partido[llave] == jug["ultimo_gol"][llave] for llave in ["date","home_team", "away_team"]):
                jug["ultimo_gol"]["home_score"] = partido["home_score"]
                jug["ultimo_gol"]["away_score"] = partido["away_score"]
                break
            
    num_jugadores = lt.size(informacion_jugadores)
    num_partidos = lt.size(nombres_partidos)
    num_torneos = lt.size(nombres_torneos)
    num_goles = goles
    num_penalty = goles_penales
    num_autogoles = goles_autogoles


    if lt.size(top_jug) > 6:
        tamano = lt.size(top_jug)
        resultado = lt.subList(top_jug,1,3) 
        i = 2
        while i >= 0:
            if n_jugadores <= tamano:
                valor = lt.getElement(top_jug,n_jugadores-i)
                lt.addLast(resultado,valor)
                i = i-1
            else:
                valor = lt.getElement(tamano,tamano-i)
                lt.addLast(resultado,valor)
                i = i-1
        return num_jugadores,num_partidos,num_torneos,num_goles,num_penalty,num_autogoles, resultado
    else:
        return num_jugadores,num_partidos,num_torneos,num_goles,num_penalty,num_autogoles, lt.subList(top_jug,1,min(n_jugadores,lt.size(top_jug)))

    
def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

# 
# FUNCIONES DE COMPARACIÓN
# 


def criterio_date_min(data_1, data_2):
    """_summary_

    Args:
        data_1 (str): _description_
        data_2 (): _description_

    Returns:
        bool: _description_
    """    
    date_1 = datetime.strptime(data_1["date"], "%Y-%m-%d")
    date_2 = datetime.strptime(data_2["date"], "%Y-%m-%d")
    
    if date_1 < date_2:
        return True
    elif date_1 > date_2:
        return False
    else:
        if "minute" in data_1 and "minute" in data_2:
            minute_1 = data_1["minute"]
            minute_2 = data_2["minute"]
            
            return minute_1 <= minute_2

def criterio_date_min_inverso(data_1, data_2):
    """_summary_

    Args:
        data_1 (str): _description_
        data_2 (): _description_

    Returns:
        bool: _description_
    """    
    date_1 = datetime.strptime(data_1["date"], "%Y-%m-%d")
    date_2 = datetime.strptime(data_2["date"], "%Y-%m-%d")
    
    if date_1 > date_2:
        return True
    elif date_1 < date_2:
        return False
    else:
        if "minute" in data_1 and "minute" in data_2:
            minute_1 = data_1["minute"]
            minute_2 = data_2["minute"]
            
            return minute_1 <= minute_2

def criterio_country(data_1, data_2):
    """_summary_

    Args:
        data_1 (list): _description_
        data_2 (list): _description_

    Returns:
        bool: _description_
    """    
    return data_1["country"] >= data_2["country"]
    
def criterio_anotaciones(data_1, data_2):
    if data_1["puntos_totales"] > data_2["puntos_totales"]:
        return True
    elif data_1["puntos_totales"] < data_2["puntos_totales"]:
        return False
    else:
        if data_1["goles_totales"] > data_2["goles_totales"]:
            return True
        elif data_1["goles_totales"] < data_2["goles_totales"]:
            return False
        else: 
            if data_1["goles_penalty"] > data_2["goles_penalty"]:
                return True
            elif data_1["goles_penalty"] < data_2["goles_penalty"]:
                return False
            else:
                if data_1["autogoles"] < data_2["autogoles"]:
                    return True
                elif data_1["autogoles"] > data_2["autogoles"]:
                    return False
                else:
                    if data_1["tiempo_promedio"] < data_2["tiempo_promedio"]:
                        return True
                    elif data_1["tiempo_promedio"] > data_2["tiempo_promedio"]:
                        return False        
            
def criterio_estadisticas(data_1, data_2):
    if data_1["Puntos"] > data_2["Puntos"]:
        return True
    elif data_1["Puntos"] < data_2["Puntos"]:
        return False
    else:
        if data_1["Diferencia_goles"] > data_2["Diferencia_goles"]:
            return True
        elif data_1["Diferencia_goles"] < data_2["Diferencia_goles"]:
            return False
        else: 
            
            if data_1["Penales"] > data_2["Penales"]:
                return True
            elif data_1["Penales"] < data_2["Penales"]:
                return False
            else:
                if data_1["Partidos"] < data_2["Partidos"]:
                    return True
                elif data_1["Partidos"] > data_2["Partidos"]:
                    return False
                else:
                    if data_1["Autogoles"] < data_2["Autogoles"]:
                        return True
                    elif data_1["Autogoles"] > data_2["Autogoles"]:
                        return False
                    
            
            
        
def sort(data_structs, alg_sort, cmp):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    
    match alg_sort:
        case "1":
            alg_sort = ins.sort(data_structs, cmp)
        case "2":
            alg_sort = merg.sort(data_structs, cmp)
        case "3":
            alg_sort = quk.sort(data_structs, cmp)
        case "4":
            alg_sort = se.sort(data_structs, cmp)
        case "5":
            alg_sort = sa.sort(data_structs, cmp)
            
    return alg_sort

def sort_tiempo(data_structs, alg_sort):

    resultados = data_structs['results']

    match alg_sort:
        case "1":
            alg_sort = ins.sort(resultados, criterio_date_min)
        case "2":
            alg_sort = merg.sort(resultados, criterio_date_min)
        case "3":
            alg_sort = quk.sort(resultados, criterio_date_min)
        case "4":
            alg_sort = se.sort(resultados, criterio_date_min)
        case "5":
            alg_sort = sa.sort(resultados, criterio_date_min)
            
    return alg_sort    


# 
# ALGORITMOS DE BÚSQUEDA
# 

def busq_bin_izq(data_struct, target):
    left, right = 1, lt.size(data_struct)
    result = -1 
    
    while left <= right:
        mid = left + (right - left) // 2
        id = lt.getElement(data_struct, mid)
        
        if id["date"] == target:
            result = mid  
            right = mid - 1  
        elif id["date"] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if result == -1:
        return left

    return result


def busq_bin_der(data_struct, target:str) -> int:
    left, right = 1, lt.size(data_struct)
    result = -1 #Si no encuentra el target devuelve -1  
    while left <= right:
        mid = left + (right - left) // 2
        id = lt.getElement(data_struct, mid)
        
        if id["date"] == target:
            result = mid  
            left = mid + 1  
        elif id["date"] < target:
            left = mid + 1
        else:
            right = mid - 1
            
            
    if result == -1:
        return left

    return result

def primeros_ultimos_3(dato):
     if lt.size(dato) > 6:
        tamano = lt.size(dato)
        resultado = lt.subList(dato,1,3) 
        i = 2
        while i >= 0:
            valor = lt.getElement(dato,tamano-i)
            lt.addLast(resultado,valor)
            i = i-1
        return resultado