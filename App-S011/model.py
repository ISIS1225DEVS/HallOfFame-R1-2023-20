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

from statistics import mode
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


def new_data_structs(formato):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    n_d = {"goal_scorers": lt.newList(formato),
           "results": lt.newList(formato),
           "shootouts": lt.newList(formato)}

    
    return n_d



# Funciones para agregar informacion al modelo

def addData(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    return lt.addLast(data_structs, data)

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista   
    resultados = lt.newList("ARRAY_LIST")
    tamano= int(lt.size(data_structs))
    lt.addFirst(resultados,lt.firstElement(data_structs))
    for b in range(2,4):
        p = obtener_dato(data_structs, b)
        addData(resultados, p)
    for b in range (0,3):
        p = obtener_dato(data_structs, (tamano-b))
        addData(resultados, p)
    return resultados

def dataSize(data_structure):
    """
    Retorna el tamaño de la lista de datos
    """
    return int(lt.size(data_structure))

def obtener_dato(lista,indice):
    """
    Retorna un dato a partir de su ID
    """
    return lt.getElement(lista,indice)


def req_1(lista, nom, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    finales= lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lista):
        lis={'date':cada['date'],'home_team':cada['home_team'],'away_team':cada['away_team'],'home_score':cada['home_score'],'away_score':cada['away_score'],'city':cada['city'],'country':cada['country']}  
        if condicion =="visitante" :
            if str(cada['away_team']) ==nom:
                addData(finales,lis)
        elif condicion =="local" :
            if str(cada['home_team'])== nom:
                addData(finales,lis)
        elif condicion =="indiferente":
            if str(cada['home_team'])== nom or str(cada["away_team"]) ==nom:
                addData(finales,lis)
    return finales



def req_2(lista,nombre):
    """
    Función que soluciona el requerimiento 2
    """
    finales= lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lista):
        if cada['scorer']==nombre:
            addData(finales,cada)
    return finales
            
    # TODO: Realizar el requerimiento 2

def req_3(scorers,lista,f_i,f_f,equipo):
    """
    Función que soluciona el requerimiento 3
    """
    lis=lt.newList("ARRAY_LIST")
    total=tamano=dataSize(scorers)
    local=0
    visi=0
    for cada in lt.iterator(lista):
        fecha=cada["date"]
        home= cada["home_team"]
        visitante=cada["away_team"]
        if fecha>=f_i and fecha<=f_f and (home==equipo or visitante==equipo):
           penales,auto = busqueda_binaria_scorers(scorers,fecha,1,total,home,tamano)
           cada["Penalty"]=penales
           cada["own_goal"]=auto 
           if home==equipo:
               local+=1
           if visitante==equipo:
               visi+=1
           lt.addLast(lis,cada)
    return lis,local,visi

#Funciones adicionales req 3 (busqueda_binaria_scorers)            
        
def busqueda_binaria_scorers(scorers,fecha,low,high,home,tamano):
    """Esta función se basa en una busqueda binaria modificada la cual se encarga de buscar en una determinada fecha y en sus
       posibles diferentes goles si hubo autogol y penal

    Args:
        scorers (list): lista con la infornmacion del archivo goalscorers
        fecha (str): La fecha del partido que se desea consultar
        low (int): el valor mínimo que puede recorrer en la lista
        high (int): el valor maximo que puede recorrer en la lista
        home (str): El equipo Local
        tamano (int): tamaño de la lista scorers

    Returns:
        Str o Bool: En caso de no encontrar va a retornar el str "unknown" y de lo contrario retorna el valor booleano para penales
        y para autogoles
    """
    penales=False
    auto=False
    mitad=(low+high)//2
    if low>high:
        return "unknown","unknown"
    elemento = obtener_dato(scorers,mitad)
    elemen= elemento["date"]
    casa=elemento["home_team"]
    if elemen ==fecha and home==casa:
        penales= elemento["penalty"]#DATO DEL DE LA MITAD POR SI NO HAY 
        auto=elemento["own_goal"]#   MÁS CON LA MISMA FECHA Y CIUDAD 
        atras=mitad-1
        adelante=mitad+1
        atras_c=(obtener_dato(scorers, atras))
        valor=atras_c["date"]
        casa1=atras_c["home_team"]
        adelante_c=(obtener_dato(scorers, adelante))
        val=adelante_c["date"]
        casa2=adelante_c["home_team"]
        
        while  atras >=low and valor ==fecha and casa1==home:
            if penales != "True":
                penales= (obtener_dato(scorers, atras))["penalty"]
            if auto!="True":
                auto=(obtener_dato(scorers, atras))["own_goal"]
            atras-= 1
            if atras>=1:
                valor= (obtener_dato(scorers, atras))["date"]
                casa1=(obtener_dato(scorers, atras))["home_team"]
                
        while  adelante <= high and  val==fecha and casa2==home:
            if penales != "True":
                penales= (obtener_dato(scorers, adelante))["penalty"]
            if auto!="True":
                auto=(obtener_dato(scorers, adelante))["own_goal"]
            adelante+= 1
            if adelante<=tamano:
                val=(obtener_dato(scorers, adelante))["date"]
                casa2=(obtener_dato(scorers, adelante))["home_team"]
        return penales,auto
    elif elemen >fecha:
        high= mitad-1
    else:
        low= mitad+1
    return busqueda_binaria_scorers(scorers,fecha,low,high,home,tamano)
    
