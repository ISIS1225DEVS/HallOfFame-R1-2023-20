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


def new_data_structs():

    catalogo = {'resultados': None,
               'goleadores': None,
               'penales': None}
    catalogo['resultados'] = lt.newList("ARRAY_LIST")
    catalogo['goleadores'] = lt.newList("ARRAY_LIST")
    catalogo['penales'] = lt.newList("ARRAY_LIST")



    #TODO: Inicializar las estructuras de datos
    return catalogo

# Funciones para agregar informacion al modelo

    
    
def add_resultados(catalogo,resultado):
    lt.addLast(catalogo["resultados"], resultado)
def add_goleadores(catalogo,goleador):
    lt.addLast(catalogo["goleadores"], goleador)
def add_penales(catalogo,penal):
    lt.addLast(catalogo["penales"], penal)

def Size(catalog):
    # TODO Mods de Est-3 en el Lab 2
    return lt.size(catalog)


    

    

    #TODO: Crear la función para agregar elementos a una lista



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


def data_size(catalog):


    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(catalog)


def req_1(catalog,n,condicion,equipo):
    sublista=lt.newList("ARRAY_LIST") #Creo sublista para poder modificar los datos sin riesgo
    if condicion=="indiferente": #Se revisa que condicion quiere encontrar el usuario y a partir de esto se filtra
        for i in lt.iterator(catalog):
            if i["home_team"]==equipo or i["away_team"]==equipo:
                lt.addLast(sublista,i)
    elif condicion=="local":
        for i in lt.iterator(catalog):
            if i["home_team"]==equipo:
                lt.addLast(sublista,i)
    else:
        for i in lt.iterator(catalog):
            if i["away_team"]==equipo:
                lt.addLast(sublista,i)
    sublista=merg.sort(sublista,cmp_req_1) #Se organizan los datos del mas reciente al mas viejo
    tamano=data_size(sublista) 
    if tamano< n:
        n=tamano
    
    sublista=lt.subList(sublista,1,n)#Se hace una sublista con la cantidad de datos requeridos
    return sublista,tamano
    
def cmp_req_1(dato1,dato2):
        fecha1=dato1["date"]
        fecha2=dato2["date"]
        if fecha1>fecha2:
            return 1
        elif fecha1<=fecha2:
             return 0
                
            

def req_2(catalog,ngoles,jugador):
    sublista=lt.newList("ARRAY_LIST")
    for i in lt.iterator(catalog):
        if i["scorer"]==jugador:
            lt.addLast(sublista,i)
    sublista=merg.sort(sublista,cmp_req_2) #Se organizan los datos del mas reciente al mas viejo con los minutos
    tamano=data_size(sublista) 
    if tamano< ngoles:
        ngoles=tamano
    sublista=lt.subList(sublista,1,ngoles)#Se hace una sublista con la cantidad de datos requeridos
    return sublista,tamano  

def cmp_req_2(dato1,dato2):
        fecha1=dato1["date"]
        fecha2=dato2["date"]
        if fecha1>fecha2:
            cambiar= 0
        elif fecha1<=fecha2:
             cambiar= 1
        else:
            if dato1["minute"]=="desconocido" or dato1["minute"]=="":
                dato1["minute"]=10000
                minutos1=10000
            else:
                minutos1=dato1["minute"]
            if dato2["minute"]=="desconocido" or dato2["minute"]=="":
                dato2["minute"]=10000
                minutos2=dato2["minute"]
            else:
                minutos2=dato2["minute"]
        
            if minutos1>minutos2:
                cambiar= 1
            elif  minutos1<minutos2:
                cambiar= 0
        return cambiar
                    

def req_3(catalog,equipo,old,new):
    sublista=lt.newList("ARRAY_LIST")
    visitantes=0
    locales=0
    goles=lt.newList("ARRAY_LIST")

    for goleador in lt.iterator(catalog["goleadores"]):
        if (goleador["home_team"]==equipo) or (goleador["away_team"]==equipo):
            lt.addLast(goles,goleador)
    goles=merg.sort(goles,cmp_req_3)  
    cantidadgoles= data_size(goles)
            
    for partido in lt.iterator(catalog["resultados"]):
        if partido["home_team"]==equipo:
            if (old<=partido["date"] and partido["date"]<=new):
                datoengoles=mascara_binaria(goles, 0,cantidadgoles, partido["date"])
                if datoengoles<0:
                    partido["penalty"]="Desconocido"
                    partido["own_goal"]="Desconocido"
                else: 
                    gol=lt.getElement(goles,datoengoles)
                    partido["penalty"]=gol["penalty"]
                    partido["own_goal"]=gol["own_goal"]
                locales+=1
                lt.addLast(sublista,partido)
        elif partido["away_team"]==equipo:
            if (old<=partido["date"] and partido["date"]<=new):
                datoengoles=mascara_binaria(goles, 0,cantidadgoles, partido["date"])
                if datoengoles<0:
                    partido["penalty"]="Desconocido"
                    partido["own_goal"]="Desconocido"
                else: 
                    gol=lt.getElement(goles,datoengoles)
                    partido["penalty"]=gol["penalty"]
                    partido["own_goal"]=gol["own_goal"]
                visitantes+=1
                lt.addLast(sublista,partido)
    sublista=merg.sort(sublista,cmp_req_3)
    total=locales+visitantes
    return sublista,total,visitantes,locales
