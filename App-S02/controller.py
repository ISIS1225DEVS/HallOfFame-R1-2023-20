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
import csv
import os
from datetime import datetime



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(listType):
    """
    Crea una instancia del modelo.
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(listType)
    return control


# Funciones para la carga de datos

def load_data(control, goalscorers, results, shootouts):
    """
    Carga de datos del reto.
    """
    catalog = control["model"]
    goalscorersfile = os.path.join(cf.data_dir, goalscorers)
    input_goalscorers_file = csv.DictReader(open(goalscorersfile, encoding="utf-8"))
    
    for scorers in input_goalscorers_file:
        scorers["date"] = datetime.strptime(scorers["date"], "%Y-%m-%d").date()
        if scorers["penalty"]=="":
            scorers["penalty"]="unknown"
        model.add_scorers(catalog, scorers)
    size_scorers=  model.data_size_scorers(catalog)

    resultsfile = os.path.join(cf.data_dir, results)
    input_results_file = csv.DictReader(open(resultsfile, encoding="utf-8"))
    
    for result in input_results_file:
        result["date"] = datetime.strptime(result["date"], "%Y-%m-%d").date()
        model.add_results(catalog, result)
    size_results= model.data_size_results(catalog)

    shootouts_file = os.path.join(cf.data_dir, shootouts)
    input_shootouts_file = csv.DictReader(open(shootouts_file, encoding="utf-8"))
    
    for shootout in input_shootouts_file:
        shootout["date"] = datetime.strptime(shootout["date"], "%Y-%m-%d").date()
        model.add_shootouts(catalog, shootout)
    size_shootouts = model.data_size_shootouts(catalog)
    

    return size_scorers, size_results, size_shootouts


def loadsublist(control, filetype):
    catalog = control["model"]    
    catalog["goalscorers"] = model.sort_por_fecha_menor(catalog["goalscorers"])
    catalog["results"] = model.sort_por_fecha_menor(catalog["results"])
    catalog["shootouts"] = model.sort_por_fecha_menor(catalog["shootouts"])
    return model.sublist(catalog, filetype)

def get3(list):
    return model.get3(list)

# Funciones de ordenamiento

def sort(control, sort_type):
    """
    Ordena los datos del modelo.
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    start_time = get_time()
    sorted_list = model.sort(control['model'], sort_type)
    end_time = get_time()
    delta_times = delta_time(start_time, end_time)
    return delta_times, sorted_list
    


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1_controller(control,numero_partidos, team, condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = time.time()
    results = model.req_1_model(control['model'], numero_partidos, team, condicion)
    end_time = time.time()
    execution_time = end_time - start_time
    return results, execution_time


def req_2_controller(control, numero_goles, nombre_jugador):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = time.time()
    results = model.req_2_model(control['model'], numero_goles, nombre_jugador)
    end_time = time.time()
    execution_time = end_time - start_time
    
    return results, execution_time



def req_3_controller(control, team_name, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = time.time()
    results = model.req_3_model(control["model"], team_name, initial_date, final_date)
    end_time = time.time()
    execution_time = end_time - start_time
    return results, execution_time



def req_4_controller(control, tournament_name, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = time.time()
    results = model.req_4_model(control["model"], tournament_name, initial_date, final_date)
    end_time = time.time()
    execution_time = end_time - start_time
    return results, execution_time 



def req_5(control , nombre ,fecha1 ,fecha2 ):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = time.time()
    results = model.req_5(control["model"] , nombre , fecha1 , fecha2 )
    end_time = time.time()
    execution_time = end_time - start_time
    return results, execution_time

def req_6_controller(control, n, tournament_name, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = time.time()
    results = model.req_6_model(control["model"], n, tournament_name, initial_date, final_date)
    end_time = time.time()
    execution_time = end_time - start_time
    return results, execution_time 


def req_7(control, num_jugadores, fecha1, fecha2):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = time.time()
    results7 = model.req_7(control["model"], num_jugadores, fecha1, fecha2)
    end_time = time.time()
    execution_time = end_time - start_time
    return results7, execution_time


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