def req_4(data_structs, nombreTorneo, fechaIni, fechaFin):
    """
    Función que soluciona el requerimiento 4
    """

    
    listTotalCountries = lt.newList("ARRAY_LIST") #Tiene addLast de O(1)
    
    countTotalShootouts=0
    
    fechaIni= strToDate(fechaIni)
    
    fechaFin=strToDate(fechaFin)
    
    answer=lt.newList('ARRAY_LIST') #Tiene addLast de O(1)
    
    listTotalCities=lt.newList('ARRAY_LIST') #Tiene addLast de O(1)
    
     
    
    for i in range(lt.size(data_structs['model']['results'])):
        
        matchResult=lt.getElement(data_structs['model']['results'], i) #resultado del partido
        
        matchResult['winnerByPenalty']='No penalty shootout winner' #se asigna sin ganador en caso de que no haya ganador
        
        matchResult['penalty shootout']='No penalty shootout contest' #se asigna sin contendencia en penales en caso de que no haya
        
        dateMatchResult = strToDate(matchResult['date']) #Se asigna una variable de tipo fecha para comparar fechas
        
        cityResult=matchResult['city'] 
        
        countryResult=matchResult['country']
        
        if fechaIni<dateMatchResult<fechaFin and (matchResult['tournament'].lower().replace(' ', '')== nombreTorneo.lower().replace(' ','')): #comparación de fechas
            for x in range((lt.size(data_structs['model']['shootouts']))): # COMPLEJIDAD DE i*j
                
                shooutOutMatch = lt.getElement(data_structs['model']['shootouts'], x)
                
                dateShooutOut = strToDate(shooutOutMatch['date'])
                
                shooutOutWinner=shooutOutMatch['winner']
                
                if dateShooutOut==dateMatchResult: #se comprueba para hacer el contador 
                    
                    matchResult['winnerByPenalty']=shooutOutWinner #se asigna el ganador porque hubo ganador de penales
                    
                    matchResult['penalty shootout']='Penalty shootout contest'# se asigna que si hubo contendencia por tiros desde el punto penal
                    
                    countTotalShootouts+=1 #se cuenta el total de penales 
                    
            if not lt.isPresent(listTotalCountries, countryResult): #se pregunta para no repetir ciudades y contar bien
                
                lt.addLast(listTotalCountries, countryResult)
                
            if not lt.isPresent(listTotalCities, cityResult): #se pregunta para no repetir ciudades y contar bien 
                
                lt.addLast(listTotalCities, cityResult)

            lt.addLast(answer, matchResult)
            #se añade el partido como instrucción final, una vez haya sido modificado y comprobado la información. 
            
    countTotalMatches=lt.size(answer)
    countTotalCities=lt.size(listTotalCities)
    countTotalCountries=lt.size(listTotalCountries)
    
    """
    ORDENAMIENTO BAJO 3 CRITERIOS: fecha
                                    , nombre del pais (alfabetico)
                                    , ciudad donde se disputó el partido (alfabetico)
    """
    answer = se.sort(answer, compareReq4)
    
    
    
    return countTotalMatches, countTotalCountries, countTotalCities, countTotalShootouts, answer
        
        
    # TODO: Realizar el requerimiento 4
    