def cmp_req_3(dato1,dato2):
        fecha1=dato1["date"]
        fecha2=dato2["date"]
        if fecha1>fecha2:
            return 0
        elif fecha1<=fecha2:
             return 1
def mascara_binaria(catalog, low, high, fecha):
    dato=binary_search(catalog, low, high, fecha)
    return dato
def binary_search(catalog, low, high, fecha):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
        valor=lt.getElement(catalog,mid)
 
        # If element is present at the middle itself
        if valor["date"]==fecha:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif valor["date"]< fecha:
            return binary_search(catalog, low, mid - 1, fecha)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(catalog, mid + 1, high, fecha)
 
    else:
        # Element is not present in the array
        return -1
    
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(catalog,torneo,old,new):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    sublista = lt.newList('ARRAY_LIST')
    paises = lt.newList('ARRAY_LIST')
    ciudades = lt.newList('ARRAY_LIST')
    partEsp = lt.newList('ARRAY_LIST') #partidos del torneo con datos especificos 
    penaltis = 0
    partCpen = lt.newList('ARRAY_LIST')
    partCpenw = lt.newList('ARRAY_LIST')
    partidosTorn = lt.newList('ARRAY_LIST')
    
    for partido in lt.iterator(catalog['resultados']):
        if (partido['tournament'] == torneo) and ((old<=partido["date"] and partido["date"]<=new)):
            lt.addLast(partidosTorn,partido)
            if lt.isPresent(paises,partido['country'])==0:
                lt.addLast(paises,partido['country'])
            if lt.isPresent(ciudades,partido['city'])==0:
                lt.addLast(ciudades,partido['city'])
            addMatch = [partido['date'],partido['away_team'],partido['home_team']]
            lt.addLast(partEsp,addMatch)
    
    for penal in lt.iterator(catalog['penales']):
        dicComp = [penal['date'],penal['away_team'],penal['home_team']]
        pos = lt.isPresent(partEsp,dicComp)
        if pos!=0:
            lt.addLast(partCpen,dicComp)
            dicCompw = penal['winner']
            lt.addLast(partCpenw,dicCompw)
            
    for i in range(0,data_size(partEsp)):
        partido = lt.getElement(partEsp,i)
        partidoReal = lt.getElement(partidosTorn,i)
        pos = lt.isPresent(partCpen,partido)
        if pos!=0:
            partidoReal['winner']=lt.getElement(partCpenw,pos)
            penaltis += 1
        else:
            partidoReal['winner']='Desconocido'
        
        lt.addLast(sublista,partidoReal)
        
    totPart = data_size(partidosTorn)
    totPais=lt.size(paises)
    totCit=lt.size(ciudades)
    sublista = merg.sort(sublista,cmp_req_4)
    return totPart, totPais, totCit, penaltis, sublista
    
def cmp_req_4(dato1,dato2):
    fecha1=dato1["date"]
    fecha2=dato2["date"]
    if fecha1>fecha2:
        cambiar= 1
    elif fecha1<fecha2:
         cambiar= 0
    else:
        pais1 = dato1['country']
        pais2 = dato2['country']
        if pais1>pais2:
            cambiar= 1
        elif pais1<pais2:
            cambiar= 0
        else:
            cit1 = dato1['city']
            cit2 = dato2['city']
            if cit1>cit2:
                cambiar= 1
            elif cit1<=cit2:
                cambiar= 0
    return cambiar
def req_5(catalog,jugador, finicial, ffinal):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    partidos = catalog.get("results", [])
    anotaciones = catalog.get("goalscorers", [])

    anotaciones_jugador = []
    anotaciones1 = 0

    for anotacion in anotaciones:
        if anotacion["scorer"].lower() == jugador and finicial <= anotacion["date"] <= ffinal:
            anotaciones_jugador.append(anotacion)
            anotaciones1 += 1

    torneos_anotados = set()
    penales1 = 0
    autogoles1 = 0

    for anotacion_filtrada in anotaciones_jugador:
        for partido_filtrado in partidos:
            if all(anotacion_filtrada[key] == partido_filtrado[key] for key in ["date", "home team", "away team"]):
                anotacion_filtrada["tournament"] = partido_filtrado["tournament"]
                anotacion_filtrada["home_score"] = partido_filtrado["home_score"]
                anotacion_filtrada["away_score"] = partido_filtrado["away_score"]

                if anotacion_filtrada["penalty"] == "True":
                    i_penales += 1

                if anotacion_filtrada["own_goal"] == "True":
                    i_autogoles += 1

                torneos_anotados.add(partido_filtrado["tournament"])

    torneos1 = len(torneos_anotados)

    return anotaciones1, torneos1, penales1, autogoles1, anotaciones_jugador

