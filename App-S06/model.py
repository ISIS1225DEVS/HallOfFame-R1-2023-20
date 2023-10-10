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
import random
from datetime import datetime
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


def new_data_structs(tipo_de_lista):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"results": lt.newList(tipo_de_lista),
                    "goalscorers": lt.newList(tipo_de_lista),
                    "shootouts": lt.newList(tipo_de_lista)}
    
    return data_structs



# Funciones para agregar informacion al modelo

def add_data_resutls(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["results"],data)
    return lt.size(data_structs["results"])


# Funciones para creacion de datos

def add_data_goalscorers(data_structs, data):
    """
    Crea una nueva estructura para modelar los datos
    """
    lt.addLast(data_structs["goalscorers"],data)
    return lt.size(data_structs["goalscorers"])

def add_data_shootouts(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["shootouts"],data)
    return lt.size(data_structs["shootouts"])

# Funciones de sorteo
def organizar_lista(list,cmp, alg=sa):
    if alg == "Selection":
        alg = se
    elif alg == "Insertion":
        alg = ins
    elif alg == "Shell":
        alg = sa
    else:
        alg = sa
    return alg.sort(list,cmp)

# Cmp


def cmp_fecha(dato1,dato2):
    
    if dato1["date"] > dato2["date"]:
        return True
    elif dato1["date"] < dato2["date"]:
        return False 
    else:
        if dato1["home_team"] > dato2["home_team"]:
           return False
        else: 
            return True
        
def cmp_solo_fecha(dato1, dato2):
    if dato1["date"] >= dato2["date"]:
        return True
    else:
        return False 
    