def req_5(data_structs, nombre_jugador, fecha_inicio, fecha_final):
      
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    resultados = data_structs["results"]
    goal_scorers = data_structs["goal_scorers"]
    
    lista_anotaciones = lt.newList("ARRAY_LIST")
    lista_torneo = lt.newList()
    lista_penaltis = 0
    lista_autogol = 0
    
    for goal in lt.iterator(goal_scorers):
        nombre = goal["scorer"]
        fecha = goal["date"]
        penalty = goal["penalty"]
        own_goal = goal["own_goal"]
        if nombre.lower() == nombre_jugador.lower() and fecha >= fecha_inicio and fecha <= fecha_final:
            if penalty == True:
                lista_penaltis += 1 
            if own_goal == True:
                lista_autogol += 1
            for cada in lt.iterator(resultados):
                fecha_2= cada["date"]           
                if fecha == fecha_2: 
                    torneo = cada["tournament"]
                    goal["tournament"] = torneo
                    presente = lt.isPresent(lista_torneo, torneo)
                    if presente == 0:
                        lt.addLast(lista_torneo, torneo)                    
                    lt.addLast(lista_anotaciones,goal) 
    
    cant_goles = dataSize(lista_anotaciones)                
    cant_torneos = dataSize(lista_torneo)    
    cant_penaltis = lista_penaltis
    cant_autogoles = lista_autogol
       
    return shell(lista_anotaciones, sort_goalscrit5), cant_goles, cant_torneos, cant_penaltis, cant_autogoles  

def req_6(lista,scorers):
    """
    Función que soluciona el requerimiento 6
    """
    lista_equipos=lt.newList("ARRAY_LIST")
    lista_ciudades=lt.newList("ARRAY_LIST")
    ciudades=lt.newList("ARRAY_LIST")
    resultado=lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lista):
        ciudad=cada["country"]
        fecha=cada["date"]
        high=tamano=dataSize(scorers)
        numero= lt.isPresent(lista_ciudades,ciudad)
        if numero==0:
            dic={"ciudad":ciudad,"cantidad":1}
            addData(lista_ciudades,ciudad)
            addData(ciudades,dic)
        if numero>0:
            ele=obtener_dato(ciudades,numero)
            ele["cantidad"]+=1

        casa=cada["home_team"]
        goles_casa=int(cada["home_score"])
        visitante= cada["away_team"]
        goles_visitante=int(cada["away_score"])
        list_jc=lt.newList("ARRAY_LIST")
        list_jv=lt.newList("ARRAY_LIST")
        list_resulcasa=lt.newList("ARRAY_LIST")
        list_resulvisi=lt.newList("ARRAY_LIST")
        
        puntos_casa=0
        puntos_visitante=0
        diferencia_visi=goles_visitante-goles_casa
        diferencia_casa=goles_casa-goles_visitante
        victorias_casa=0
        victorias_visi=0
        empate=0
        derrota_casa=0
        derrota_visi=0
        
        if goles_casa>goles_visitante:
            puntos_casa=3
            victorias_casa=1
            derrota_visi=1
        elif goles_visitante>goles_casa:
            puntos_visitante=3
            victorias_visi=1
            derrota_casa=1
        else:
            puntos_visitante=1
            puntos_casa=1
            empate=1
        numeroc=lt.isPresent(lista_equipos,casa)
        numerov=lt.isPresent(lista_equipos,visitante)
        if numeroc==0:
            penal_casa,auto_casa,list_jc,list_resulcasa=busqueda_binaria_scorersreq6(scorers,fecha,1,high,casa,tamano,casa,list_jc,list_resulcasa)
            diccionario={"Team":casa,"total_points":puntos_casa,"goal_difference":diferencia_casa,"penalty_points":penal_casa,"matches":1,
                         "own_goal_points":auto_casa,"wins": victorias_casa,"draws":empate,"losses":derrota_casa,"goals_for":goles_casa,
                         "goals_againts":goles_visitante,"top_scorer":list_resulcasa,"Resultados":list_jc}
            addData(lista_equipos,casa)
            addData(resultado,diccionario)
        if numeroc>0:
            elemento=obtener_dato(resultado,numeroc)
            list_jc=elemento["Resultados"]
            list_resulcasa=elemento["top_scorer"]
            penal_casa,auto_casa,list_jc,list_resulcasa=busqueda_binaria_scorersreq6(scorers,fecha,1,high,casa,tamano,casa,list_jc,list_resulcasa)
            elemento["top_scorer"]=list_resulcasa
            elemento["Resultados"]=list_jc
            elemento["total_points"]+=puntos_casa
            elemento["goal_difference"]+=diferencia_casa
            elemento["matches"]+=1
            elemento["wins"]+=victorias_casa
            elemento["draws"]+=empate
            elemento["losses"]+=derrota_casa
            elemento["goals_for"]+=goles_casa
            elemento["goals_againts"]+=goles_visitante
            elemento["penalty_points"]+=penal_casa
            elemento["own_goal_points"]+=auto_casa
        if numerov==0:
            penal_visi,auto_visi,list_jv,list_resulvisi=busqueda_binaria_scorersreq6(scorers,fecha,1,high,casa,tamano,visitante,list_jv,list_resulvisi)
            diccionario={"Team":visitante,"total_points":puntos_visitante,"goal_difference":diferencia_visi,"penalty_points":penal_visi,"matches":1,
                         "own_goal_points":auto_visi,"wins":victorias_visi,"draws":empate,"losses":derrota_visi,"goals_for":goles_visitante,
                         "goals_againts":goles_casa,"top_scorer":list_resulvisi,"Resultados":list_jv}
            addData(resultado,diccionario)
            addData(lista_equipos,visitante) 
        if numerov>0:
            elemento=obtener_dato(resultado,numerov)
            list_jv=elemento["Resultados"]
            list_resulvisi=elemento["top_scorer"]
            penal_visi,auto_visi,list_jv,list_resulvisi=busqueda_binaria_scorersreq6(scorers,fecha,1,high,casa,tamano,visitante,list_jv,list_resulvisi)
            elemento["top_scorer"]=list_resulvisi
            elemento["Resultados"]=list_jv
            elemento["total_points"]+=puntos_visitante
            elemento["goal_difference"]+=diferencia_visi
            elemento["matches"]+=1
            elemento["wins"]+=victorias_visi
            elemento["draws"]+=empate
            elemento["losses"]+=derrota_visi 
            elemento["goals_for"]+=goles_visitante
            elemento["goals_againts"]+=goles_casa
            elemento["penalty_points"]+=penal_visi
            elemento["own_goal_points"]+=auto_visi
    ciudad_moda=""
    for cada in lt.iterator(ciudades):
        mayor=0
        if cada["cantidad"]>mayor:
            ciudad_moda=cada["ciudad"]
    cantidad_equipos= dataSize(lista_equipos)
    for cada in lt.iterator(resultado):
        lis=cada["top_scorer"]
        lisa=respuesta_jugador(lis)
        cada["top_scorer"]=lisa
        del cada["Resultados"] 
    return cantidad_equipos,ciudad_moda,shell(resultado,comparacionreq6)

