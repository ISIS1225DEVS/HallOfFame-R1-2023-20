"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
import time
import threading

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def new_controller(tipo_de_lista="ARRAY_LIST"):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_de_lista)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Últimos N partidos de un equipo segun su condición")
    print("3- Primeros N goles anotados por un jugador")
    print("4- Partidos que disputó un equipo durante un periodo")
    print("5- Partidos relacionados con un torneo durante un periodo")
    print("6- Anotaciones de un jugador durante un periodo")
    print("7- Clasificar los N mejores equipos de un torneo en un periodo")
    print("8- Clasificar los N mejores anotadores en partidos oficiales en un periodo")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("10- Tiempos de carga")
    print("0- Salir")


def load_data(control,prefijo, alg):
    """
    Carga los datos
    Fecha del partido.Equipo local.Equipo visitante.Marcador final (goles del local – goles del visitante).Liga a la que está asociado el encuentro.País y ciudad en el que se desarrolló el encuentro.
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control,prefijo, alg)
    return data

def print_data(tupla):
    """
        Función que imprime un dato dado su ID
    """
    print(f"Se cargaron {tupla[1]} partidos en results")
    print(f"Se cargaron {tupla[2]} partidos en goalscorers")
    print(f"Se cargaron {tupla[3]} partidos en shootouts")
    pass

def sublist (list):
    primeros=None
    ultimos=None
    if lt.size(list)>=6:
        primeros= lt.subList(list,1,3)
        ultimos = lt.subList(list,(lt.size(list))-2,3)
    else:
        primeros=list
    return primeros,ultimos 

def tablas_results (list):
    headers_results=["date","home_team","away_team","home_score","away_score","tournament","city","country"]
    primeros,ultimos = list
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        total= []
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"],linea["away_team"],linea["home_score"],linea["away_score"],linea["tournament"],linea["city"],linea["country"]]
            total.append(lista1)
        for linea in ultimos:
            lista2=[linea["date"], linea["home_team"],linea["away_team"],linea["home_score"],linea["away_score"],linea["tournament"],linea["city"],linea["country"]]
            total.append(lista2)
    return (tabulate(total, headers=headers_results))

def tablas_shootouts (list):
    headers_results=["date","home_team","away_team","winner"]
    primeros,ultimos = list
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        total= []
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"],linea["away_team"],linea["winner"]]
            total.append(lista1)
        for linea in ultimos:
            lista2=[linea["date"], linea["home_team"],linea["away_team"],linea["winner"]]
            total.append(lista2)
    return (tabulate(total, headers=headers_results))
            
def tablas_goalscorers (list):
    headers_results=["date","home_team","away_team","team","scorer","minute","own_goal","penalty"]
    primeros,ultimos = list
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        total= []
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"],linea["away_team"],linea["team"],linea["scorer"],linea["minute"],linea["own_goal"],linea["penalty"]]
            total.append(lista1)
        for linea in ultimos:
            lista2=[linea["date"], linea["home_team"],linea["away_team"],linea["team"],linea["scorer"],linea["minute"],linea["own_goal"],linea["penalty"]]
            total.append(lista2)
    return (tabulate(total, headers=headers_results))

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed



def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def print_req_1(control, n, equipo, condicion):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    res = controller.req_1(control, equipo, condicion)
    cantidad = lt.size(res)
    if n < lt.size(res):
        res_corta = lt.subList(res, 1, n)
    else:
        res_corta = res
    lista = sublist(res_corta)
    primeros = lista[0]
    ultimos = lista[1]
    headers_results = ["date", "home_team", "away_team", "country", "city", "home_score", "away_score"]
    total = []
    if primeros != None:
        primeros = primeros["elements"]
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"],linea["away_team"],linea["country"],linea["city"],linea["home_score"], linea["away_score"]]
            total.append(lista1)
    if ultimos != None:
        ultimos = ultimos["elements"]
        for linea in ultimos:
           lista2=[linea["date"], linea["home_team"],linea["away_team"],linea["country"],linea["city"],linea["home_score"], linea["away_score"]]
           total.append(lista2)
    print(f"Total matches found: {cantidad}")
    print(f"Selecting {n} matches...")
    print()
    if cantidad < 6:
        print("The team results has less than 6 records...")
    elif cantidad > 6:
        print("The team results has more than 6 records...")
    else:
        print("The team results has 6 records...")
    return (tabulate(total, headers=headers_results))

    


def print_req_2(control,jugador,ng):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2

    headers_results = ["date","home_team","away_team","team","scorer","minute","own_goal","penalty"]

    resulto2 = controller.req_2(control,jugador,ng)
    rfinal = []
    nelem = int(lt.size(resulto2))

    print("Total scorers found: " + str(nelem))
    print("selecting " + str(nelem) + " scorers. . .")

    conti = 0

    if ng <= 6 or nelem <= 6:
        for f in lt.iterator(resulto2):
            lct = [f["date"],f["home_team"],f["away_team"],f["team"],f["scorer"],f["minute"],f["own_goal"],f["penalty"]]
            rfinal.append(lct)
        if nelem < 6:
            print("Goal scorers has less than 6 records")
        else: 
            print("Goal scorers has 6 records")
    elif nelem > 6:
        for f in lt.iterator(resulto2):
            if conti<=3 or conti > nelem-3:
                lct = [f["date"],f["home_team"],f["away_team"],f["team"],f["scorer"],f["minute"],f["own_goal"],f["penalty"]]
                rfinal.append(lct)
            conti+=1
        print("Goal scorers more than 6 records")
    return (tabulate(rfinal,headers=headers_results))




def print_req_3(control, equipo, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    headers_results=["date","home_score", "away_score", "home_team", "away_team","country","city","tournament","penalty", "own_goal"]
    primeros,ultimos = sublist(controller.req_3(control, equipo, fecha_inicial, fecha_final))
    total= []
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        for linea in primeros:
            if "penalty" not in linea:
                linea["penalty"] = "unkown"
            if "own_goal" not in linea:
                linea["own_goal"] = "unkown"
            lista1=[linea["date"], linea["home_score"], linea["away_score"], linea["home_team"],linea["away_team"],linea["country"],linea["city"],linea["tournament"],linea["penalty"],linea["own_goal"]]
            total.append(lista1)
        for linea in ultimos:
            if "penalty" not in linea:
                linea["penalty"] = "unkown"
            if "own_goal" not in linea:
                linea["own_goal"] = "unkown"
            lista2=[linea["date"], linea["home_score"], linea["away_score"], linea["home_team"],linea["away_team"],linea["country"],linea["city"],linea["tournament"],linea["penalty"],linea["own_goal"]]
            total.append(lista2)
    elif primeros != None:
        primeros = primeros['elements']
        for linea in primeros:
            if "penalty" not in linea:
                linea["penalty"] = "unkown"
            if "own_goal" not in linea:
                linea["own_goal"] = "unkown"
            lista1=[linea["date"], linea["home_score"], linea["away_score"], linea["home_team"],linea["away_team"],linea["country"],linea["city"],linea["tournament"],linea["penalty"],linea["own_goal"]]
            total.append(lista1)
    todos = controller.req_3(control, equipo, fecha_inicial, fecha_final)
    home_games = 0
    away_games = 0
    for game in lt.iterator(todos):
        if game["home_team"] == equipo:
            home_games += 1
        if game["away_team"] == equipo:
            away_games += 1
    print(f"{equipo} Total games: {lt.size(todos)}")
    print(f"{equipo} home games: {home_games}")
    print(f"{equipo} away games: {away_games}")
    print()
    if lt.size(todos) < 6:
        print("The team results has less than 6 records...")
    elif lt.size(todos) > 6:
        print("The team results has more than 6 records...")
    else:
        print("The team results has 6 records...")
    return (tabulate(total, headers=headers_results))


def print_req_4(control, torneo, f1, f2):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    resulto1 = controller.req_4(control, torneo, f1, f2)
    encabe = ["date", "tournament", "country", "city", "home_team", "away_team","home_score", "away_score", "winner"]
    final = []
    Totp = 0
    Totc = 0 
    Tots = 0
    ult = int(lt.size(resulto1))
    equipos = []
    ciudades = []
    ganadores = []
    conte = 0

    #conseguir el numero total de equipos, paises, ciudades y shootouts
    for j in lt.iterator(resulto1):
        
        conte += 1

        if j["away_team"] not in equipos or j["home_team"] not in equipos:
            equipos.append(j["away_team"])
            Totp += 1

        
        if j["city"] not in ciudades:
            ciudades.append(j["city"])
            Totc += 1

        if str(j["winner"]) != "Unknow" and j["winner"] not in ganadores:
            ganadores.append(j["winner"])
            Tots += 1
        if ult > 6 and conte <= 3 or conte > ult-3:
            lst1 = [j["date"],j["tournament"],j["country"],j["city"],j["home_team"],j["away_team"],j["home_score"],j["away_score"],j["winner"]]
            final.append(lst1)
        elif ult < 6:
            lst1 = [j["date"],j["tournament"],j["country"],j["city"],j["home_team"],j["away_team"],j["home_score"],j["away_score"],j["winner"]]
            final.append(lst1)
        
    #imprimir los resultados   
    print(str(torneo)+" Total matches " + str(lt.size(resulto1)))
    print(str(torneo)+" Total countries " + str(Totp))
    print(str(torneo)+" Total cities " + str(Totc))
    print(str(torneo)+" Total shootouts " + str(Tots))
    print()
    
    if ult >= 6:
        print("The tournament results has 6 or more records")
           
    elif ult < 6:
        print("The tournament results has less than 6 records")


    return (tabulate(final,headers=encabe))



def print_req_5(control, nombre_jugador, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    headers_results = ["date", "minute", "home_team", "away_team", "team", "home_score", "away_score", "tournament","penalty", "own_goal"]
    tabla=lt.des_todo(controller.req_5(control, nombre_jugador, fecha_inicial, fecha_final))
    torneos = controller.req_5(control, nombre_jugador, fecha_inicial, fecha_final)[1]
    goles = controller.req_5(control, nombre_jugador, fecha_inicial, fecha_final)[2]
    penales = controller.req_5(control, nombre_jugador, fecha_inicial, fecha_final)[3]
    autogoles = controller.req_5(control, nombre_jugador, fecha_inicial, fecha_final)[4]
    tabla_filtrada=lt.sublistn(tabla)
    
    return (tabulate(tabla_filtrada, headers=headers_results), torneos, goles, penales, autogoles)


def print_req_6(control,eqp,trn,f1,f2):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    tit = ["team","total_points","goal_diference","penalty_points","matches",
               "own_goal_points","wins","losses","draws","goals_for","goals_againts","best_scorer"]
    tito = ["scorer","goals","Matches","avg_time [min]"]

    elreturn = controller.req_6(control,eqp,trn,f1,f2)
    data = elreturn["data"]

    
    print(trn + " Total teams: " + str(elreturn["t_teams"]))
    print(trn + " Total matches: " + str(elreturn["t_matches"]))
    print(trn + " Total countries: " + str(elreturn["t_countries"]))
    print(trn + " Total cities: " + str(elreturn["t_cities"]))
    print(trn + " City with more matches: " + str(elreturn["b_city"]))
    
    lf = []

    conte = 0
    
    for d in lt.iterator(data):
            
        r = d["better_player"]

        if int(eqp) <= 6 or lt.size(data) <= 6:

            if r != "Unknown":
                r = d["better_player"]
                list0 = [tito,[r["scorer"],r["goals"],r["matches"],r["avg_time"]]]
                
            else:
                list0 = [tito,[0,0,0,0]]
        
            
            
            
            listo = [d["team"],d["total_points"],d["goal_diference"],d["penalty_points"]
                     , d["matches"],d["own_goal_points"],d["wins"],d["draws"],d["losses"],
                     d["goals_for"],d["goals_againts"],tabulate(list0,headers="firstrow")]
            lf.append(listo)

        elif conte < 3 or conte >= lt.size(data)-3:
            
            if r != "Unknown":
                r = d["better_player"]
                list0 = [tito,[r["scorer"],r["goals"],r["matches"],r["avg_time"]]]
                
            else:
                list0 = [tito,[0,0,0,0]]
        

            listo = [d["team"],d["total_points"],d["goal_diference"],d["penalty_points"]
                     , d["matches"],d["own_goal_points"],d["wins"],d["draws"],d["losses"],
                     d["goals_for"],d["goals_againts"],tabulate(list0,headers="firstrow")]
            lf.append(listo)
        conte += 1

    return tabulate(lf,headers=tit)



def print_req_7(control, num_jugadores, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    headers_tabla_grande=["scorer","total_points","total_goals", "penalty_goals", "own_goals", "avg_time [min]", "total_tournaments", "scored_in_wins", "scored_in_losses", "scored_in_draws","last goal"]
    headers_tabla_chiquita=["date","tournamet","home_team","away_team","home_score","away_score","minute","penalty","own_goal"]
    posicion_de_respuesta=controller.req_7(control, num_jugadores, fecha_inicial, fecha_final)
    respuesta = 0
    tabla = []
    if lt.size(posicion_de_respuesta[0]) >=6:
        respuesta = sublist(posicion_de_respuesta[0])
        primeros,ultimos = respuesta
        for i in respuesta:
            for j in i["elements"]:
                posicion=[headers_tabla_chiquita,j["elements"][10]["elements"]]
                j["elements"][10] = tabulate(posicion, headers="firstrow")
        for k in primeros["elements"]:
            tabla.append(k["elements"])
        for k in ultimos["elements"]:
            tabla.append(k["elements"])
        
    else:
        respuesta = posicion_de_respuesta[0]
        for j in respuesta["elements"]:
                posicion=[headers_tabla_chiquita,j["elements"][10]["elements"]]
                j["elements"][10] = tabulate(posicion, headers="firstrow")
                tabla.append(j["elements"])
    
    
    return (tabulate(tabla,headers=headers_tabla_grande, maxheadercolwidths=20),posicion_de_respuesta[1],posicion_de_respuesta[2],posicion_de_respuesta[3],posicion_de_respuesta[4],posicion_de_respuesta[5],posicion_de_respuesta[6])




def print_req_8(control, equipo1, equipo2, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    info = controller.req_8_primera_parte(control, equipo1, fecha_inicial, fecha_final)
    print()
    print(f"---------- {equipo1} Statistics ----------")
    print(f"           Years: {info[0]}")
    print(f"           Total matches: {info[1]+info[2]}")
    print(f"           Total home matches: {info[1]}")
    print(f"           Total away matches: {info[2]}")
    print(f"           Oldest match date: {info[3]}")
    newest_headers = ["date","home_team", "away_team","home_score", "away_score", "country","city","tournament"]
    newest = [[info[4]["date"], info[4]["home_team"], info[4]["away_team"], info[4]["home_score"], info[4]["away_score"], info[4]["country"], info[4]["city"], info[4]["tournament"]]]
    print(f"           +++Newest match data+++")
    print()
    print(tabulate(newest, newest_headers))
    print()
    print(f"---------- yearly statistics ----------")
    print()

    top_scorer_headers = ["scorer", "goals", "matches", "avg_time [min]"]
    primeros_, ultimos_ = sublist(info[6])
    if primeros_ != None and ultimos_ != None:
        primeros_ = primeros_['elements']
        ultimos_ = ultimos_['elements']
    elif primeros_ != None:
        primeros_ = primeros_['elements']

    i = 0
    yearly_headers = ["year", "matches", "total_points", "goal_difference", "penalties", "own_goals", "wins", "draws", "losses", "goals_for", "goals_against", "top_scorer"]
    yearly = []
    primeros,ultimos = sublist(info[5])
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        for linea in primeros:
            scorer=[[primeros_[i]["scorer"], primeros_[i]["goals"], primeros_[i]["matches"], primeros_[i]["avg_time"]]]
            tabla_scorer = (tabulate(scorer, headers=top_scorer_headers))
            lista1=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista1)
            i += 1
        i = 0
        for linea in ultimos:
            scorer=[[ultimos_[i]["scorer"], ultimos_[i]["goals"], ultimos_[i]["matches"], ultimos_[i]["avg_time"]]]
            tabla_scorer = tabulate(scorer, headers=top_scorer_headers)
            lista2=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista2)
            i += 1
        i = 0
    elif primeros != None:
        primeros = primeros['elements']
        for linea in primeros:
            scorer=[[primeros_[i]["scorer"], primeros_[i]["goals"], primeros_[i]["matches"], primeros_[i]["avg_time"]]]
            tabla_scorer = tabulate(scorer, headers=top_scorer_headers)
            lista1=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista1)
            i += 1
    tabla_yearly = tabulate(yearly, headers=yearly_headers)
    print(tabla_yearly)

    info = controller.req_8_primera_parte(control, equipo2, fecha_inicial, fecha_final)
    print()
    print(f"---------- {equipo2} Statistics ----------")
    print(f"           Years: {info[0]}")
    print(f"           Total matches: {info[1]+info[2]}")
    print(f"           Total home matches: {info[1]}")
    print(f"           Total away matches: {info[2]}")
    print(f"           Oldest match date: {info[3]}")
    newest_headers = ["date","home_team", "away_team","home_score", "away_score", "country","city","tournament"]
    newest = [[info[4]["date"], info[4]["home_team"], info[4]["away_team"], info[4]["home_score"], info[4]["away_score"], info[4]["country"], info[4]["city"], info[4]["tournament"]]]
    print(f"           +++Newest match data+++")
    print()
    print(tabulate(newest, newest_headers))
    print()
    print(f"---------- yearly statistics ----------")
    print()

    top_scorer_headers = ["scorer", "goals", "matches", "avg_time [min]"]
    primeros_, ultimos_ = sublist(info[6])
    if primeros_ != None and ultimos_ != None:
        primeros_ = primeros_['elements']
        ultimos_ = ultimos_['elements']
    elif primeros_ != None:
        primeros_ = primeros_['elements']

    i = 0
    yearly_headers = ["year", "matches", "total_points", "goal_difference", "penalties", "own_goals", "wins", "draws", "losses", "goals_for", "goals_against", "top_scorer"]
    yearly = []
    primeros,ultimos = sublist(info[5])
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        for linea in primeros:
            scorer=[[primeros_[i]["scorer"], primeros_[i]["goals"], primeros_[i]["matches"], primeros_[i]["avg_time"]]]
            tabla_scorer = (tabulate(scorer, headers=top_scorer_headers))
            lista1=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista1)
            i += 1
        i = 0
        for linea in ultimos:
            scorer=[[ultimos_[i]["scorer"], ultimos_[i]["goals"], ultimos_[i]["matches"], ultimos_[i]["avg_time"]]]
            tabla_scorer = tabulate(scorer, headers=top_scorer_headers)
            lista2=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista2)
            i += 1
        i = 0
    elif primeros != None:
        primeros = primeros['elements']
        for linea in primeros:
            scorer=[[primeros_[i]["scorer"], primeros_[i]["goals"], primeros_[i]["matches"], primeros_[i]["avg_time"]]]
            tabla_scorer = tabulate(scorer, headers=top_scorer_headers)
            lista1=[linea["year"], linea["matches"], linea["total_points"], linea["goal_difference"], linea["penalties"], linea["own_goals"], linea["wins"], linea["draws"], linea["losses"], linea["goals_for"], linea["goals_against"], tabla_scorer]
            yearly.append(lista1)
            i += 1
    tabla_yearly = tabulate(yearly, headers=yearly_headers)
    print(tabla_yearly)

def print_req_8_segunda_parte(control, equipo1, equipo2, fecha_inicial, fecha_final):
    info = controller.req_8_segunda_parte(control, equipo1, equipo2, fecha_inicial, fecha_final)
    print()
    print(f"---------- {equipo1} vs {equipo2} Statistics ----------")
    print(f"           Total matches: {info[0]}")
    print(f"           Total wins for {equipo1}: {info[1]}")
    print(f"           Total losses for {equipo1}: {info[2]}")
    print(f"           Total wins for {equipo2}: {info[3]}")
    print(f"           Total losses for {equipo2}: {info[4]}")
    print(f"           Total draws: {info[5]}")
    print()
    print(f"           +++ Newest match data +++")
    print()

    primera_tabla_headers = ["date", "home_team", "away_team", "home_score", "away_score", "country", "city", "tournament"]
    primera_tabla = [[info[6]["date"], info[6]["home_team"], info[6]["away_team"], info[6]["home_score"], info[6]["away_score"], info[6]["country"], info[6]["city"], info[6]["tournament"]]]
    print(tabulate(primera_tabla, headers=primera_tabla_headers))
    print()
    print(f"           +++ Match scorers +++")
    print()
    if lt.size(info[7]) < 6:
        print("Goal scorers results has less than 6 records...")
    elif lt.size(info[7]) > 6:
        print("Goal scorers results has more than 6 records...")
    else:
        print("The team results has 6 records...")

    primeros, ultimos = sublist(info[7])
    segunda_tabla_headers = ["date", "home_team", "away_team", "team", "scorer", "minute", "own_goal", "penalty"]
    segunda_tabla = []
    if primeros != None and ultimos != None:
        primeros = primeros['elements']
        ultimos = ultimos['elements']
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"], linea["away_team"], linea["team"], linea["scorer"], linea["minute"], linea["own_goal"], linea["penalty"]]
            segunda_tabla.append(lista1)
        for linea in ultimos:
            lista2=[linea["date"], linea["home_team"], linea["away_team"], linea["team"], linea["scorer"], linea["minute"], linea["own_goal"], linea["penalty"]]
            segunda_tabla.append(lista2)
    elif primeros != None and lt.size(primeros) > 0:
        primeros = primeros['elements']
        for linea in primeros:
            lista1=[linea["date"], linea["home_team"], linea["away_team"], linea["team"], linea["scorer"], linea["minute"], linea["own_goal"], linea["penalty"]]
            segunda_tabla.append(lista1)
    else:
        lista = [info[6]["date"], info[6]["home_team"], info[6]["away_team"], "Unkown", "Unkown", "Unkown", "Unkown", "Unkown"]
        segunda_tabla.append(lista)

    print(tabulate(segunda_tabla, headers=segunda_tabla_headers))
    

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Seleccione qué porcentaje de datos desea cargar...")
            print("1. 5%")
            print("2. 10%")
            print("3. 20%")
            print("4. 30%")
            print("5. 50%")
            print("6. 80%")
            print("7. Large")
            print("8. Small")
            prefijo="nada xd"
            porcentaje=int(input("Seleccione una opción para continuar: "))
            if porcentaje==1:
                prefijo="5pct"
            elif porcentaje==2:
                prefijo="10pct"
            elif porcentaje==3:
                prefijo="20pct"
            elif porcentaje==4:
                prefijo="30pct"
            elif porcentaje==5:
                prefijo="50pct"
            elif porcentaje==6:
                prefijo="80pct"
            elif porcentaje==7:
                prefijo="large"
            elif porcentaje==8:
                prefijo="small"
           
            alg = "Shell"
            print("Cargando información de los archivos ....\n")

            data = load_data(control, prefijo, alg)
            print_data(data)
            #print(sublist(data[0]["results"]))
            print(tablas_results(sublist(data[0]["results"])))
            print()
            print()
            print(tablas_shootouts(sublist(data[0]["shootouts"])))
            print()
            print()
            print(tablas_goalscorers(sublist(data[0]["goalscorers"])))
            
        elif int(inputs) == 2:
            print("========= Req No. 1 Inputs =========")
            n = int(input("Number of matches: "))
            equipo = input("Team name: ")
            condicion = input("Team condition: ")
            print()
            print("========= Req No. 1 Results =========")
            start_time = getTime()
            print(print_req_1(control, n, equipo, condicion))
            end_time = getTime()
            delta_time = deltaTime(start_time, end_time)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")

        elif int(inputs) == 3:
            print("========= Req No. 2 Inputs =========")
            ng = int(input("Number of scores: "))
            jugador = input("Scorer name: ")
            print()
            print("========= Req No. 2 Results =========")
            tiempo_i = getTime()
            print(print_req_2(control,jugador,ng))
            tiempo_f = getTime()
            delta_time = deltaTime(tiempo_i, tiempo_f)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")

            

        elif int(inputs) == 4:
            print("========= Req No. 3 Inputs =========")
            equipo = input("Team name: ")
            fecha_inicial = input("Start date: ")
            fecha_final = input("End date: ")
            print()
            print("========= Req No. 3 Results =========")
            start_time = getTime()
            print(print_req_3(control, equipo, fecha_inicial, fecha_final))
            end_time = getTime()
            delta_time = deltaTime(start_time, end_time)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")


        elif int(inputs) == 5:
            print("========= Req No. 4 Inputs =========")
            torneo = input("Tournament name: ")
            f1 = input("Start date In YYYY-mm-dd: ")
            f2 = input("End date In YYYY-mm-dd: ")
            print()
            print("========= Req No. 4 Results =========")
            tiempo_i = getTime()
            print(print_req_4(control,torneo,f1,f2))
            tiempo_f = getTime()
            delta_time = deltaTime(tiempo_i, tiempo_f)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")


        elif int(inputs) == 6:  
            nombre_jugador = input("Seleccione el nombre del jugador: ")
            fecha_inicial = input("Seleccione la fecha inicial: ")
            fecha_final = input("Seleccione la fecha final: ")
            print("============Req No. 5 Inputs==========")
            print(f"Player name : {nombre_jugador}")
            print(f"Player name : {fecha_inicial}")
            print(f"Player name : {fecha_final}")
            print("============Req No. 5 Results==========")
            start_time= getTime()
            respuesta_final=print_req_5(control, nombre_jugador, fecha_inicial, fecha_final)
            end_time= getTime()
            delta_time= deltaTime(start_time,end_time)
            print(f"{nombre_jugador} total goals: {respuesta_final[2]}")
            print (f"{nombre_jugador} total tournaments: {respuesta_final[1]}")
            print (f"{nombre_jugador} total penalties: {respuesta_final[3]}")
            print (f"{nombre_jugador} total own goals: {respuesta_final[4]}")
            print(respuesta_final[0])
            result = f"{delta_time:.3f}"
            print(f"la función se demora {result} ms")

        elif int(inputs) == 7:
            print("========= Req No. 6 Inputs =========")
            trn = input("Tournament name: ")
            eqp = input("Top N of teams: ")
            
            f1 = input("Start date In YYYY-mm-dd: ")
            f2 = input("End date In YYYY-mm-dd: ")
            print()
            print("========= Req No. 6 Results =========")
            tiempo_i = getTime()
            print(print_req_6(control,eqp,trn,f1,f2))
            tiempo_f = getTime()
            delta_time = deltaTime(tiempo_i, tiempo_f)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")

        elif int(inputs) == 8:
            print("============Req No. 7 Inputs==========")
            num_jugadores = input("Seleccione el número de jugadores que desea: ")
            fecha_inicial = input("Seleccione la fecha inicial: ")
            fecha_final = input("Seleccione la fecha final: ")
            print(f"TOP {num_jugadores} scorer ranking")
            print(f"start date: {fecha_inicial}")
            print(f"end date: {fecha_final}")
            
            print("============Req No. 7 Results==========")
            start_time= getTime()
            respuesta_final = print_req_7(control, num_jugadores, fecha_inicial, fecha_final)
            end_time= getTime()
            delta_time= deltaTime(start_time,end_time)
            print(f"Official tournaments total players: {respuesta_final[1]}")
            print(f"Official tournaments total matches: {respuesta_final[2]}")
            print(f"Official tournaments total goals: {respuesta_final[3]}")
            print(f"Official tournaments total penalties: {respuesta_final[4]}")
            print(f"Official tournaments total own goals: {respuesta_final[5]}")
            print(f"Official tournaments total tournaments: {respuesta_final[6]}")
            print(respuesta_final[0])
            result = f"{delta_time:.3f}"
            print(f"la función se demora {result} ms")

        elif int(inputs) == 9:
            print("========= Req No. 8 Inputs (BONUS) =========")
            equipo1 = input("Team 1 name: ")
            equipo2 = input("Team 2 name: ")
            fecha_inicial = input("Start date: ")
            fecha_final = input("End date: ")
            print()
            print("========= Req No. 8(bono) Results (BONUS) =========")
            start_time = getTime()
            print_req_8(control, equipo1, equipo2, fecha_inicial, fecha_final)
            print()
            print_req_8_segunda_parte(control, equipo1, equipo2, fecha_inicial, fecha_final)
            end_time = getTime()
            delta_time = deltaTime(start_time, end_time)
            result = f"{delta_time:.3f}"
            print()
            print(f"La función se demora {result} ms.")

        elif int(inputs) == 10:
            tipo_de_lista = input("Tipo de lista donde quiere cargar el catálogo: ")
            prefijo = input("Archivo que deseas leer (small, 5pct, 10pct, 20pct, 30pct, 50pct, 80pct, large): ")
            alg = input("Tipo de algoritmo de ordenamiento que deseas usar (Selection, Insertion, Shell): ")
            control = new_controller(tipo_de_lista)
            start_time = getTime()
            data = load_data(control, prefijo, alg)
            end_time = getTime()
            delta_time = deltaTime(start_time, end_time)
            result = f"{delta_time:.3f}"
            print(f"Para {prefijo} con {alg} Sort y {tipo_de_lista}, delta tiempo: {str(result)}[ms]")

       

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