#FUNCION 2 REQ 5
"""def req_5(jugador,finicial,ffinal,data):
    
    Función que soluciona el requerimiento 5
    
    # TODO: Realizar el requerimiento 5
    partidos = data.get("results", [])
    anotaciones = data.get("goalscorers", [])

    anotaciones_jugador = []
    i_anotaciones = 0

    for anotacion in anotaciones:
        if anotacion["scorer"].lower() == jugador and finicial <= anotacion["date"] <= ffinal:
            anotaciones_jugador.append(anotacion)
            i_anotaciones += 1

    torneos_anotados = set()
    i_penales = 0
    i_autogoles = 0

    for anotacion_filtrada in anotaciones_jugador:
        for partido_filtrado in partidos:
            if all(anotacion_filtrada[key] == partido_filtrado[key] for key in ["date", "home team", "away team"]):
                anotacion_filtrada["tournament"] = partido_filtrado["tournament"]
                anotacion_filtrada["home_score"] = partido_filtrado["home_score"]
                anotacion_filtrada["away_score"] = partido_filtrado["away_score"]

                if anotacion_filtrada["penalty"] == "True":
                    i_penales += 1

                if anotacion_filtrada["own_goal"] == "True":
                    i_autogoles += 1

                torneos_anotados.add(partido_filtrado["tournament"])

    i_torneos = len(torneos_anotados)

    return i_anotaciones, i_torneos, i_penales, i_autogoles, anotaciones_jugador"""

