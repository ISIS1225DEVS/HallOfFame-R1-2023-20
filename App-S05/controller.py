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
 """

import config as cf
import model
import time
import datetime
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    modelo={"model":None}

    modelo["model"]=model.new_data_structs()

    #TODO: Llamar la función del modelo que crea las estructuras de datos
    return modelo
def cargarresultados(catalog,archivo):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """

    archivo = cf.data_dir + 'football/results-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'))
    for resultado in input_file:
        resultado['date']=datetime.datetime.strptime(resultado["date"], "%Y-%m-%d").date()
        resultado['home_score']=int(resultado['home_score'])
        resultado['away_score']=int(resultado['away_score'])
        resultado.pop("neutral")
        model.add_resultados(catalog, resultado)
    sizeresultados = model.Size(catalog["resultados"])
    return sizeresultados

    


def cargarpenaltis(catalog,archivo):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    archivo = cf.data_dir + 'football/shootouts-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'))
    for penal in input_file:
        penal['date']=datetime.datetime.strptime(penal["date"], "%Y-%m-%d").date()
        model.add_penales(catalog, penal)
    sizepenales = model.Size(catalog["penales"])
    return sizepenales
def cargargoleadores(catalog,archivo):
    """
    Carga la información que asocia tags con libros.
    """
    archivo = cf.data_dir + "football/goalscorers-utf8-"+archivo+".csv"
    input_file = csv.DictReader(open(archivo, encoding='utf-8'))
    for goleadores in input_file:
        goleadores['date']=datetime.datetime.strptime(goleadores["date"], "%Y-%m-%d").date()
        if goleadores['minute']=="":
            goleadores['minute']=="desconocido"
        else:
            goleadores['minute']=float((goleadores['minute']))
            
        if  goleadores['own_goal']=='':
            goleadores['own_goal']="desconocido"
        else:
            goleadores['own_goal']=((goleadores['own_goal']).lower()=="true")
        if  goleadores['penalty']=='':
            goleadores['penalty']="desconocido"
        else:
            goleadores['penalty']=(goleadores['penalty'].lower()=="true")
        model.add_goleadores(catalog, goleadores)
    sizegoleadores = model.Size(catalog["goleadores"])       
    return sizegoleadores


# Funciones para la carga de datos

def load_data(modelo,archivo):
     catalog = modelo['model']
     sizeresultados=cargarresultados(catalog,archivo)
     resultados_sorted=model.sort_resultados_carga(catalog)
     sizepenales=cargarpenaltis(catalog,archivo)
     penales_sorted=model.sort_penales_carga(catalog)
     sizegoleadores=cargargoleadores(catalog,archivo)
     goleadores_sorted=model.sort_goleadores_carga(catalog)
     sizetotal=sizeresultados+sizegoleadores+sizepenales
       
     return sizeresultados,sizepenales,sizegoleadores,sizetotal,catalog,resultados_sorted,goleadores_sorted,penales_sorted

def lab4(catalog,carga,tipo,doc):
    sizeresultados=(model.Size(catalog["goleadores"]))*doc
    startime=get_time()
    resultadosorg=model.lab4(catalog,carga,tipo,sizeresultados)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return resultadosorg,deltatime,sizeresultados

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,npartidos,condicion,equipo):
    startime=get_time()
    partidos,tamano=model.req_1(catalog["resultados"],equipo,condicion,npartidos)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return partidos,tamano,deltatime
    


def req_2(catalog,ngoles,jugador):
    startime=get_time()
    goles,tamano=model.req_2(catalog["goleadores"],ngoles,jugador)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return goles,tamano,deltatime
    

def req_3(catalog,equipo,year1,year2):
    year1=datetime.datetime.strptime(year1,"%Y-%m-%d").date()
    year2=datetime.datetime.strptime(year2,"%Y-%m-%d").date()
    if year1>year2:
        old=year2
        new=year1
    else:
        old=year1
        new=year2
    startime=get_time()
    sublista,total,visitantes,locales=model.req_3(catalog,equipo,old,new)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return sublista,total,visitantes,locales,deltatime
        
        
    #|


def req_4(catalog, torneo, fecha1, fecha2):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
    if date1>date2:
        old=date2
        new=date1
    else:
        old=date1
        new=date2
    startime = get_time()
    totPart,totPais,totCit,totPen,lista = model.req_4(catalog, torneo, old, new)
    endtime = get_time()
    deltatime= delta_time(startime, endtime)
    return totPart,totPais, totCit,totPen,lista,deltatime


def req_5(catalog, nombre_jugador, fecha_inicio, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    
    num_anotaciones, num_torneos, num_penales, num_autogoles, datos = model.req_5(catalog, nombre_jugador, fecha_inicio, fecha_final)

    return num_anotaciones, num_torneos, num_penales, num_autogoles, datos

    # TODO: Modificar el requerimiento 5
    
#i_anotaciones, i_torneos, i_penales, i_autogoles, 


def req_6(torneo,year1,year2,nequipos,catalog):
    year1=datetime.datetime.strptime(year1,"%Y-%m-%d").date()
    year2=datetime.datetime.strptime(year2,"%Y-%m-%d").date()
    if year1>year2:
        old=year2
        new=year1
    else:
        old=year1
        new=year2
    startime=get_time()
    lista,cantidadpartidos,ciudadescan,paisescan,ciudadmasjugada=model.req_6(torneo,old,new,nequipos,catalog)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return lista,cantidadpartidos,ciudadescan,paisescan,ciudadmasjugada,deltatime



def req_7(year1,year2,nequipos,catalog):
    year1=datetime.datetime.strptime(year1,"%Y-%m-%d").date()
    year2=datetime.datetime.strptime(year2,"%Y-%m-%d").date()
    if year1>year2:
        old=year2
        new=year1
    else:
        old=year1
        new=year2
    startime=get_time()
    jugadoresdata,cantidadjugadores,totalauto,totalpenale,totalgoles,cantidadpartidos=model.req_7(year1,year2,nequipos,catalog)
    endtime=get_time()
    deltatime= delta_time(startime, endtime)
    return jugadoresdata,cantidadjugadores,totalauto,totalpenale,totalgoles,cantidadpartidos,deltatime



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