#Funciones adicionales requerimiento 6(busqueda_binaria_scorersreq6)

def busqueda_binaria_scorersreq6(scorers,fecha,low,high,home,tamano,team,list_j,list_resul):
    """Esta función se basa en una busqueda binaria modificada la cual se encarga de buscar en una determinada fecha y en sus
       posibles diferentes goles si hubo autogol y penal

    Args:
        scorers (list): lista con la infornmacion del archivo goalscorers
        fecha (str): La fecha del partido que se desea consultar
        low (int): el valor mínimo que puede recorrer en la lista
        high (int): el valor maximo que puede recorrer en la lista
        home (str): El equipo Local
        tamano (int): tamaño de la lista scorers
        team (str): Equipo del cual se desea consultar, es como tal el que hizo el gol o autogol
        list_j (list): Lista donde se encuentran los jugadores de ese equipo que ya se tiene la información
        list_result (list): Lista de los jugadores con su información 

    Returns:
        la cantidad total de autogoles y penales metidos por el equipo, la lista con los jugadores que ya se tiene informacion de gol y una lista con la informacion de
        los jugadores que han hecho gol en el equipo.
    """
    r_p=0
    r_a=0
    mitad=(low+high)//2
    if low>high:
        return 0,0,list_j,list_resul
    elemento = obtener_dato(scorers,mitad)
    elemen= elemento["date"]
    casa=elemento["home_team"]
    equipo=elemento["team"]
    jugador=elemento["scorer"]
    indice=lt.isPresent(list_j,jugador)
    if elemen ==fecha and home==casa and equipo==team:
        if indice==0:
            partidos=lt.newList("ARRAY_LIST")
            addData(partidos,elemen)
            diccionario={"Scorer":jugador,"goals":1,"matches":partidos,"avg_time":(float(elemento["minute"]))}
            addData(list_j,jugador)
            addData(list_resul,diccionario)
        if indice >0:
            scorer=obtener_dato(list_resul,indice)
            scorer["goals"]+=1
            partidos=scorer["matches"]
            n=lt.isPresent(partidos,elemen)
            if 0==n:
                addData(partidos,elemen)
                scorer["matches"]=partidos
            scorer["avg_time"]+=(float(elemento["minute"]))
        if elemento["penalty"]=="True":
            r_p= r_p+1
        if elemento["own_goal"]=="True":
            r_a=r_a+1
        atras=mitad-1
        adelante=mitad+1
        
        antes=(obtener_dato(scorers, atras))#Datos para el valor menor
        valor= antes["date"]
        casa1=antes["home_team"]
        equipo1=antes["team"]
        jugador1= antes["scorer"]
        indice1=lt.isPresent(list_j,jugador1)
        
        despues=(obtener_dato(scorers, adelante))#Datos para el valor mayor
        val=despues["date"]
        casa2=despues["home_team"]
        equipo2=despues["team"]
        jugador2= despues["scorer"]
        indice2=lt.isPresent(list_j,jugador2)
        
        while  atras >=low and valor ==fecha and casa1==home and equipo1==team: #Para buscar los que cumplan con los requerimientos, pero ordenados esten antes 
            if indice1==0:
                fechas=lt.newList("ARRAY_LIST")
                addData(fechas,valor)
                diccionari={"Scorer":jugador1,"goals":1,"matches":fechas,"avg_time":(float(antes["minute"]))}
                addData(list_j,jugador1)
                addData(list_resul,diccionari)
            if indice1 >0:
                scorer=obtener_dato(list_resul,indice1)
                scorer["goals"]+=1
                partidos=scorer["matches"]
                n=lt.isPresent(partidos,valor)
                if n==0:
                    lt.addLast(partidos,valor)
                    scorer["matches"]=partidos
                scorer["avg_time"]+=(float(antes["minute"]))
            if antes["penalty"]=="True":
                r_p= r_p+1
            if antes["own_goal"]=="True":
                r_a=r_a+1
            atras-= 1
            if atras>=1:
                antes=(obtener_dato(scorers, atras))
                valor= antes["date"]
                casa1=antes["home_team"]
                equipo1=antes["team"]
                jugador1= antes["scorer"]
                indice1=lt.isPresent(list_j,jugador1)
                
        while  adelante <= high and  val==fecha and casa2==home and equipo2==team: #Para buscar los que cumplan con los requerimientos, pero ordenados esten despues
            if indice2==0:
                fechas=lt.newList("ARRAY_LIST")
                addData(fechas,val)
                diccionari={"Scorer":jugador2,"goals":1,"matches":fechas,"avg_time":(float(despues["minute"]))}
                addData(list_j,jugador2)
                addData(list_resul,diccionari)
            if indice2 >0:
                scorer=obtener_dato(list_resul,indice2)
                scorer["goals"]+=1
                partidos=scorer["matches"]
                n=lt.isPresent(partidos,val)
                if n==0:
                    addData(partidos,val)
                scorer["matches"]=partidos
                scorer["avg_time"]+=(float(despues["minute"]))
            if despues["penalty"]=="True":
                r_p= r_p+1
            if despues["own_goal"]=="True":
                r_a=r_a+1
            adelante+= 1
            if adelante<=tamano:
                despues=(obtener_dato(scorers, adelante))
                val=despues["date"]
                casa2=despues["home_team"]
                equipo2=despues["team"]
                jugador2= despues["scorer"]
                indice2=lt.isPresent(list_j,jugador2)

        return r_p,r_a,list_j,list_resul
    elif elemen >=fecha:
        high= mitad-1
    else:
        low= mitad+1
    return busqueda_binaria_scorersreq6(scorers,fecha,low,high,home,tamano,team,list_j,list_resul)