def req_6(torneo,old,new,nequipos,catalog):
    ciudades=lt.newList("ARRAY_LIST") #Contiene el las ciudades y la cantidad de partidos jugador en cada una
    partidos=lt.newList("ARRAY_LIST") #Partidos jugando en el torneo y el periodo de tiempo
    equipos=lt.newList("ARRAY_LIST") #Nombre de los equipos en el torneo
    jugadores=lt.newList("ARRAY_LIST") #Nombre de todos los jugadores que participaron en el torneo
    paises=lt.newList("ARRAY_LIST") #Paises donde se jugo el torneo 
    lista=lt.newList("ARRAY_LIST") #Lista  a devolver con todo lo que pedido por el req
    datosjugadores=lt.newList("ARRAY_LIST")   #Datos de los jugadores, equipo,goles, partidos y minutos.
    ciudadescan=0 #Cantidad de ciudades donde se jugaron partidos
    ciudadesnombres=lt.newList("ARRAY_LIST") #Solo guarda el nombre de las ciudades
    paisescan=0#Cantidad de ciudades donde se jugaron partidos
    cantidadpartidos=data_size(catalog["resultados"]) 
    cantidadgoleadores=data_size(catalog["goleadores"])
    cantidadpenales=data_size(catalog["penales"])
    mayor = max(cantidadpartidos, cantidadgoleadores, cantidadpenales)
    for indice in range(0,mayor):
        if indice<=cantidadpartidos:
            partido=lt.getElement(catalog["resultados"],indice)
            if (old<=partido["date"] and new>=partido["date"] )and partido["tournament"]==torneo: 
            #Revisa que el partido haga parte de los datos que nos interesan
                if lt.isPresent(ciudadesnombres,partido["city"])==0:
                    '''Si la ciudad donde se jugo no habia sido registrada agrega el nombre a la lista de nombres de ciudades y luego 
                    la agrega a los datos de ciudades en ciudades con un valor de 1 representado que es el primer partido encontrado 
                    en esa ciudad'''
                    ciudadescan+=1
                    dicciudad={partido["city"]:1}
                    lt.addLast(ciudadesnombres,partido["city"])
                    lt.addLast(ciudades,dicciudad)
                else:
                    '''Agrega un partido mas al dic del nombre de la ciudad en ciudades, para esto usa el indice del nombre de la ciudad
                    guardo en nombre ciudades ya que estas dos listas comparten el mismo nombre'''
                    posicion=lt.isPresent(ciudadesnombres,partido["city"])
                    (lt.getElement(ciudades,posicion))[partido["city"]]+=1
                if lt.isPresent(paises,partido["country"])==0:
                #Hace lo mismo que con las ciudades pero con paises
                    paisescan+=1
                    lt.addLast(paises,partido["country"])
                agregarpartido=[partido["date"],partido["away_team"],partido["home_team"]]
                '''Guarda los datos fundamentales para luego buscar ese mismo partido en jugadores'''
                lt.addLast(partidos,agregarpartido)
                '''AQUI COMIENZA A ANALISAR LOS EQUIPOS DEL PARTIDO, PRIMERO LOCAL Y LUEGO VISITANTE'''
                if lt.isEmpty(equipos)==True:
                    dic=obtener_datos_partido_nuevo(partido,"home_team")
                    lt.addLast(equipos,partido["home_team"])
                    lt.addLast(lista,dic) #Adiciona los datos del equipo a la lista a retornar
                elif lt.isPresent(equipos,partido["home_team"])==0:
                    dic=obtener_datos_partido_nuevo(partido,"home_team")
                    lt.addLast(equipos,partido["home_team"])
                    lt.addLast(lista,dic)
                else: 
                    posicion=lt.isPresent(equipos,partido["home_team"]) 
                    #Si esta presente, busca la posicion donde estan los datos de equipo, esto lo hace con la lista de nombres de equipos
                    #que tiene el mismo orden que la lista a retornar
                    agregar_datos_equipo(lt.getElement(lista,posicion),partido,"home_team")
                    
                    
                 #Realiza lo mismo que hizo antes pero con el equipo visitante   
                if lt.isPresent(equipos,partido["away_team"])==0:

                    dic=obtener_datos_partido_nuevo(partido,"away_team")
                    lt.addLast(equipos,partido["away_team"])
                    lt.addLast(lista,dic)
                else:
                    posicion=lt.isPresent(equipos,partido["away_team"])
                    agregar_datos_equipo(lt.getElement(lista,posicion),partido,"away_team")
    #Con los partidos del torneo y los datos de goleadores, comienza a organizar los datos de los goleadores      
    cantidadpartidos=data_size(partidos)
    mayor=max(cantidadgoleadores,cantidadpartidos)
    for indice in range(0,mayor):
        jugador=lt.getElement(catalog["goleadores"],indice)
        diccomparar=[jugador["date"],jugador["away_team"],jugador["home_team"]] 
        #Con esto se revisa que el partido si sea parte del torneo usando la lista de partidos
        if lt.isPresent(partidos,diccomparar)!=0:
            #Ya sabiendo que el partido si es parte del torneo, se agregan los datos del jugador al la lista datosjugadores y 
            # se guarda su nombre en jugadores, estas dos lista comparten que el jugador y su datos estan en la misma posicion 
            #a pesar de ser diferentes listas
                if lt.isPresent(jugadores,jugador["scorer"])==0:
                    jugadordic={"team":jugador["team"],"goles":1,"partidos":lt.newList("ARRAY_LIST")
                                ,"minutos":jugador["minute"]}
                    if jugador["penalty"]==True:
                        jugadordic["penalty"]=1
                    else:
                        jugadordic["penalty"]=0
                    if jugador["own_goal"]==True:
                        jugadordic["own_goal"]=1
                    else:
                        jugadordic["own_goal"]=0
                        
                        
                    lt.addLast(jugadordic["partidos"],jugador["date"])
                    lt.addLast(datosjugadores,{jugador["scorer"]:jugadordic})
                    lt.addLast(jugadores,jugador["scorer"])
                else:
                    #Si ya existe el jugador en los datos, se agregan los datos del partidos a las estadisticas, se usa
                    #el indice de la lista de nombres para saber donde estan sus datos en la lista datosjugadores
                    jugadoraddicionar=lt.isPresent(jugadores,jugador["scorer"])
                    dic=lt.getElement(datosjugadores,jugadoraddicionar)[jugador["scorer"]]
                    dic["goles"]=dic["goles"]+1
                    #Se revisa que este partido no este registrado, si no se agrega el partido a la lista de partidos donde mete gol
                    if lt.isPresent(dic["partidos"],jugador["date"])==0:
                        lt.addLast(dic["partidos"],jugador["date"])
                    dic["minutos"]=dic["minutos"]+jugador["minute"]#Se van sumando los minutos donde mete gol, para luego sacar el promedio
                    if jugador["penalty"]==True:
                        dic["penalty"]+=1
                    if jugador["own_goal"]==True:
                         dic["own_goal"]+=1
                    datosjugadores[jugadoraddicionar]=dic
                    lt.getElement(datosjugadores,jugadoraddicionar)[jugador["scorer"]]= dic
    lista=maximos_goleadores(equipos,datosjugadores,lista,jugadores)
    quk.sort(lista,cmp_resultados_req6)
    lista=lt.subList(lista,1,nequipos)
    cantidadpartidos=data_size(partidos)
    ciudadmasjugada= ciudad_mas_jugada(ciudades,ciudadesnombres)
    return lista,cantidadpartidos,ciudadescan,paisescan,ciudadmasjugada

