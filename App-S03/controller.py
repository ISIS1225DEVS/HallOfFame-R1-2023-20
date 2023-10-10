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
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(consulta_EDD):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    return model.new_data_structs(consulta_EDD)


# Funciones para la carga de datos
def load_data(control, size):
    for archivo in ["goalscorers", "results", "shootouts"]:
        file = cf.data_dir + f"Challenge-1/football/{archivo}-utf8-{size}.csv"
        input_file = csv.DictReader(open(file, encoding='utf-8'))
        for element in input_file:
            model.add_data(control, archivo, element)
    

def sort(control, alg_ord):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    return model.sort(control, alg_ord)

def sort_tiempo(control, alg_ord):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    start_time = get_time()
    model.sort_tiempo(control, alg_ord)
    final_tiempo = get_time()
    return delta_time(start_time,final_tiempo)



# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(n,n_equipo,condicion,control,valor_ord):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1


    t0 = get_time()
    total_partidos, resultado = model.req_1(n,n_equipo,condicion,control,valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return total_partidos, resultado, dt

def req_2(control, consulta_jugador, consulta_goles, valor_ord):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    t0 = get_time()
    num_goles, goles = model.req_2(control, consulta_jugador, consulta_goles, valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_goles, goles, dt


def req_3(control, consulta_equipo, consulta_fecha_i, consulta_fecha_f, valor_ord):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    
    t0 = get_time()
    num_partidos, num_partidos_L, num_partidos_V, datos = model.req_3(control, 
                                                                      consulta_equipo, 
                                                                      consulta_fecha_i, 
                                                                      consulta_fecha_f,
                                                                      valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_partidos,num_partidos_L,num_partidos_V,datos,dt

def req_4(control,consulta_torneo, consulta_fecha_i, consulta_fecha_f, valor_ord):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    t0 = get_time()
    num_partidos, num_paises, num_ciudades, num_partidosxpenales, datos = model.req_4(control, 
                                                                                  consulta_torneo, 
                                                                                  consulta_fecha_i, 
                                                                                  consulta_fecha_f,
                                                                                  valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_partidos, num_paises, num_ciudades, num_partidosxpenales, datos , dt

def req_5(control, consulta_jugador, consulta_fecha_i, consulta_fecha_f,valor_ord):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    t0 = get_time()
    num_anotaciones, num_torneos, num_penales, num_autogoles, datos = model.req_5(control, 
                                                                                  consulta_jugador, 
                                                                                  consulta_fecha_i, 
                                                                                  consulta_fecha_f,valor_ord)
   
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_anotaciones, num_torneos, num_penales, num_autogoles, datos,dt 

def req_6(control, consulta_n_mejores, consulta_torneo, consulta_fecha_i, consulta_fecha_f,valor_ord):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    t0=get_time()
    num_equipos, num_partidos, num_paises, num_ciudades, ciudad_md, equipos = model.req_6(control, 
                                                                            consulta_n_mejores, 
                                                                            consulta_torneo, 
                                                                            consulta_fecha_i, 
                                                                            consulta_fecha_f,valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_equipos, num_partidos, num_paises, num_ciudades, ciudad_md, equipos,dt

def req_7(control,consulta_n_jugadores,consulta_fecha_i,consulta_fecha_f,valor_ord):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    t0 = get_time()
    num_anotadores, num_partidos,num_torneos, num_anotaciones, goles_penal, autogoles, anotadores = model.req_7(control, 
                                                                                 consulta_n_jugadores,
                                                                                 consulta_fecha_i, 
                                                                                 consulta_fecha_f,valor_ord)
    tf = get_time()
    dt = delta_time(t0,tf)
    return num_anotadores, num_partidos,num_torneos, num_anotaciones, goles_penal, autogoles, anotadores,dt

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