def respuesta_jugador(list_res):
    """Esta función es para conocer el mejor jugador del equipo (más goles marcados en menos partidos y con un promedio de tiempo más bajo)

    Args:
        list_res (list): La lista que tiene los resultados de los jugadores anotadores del equipo

    Returns:
        list: Retorna una liosta con la información del mejor jugador
    """
    lista=lt.newList("ARRAY_LIST")
    if lt.isEmpty(list_res)==False:
        list_res=shell(list_res,comparacionresreq6)
        jugador=obtener_dato(list_res,1)
        partidos=jugador["matches"]
        partidos=dataSize(partidos)
        jugador["matches"]=partidos
        goles=jugador["goals"]
        tiempo=jugador["avg_time"]
        promedio= tiempo/goles
        jugador["avg_time"]=promedio
        addData(lista,jugador)
    return lista
                
def req7(scorers,f_i,f_f,results):
    auto=0
    penal=0
    goles=0
    partidos=lt.newList("ARRAY_LIST")
    torneo=lt.newList("ARRAY_LIST")
    list_anotadores=lt.newList("ARRAY_LIST")
    list_result=lt.newList("ARRAY_LIST")
    for cada in lt.iterator(scorers):
        dat= cada["date"]
        home=cada["home_team"]
        if dat>=f_i and dat<=f_f:
            high=tamano=dataSize(results)
            oficial,tourn =busqueda_binaria_req7(results,dat,1,high,home,tamano)
            if oficial ==True:
                equipo=cada["team"]
                puntaje_casa,puntaje_visi,victoria,derrota,empate=busqueda_binaria_req7_2(results,dat,1,high,home,tamano,equipo)
                goles+=1
                añadir=True
                penaless=cada["penalty"]
                print(penaless)
                autogol=cada["own_goal"]
                print(autogol)
                visitante=cada["away_team"]
                puntos=1
                penales=0
                auto_goles=0
                tiempo=float(cada["minute"])
                if autogol=="True":
                    auto+=1
                    puntos-=1
                    auto_goles=1
                if penaless=="True":
                    penal+=1
                    puntos+=1
                    penales=1
                for par in lt.iterator(partidos):
                    if par["home"]==home and par["date"]==dat:
                        añadir =False
                if añadir ==True:
                    parti= {"home":home,"date":dat}
                    lt.addLast(partidos,parti)
                n=lt.isPresent(torneo,tourn)
                if n==0:
                    lt.addLast(torneo,tourn)
                scorer=cada["scorer"]
                indice= lt.isPresent(list_anotadores,scorer)
                list_ultimo=lt.newList("ARRAY_LIST")
                ultimo={"date":dat,"home_team":home,"away_team":visitante,"home_score":puntaje_casa,"away_score":puntaje_visi,"minute":tiempo,"penalty":penaless,"own_goals":autogol}
                lt.addLast(list_ultimo,ultimo)
                if indice ==0:
                    torneo_jugador=lt.newList("ARRAY_LIST")
                    lt.addLast(torneo_jugador,tourn)
                    dic={"scorer":scorer,"total_points":puntos,"total_goals":1,"penalty":penales,"own_goal":auto_goles,"avg_time":tiempo,"tournaments":torneo_jugador,
                         "scored_in_wins":victoria,"scored_in_losses":derrota,"scored_in_draws":empate,"last_goal":list_ultimo}
                    lt.addLast(list_anotadores,scorer)
                    lt.addLast(list_result,dic)
                elif indice>0:
                    elemento = lt.getElement(list_result,indice)
                    elemento["total_points"]+=puntos
                    elemento["total_goals"]+=1
                    elemento["penalty"]+=penales
                    elemento["own_goal"]+=auto_goles
                    elemento["avg_time"]+=tiempo
                    torneo_jug=elemento["tournaments"]
                    n=lt.isPresent(torneo_jug,tourn)
                    if n==0:
                        lt.addLast(torneo_jug,tourn)
                        elemento["tournaments"]=torneo_jug
                    elemento["scored_in_wins"]+=victoria
                    elemento["scored_in_losses"]+=derrota
                    elemento["scored_in_draws"]+=empate
                    elemento["last_goal"]=ultimo
    for cada in lt.iterator(list_result):
        goles=cada["total_goals"]
        minutos=cada["avg_time"]
        cada["avg_time"]=minutos/goles
        torneos=cada["tournaments"]
        cada["tournaments"]=dataSize(torneos)
    total_anotadores=dataSize(list_anotadores)
    total_partidos=dataSize(partidos)
    total_torneo=dataSize(torneo)
    total_goles=goles
    total_penal=penal
    total_auto= auto
    return total_anotadores,total_partidos,total_torneo,total_goles,total_penal,total_auto,list_result