def   ciudad_mas_jugada(ciudades,ciudadesnombres):
    i=1
    maxciudad=0
    aparaciones=0
    for ciudad in lt.iterator(ciudades):
        nombre=lt.getElement(ciudadesnombres,i)
        i+=1
        if aparaciones<ciudad[nombre]:
            maxciudad=nombre
            aparaciones=ciudad[nombre]
    return maxciudad
def obtener_datos_partido_nuevo(partido,team):
    if team=="away_team": 
#Si se esta analizando el equipo visitante, se debe tener encuenta eso para saber los goles a favor y encontra.
        golesfav=partido["away_score"]
        golescontra=partido["home_score"]
        diferenciagol=golesfav-golescontra
    else:
        golesfav=partido["home_score"]
        golescontra=partido["away_score"]
        diferenciagol=golesfav-golescontra    
    if golescontra<golesfav:
        win=1
        loses=0
        draw=0
        puntos=3
    elif golescontra>golesfav:
        win=0
        loses=1
        draw=0
        puntos=0
    else:
        win=0
        loses=0
        draw=1
        puntos=1
#El diccionario con todo lo que pide el req, goleador se configura luego.
    dic={"team":partido[team],"puntos":puntos,"partidos":1,"gol_for":golesfav,"gol_against":golescontra,"wins":win,
         "loses": loses,"draw":draw,"diferencia_gol":diferenciagol,"partidos":1,"goleador":0,"penales":0,"auto_gol":0}
    return dic 
def agregar_datos_equipo(antiguo,partido,team):
    antiguo["partidos"]+=1 #Le agrega un partido al equipo
    #Tambien revisa la condicion del equipo para saber como manejar el resto de datos
    if team=="away_team":
        golesequipo="away_score"
        golescontra="home_score"
        antiguo["gol_for"]=antiguo["gol_for"]+partido["away_score"] 
        #Le suma los goles del partido a lo ya guardos, hace lo mismo con la diferencia y lo encontra
        antiguo["gol_against"]=antiguo["gol_against"]+partido["home_score"]
        antiguo["diferencia_gol"]= antiguo["gol_for"]-antiguo["gol_against"]
    else:
        golesequipo="home_score"
        golescontra="away_score"
        antiguo["gol_for"]=antiguo["gol_for"]+partido["home_score"]
        antiguo["gol_against"]=antiguo["gol_against"]+partido["away_score"]
        antiguo["diferencia_gol"]= antiguo["gol_for"]-antiguo["gol_against"]
        
    #Revisa quien gano:agrega victoria, empate  o derrota 
    #y dependinedo de eso le suma puntos a los que ya habia cargado  
    if partido[golescontra]<partido[golesequipo]:
        antiguo["wins"]+=1
        antiguo["puntos"]+=3
    elif partido[golescontra]>partido[golesequipo]:
        antiguo["loses"]+=1
    else:
        antiguo["draw"]+=1
        antiguo["puntos"]+=1

def maximos_goleadores(equipos,datajugadores,lista,jugadores):
    i=1
    for jugador in lt.iterator(datajugadores):
        #Como los datos del jugador estan guardados en su nombre, se ingresa primero al dato en datajugadores 
        #y para ver las estadisticas del jugador se ingresa con su nombre
        nombre=lt.getElement(jugadores,i)
        estadisticas=jugador[nombre]
        i+=1
        indice=lt.isPresent(equipos,estadisticas["team"])
        #Se busca el equipo de jugador en la lista con todos los datos del equipo
        equipo=lt.getElement(lista,indice)
        if estadisticas["penalty"]==True:
            equipo["penales"]=1+equipo["penales"]
        if estadisticas['own_goal']==True:
            equipo['auto_gol']=1+equipo['auto_gol']
        if equipo["goleador"]==0: #Se revisa si hay otro jugador ya guardado como goleador del equipo, si no , se guarda ese jugador
            esta={}
            esta['goles']=estadisticas["goles"]
            esta["partidos"]=data_size(estadisticas["partidos"]) #Se guarda la cantidad de partidos donde marco gol el jugador
            esta["average_min"]=estadisticas["minutos"]/esta["partidos"] 
            #Se saca el promedio de minutos porque estadisticas["minutos"] es la suma de todos los minutos donde marco 
            # #y esta["partidos"] es la cantidad de partidos que jugo"
            esta["goleador"]=nombre
            equipo["goleador"]=esta
            lt.changeInfo(lista,indice,equipo) #Finalmente se actualiza la informacion del equipo con su goleador
        else:
            goleador=equipo["goleador"] 
            if goleador["goles"]<estadisticas["goles"]:
    #Si el equipo ya tiene un jugador como goleador, se compara el nuevo jugador con el anterior guardado para ver quien tiene mas goles
                esta={}
                esta['goles']=estadisticas["goles"]
                esta["partidos"]=data_size(estadisticas["partidos"])
                esta["average_min"]=estadisticas["minutos"]/esta["partidos"]
                esta["goleador"]=nombre
                equipo["goleador"]=esta
                lt.changeInfo(lista,indice,equipo)
            
    return lista

