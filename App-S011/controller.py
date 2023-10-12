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
import DISClib.ADT.list as lt
from DISClib.ADT import list as ls
import model
import time
import csv
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs("ARRAY_LIST")
    return control


# Funciones para la carga de datos

def load_data(control, filegoalscorers, fileresults, fileshootouts):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    x=load_goal_scorers(control['model']['goal_scorers'],filegoalscorers) 
    y=load_results(control['model']['results'],fileresults)
    z=load_shootouts(control['model']['shootouts'], fileshootouts)
    return x,y,z
        
def load_goal_scorers(n_d, filename):
    goals_file = cf.data_dir  +filename
    input_file = csv.DictReader(open(goals_file, encoding='utf-8'))
    for goals in input_file:
        model.addData(n_d, goals)
    
    return model.dataSize(n_d)


        
def load_results(n_d, filename):
    resultsfile = cf.data_dir + filename
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    for results in input_file:
        model.addData(n_d, results)
    return model.dataSize(n_d)


def load_shootouts(n_d, filename):
    shootoutsfile = cf.data_dir  + filename
    input_file = csv.DictReader(open(shootoutsfile, encoding='utf-8'))
    for shootout in input_file:
        model.addData(n_d, shootout)
    return model.dataSize(n_d)


    

# Funciones de ordenamiento

def sorter(control,lis,ordenamiento):
    """
    Ordena los datos del modelo
    """
    lista= control['model'][lis]
    return(model.shell(lista, ordenamiento))
    #TODO: Llamar la función del modelo para ordenar los datos
    


# Funciones de consulta sobre el catálogo

def get_data(control):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un 
    p = control['model']['goal_scorers']
    prim= model.get_data(p)
    s = control['model']['results']
    sec= model.get_data(s)
    t= control['model']['shootouts']
    ter = model.get_data(t)
    return prim, sec, ter
        


def req_1(control,nom,condicion,numero):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    lista=control["model"]["results"]
    resultad=model.req_1(lista,nom,condicion)
    tamano=model.dataSize(resultad)
    orden=model.sort_criteria
    lista= model.shell(resultad,orden)
    resultad=model.sublist(lista,1,numero)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    if numero>6:
        return "Tiene más de seis resultados",model.get_data(resultad),tamano,deltatime
    else:
        return "Tiene menos de seis resultados",resultad,tamano,deltatime


def req_2(control,nombre,numero):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()
    lis='goal_scorers'
    ordenamiento= model.sort_goalscrit
    lista= sorter(control,lis,ordenamiento)
    li=model.req_2(lista,nombre)
    tamano=model.dataSize(li)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    if numero>6 and tamano>6:
        return "Tiene más de seis resultados",model.get_data(li),tamano,deltatime
    else:
        return "Tiene menos de seis resultados",li,tamano,deltatime
    
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control,nombre,f_i,f_f):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    li=control["model"]["results"]
    criterio=model.sort_criterioreq3
    scorers= sorter(control,'goal_scorers',criterio)
    sublista,home,visita=model.req_3(scorers,li,f_i,f_f,nombre)
    ordenamiento= model.sort_crit_menor
    lista= model.shell(sublista,ordenamiento)
    tamano=model.dataSize(sublista)
    home=model.dataSize(model.req_1(sublista, nombre,"local"))
    visita=model.dataSize(model.req_1(sublista, nombre,"visitante"))
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    if  tamano>6:
        return "Tiene más de seis resultados",model.get_data(lista),tamano,home,visita,deltatime
    else:
        return "Tiene menos de seis resultados",lista,tamano,home,visita,deltatime



def req_4(control, nombreTorneo, fechaIni, fechaFin):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
   
    partidosTotales,totalPaises,totalCiudades,totalPenales,listaPartidos =  model.req_4(control, nombreTorneo, fechaIni, fechaFin) #retorna una tupla :D
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
        
    return listaPartidos, partidosTotales, totalPaises, totalCiudades, totalPenales,deltatime
        
        
        


def req_5(control,nombre_jugador, fecha_inicio, fecha_final,):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    resultado,goles,torneo, penaltis, autogoles = model.req_5(control["model"],nombre_jugador,fecha_inicio,fecha_final)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    if goles > 6:
        return "Tiene mas de seis resultados", model.get_data(resultado),goles, torneo, penaltis, autogoles,deltatime
    
    else:
        return "Tiene menos de seis resultados", resultado, goles,torneo, penaltis, autogoles,deltatime


def req_6(control,torneo,f_i,f_f,top):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    criterio=model.sort_criterioreq3
    scorers= sorter(control,'goal_scorers',criterio)
    partidos ,paises,ciudades,c,lista=model.req_4(control,torneo,f_i,f_f)
    equipos,moda,resultado=model.req_6(lista,scorers)
    sublista=model.sublist(resultado,1,top)
    tamano=model.dataSize(sublista)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    if  tamano>6:
        return "Tiene más de seis resultados",model.get_data(sublista),equipos,partidos,paises,ciudades,moda,deltatime
    else:
        return "Tiene menos de seis resultados",sublista,equipos,partidos,paises,ciudades,moda,deltatime
    # TODO: Modificar el requerimiento 6



def req_7(control, fechaIni, fechaFin,top):
    """
    Retorna el resultado del requerimiento 7
    """
    comparacion= model.sortingReq7
    ordenamiento= model.sort_criterioreq3
    orden=model.sort_crit_menor
    scorers=sorter(control,'goal_scorers',ordenamiento)
    result=sorter(control,"results",orden)
    anotadores,partidos,torneos,goles,penales, auto,resultado= model.req7(scorers,fechaIni,fechaFin,result)
    resultado=model.shell(resultado,comparacion)
    resultado= model.sublist(resultado,1,top)
    if  anotadores>6:
        return "Tiene más de seis resultados",model.get_data(resultado),anotadores,partidos,torneos,goles,penales, auto
    else:
        return "Tiene menos de seis resultados",resultado,anotadores,partidos,torneos,goles,penales, auto
    # TODO: Modificar el requerimiento 7
                        

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
def sublista(control,numero):
    x = control['model']['results']
    size = int(model.dataSize(x))
    if numero <= size: 
        return model.sublist(x,numero)
    else:
        return 1

def sort (lista, ordenamiento):
    comparacion = model.cmp_partidos_by_fecha_y_pais
    start_time= 0
    end_time= 0

    if ordenamiento == 1:
        start_time= get_time()
        model.insertion(lista,comparacion)
        end_time= get_time()
    
    elif ordenamiento == 2:
        start_time= get_time()
        print(model.shell(lista, comparacion))
        end_time= get_time()
    else:
        start_time= get_time()
        model.selection(lista, comparacion)
        end_time= get_time()
    d_time= delta_time(start_time,end_time)
    return d_time