def busqueda_binaria_req7(results,fecha,low,high,home,tamano):
    """Esta función se basa en una busqueda binaria modificada la cual se encarga de buscar en una determinada fecha y en sus
       posibles diferentes goles si hubo autogol y penal

    Args:
        scorers (list): lista con la infornmacion del archivo goalscorers
        fecha (str): La fecha del partido que se desea consultar
        low (int): el valor mínimo que puede recorrer en la lista
        high (int): el valor maximo que puede recorrer en la lista
        home (str): El equipo Local
        tamano (int): tamaño de la lista scorers

    Returns:
        Str o Bool: En caso de no encontrar va a retornar el str "unknown" y de lo contrario retorna el valor booleano para penales
        y para autogoles
    """
    oficial=True
    mitad=(low+high)//2
    if low>high:
        return "unknown","unknown"
    elemento = obtener_dato(results,mitad)
    elemen= elemento["date"]
    casa= elemento["home_team"]
    trofeo=elemento["tournament"]
    if elemen ==fecha and home==casa:
        if trofeo=="Friendly":
            oficial =False
        return oficial,trofeo
    elif elemen >fecha:
        high= mitad-1
    else:
        low= mitad+1
    return busqueda_binaria_req7(results,fecha,low,high,home,tamano)

def busqueda_binaria_req7_2(results,fecha,low,high,home,tamano,equipo):
    """Esta función se basa en una busqueda binaria modificada la cual se encarga de buscar en una determinada fecha y en sus
       posibles diferentes goles si hubo autogol y penal

    Args:
        scorers (list): lista con la infornmacion del archivo goalscorers
        fecha (str): La fecha del partido que se desea consultar
        low (int): el valor mínimo que puede recorrer en la lista
        high (int): el valor maximo que puede recorrer en la lista
        home (str): El equipo Local
        tamano (int): tamaño de la lista scorers

    Returns:
        Str o Bool: En caso de no encontrar va a retornar el str "unknown" y de lo contrario retorna el valor booleano para penales
        y para autogoles
    """
    victoria=0
    derrota=0
    empate=0
    mitad=(low+high)//2
    if low>high:
        return "unknown","unknown"
    elemento = obtener_dato(results,mitad)
    elemen= elemento["date"]
    casa=elemento["home_team"]
    marcador_casa= elemento["home_score"]
    marcador_visi=elemento["away_score"]
    visi=elemento["away_team"]
    if elemen ==fecha and home==casa:
        if marcador_casa==marcador_visi:
            empate=1
        elif marcador_casa>marcador_visi:
            if casa==equipo:
                victoria=1
            else:
                derrota=1
        elif marcador_visi>marcador_casa:
            if visi==equipo:
                victoria=1
            else:
                derrota=1
        return marcador_casa,marcador_visi,victoria,derrota,empate
    elif elemen >fecha:
        high= mitad-1
    else:
        low= mitad+1
    return busqueda_binaria_req7_2(results,fecha,low,high,home,tamano,equipo)
            
                   