"""
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6


def cmp_resultados_req6(dato1,dato2):
        punto1=dato1["puntos"]
        punto2=dato2["puntos"]
        if punto1>punto2:
            return 1
        elif punto2>punto1:
            return 0
        else:
            diferenciagoles1=dato1["diferencia_gol"]
            diferenciagoles2=dato2["diferencia_gol"]
            if diferenciagoles1>diferenciagoles2:
                return 1
            elif diferenciagoles1<diferenciagoles2:
                return 0
            else:
                punto1=dato1["penales"]
                punto2=dato2["penales"]
                if punto1>punto2:
                    return 1
                elif punto2>punto1:
                    return 0
                else:
                    punto1=dato1["partidos"]
                    punto2=dato2["partidos"]
                    if punto1>punto2:
                        return 1
                    elif punto2>punto1:
                        return 0
                    else:
                        punto1=dato1["auto_gol"]
                        punto2=dato2["auto_gol"]
                        if punto1<punto2:
                            return 1
                        elif punto2<=punto1:
                            return 0
                        
            


def req_7(old,new,nequipos,catalog):
    partidosbuscar,goleadores,torneos,partidosfiltrados=filtrarpartidos(catalog,old,new)
    jugadores=lt.newList("ARRAY_LIST")
    jugadoresdata=lt.newList("ARRAY_LIST")
    torneos_cada_jugador=lt.newList("ARRAY_LIST")
    totalgoles=data_size(goleadores)
    totalauto=0
    totalpenale=0
    for jugador in lt.iterator(goleadores):
        diccomparar=[jugador["date"],jugador["away_team"],jugador["home_team"]] 
        #Con esto se revisa que el partido si sea parte del torneo usando la lista de partidos
        posicionpartido=lt.isPresent(partidosbuscar,diccomparar)
        if posicionpartido!=0:
            partido=lt.getElement(partidosfiltrados,posicionpartido)
            if lt.isPresent(jugadores,jugador["scorer"])==0:
                agregar={"scorer":jugador["scorer"],"goles":1,'own_goal':0,'penalty':0,"ultimo_gol":0,"score_wins":0
                         ,"score_lose":0,"score_draft":0,"total_tournaments":1}
                
               
                
                if jugador["own_goal"]==True:
                    agregar["own_goal"]=1
                    totalauto+=1
                if jugador["penalty"]==True:
                    agregar["penalty"]=1
                    totalpenale+=1
                agregar["puntaje"]=agregar["penalty"]+agregar["goles"]-agregar["own_goal"]
                agregar["ultimo_gol"]=obtenerultimogol_new(partido,jugador)
                agregar["avg_time"]=jugador["minute"]
                resultado=finalpartido(partido,jugador)
                if resultado==0:
                    agregar["score_draft"]=1
                elif resultado==1:
                    agregar["score_wins"]=1
                else:
                    agregar["score_lose"]=1
                listajugador=lt.newList("ARRAY_LIST")
                lt.addLast(listajugador,partido["tournament"])
                lt.addLast(torneos_cada_jugador,{jugador["scorer"]:listajugador})
                lt.addLast(jugadores,jugador["scorer"])
                lt.addLast(jugadoresdata,agregar)
            else:
                ubicacion=lt.isPresent(jugadores,jugador["scorer"])
                datos=lt.getElement(jugadoresdata,ubicacion)

                partidos=datos["score_wins"]+datos["score_lose"]+datos["score_draft"]
                if jugador["own_goal"]==True:
                    datos["own_goal"]+=1
                    datos["puntaje"]-=1
                    totalauto+=1
                if jugador["penalty"]==True:
                    datos["penalty"]+=1
                    datos["puntaje"]+=1
                    totalpenale+=1
                datos["puntaje"]+=1
                datos["goles"]+=1
                resultado=finalpartido(partido,jugador)
                if resultado==0:
                    datos["score_draft"]+=1
                elif resultado==1:
                    datos["score_wins"]+=1
                else:
                   datos["score_lose"]+=1
                datos["ultimo_gol"]=comparacion_ultimogol_new(partido,jugador,datos)
                datos["avg_time"]=((datos["avg_time"]*partidos)+jugador["minute"])/(datos["score_wins"]+datos["score_lose"]+datos["score_draft"])
                datos["total_tournaments"]+=revisar_torneo(partido,torneos_cada_jugador,jugador,ubicacion)
                lt.changeInfo(jugadoresdata,ubicacion,datos)
    quk.sort(jugadoresdata,cmp_req7)
    cantidadjugadores=data_size(jugadoresdata)
    jugadoresdata=lt.subList(jugadoresdata,1,nequipos)
   
    cantidadpartidos=data_size(partidosfiltrados)
    return jugadoresdata,cantidadjugadores,totalauto,totalpenale,totalgoles,cantidadpartidos

def revisar_torneo(partido,torneos_cada_jugador,jugador,ubicacion):
    
    torneos=lt.getElement(torneos_cada_jugador,ubicacion)[jugador["scorer"]]
    if lt.isPresent(torneos,partido["tournament"])==0:
        lt.addLast(torneos,partido["tournament"])
        lt.getElement(torneos_cada_jugador,ubicacion)[jugador["scorer"]]=torneos
        return 1
    else:
        return 0
        
     
def cmp_req7(dato1,dato2):
    punto1=dato1["puntaje"]
    punto2=dato2["puntaje"]
    if punto1>punto2:
        return 1
    elif punto2>punto1:
        return 0
    else:
        punto1=dato1["goles"]
        punto2=dato2["goles"]
        if punto1>punto2:
            return 1
        elif punto2>punto1:
            return 0
        else:
            punto1=dato1["penalty"]
            punto2=dato2["penalty"]
            if punto1>punto2:
                return 1
            elif punto2>punto1:
                return 0
            else:
                punto1=dato1["own_goal"]
                punto2=dato2["own_goal"]
                if punto1>punto2:
                    return 0
                elif punto2>punto1:
                    return 1
                else:
                    punto1=dato1["avg_time"]
                    punto2=dato2["avg_time"]
                    if punto1>punto2:
                        return 0
                    elif punto2>=punto1:
                        return 1
                
        
      
                
def comparacion_ultimogol_new(partido,jugador,datos):
    if datos["ultimo_gol"]["date"]<jugador["date"]:
        dic={"date":partido["date"],"home_team":partido["home_team"],"away_team":partido["away_team"],
             "home_score":partido["home_score"],"away_score":partido["away_score"],"minute":jugador["minute"],
             "penalty":jugador["penalty"],"own_goal":jugador["own_goal"]}
    else:
        dic=datos['ultimo_gol']
    return dic
                    
                
    
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass
def obtenerultimogol_new(partido,jugador):
        dic={"date":partido["date"],"home_team":partido["home_team"],"away_team":partido["away_team"],
             "score_home":partido["home_score"],"away_score":partido["away_score"],"minute":jugador["minute"],
             "penalty":jugador["penalty"],"own_goal":jugador["own_goal"]}
        return dic
def finalpartido(partido,jugador):
    if partido["home_score"]>partido["away_score"]:
        ganador=partido["home_team"]
    elif partido["home_score"]<partido["away_score"]:
        ganador=partido["away_team"]
    else:
        resultado=0
        return resultado
    if ganador==jugador["team"]:
        resultado=1
    else: resultado=-1
    return resultado 
        
        
    

def filtrarpartidos(catalog,old,new):
    cantidadpartidos=data_size(catalog["resultados"]) 
    cantidadgoleadores=data_size(catalog["goleadores"])
    torneos=lt.newList("ARRAY_LIST") #Guarda los nombres de los torneos sin repetir 
    partidosbuscar=lt.newList("ARRAY_LIST") #Partidos jugado en periodo, con fecha y equipos
    partidosfiltrados=lt.newList("ARRAY_LIST")#Partidos filtrados
    goleadores=lt.newList("ARRAY_LIST") #goleadores en periodo de tiempo
    mayor = max(cantidadpartidos, cantidadgoleadores)
    for indice in range(0,mayor):
        if indice<=cantidadpartidos:
         partido=lt.getElement(catalog["resultados"],indice)
         if (old<=partido["date"] and new>=partido["date"] )and partido["tournament"]!="Friendly":
                agregarpartido=[partido["date"],partido["away_team"],partido["home_team"]]
                '''Guarda los datos fundamentales para luego buscar ese mismo partido en jugadores'''
                lt.addLast(partidosbuscar,agregarpartido) 
                lt.addLast(partidosfiltrados,partido )

                if lt.isPresent(torneos,partido["tournament"])==0:
                    lt.addLast(torneos,partido["tournament"])
        if indice<=cantidadgoleadores:
                goleador=lt.getElement(catalog["goleadores"],indice)   
                if (old<=goleador["date"] and new>=goleador["date"] ):
                    lt.addLast(goleadores,goleador) 
    torneos=data_size(torneos)
    return partidosbuscar,goleadores,torneos,partidosfiltrados
        

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
def lab4(catalog,carga,tipo,sizeresultados):
    copiaparteresultados=lt.subList(catalog["resultados"],0,sizeresultados)
    listaordenar=lt.newList(tipo)
    listaordenar=copiaparteresultados
    listaordenar=sort_resultadosop10(listaordenar,carga)
    return listaordenar
    
def sort_resultadosop10(catalog,carga):
    # A partir del tipo de carga elegido por el usuario se usa un ordenamiento diferente.
    if carga=="Selection": 
        return se.sort(catalog,cmp_resultadosop10)
    elif carga=="Insertion":
        return ins.sort(catalog,cmp_resultadosop10)
    elif carga=="Shell":
        return sa.sort(catalog,cmp_resultadosop10)
    elif carga=="Merge":
        return merg.sort(catalog,cmp_resultadosop10)
    elif carga=="Quick":
        return quk.sort(catalog,cmp_resultadosop10)
        
def cmp_resultadosop10(dato1,dato2):
    fecha1=dato1["date"]
    fecha2=dato2["date"]
    if fecha1>fecha2:
        return 0
    elif fecha1<fecha2:
        return 1
    else:
        goles1_local=dato1["city"]
        goles2_local=dato2["city"]
        if goles1_local>goles2_local:
            return 1
        elif goles1_local<=goles2_local:
            return 0
def sort_resultados_carga(catalog):
    orden_resultados=lt.subList(catalog["resultados"],0,Size(catalog["resultados"]))
    orden_resultados=merg.sort(orden_resultados,cmp_resultados)
    return orden_resultados
def cmp_resultados(dato1,dato2):
    fecha1=dato1["date"]
    fecha2=dato2["date"]
    if fecha1>fecha2:
        return 1
    elif fecha1<fecha2:
        return 0
    else:
        goles1_local=dato1["home_score"]
        goles2_local=dato2["home_score"]
        if goles1_local>goles2_local:
            return 1
        elif goles1_local<goles2_local:
            return 0
        else:
            goles1_vis=dato1["away_score"]
            goles2_vis=dato2["away_score"]
            if goles1_vis>goles2_vis:
                return 1
            elif goles1_vis<=goles2_vis:
                return 0
def sort_penales_carga(catalog):
    orden_penales=lt.subList(catalog["penales"],0,Size(catalog["penales"]))
    orden_penales=merg.sort(orden_penales,cmp_penales)
    return orden_penales

def cmp_penales(dato1,dato2):
    fecha1=dato1["date"], "%Y-%m-%d"
    fecha2=dato2["date"], "%Y-%m-%d"
    if fecha1>fecha2:
        return 1
    elif fecha1<fecha2:
        return 0
    else:
        goles1_local=dato1["home_team"]
        goles2_local=dato2["home_team"]
        if goles1_local>goles2_local:
            return 1
        elif goles1_local<goles2_local:
            return 0
        else:
            goles1_vis=dato1["away_team"]
            goles2_vis=dato2["away_team"]
            if goles1_vis>goles2_vis:
                return 1
            elif goles1_vis<=goles2_vis:
                return 0
def sort_goleadores_carga(catalog):
    orden_goleadores=lt.subList(catalog["goleadores"],0,Size(catalog["goleadores"]))
    orden_goleadores=merg.sort(orden_goleadores,cmp_goleadores)
    return orden_goleadores


def cmp_goleadores(dato1,dato2):
    cambiar=0
    fecha1=dato1["date"]
    fecha2=dato2["date"]
    if fecha1>fecha2:
        cambiar=1
    elif fecha1<fecha2:
        cambiar=0
    else:
        if dato1["minute"]=="desconocido" or dato1["minute"]=="":
            dato1["minute"]=10000
            minutos1=10000
        else:
            minutos1=dato1["minute"]
        if dato2["minute"]=="desconocido" or dato2["minute"]=="":
            dato2["minute"]=10000
            minutos2=dato2["minute"]
        else:
            minutos2=dato2["minute"]
       
        if minutos1>minutos2:
            cambiar= 1
        elif  minutos1<minutos2:
            cambiar= 0
        
        else:
            goliador1=dato1["scorer"]
            goliador2=dato2["scorer"]
            if goliador1>goliador2:
                cambiar= 1
            elif goliador1<=goliador2:
                cambiar= 0
    if dato1["minute"]==10000:
        dato1["minute"]="desconocido"
    elif dato2["minute"]==10000:
        dato2["minute"]="desconocido"
    
    return cambiar
