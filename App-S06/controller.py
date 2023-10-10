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
...
csv.field_size_limit(2147483647)



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tipo_de_lista):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(tipo_de_lista)
    return control


# Funciones para la carga de datos


def load_data(control,prefijo, alg):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    filename = cf.data_dir + f"Challenge-1/football/results-utf8-{prefijo}.csv"
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))

    for result in input_file:
        num_resutls = model.add_data_resutls(control["model"], result)
    
    filename = cf.data_dir + f"Challenge-1/football/goalscorers-utf8-{prefijo}.csv"
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))

    for scorer in input_file:
        num_scorer = model.add_data_goalscorers(control["model"], scorer)

    filename = cf.data_dir + f"Challenge-1/football/shootouts-utf8-{prefijo}.csv"
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))

    for shootout in input_file:
        num_shootout = model.add_data_shootouts(control["model"], shootout)
        
    model.sortear_carga(control["model"], alg)

    
    return control["model"],num_resutls,num_scorer,num_shootout
    


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


def req_1(control, equipo, condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    return model.req_1(control["model"], equipo, condicion)


def req_2(control,jugador,ng):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    return model.req_2(control["model"],jugador,ng)



def req_3(control, equipo, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    return model.req_3(control["model"], equipo, fecha_inicial, fecha_final)


def req_4(control, torneo, f1, f2):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    return model.req_4(control["model"], torneo, f1, f2)

    


def req_5(control, nombre_jugador, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    return model.req_5(control["model"], nombre_jugador, fecha_inicial, fecha_final)


def req_6(control,eqp,trn,f1,f2):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    return model.req_6_parte2(control["model"],eqp,trn,f1,f2)


def req_7(control, num_jugadores, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control["model"], num_jugadores, fecha_inicial, fecha_final)


def req_8_primera_parte(control, equipo, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 8, primera parte
    """
    # TODO: Modificar el requerimiento 8
    return model.req_8_primera_parte(control["model"], equipo, fecha_inicial, fecha_final)

def req_8_segunda_parte(control, equipo1, equipo2, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 8, segunda parte
    """
    return model.req_8_segunda_parte(control["model"], equipo1, equipo2, fecha_inicial, fecha_final)


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