def sortingReq7(dato1, dato2):

    """

    Args:
        dato1 (_type_): Primer dato a comparar
        dato2 (_type_): Segundo dato a comparar
    """
    if dato1['total_points']> dato2['total_points']:
        return True
    elif dato1['total_points']== dato2['total_points']:
        if dato1['total_goals']>dato2['total_goals']:
            return True
        elif dato1['total_goals']==dato2['total_goals']:
            if dato1['avg_time']<dato2['avg_time']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compareReq4(objeto1, objeto2):
    """
    criterio de ordenamiento para ordenar 
    por 3 parametros (date, country, city).

    Args:
        objeto1 (_type_): partido con resultados
        objeto2 (_type_): partido con resultados

    Returns:
        Boolean: un booleano dependiendo 
        de los criterios evaluados
    """
    if objeto1["date"] > objeto2["date"]:
        return True
    elif objeto1["date"] < objeto2["date"]:
        return False
    else:
        if objeto1["country"] < objeto2["country"]:
            return True
        elif objeto1["country"] > objeto2["country"]:
            return False
        else:
            return objeto1["city"] < objeto2["city"]
        
def sort_criterioreq3(data_1, data_2):
    """sortCriteriareq3 criterio de ordenamiento para el requerimiento 3

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        Bool: Retorna un booleano segun el criterio evaluado 
    """
    if (float(data_1["date"].replace("-","")) < float(data_2["date"].replace("-",""))):
        return True
    elif (float(data_1["date"].replace("-","")) == float(data_2["date"].replace("-",""))):
        if data_1["home_team"] < data_2["home_team"]:
            return True
        elif data_1["home_team"] == data_2["home_team"]:
            if (data_1["team"]) < (data_2["team"]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
        


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento de mayor a menor para las funciones de ordenamiento 

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        el criterio que es sde mayor a menor 
    """
    return (float(data_1["date"].replace("-","")) > float(data_2["date"].replace("-","")))

def sort_crit_menor(data_1, data_2):
    """sortCriteria criterio de ordenamiento de menor a mayor para las funciones de ordenamiento 

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        el criterio que es de menor a mayor  
    """
    return (float(data_1["date"].replace("-","")) < float(data_2["date"].replace("-","")))

def sort_goalscrit(data_1, data_2):
    """Esta duncion da el criterio de ordenamiento para el el archivo de goalscorers

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        Bool: Retorna un booleano segun el criterio evaluado 
    """
    if float(data_1["date"].replace("-","")) < float(data_2["date"].replace("-","")):
        return True
    elif float(data_1["date"].replace("-","")) == float(data_2["date"].replace("-","")):
        if (data_1["minute"]) < (data_2["minute"]):
            return True
        else:
            return False
    else:
        return False
def sort_goalscrit5(data_1, data_2):
    """Esta duncion da el criterio de ordenamiento para el el archivo de goalscorers

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        Bool: Retorna un booleano segun el criterio evaluado 
    """
    if float(data_1["date"].replace("-","")) > float(data_2["date"].replace("-","")):
        return True
    elif float(data_1["date"].replace("-","")) == float(data_2["date"].replace("-","")):
        if (data_1["minute"]) < (data_2["minute"]):
            return True
        else:
            return False
    else:
        return False
def comparacionresreq6(dato1,dato2):
    """Esta duncion da el criterio de ordenamiento para el requerimiento 6 con los jugadore

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        Bool: Retorna un booleano segun el criterio evaluado 
    """
    if dato1["goals"]>dato2["goals"]:
        return True
    elif  dato1["goals"]==dato2["goals"]:
        if  dataSize(dato1["matches"])<(dataSize(dato2["matches"])):
            return True
        elif  dataSize(dato1["matches"])==(dataSize(dato2["matches"])):
            if  dato1["avg_time"]<dato2["avg_time"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def comparacionreq6(dato1,dato2):
    """Esta duncion da el criterio de ordenamiento para el resultado del requerimiento 6

    Args:
        data1 (_type_): primer dato a comparar
        data2 (_type_): Segundo dato a comparar

    Returns:
        Bool: Retorna un booleano segun el criterio evaluado 
    """
    if dato1["total_points"]>dato2["total_points"]:
        return True
    elif dato1["total_points"]==dato2["total_points"]:
        if dato1["goal_difference"]>dato2["goal_difference"]:
            return True
        elif dato1["goal_difference"]==dato2["goal_difference"]:
            if dato1["penalty_points"]>dato2["penalty_points"]:
                return True
            elif dato1["penalty_points"]==dato2["penalty_points"]:
                if dato1["matches"]<dato2["matches"]:
                    return True
                elif dato1["matches"]==dato2["matches"]:
                    if dato1["own_goal_points"]<dato2["own_goal_points"]:
                        return True
                    else:
                        False
                else:
                    False
            else:
                False
        else:
            False
    else:
        return False
        
    #TODO: Crear función comparadora para ordenar
    

def cmp_partidos_by_fecha_y_pais (resultado1,resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelva falso (False).
    Args:
         Resultado1: información del primer registro de resultados FIFA que incluye
                     “date” y el “country”
         impuesto2: información del segundo registro de resultados FIFA que incluye
                    “date"
    """
    if float(resultado1["date"].replace("-","")) == float(resultado2["date"].replace("-","")):
        if resultado1["country"].lower()< resultado2["country"].lower():
            return True
        else:
            return False
    elif float(resultado1["date"].replace("-","")) > float(resultado2["date"].replace("-","")):
        return True
    else:
        return False
# Funciones de ordenamiento

def sublist(lista,inicio,numero):
    lista = lt.subList(lista,inicio,numero)
    return lista
def insertion(lista, comparacion):
    return ins.sort(lista,comparacion)
    
def shell(lista, comparacion):
    return sa.sort(lista, comparacion)

def selection(lista, comparacion):
    return se.sort(lista, comparacion)
"""
    =================================================================================
    FUNCIONES ADICIONALES PARA EL MANEJO DE DATOS CON MÁS FACILIDAD
    =================================================================================
    """
    
def strToDate(stringDate):
    """_summary_

    Args:
        stringDate (_str_): el string tiene que estar de la forma: "YYYY-mm-dd" 
    """
    return datetime.strptime(stringDate, '%Y-%m-%d').date()