def cmp_partidos_by_fecha_y_pais (resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelva falso (False).
    Args:
    Resultado1: información del primer registro de resultados FIFA que incluye
    “date” y el “country”
    impuesto2: información del segundo registro de resultados FIFA que incluye
    “date” y el “country”
    """
    if resultado1["date"] < resultado2["date"]:
        return True
    elif resultado1["date"] == resultado2["date"]:
        if resultado1["country"] <= resultado2["country"]:
            return True
        else:
            return False
    else:
        return False

def cmp_fecha_req2(dato1,dato2):
    #organiza de tal forma que los primeros resultados sean los partidos viejos para facilitar el req 2
    if dato1["date"] < dato2["date"]:
        return True
    else:
        return False 
    
def cmp_goles_req6(dato1,dato2):
    #organiza de tal frma que los primeros resultados sean los partidos viejos para facilitar el req 2
    if dato1["goals"] >= dato2["goals"]:
        return True
    else:
        return False

def cmp_puntos_req6(dato1,dato2):
    #organiza de tal forma que los primeros resultados sean los partidos viejos para facilitar el req 2
    if dato1["total_points"] > dato2["total_points"]:
    
         return True
    elif dato1["total_points"] > dato2["total_points"]:
        if dato1["goal_diference"] > dato2["goal_diference"]:
            return True
        elif dato1["goal_diference"] == dato2["goal_diference"]:
            if dato1["penalty_points"] > dato2["penalty_points"]:
                return True
            elif dato1["penalty_points"] == dato2["penalty_points"]:
                if dato1["matches"] < dato2["matches"]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
        
    
def sortear_carga(data_structs, alg):
    
    data_structs["results"] = organizar_lista(data_structs["results"],cmp_fecha, alg)
    data_structs["shootouts"] = organizar_lista(data_structs["shootouts"],cmp_fecha, alg)
    data_structs["goalscorers"] = organizar_lista(data_structs["goalscorers"],cmp_fecha, alg)
    
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



def req_1(data_structs, equipo, condicion, alg=sa):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    resultados = organizar_lista(data_structs["results"],cmp_fecha, alg)
    res = lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(resultados):
        if (condicion.upper() == "LOCAL" or condicion.upper() == "INDIFERENTE" or condicion.upper() == "HOME"):
            if (resultado["home_team"].upper() == equipo.upper()):
                lt.addLast(res, {"date": resultado["date"], 'home_team': resultado["home_team"], 'away_team': resultado['away_team'], 'country': resultado['country'], 'city': resultado['city'], 'home_score': resultado['home_score'], 'away_score': resultado['away_score']})
        if (condicion.upper() == "VISITANTE" or condicion.upper() == "INDIFERENTE" or condicion.upper() == "AWAY"):
            if (resultado["away_team"].upper() == equipo.upper()):
                lt.addLast(res, {"date": resultado["date"], 'home_team': resultado["home_team"], 'away_team': resultado['away_team'], 'country': resultado['country'], 'city': resultado['city'], 'home_score': resultado['home_score'], 'away_score': resultado['away_score']})
    res = organizar_lista(res, cmp_fecha, alg)
    return res



def req_2(data_structs, jugador, ng, alg=sa):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    goles = data_structs["goalscorers"]
    resulto_juga = lt.newList("ARRAY_LIST")
    for g in lt.iterator(goles):
        if g["scorer"] == jugador:
            lt.addLast(resulto_juga,{"date":g["date"],"home_team":g["home_team"],"away_team":g["away_team"],
                                     "team":g["team"],"scorer":g["scorer"],"minute":g["minute"],
                                     "own_goal":g["own_goal"],"penalty":g["penalty"]})
    r_inverto = organizar_lista(resulto_juga,cmp_fecha_req2,alg)

    return r_inverto



def req_3(data_structs, equipo, fecha_inicial, fecha_final, alg=sa):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    resultados = data_structs["results"]
    res = lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(resultados):
        if ((resultado["home_team"] == equipo) or (resultado["away_team"] == equipo) )and (fecha_inicial < resultado["date"]) and (fecha_final > resultado["date"]):
            lt.addLast(res, {"date": resultado["date"], 'home_team': resultado["home_team"], 'away_team': resultado['away_team'], 'home_score': resultado['home_score'], 'away_score': resultado['away_score'], 'tournament': resultado['tournament'], 'city': resultado['city'], 'country': resultado['country']})
    goalscorers = data_structs["goalscorers"]
    goals = lt.newList("ARRAY_LIST")
    for goalscorer in lt.iterator(goalscorers):
        if ((goalscorer["home_team"] == equipo) or (goalscorer["away_team"] == equipo) )and (fecha_inicial < goalscorer["date"]) and (fecha_final > goalscorer["date"]):
            lt.addLast(goals, {'date': goalscorer['date'], 'penalty': goalscorer['penalty'], 'own_goal': goalscorer['own_goal']})
    todo = lt.newList("ARRAY_LIST")
    for i in lt.iterator(res):
        lt.addLast(todo, i)
    for j in lt.iterator(goals):
        lt.addLast(todo, j)
    todo_organizado = organizar_lista(todo, cmp_solo_fecha, alg)
    ultimo = lt.newList("ARRAY_LIST")
    i = 0
    for dato in lt.iterator(todo_organizado):
        if ultimo["elements"] == []:
            lt.addLast(ultimo, dato)
            i += 1
        elif dato["date"] == ultimo["elements"][i-1]["date"]:
            ultimo["elements"][i-1].update(dato)
            #intenté hacer esto con addLast() pero no podía porque tengo que 
            # adicionarle algo a cada diccionario dentro del arreglo "ultimo". 
            # Por lo tanto, debía usar update, lo siento :( ¿Me perdonan? 
        else:
            lt.addLast(ultimo, dato)        
            i += 1
    return ultimo

def req_4(data_structs, torneo, f1, f2, alg=sa):

    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    #Encontrar los partidos del torneo en el tiempo condicion
    resulto = data_structs["results"]
    winero = data_structs["shootouts"]

    r_results = lt.newList("ARRAY_LIST")
    for r in lt.iterator(resulto):
        rta = "Unknow" 
        if (r["tournament"] == torneo) and (r["date"] > f1) and (r["date"] < f2):
            for W in lt.iterator(winero):
                if W["date"] == r["date"] and (r["home_team"]== W["winner"] or r["away_team"]== W["winner"]):
                     rta = W["winner"]
                     break
            lt.addLast(r_results,{"date": r["date"], "tournament": r["tournament"], "country":r["country"], 
                                  "city":r["city"], "home_team":r["home_team"], "away_team":r["away_team"],
                                  "home_score":r["home_score"], "away_score":r["away_score"], "winner":rta})
    
    rt = organizar_lista(r_results, cmp_solo_fecha, alg)
    
    return rt

    """"
    #Encontrar el ganador de los partidos
    winero = data_structs["shootouts"]
    ganadores = lt.newList("ARRAY_LIST")      
    for W in lt.iterator(winero):
        if W["date"]>= f1 and W["date"]<=f2:
            lt.addLast(ganadores, {"date": W["date"],"winner": W["winner"]})
        elif: 
    """
    """""
    #unirlos y limpiar ganadores que tengan la misma fecha difrente tonero
    t = lt.newList("ARRAY_LIST") 
    for j in lt.iterator(r_results):
        lt.addLast(t,j)
    for z in ganadores:
        lt.addLast(t,z)
    
    tsorted = organizar_lista(t,cmp_fecha,alg)
    cont = 0
    resultof = lt.newList("ARRY_LIST")
    for res in iteratro(tsorted):
        if tsorted["elementes"]==[]:
            lt.addLast(resultof,res)
            cont = cont + 1
        elif res["date"] == resultof["elements"][cont-1]["date"] and res["winner"]==resultof["away_team"]:
            res.update
        else:
            lt.addLast(resultof, res)        
            cont = cont+1
    return resultof
    """

def convert_time(text):
    return datetime.strptime(text,"%Y-%m-%d")

def req_5(data_structs, nombre_jugador, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    goles = 0
    penales = 0
    autogoles = 0
    
    resultados = organizar_lista(data_structs["results"],cmp_fecha)
    jugadores = organizar_lista(data_structs["goalscorers"],cmp_fecha)
    todo = lt.newList("ARRAY_LIST")
    res_date = lt.newList("ARRAY_LIST")
    res_minute = lt.newList("ARRAY_LIST")
    res_home_team = lt.newList("ARRAY_LIST")
    res_away_team = lt.newList("ARRAY_LIST")
    res_team = lt.newList("ARRAY_LIST")
    goal_home_score = lt.newList("ARRAY_LIST")
    goal_away_score = lt.newList("ARRAY_LIST")
    goal_tournament = lt.newList("ARRAY_LIST")
    res_penalty = lt.newList("ARRAY_LIST")
    res_own_goal = lt.newList("ARRAY_LIST")
    
    
    for jugador in lt.iterator(jugadores):
        if (convert_time(jugador["date"]) >= convert_time(fecha_inicial)) and (convert_time(fecha_final) >= convert_time(jugador["date"])): 
            if jugador["scorer"] == nombre_jugador:
                goles +=1
                if jugador["penalty"]=="True":
                    penales +=1
                if jugador["own_goal"]=="True":
                    autogoles +=1
                if jugador["date"] != "":
                    lt.addLast(res_date,jugador["date"])
                else:
                    lt.addLast(res_date,"Unknown")
                if jugador["minute"] != "":
                    lt.addLast(res_minute,jugador["minute"])
                else: 
                    lt.addLast(res_minute,"Unknown")
                if jugador["home_team"] != "":
                    lt.addLast(res_home_team,jugador["home_team"])
                else: 
                    lt.addLast(res_home_team,"Unknown")
                if jugador["away_team"]:
                    lt.addLast(res_away_team,jugador["away_team"])
                else:
                    lt.addLast(res_away_team,"Unknown")
                if jugador["team"] != "":
                    lt.addLast(res_team,jugador["team"])
                else:
                    lt.addLast(res_team,"Unknown")
                if jugador["penalty"] != "":
                    lt.addLast(res_penalty,jugador["penalty"])
                else:
                    lt.addLast(res_penalty,"Unknown")
                if jugador["own_goal"] != "":
                    lt.addLast(res_own_goal,jugador["own_goal"])
                else: 
                    lt.addLast(res_own_goal,"Unknown")
                
                
    for resultado in lt.iterator(resultados):
        for i in range(lt.size(res_own_goal)):
            if res_date["elements"][i] == resultado["date"]:
                if res_home_team["elements"][i] == resultado["home_team"] and res_away_team["elements"][i] == resultado["away_team"]:
                    if resultado["home_score"] != "":
                        lt.addLast(goal_home_score,resultado["home_score"])
                    else:
                        lt.addLast(goal_home_score,"Unknown")
                    if resultado["away_score"] != "":
                        lt.addLast(goal_away_score,resultado["away_score"])
                    else:
                        lt.addLast(goal_away_score,"Unknown")
                    if resultado["tournament"] != "":
                        lt.addLast(goal_tournament,resultado["tournament"])
                    else: 
                        lt.addLast(goal_tournament,"Unknown")
                
    lt.addLast(todo,res_date), lt.addLast(todo,res_minute), lt.addLast(todo,res_home_team), lt.addLast(todo,res_away_team)
    lt.addLast(todo,res_team), lt.addLast(todo,goal_home_score), lt.addLast(todo,goal_away_score), lt.addLast(todo,goal_tournament)
    lt.addLast(todo,res_penalty), lt.addLast(todo,res_own_goal)
    torneos=len(list(set(goal_tournament["elements"])))
    return (todo, torneos, goles, penales, autogoles)

def req_6_p1(lst,equipo,f1,f2,alg=sa):
    #Esta funcion me da el mejor jugador de cada equipo
    
    pr = lt.newList("ARRAY_LIST")
    orden = lt.newList("ARRAY_LIST")
    jugadores = lt.newList("ARRAY_LIST")
    
    for j in lt.iterator(lst):
        
        if  (str(j["team"]) == str(equipo)) and (j["own_goal"] == "False") :
            
            lt.addLast(pr,{"scorer":j["scorer"],"minute":j["minute"]})
            
            if j["scorer"] not in jugadores["elements"]:
                lt.addLast(jugadores,j["scorer"])

    for juga in lt.iterator(jugadores):
        go = 0
        matches = 0
        avgt = 0
        for r in lt.iterator(pr):
            if r["scorer"] == juga:
                go += 1
                matches += 1
                if r["minute"] !="": 
                    avgt = (avgt + float(r["minute"]))
                else:
                    avgt = (avgt+1)
        if matches >= 1:
            avgt = round(avgt/matches,1)
        lt.addLast(orden,{"scorer":juga,"goals":go,"matches":matches,"avg_time": avgt})
    if lt.size(orden) > 0:
        mejor = organizar_lista(orden,cmp_goles_req6,alg)
        mejorsito = mejor["elements"][0]
        return (mejorsito)
    else:
        return "Unknown"


def req_6_parte2(data_structs,eqp,trn,f1,f2,alg=sa):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    #Primera parte: sacar los partidos del torneo en la fecha
    
    partidos = data_structs["results"]
    paises = lt.newList("ARRAY_LIST")
    ciudades = lt.newList("ARRAY_LIST")
    ciudade = lt.newList("ARRAY_LIST")
    equipos = lt.newList("ARRAY_LIST")
    rpart = lt.newList("ARRAY_LIST")
    

    for p in lt.iterator(partidos):
        if (p["tournament"] == trn) and (p["date"] > f1) and (p["date"] < f2):
            
            lt.addLast(rpart,{"date": p["date"], "tournament": p["tournament"], "country":p["country"], 
                                  "city":p["city"], "home_team":p["home_team"], "away_team":p["away_team"],
                                  "home_score":p["home_score"], "away_score":p["away_score"]})
            lt.addLast(ciudade,p["city"])
            
            if p["country"] not in paises["elements"]:
                lt.addLast(paises,p["country"])

            if p["city"] not in ciudades["elements"]:
                lt.addLast(ciudades,p["city"])
            
            if p["home_team"] not in equipos["elements"]:
                lt.addLast(equipos,p["home_team"])

            elif p["away_team"] not in equipos["elements"]:
                lt.addLast(equipos,p["away_team"])
            

    #sacar los penales y de más

    goles = data_structs["goalscorers"]
    pr = lt.newList("ARRAY_LIST")
    toti = lt.newList("ARRAY_LIST")
    for j in lt.iterator(goles):
        if (j["date"] > f1) and (j["date"] < f2) and (j["penalty"] == "True" or j["own_goal"] == "True"):
            lt.addLast(pr,{"date":j["date"],"team":j["team"],"scorer":j["scorer"],"own_goal":j["own_goal"],"penalty":j["penalty"]})
            lt.addLast(toti,{"team":j["team"],"scorer":j["scorer"],"own_goal":j["own_goal"],"minute":j["minute"]})
        
        elif (j["date"] > f1) and (j["date"] < f2):
            lt.addLast(toti,{"team":j["team"],"scorer":j["scorer"],"own_goal":j["own_goal"],"minute":j["minute"]})

    #Hallar total de cada pais
    
    final = lt.newList("ARRAY_LIST")
    for group in lt.iterator(equipos):
        tpuntos = 0
        tvic = 0
        goaldif = 0
        tmach = 0
        tloses = 0
        tdraws = 0
        tgoals = 0
        goaldifo = 0
        pp = 0
        autop = 0
        for r in lt.iterator(rpart):
            if r["home_team"] == group:
                tgoals = tgoals + int(r["home_score"])
                goaldif = goaldif + int(r["away_score"])
                if r["home_score"] > r["away_score"]:
                    tvic += 1
                elif r["home_score"] < r["away_score"]:
                    tloses += 1
                else: 
                    tdraws += 1
                tmach += 1
            elif r["away_team"] == group:
                tgoals = tgoals + int(r["away_score"])
                goaldif = goaldif + int(r["home_score"])
                if int(r["home_score"]) < int(r["away_score"]):
                    tvic += 1
                elif int(r["home_score"]) > int(r["away_score"]):
                    tloses += 1
                else:
                    tdraws += 1
                tmach += 1
        
        for s in lt.iterator(pr):
            if s["team"] == group:
                if s["penalty"]!= False:
                    pp += 1
                elif s["own_goal"]!= False:
                    autop += 1
        
        tpuntos = int((tvic*3)) + int(tdraws)
        goaldifo = int(tgoals) - int(goaldif)

        lt.addLast(final,{"team":group,"total_points":tpuntos,"goal_diference":goaldifo,
                          "penalty_points": pp,"matches":tmach,"own_goal_points":autop,"wins":tvic,
                          "draws":tdraws, "losses":tloses, 
                          "goals_for":tgoals, "goals_againts": goaldif, 
                          "better_player":req_6_p1(toti,group,f1,f2,alg)})
    
    if lt.size(final)>int(eqp):
        ultima = lt.subList(organizar_lista(final,cmp_puntos_req6,alg),1,int(eqp))
    else:
        ultima = organizar_lista(final,cmp_puntos_req6,alg)
    contec = 0 
    cc = lt.newList("ARRAY_LIST")
    for c in lt.iterator(ciudades):
        for z in lt.iterator(ciudade):
            if z == c:
                contec+=1
        lt.addLast(cc,{"city":c,"goals":contec})
    
    orgc = organizar_lista(cc,cmp_goles_req6)
    mejorc = orgc["elements"][1]["city"]


    
    elreturn = {"t_matches":lt.size(rpart),"t_countries":lt.size(paises),"t_teams":lt.size(equipos),"t_cities":lt.size(ciudades),"b_city":mejorc,"data":ultima}
    return elreturn
def cmp_score(dato1,dato2):
    if dato1["elements"][1]>dato2["elements"][1]:
        return True
    elif dato1["elements"][1]<dato2["elements"][1]:
        return False
    else:
        if dato1["elements"][2]>dato2["elements"][2]:
            return True
        elif dato1["elements"][2]<dato2["elements"][2]:
            return False
        else:
            if dato1["elements"][3]>dato2["elements"][3]:
                return True
            elif dato1["elements"][3]<dato2["elements"][3]:
                return False
            else: 
                if (type(dato1["elements"][5])==str and (type(dato2["elements"][5])==int or type(dato2["elements"][5])==float)) or (type(dato1["elements"][5])==str and type(dato2["elements"][5])==str):
                    return False
                elif (type(dato2["elements"][5])==str and (type(dato1["elements"][5])==int or type(dato1["elements"][5])==float)):
                    return True
                else:
                    if dato1["elements"][5]<dato2["elements"][5]:
                        return True
                    else:
                        return False
                
def req_7(data_structs, num_jugadores, fecha_inicial, fecha_final):
    #pongo las cosas que hay que retornar de una
    anotadores_totales = 0
    partidos_totales = 0
    torneos_totales = lt.newList("ARRAY_LIST")
    anotaciones_totales = 0
    penales_totales =0
    autogoles_totales = 0
    
    fecha1=convert_time(fecha_inicial)
    fecha2=convert_time(fecha_final)
    lista_jugadores_filtrada = lt.newList("ARRAY_LIST")
    lista_partidos_filtrada = lt.newList("ARRAY_LIST")
    #primer recorrido, encuentro jugadores dentro de las fechas establecidas
    for jugador in data_structs["goalscorers"]["elements"]:
        fecha_jugador=convert_time(jugador["date"])
        if fecha_jugador>=fecha1 and fecha_jugador<=fecha2:
            lt.addLast(lista_jugadores_filtrada,jugador)
    
    
    #segundo recorrido, encuentro partidos dentro de las fechas establecidas
    for resultado in data_structs["results"]["elements"]:
        fecha_partido=convert_time(resultado["date"])
        if fecha_partido>=fecha1 and fecha_partido<=fecha2:
            lt.addLast(lista_partidos_filtrada,resultado)
    #termino de hacer dos sublistas para descartar los partidos que no me sirven. 
    #estas ya están organizadas de forma descendente (carita feliz)
    #creo lista con TODAS las estadísticas
    estadisticas_completas = lt.newList("ARRAY_LIST")
    #creo lista solo con nombres de jugadores
    #index de jugador en una lista=index del mismo en la otra
    #esta lista jugadores tiene nombres unicos mi bro
    lista_jugadores=lt.newList("ARRAY_LIST")
    lista_jugadores_filtrada = organizar_lista(lista_jugadores_filtrada,cmp_fecha)
    lista_partidos_filtrada = organizar_lista(lista_partidos_filtrada,cmp_fecha)
    
    #empuiezo a llenarlas
           
    for jugador in lt.iterator(lista_jugadores_filtrada):
        
        lista_estadisticas=lt.newList("ARRAY_LIST")
        nombre_jugador = jugador["scorer"]
        equipo_jugador = jugador["home_team"]
        adversario_jugador = jugador["away_team"]
        if lt.isPresent(lista_jugadores,nombre_jugador)==0:
            
            #ahora necesito recorrer results, haré busqueda binaria iterativa:
            izquierda, derecha = 1, lt.size(lista_partidos_filtrada)
            while  izquierda<= derecha:
                medio = (izquierda+derecha)//2
                fecha_partido = convert_time(jugador["date"])
                if convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) == fecha_partido:
                    if lt.getElement(lista_partidos_filtrada,medio)["home_team"] == equipo_jugador and lt.getElement(lista_partidos_filtrada,medio)["away_team"]==adversario_jugador:
                        
                        #si el partido es amistoso, muere
                        if "Friendly"== lt.getElement(lista_partidos_filtrada,medio)["tournament"] or ""== jugador["scorer"]:
                            break
                        lt.addLast(lista_jugadores,nombre_jugador)
                        #creo el diccionario de jugador y empiezo a llenarlo
                        lt.addLast(lista_estadisticas,nombre_jugador) #1
                        lt.addLast(lista_estadisticas,0) #2
                        lt.addLast(lista_estadisticas,1) #3
                        if jugador["penalty"] == "True":
                            lt.addLast(lista_estadisticas,1) #4
                            penales_totales+=1
                        else:
                            lt.addLast(lista_estadisticas,0) #4
                        if jugador["own_goal"] == "True":
                            lt.addLast(lista_estadisticas,1) #5
                            autogoles_totales+=1
                        else:
                            lt.addLast(lista_estadisticas,0) #5
                        if jugador["minute"] == "":
                            lt.addLast(lista_estadisticas,-1)
                        else: 
                            lt.addLast(lista_estadisticas,float(jugador["minute"])) #6
                        #hago lista para meter todos los torneos y al final cuento unicos
                        torneos_repetidos= lt.newList("ARRAY_LIST")
                        lt.addLast(torneos_repetidos,lt.getElement(lista_partidos_filtrada,medio)["tournament"]) #7
                        lt.addLast(torneos_totales,lt.getElement(lista_partidos_filtrada,medio)["tournament"])
                        lt.addLast(lista_estadisticas,torneos_repetidos)
                        #discrimino si jugador pierde o gana
                        if jugador["team"] == lt.getElement(lista_partidos_filtrada,medio)["home_team"]:
                            meinteresa = lt.getElement(lista_partidos_filtrada,medio)
                            if lt.getElement(lista_partidos_filtrada,medio)["home_score"]>lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,1) #8
                                lt.addLast(lista_estadisticas,0) #9
                                lt.addLast(lista_estadisticas,0) #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]<lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,0) #8
                                lt.addLast(lista_estadisticas,1) #9
                                lt.addLast(lista_estadisticas,0) #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]==lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,0) #8
                                lt.addLast(lista_estadisticas,0) #9
                                lt.addLast(lista_estadisticas,1) #10
                        elif jugador["team"] == lt.getElement(lista_partidos_filtrada,medio)["away_team"]:
                            
                            if lt.getElement(lista_partidos_filtrada,medio)["home_score"]<lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,1) #8
                                lt.addLast(lista_estadisticas,0) #9
                                lt.addLast(lista_estadisticas,0) #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]>lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,0) #8
                                lt.addLast(lista_estadisticas,1) #9
                                lt.addLast(lista_estadisticas,0) #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]==lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                lt.addLast(lista_estadisticas,0) #8
                                lt.addLast(lista_estadisticas,0) #9
                                lt.addLast(lista_estadisticas,1) #10
                        #como la lista de goalscorers está ordenada descendientemente, el primer gol encontrado es el más reciente, por ende:
                        ultimo_gol = lt.newList("ARRAY_LIST")
                        lt.addLast(ultimo_gol,jugador["date"])
                        lt.addLast(ultimo_gol,lt.getElement(lista_partidos_filtrada,medio)["tournament"])
                        lt.addLast(ultimo_gol,jugador["home_team"])
                        lt.addLast(ultimo_gol,jugador["away_team"])
                        lt.addLast(ultimo_gol,lt.getElement(lista_partidos_filtrada,medio)["home_score"])
                        lt.addLast(ultimo_gol,lt.getElement(lista_partidos_filtrada,medio)["away_score"])
                        lt.addLast(ultimo_gol,jugador["minute"])
                        lt.addLast(ultimo_gol,jugador["penalty"])
                        lt.addLast(ultimo_gol,jugador["own_goal"])
                        
                        #meto la super matriz de ultimo gol a la la ultima posicion de mi sensual array
                        lt.addLast(lista_estadisticas,ultimo_gol)
                        lt.addLast(estadisticas_completas,lista_estadisticas)
                        posicion = lt.isPresent(lista_jugadores,nombre_jugador)
                        posicion_para_llenar = estadisticas_completas["elements"][posicion-1]["elements"]
                        posicion_para_llenar[1] = posicion_para_llenar[2]+posicion_para_llenar[3]-posicion_para_llenar[4] #2
                        break
                    else:
                    # Si el objetivo es menor, buscar en la mitad izquierda
                    
                        if lt.getElement(lista_partidos_filtrada,medio)["home_team"] < equipo_jugador:
                            
                            izquierda= medio + 1
                        else:
                            derecha= medio - 1
                
                elif convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) > fecha_partido:
                    izquierda= medio + 1
                elif convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) < fecha_partido:
                    derecha= medio - 1
        #si entra acá es que si está en una linea y por ende solo tengo que adicionar los datos al ADT
        elif lt.isPresent(lista_jugadores,nombre_jugador)!=0:
            posicion = lt.isPresent(lista_jugadores,nombre_jugador)
            
            #hago busqueda binaria pt.2  para encontrar el partido
            izquierda, derecha = 1, lt.size(lista_partidos_filtrada)
            while  izquierda<= derecha:
                medio = (izquierda+derecha)//2
                fecha_partido = convert_time(jugador["date"])
                if convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) == fecha_partido:
                    if lt.getElement(lista_partidos_filtrada,medio)["home_team"] == equipo_jugador and lt.getElement(lista_partidos_filtrada,medio)["away_team"]==adversario_jugador:
                        #si el partido es amistoso, muere
                        if "Friendly"== lt.getElement(lista_partidos_filtrada,medio)["tournament"] or ""== jugador["scorer"]:
                            break
                        #lleno el diccionario
                        posicion_para_llenar = estadisticas_completas["elements"][posicion-1]["elements"]
                        posicion_para_llenar[2] +=1 #3
                        if jugador["penalty"] == "True":
                            posicion_para_llenar[3] +=1 #4
                            penales_totales +=1
                        else:
                            posicion_para_llenar[3] +=0 #4
                        if jugador["own_goal"] == "True":
                            posicion_para_llenar[4] +=1 #5
                            autogoles_totales +=1
                        else:
                            posicion_para_llenar[4] +=0 #5
                        if jugador["minute"]=="":
                            posicion_para_llenar[5] = float(posicion_para_llenar[5])
                        else:
                            if posicion_para_llenar[5]!=-1:
                                posicion_para_llenar[5] = (float(posicion_para_llenar[5]) + float(jugador["minute"]))/2 #6
                            else:
                                posicion_para_llenar[5]=float(jugador["minute"])
                        #hago addlast a la lista chiquita de torneos
                        voyaagregar= lt.getElement(lista_partidos_filtrada,medio)["tournament"]
                        #lt.addLast(estadisticas_completas["elements"][posicion-1],lt.getElement(lista_partidos_filtrada,medio)["tournament"]) #7
                        lt.addLast(torneos_totales,lt.getElement(lista_partidos_filtrada,medio)["tournament"])
                        #discrimino si jugador pierde o gana
                        if jugador["team"] == lt.getElement(lista_partidos_filtrada,medio)["home_team"]:
                            
                            if lt.getElement(lista_partidos_filtrada,medio)["home_score"]>lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 1 #8
                                posicion_para_llenar[8]+= 0 #9
                                posicion_para_llenar[9]+= 0 #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]<lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 0 #8
                                posicion_para_llenar[8]+= 1 #9
                                posicion_para_llenar[9]+= 0 #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]==lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 0 #8
                                posicion_para_llenar[8]+= 0 #9
                                posicion_para_llenar[9]+= 1 #10
                        elif jugador["team"] == lt.getElement(lista_partidos_filtrada,medio)["away_team"]:
                            
                            if lt.getElement(lista_partidos_filtrada,medio)["home_score"]<lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 1 #8
                                posicion_para_llenar[8]+= 0 #9
                                posicion_para_llenar[9]+= 0 #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]>lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 0 #8
                                posicion_para_llenar[8]+= 1 #9
                                posicion_para_llenar[9]+= 0 #10
                            elif lt.getElement(lista_partidos_filtrada,medio)["home_score"]==lt.getElement(lista_partidos_filtrada,medio)["away_score"]:
                                posicion_para_llenar[7]+= 0 #8
                                posicion_para_llenar[8]+= 0 #9
                                posicion_para_llenar[9]+= 1 #10
                        posicion_para_llenar[1] = posicion_para_llenar[2]+posicion_para_llenar[3]-posicion_para_llenar[4] #2
                        break
                    else:
                    # Si el objetivo es menor, buscar en la mitad izquierda
                    
                        if lt.getElement(lista_partidos_filtrada,medio)["home_team"] < equipo_jugador:
                            
                            izquierda= medio + 1
                        else:
                            derecha= medio - 1
                
                elif convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) > fecha_partido:
                    izquierda= medio + 1
                elif convert_time(lt.getElement(lista_partidos_filtrada,medio)["date"]) < fecha_partido:
                    derecha= medio - 1
        #si entra acá es que si está en una linea y por ende solo tengo que adicionar los datos al ADT
    
    anotadores_totales = lt.size(lt.quitar_repetidos(lista_jugadores))-1
    partidos_totales = lt.size(lista_partidos_filtrada)
    
    anotaciones_totales = lt.size(lista_jugadores_filtrada)
    estadisticas_completas = organizar_lista(estadisticas_completas,cmp_score)
    if int(num_jugadores)<=lt.size(estadisticas_completas):
        estadisticas_completas = lt.subList(estadisticas_completas,1,int(num_jugadores))    
    else:
        print("Hay menos anotadores en estas fechas de los que pidió")
    posi=1
    for i in lt.iterator(estadisticas_completas):
        estadisticas_completas["elements"][posi-1]["elements"][6] = lt.size(lt.quitar_repetidos(lt.getElement(i,7)))
        posi +=1
    torneos_totales=lt.size(lt.quitar_repetidos(torneos_totales))
    
        
    return (estadisticas_completas,anotadores_totales, partidos_totales, anotaciones_totales, penales_totales, autogoles_totales, torneos_totales)

def req_8_primera_parte(data_structs, equipo, fecha_inicial, fecha_final, alg=sa):
    """
    Función que soluciona la primera parte de la primera parte del requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    resultados = data_structs["results"]
    local = 0
    visitante = 0
    res = lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(resultados):
        if ((resultado["home_team"] == equipo) or (resultado["away_team"] == equipo) )and (fecha_inicial < resultado["date"]) and (fecha_final > resultado["date"]) and (resultado["tournament"] != "Friendly"):
            lt.addLast(res, {"date": resultado["date"], 'home_team': resultado["home_team"], 'away_team': resultado['away_team'], 'home_score': resultado['home_score'], 'away_score': resultado['away_score'], 'country': resultado['country'], 'city': resultado['city'], 'tournament': resultado['tournament']})
            if resultado["home_team"] == equipo:
                local += 1
            else:
                visitante += 1
    goalscorers = data_structs["goalscorers"]
    goals = lt.newList("ARRAY_LIST")
    for goalscorer in lt.iterator(goalscorers):
        if ((goalscorer["home_team"] == equipo) or (goalscorer["away_team"] == equipo) )and (fecha_inicial < goalscorer["date"]) and (fecha_final > goalscorer["date"]):
            lt.addLast(goals, {'date': goalscorer['date'], "scorer": goalscorer["scorer"], "minute": goalscorer["minute"], 'penalty': goalscorer['penalty'], 'own_goal': goalscorer['own_goal']})
    todo = lt.newList("ARRAY_LIST")
    for i in lt.iterator(res):
        lt.addLast(todo, i)
    for j in lt.iterator(goals):
        lt.addLast(todo, j)
    todo_organizado = organizar_lista(todo, cmp_solo_fecha, alg)

    scorer = []
    jugador = []
    goleadores = lt.newList("ARRAY_LIST")
    jugadores = lt.newList("ARRAY_LIST")
    for dato in lt.iterator(goals):
        anio = dato["date"].split("-")[0]
        if goleadores["elements"] == [] or (lt.lastElement(goleadores)[0] != anio):
            lt.addLast(goleadores, [anio, [dato["scorer"], dato["date"], dato["minute"]]])
            lt.addLast(jugadores, [anio, dato["scorer"]])
            scorer = []
            jugador = []
            scorer.append(anio)
            jugador.append(anio) 
        else:
            lt.changeInfo(goleadores, lt.isPresent(goleadores, lt.lastElement(goleadores)), scorer)
            lt.changeInfo(jugadores, lt.isPresent(jugadores, lt.lastElement(jugadores)), jugador)
        sublista = [] 
        sublista.append(dato["scorer"])
        sublista.append(dato["date"])
        sublista.append(dato["minute"]) 
        scorer.append(sublista)
        jugador.append(dato["scorer"])
    
    jugadores_ultimo = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(jugadores):
        dic = {"year": lista[0]}       
        for jugador in lista[1:]:
            if jugador not in dic:
                dic[jugador] = 1
            else:
                dic[jugador] += 1
        lt.addLast(jugadores_ultimo, dic)
    
    mejor_jugador = lt.newList("ARRAY_LIST")
    for diccionario in lt.iterator(jugadores_ultimo):
        mejor = ""
        goles = 0
        nuevo_dic = {"year": diccionario["year"]}
        for key, value, in diccionario.items():
            if key != "year":
                if value > goles:
                    goles = value
                    mejor = key
        nuevo_dic["scorer"] = mejor
        nuevo_dic["goals"] = goles
        lt.addLast(mejor_jugador, nuevo_dic)
    
    cantidad_de_partidos = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(goleadores):
        dic = {"year": lista[0]}
        for jugador in lista[1:]:
            if jugador[0] not in dic:
                dic[jugador[0]] = 1
                fecha = jugador[1]  
            else:
                if fecha != jugador[1]:
                    fecha = jugador[1]
                    dic[jugador[0]] += 1
        lt.addLast(cantidad_de_partidos, dic)

    promedio_de_minutos = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(goleadores):
        dic = {"year": lista[0]}
        for jugador in lista[1:]:
            if jugador[0] not in dic:
                dic[jugador[0]] = float(jugador[2])
                dic[f"{jugador[0]}_veces"] = 1
            else:
                dic[f"{jugador[0]}_veces"] += 1
                dic[jugador[0]] = (dic[jugador[0]] + float(jugador[2]))/dic[f"{jugador[0]}_veces"]
        lt.addLast(promedio_de_minutos, dic)
    
    informacion_del_mejor_jugador = lt.newList("ARRAY_LIST")
    for i in range(lt.size(mejor_jugador)):
        year = mejor_jugador["elements"][i]["year"]
        scorer = mejor_jugador["elements"][i]["scorer"]
        goals = mejor_jugador["elements"][i]["goals"]
        matches = cantidad_de_partidos["elements"][i][scorer]
        avg_time = promedio_de_minutos["elements"][i][scorer]
        dic = {"year": year, "scorer": scorer, "goals": goals, "matches": matches, "avg_time": avg_time}
        lt.addLast(informacion_del_mejor_jugador, dic)
    
    anios = lt.newList("ARRAY_LIST")
    penalty = 0
    own_goal = 0
    goal_difference = 0
    wins = 0
    losses = 0
    ties = 0
    puntos = 0
    goles_a_favor = 0
    goles_en_contra = 0
    matches = 0
    for dato in lt.iterator(todo_organizado):
        anio = dato["date"].split("-")[0]
        if "penalty" in dato:
            if dato["penalty"] == "True":
                    penalty = 1
        if "own_goal" in dato:
            if dato["own_goal"] == "True":
                    own_goal = 1
        if "home_team" in dato:
            matches = 1
            if dato["home_team"] == equipo:
                goal_difference = int(dato["home_score"])-int(dato["away_score"])
                goles_a_favor = int(dato["home_score"])
                goles_en_contra = int(dato["away_score"])
            else:
                goal_difference = int(dato["away_score"])-int(dato["home_score"])
                goles_a_favor = int(dato["away_score"])
                goles_en_contra = int(dato["home_score"])
            if goal_difference > 0:
                wins = 1
                puntos = 3
            elif goal_difference < 0:
                losses = 1
            else:
                ties = 1
                puntos = 1
        if (anios["elements"] == []) or (lt.lastElement(anios)["year"] != anio):
            lt.addLast(anios, {"year": anio, "matches": matches, "total_points": puntos, "goal_difference": goal_difference, "penalties": penalty, "own_goals": own_goal, "wins": wins, "draws": ties, "losses": losses, "goals_for": goles_a_favor, "goals_against": goles_en_contra})
        else:
            lt.lastElement(anios)["matches"] += matches
            lt.lastElement(anios)["total_points"] += puntos
            lt.lastElement(anios)["goal_difference"] += goal_difference
            lt.lastElement(anios)["penalties"] += penalty
            lt.lastElement(anios)["own_goals"] += own_goal
            lt.lastElement(anios)["wins"] += wins
            lt.lastElement(anios)["draws"] += ties
            lt.lastElement(anios)["losses"] += losses
            lt.lastElement(anios)["goals_for"] += goles_a_favor
            lt.lastElement(anios)["goals_against"] += goles_en_contra
        penalty = 0
        own_goal = 0
        goal_difference = 0
        wins = 0
        losses = 0
        ties = 0
        puntos = 0
        goles_a_favor = 0
        goles_en_contra = 0
        matches = 0

    primero = lt.firstElement(res)
    ultima_fecha = lt.lastElement(res)["date"]
    primera_fecha = primero["date"]
    ultimo_anio = ultima_fecha.split("-")[0]
    primer_anio = primera_fecha.split("-")[0]
    years = int(primer_anio) - int(ultimo_anio)
    
    return (years, local, visitante, ultima_fecha, primero, anios, informacion_del_mejor_jugador)

def req_8_segunda_parte(data_structs, equipo1, equipo2, fecha_inicial, fecha_final, alg=sa):
    """
    Función que soluciona la segunda parte de la primera parte del requerimiento 8
    """
    resultados = data_structs["results"]
    res = lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(resultados):
        if ((resultado["home_team"] == equipo1) and (resultado["away_team"] == equipo2)) or ((resultado["home_team"] == equipo2) and (resultado["away_team"] == equipo1)) and (fecha_inicial < resultado["date"]) and (fecha_final > resultado["date"]) and (resultado["tournament"] != "Friendly"):
            lt.addLast(res, {"date": resultado["date"], 'home_team': resultado["home_team"], 'away_team': resultado['away_team'], 'home_score': resultado['home_score'], 'away_score': resultado['away_score'], 'country': resultado['country'], 'city': resultado['city'], 'tournament': resultado['tournament']})
    
    cantidad_de_partidos = lt.size(res)
    victoria_equipo1 = 0
    derrotas_equipo1 = 0
    victoria_equipo2 = 0
    derrotas_equipo2 = 0
    empates = 0
    for partido in lt.iterator(res):
        if partido["home_team"] == equipo1:
            if partido["home_score"] > partido["away_score"]:
                victoria_equipo1 += 1
                derrotas_equipo2 += 1
            elif partido["home_score"] < partido["away_score"]:
                victoria_equipo2 += 1
                derrotas_equipo1 += 1
            else:
                empates += 1
        elif partido["home_team"] == equipo2:
            if partido["home_score"] > partido["away_score"]:
                victoria_equipo2 += 1
                derrotas_equipo1 += 1
            elif partido["home_score"] < partido["away_score"]:
                victoria_equipo1 += 1
                derrotas_equipo2 += 1
            else:
                empates += 1
        
    ultimo_partido = lt.firstElement(res)
    goalscorers = data_structs["goalscorers"]
    ultimo_partido_jugador = lt.newList("ARRAY_LIST")
    for jugador in lt.iterator(goalscorers):
        if (jugador["date"] == ultimo_partido["date"]) and (jugador["home_team"] == ultimo_partido["home_team"]) and (jugador["away_team"] == ultimo_partido["away_team"]):
            lt.addLast(ultimo_partido_jugador, jugador)


    return (cantidad_de_partidos, victoria_equipo1, derrotas_equipo1, victoria_equipo2, derrotas_equipo2, empates, ultimo_partido, ultimo_partido_jugador)



# Funciones utilizadas para comparar elementos dentro de una lista

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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def resultSize(catalog):
    return lt.size(catalog['results'])

def goalscorersSize(catalog):
    return lt.size(catalog['goalscorers'])

def shootoutsSize(catalog):
    return lt.size(catalog['shootouts'])