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
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
from tabulate import tabulate
import threading
import gc


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    
    control = controller.new_controller()

    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Ordenar los partidos por fecha y país")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos

    match, goalscorers, shootouts, delta_time_matches, delta_time_scorers, dela_time_shootouts = controller.load_data(control)

    return match, goalscorers, shootouts, delta_time_matches, delta_time_scorers, dela_time_shootouts

def printLoadedData(control):

    matches, goalscorers, shootouts, delta_time_matches, delta_time_scorers, delta_time_shootouts = load_data(control)
    data_matches = lt.newList('ARRAY_LIST')
    data_goalscorers = lt.newList('ARRAY_LIST')
    data_shootouts = lt.newList('ARRAY_LIST')
    for i in range(1,4):
        match = lt.getElement(control['model']['matches'],i)
        dato_match  = match.copy()
        dato_match['date'] = str(dato_match['date'])[0:10]
        goal_scorer = lt.getElement(control['model']['goal_scorers'],i)
        dato_goal_scorer = goal_scorer.copy()
        dato_goal_scorer['date'] = str(dato_goal_scorer['date'])[0:10]
        shootout = lt.getElement(control['model']['shootouts'],i)
        dato_shootout = shootout.copy()
        dato_shootout['date'] = str(dato_shootout['date'])[0:10]
        lt.addLast(data_matches, dato_match)
        lt.addLast(data_goalscorers, dato_goal_scorer)
        lt.addLast(data_shootouts, dato_shootout)
    
    tamanio_matches = lt.size(control['model']['matches'])
    tamanio_goal_scorers = lt.size(control['model']['goal_scorers'])
    tamanio_shootouts = lt.size(control['model']['shootouts'])
    for i in range(tamanio_matches-2,tamanio_matches+1):
        match = lt.getElement(control['model']['matches'],i)
        dato_match = match.copy()
        dato_match['date'] = str(dato_match['date'])[0:10]
        lt.addLast(data_matches, dato_match)
    for i in range(tamanio_goal_scorers-2,tamanio_goal_scorers+1):
        goal_scorer = lt.getElement(control['model']['goal_scorers'],i)
        dato_goal_scorer = goal_scorer.copy()
        dato_goal_scorer['date'] = str(dato_goal_scorer['date'])[0:10]
        lt.addLast(data_goalscorers,dato_goal_scorer)
    for i in range(tamanio_shootouts-2, tamanio_shootouts+1):
        shootout = lt.getElement(control['model']['shootouts'],i)
        dato_shootout = shootout.copy()
        dato_shootout['date'] = str(dato_shootout['date'])[0:10]
        lt.addLast(data_shootouts, dato_shootout)

    table_matches = tabulate(data_matches['elements'], headers='keys', tablefmt="grid", stralign="center")
    table_goalScorers=tabulate(data_goalscorers['elements'], headers='keys', tablefmt="grid", stralign="center")
    table_shootouts = tabulate(data_shootouts['elements'], headers='keys', tablefmt="grid", stralign="center")

    delimiter = "-----------------------------------------------"
    title = "===========================================\n=========== FIFA RECORDS REPORT ===========\n==========================================="
    match_count = f"Match result count: {matches}"

    goal_count = f"Goal scorers count: {goalscorers}"
    penalty_count = f"Shootout-Penalty definition count: {shootouts}"

    printing_results = "Printing results for the first 3 and last 3 records on file"

    matchTitle = "---- MATCH RESULTS ----"
    totalMatch = f"        Total match results:{matches}"
    messageMatch="Results struct has more than 6 records..."

    goalScorersTitle="---- GOAL SCORERS ----"
    totalGoalScorers= f"        Total goal scorers:{goalscorers}"
    messageGoalScorers="Goal scorers struct has more than 6 records..."

    shootoutsTitle="---- SHOOTOUTS ----"
    totalShootouts= f"        Total shootouts:{shootouts}"
    messageShootouts="Shootouts struct has more than 6 records..."

    formatted_table = f"{delimiter}\n{match_count}\n{goal_count}\n{penalty_count}\n{delimiter}\n\n{title}\n\n{printing_results}\n\n{matchTitle}\n{totalMatch}\n{messageMatch}\n\n{table_matches}\n\n{delimiter}\n\n{goalScorersTitle}\n{totalGoalScorers}\n{messageGoalScorers}\n\n{table_goalScorers}\n\n{delimiter}\n\n{shootoutsTitle}\n{totalShootouts}\n{messageShootouts}\n\n{table_shootouts}\n\n{delimiter}"

    # Print the formatted table
    print(f'Para una muestra de {lt.size(control["model"]["matches"])} resultados, el tiempo de carga de datos es: {delta_time_matches} ms.') 
    print(f'Para una muestra de {lt.size(control["model"]["goal_scorers"])} anotaciones, el tiempo de carga de datos es: {delta_time_scorers} ms.') 
    print(f'Para una muestra de {lt.size(control["model"]["shootouts"])} resultados por penaltis, el tiempo de carga de datos es: {delta_time_shootouts} ms.')
    print(formatted_table)

def modificar_listas(control):
    controller.modificar_listas(control)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, partidos, equipo, condicion):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print('\n=============== Req. No. 1 Results ===============\n')
    if condicion == '3':
        estado = 'Indiferente'
    elif condicion == '2':
        estado = 'Visitante'
    else:
        estado = 'Local'
    respuesta, size, igualdad, delta_time = controller.req_1(control, partidos, equipo, condicion)
    datos = []
    if not igualdad:
        print(f'La cantidad de partidos seleccionados para {equipo} excede la cantidad de partidos disponibles.\n')
        if size == 0:
            print('No se encontraron partidos para este equipo.\n')
        else:
            print(f'Para {lt.size(control["model"]["matches"])} resultados, el tiempo de ejecución es de {delta_time} ms.\n')
            print(f'Se encontraron {size} partidos para {equipo} con condición de {estado}.\n')
            if size <= 6:
                for match in lt.iterator(respuesta):
                    dato=match.copy()
                    dato['date'] = str(dato['date'])[0:11]
                    del dato['id']
                    del dato['tournament']
                    del dato['neutral']
                    datos.append(dato)
                table_matches = tabulate(datos, headers = 'keys',tablefmt='grid',stralign='center')
                print(table_matches)
            else:
                resultados=lt.newList('SINGLE_LINKED')
                for i in range(1,4):
                    elemento = lt.getElement(respuesta,i)
                    lt.addLast(resultados,elemento)
                for i in range(size-2,size+1):
                    elemento = lt.getElement(respuesta, i)
                    lt.addLast(resultados, elemento)
                for match in lt.iterator(resultados):
                    dato = match.copy()
                    dato['date'] = str(dato['date'])[0:11]
                    del dato['id']
                    del dato['tournament']
                    del dato['neutral']
                    datos.append(dato)
                print( 'Los 3 primeros partidos y los 3 últimos partidos encontrados son:\n')
                table_matches = tabulate(datos,headers = 'keys', tablefmt='grid',stralign='center')
                print(table_matches)
    else:
        print(f'Para {lt.size(control["model"]["matches"])} resultados, el tiempo de ejecución es de {delta_time} ms.\n')
        print(f'Se encontraron {size} partidos para {equipo} con condición de {estado}.\n')
        if size <= 6:
            for match in lt.iterator(respuesta):
                dato = match.copy()
                dato['date'] = str(dato['date'])[0:11]
                del dato['id']
                del dato['tournament']
                del dato['neutral']
                datos.append(dato)
            table_matches = tabulate(datos, headers = 'keys',tablefmt='grid',stralign='center')
            print(table_matches)
        else:
            print('Los resultados encontrados tienen más de 6 registros.\n')
            resultados=lt.newList('SINGLE_LINKED')
            for i in range(1,4):
                elemento = lt.getElement(respuesta,i)
                lt.addLast(resultados,elemento)
            for i in range(size-2,size+1):
                elemento = lt.getElement(respuesta, i)
                lt.addLast(resultados, elemento)
            for match in lt.iterator(resultados):
                dato = match.copy()
                dato['date'] = str(dato['date'])[0:11]
                del dato['id']
                del dato['tournament']
                del dato['neutral']
                datos.append(dato)
            print('Los 3 primeros partidos y los 3 últimos partidos encontrados son:\n')
            table_matches = tabulate(datos,headers = 'keys', tablefmt='grid',stralign='center')
            print(table_matches)


def print_req_2(control, nombreJugador, numeroGoles):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print('\n=============== Req. No. 2 Results ===============\n')

    respuesta, size, vacio, deltaTime  = controller.req_2(control, nombreJugador, numeroGoles)

    if vacio:
        print(f'No se encontro ninguna anotación del jugador {nombreJugador.capitalize()}.\n')
    else:
        print(f'{nombreJugador.capitalize()} ha anotado un total de {size} goles.\n')

    tamanio = lt.size(respuesta)
    
    if tamanio <= 6:
        print('El número de goles encontrados es menor a 6:')
        data=[]
        for anotacion in lt.iterator(respuesta):
            dato = anotacion.copy()
            del dato['id']
            dato['date'] = str(dato['date'])[0:10]
            data.append(dato)
   
    else:
        print(f'Las primeras 3 y ultimas 3 anotaciones (de los primeros {numeroGoles} anotados):')
        data=[]
        for i in range(1,4):
            anotacion = lt.getElement(respuesta,i)
            dato = anotacion.copy()
            del dato['id']
            dato['date'] = str(dato['date'])[0:10]
            data.append(dato)
        for i in range (tamanio-2,tamanio+1):
            anotacion =lt.getElement(respuesta,i)
            dato = anotacion.copy()
            del dato['id']
            dato['date'] = str(dato['date'])[0:10]
            data.append(dato)

    table_Ngoles = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
    print(table_Ngoles)


def print_req_3(control, nombre, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    print('\n=============== Req. No. 3 Results ===============\n')
    respuesta, numeroPartidos, localmatch, visitantematch, vacio, deltaTime  = controller.req_3(control, nombre, fecha_i, fecha_f)

    if vacio:
        print(f'No se encontraron partidos de {nombre} en el rango indicado.\n')
    else:
        print(f'Total partidos de {nombre.capitalize()}: {numeroPartidos}')
        print(f'Partidos de {nombre.capitalize()} como local: {localmatch}')
        print(f'Partidos de {nombre.capitalize()} como visitante: {visitantematch}\n')

        if numeroPartidos <= 6:
            data=[]
            for partido in lt.iterator(respuesta):
                dato = partido.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        else:
            print('Los primeros 3 partidos y los últimos 3 partidos son:')
            data=[]
            for i in range(1,4):
                partido = lt.getElement(respuesta,i)
                dato = partido.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
            for i in range (numeroPartidos-2,numeroPartidos+1):
                partido =lt.getElement(respuesta,i)
                dato = partido.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        table_partidos = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
        print(table_partidos)


def print_req_4(control, nombre, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print('\n=============== Req. No. 4 Results ===============\n')
    partidos, paises, ciudades, penalties, torneo, vacio, deltaTime = controller.req_4(control, nombre, fecha_i, fecha_f)
    if vacio:
        print(f'No se encontraron partidos del torneo {nombre} en el rango indicado.\n')
    else:
        print(f'{nombre} total de partidos: {partidos}')
        print(f'{nombre} total de países involucrados: {paises}')
        print(f'{nombre} total de ciudades involucradas: {ciudades}')
        print(f'{nombre} total de partidos definidos por penaltis: {penalties}')

        if lt.size(torneo) <= 6:
            data=[]
            for anotacion in lt.iterator(torneo):
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        else:
            print('Las primeras 3 anotaciones y las últimas 3 anotaciones son:')
            data=[]
            for i in range(1,4):
                anotacion = lt.getElement(torneo,i)
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
            for i in range (lt.size(torneo)-2,lt.size(torneo)+1):
                anotacion =lt.getElement(torneo,i)
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        table_torneo = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
        print(table_torneo)

        print('El tiempo de ejecución fue de: ' + str(round(deltaTime,2)))


def print_req_5(control, nombre, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print('\n=============== Req. No. 5 Results ===============\n')
    respuesta, anotaciones, torneos, penaltis, autogoles, vacio, deltaTime = controller.req_5(control, nombre, fecha_i, fecha_f)
    if vacio:
        print(f'No se encontraron anotaciones de {nombre} en el rango indicado.\n')
    else:
        print(f'Para una muestra de {str(lt.size(control["model"]["matches"]))} resultados y {str(lt.size(control["model"]["goal_scorers"]))} anotaciones, el tiempo de ejecución es {str(deltaTime)} ms.\n')
        print(f'{nombre} total de goles: {anotaciones}')
        print(f'{nombre} total de torneos donde anotó: {torneos}')
        print(f'{nombre} total de penaltis: {penaltis}')
        print(f'{nombre} total autogoles: {autogoles}\n')

        if anotaciones <= 6:
            data=[]
            for anotacion in lt.iterator(respuesta):
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        else:
            print('Las primeras 3 anotaciones y las últimas 3 anotaciones son:')
            data=[]
            for i in range(1,4):
                anotacion = lt.getElement(respuesta,i)
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
            for i in range (anotaciones-2,anotaciones+1):
                anotacion =lt.getElement(respuesta,i)
                dato = anotacion.copy()
                del dato['id']
                dato['date'] = str(dato['date'])[0:10]
                data.append(dato)
        table_anotaciones = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
        print(table_anotaciones)

def print_req_6(control, cantidad_equipos, torneo,fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print('\n=============== Req. No. 6 Results ===============\n')
    respuesta, equipos, partidos, paises, ciudades, max_ciudad, vacio, delta_time = controller.req_6(control, cantidad_equipos, torneo, fecha_i, fecha_f)
    if vacio:
        print(f'No se encontraron equipos que hayan participado en {torneo} en el rango de tiempo indicado.\n')
    else:
        print(f'Para una muestra de {lt.size(control["model"]["matches"])} resultados y {lt.size(control["model"]["goal_scorers"])} anotaciones el tiempo de ejecución es de {delta_time} ms.\n')
        print(f'El total de equipos que participaron en {torneo} es {equipos}.')
        print(f'El total de encuentros disputados en {torneo} en el periodo de tiempo dado es {partidos}.')
        print(f'El total de países involucrados en {torneo} es {paises}.')
        print(f'El total de ciudades involucradas en {torneo} es {ciudades}.')
        print(f'La ciudad donde más partidos se han disputado de {torneo} es {max_ciudad}.\n')

        if int(cantidad_equipos) <= 6:
            data = []
            for equipo in lt.iterator(respuesta):
                dato = equipo.copy()
                del dato['id']
                del dato['resultados']
                dato['jugador'] = tabulate([dato['jugador']], headers = 'keys', tablefmt = 'grid', stralign = 'center')
                data.append(dato)
        else:
            print('Los primeros 3 equipos y los últimos 3 equipos del ranking son:')
            data=[]
            for i in range(1,4):
                equipo = lt.getElement(respuesta,i)
                dato = equipo.copy()
                del dato['id']
                del dato['resultados']
                dato['jugador'] = tabulate([dato['jugador']], headers = 'keys', tablefmt = 'grid', stralign = 'center')
                data.append(dato)
            for i in range (int(cantidad_equipos)-2,int(cantidad_equipos)+1):
                equipo =lt.getElement(respuesta,i)
                dato = equipo.copy()
                del dato['id']
                del dato['resultados']
                dato['jugador'] = tabulate([dato['jugador']], headers = 'keys', tablefmt = 'grid', stralign = 'center')
                data.append(dato)
        table_equipos = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
        print(table_equipos)


def print_req_7(control, numeroJugadores, fecha_i, fecha_f):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    print('\n=============== Req. No. 7 Results ===============\n')

    anotadoresTotales, partidosUnicos, torneosUnicos, GolesTotales, Penales, Autogol, respuestaFinal, vacio, deltaTime = controller.req_7(control, numeroJugadores, fecha_i, fecha_f)
    print(deltaTime)
    if vacio:
        print(f'No se encontraron jugadores que hayan anotado goles en el rango de tiempo indicado.\n')
    else:
        print(f'TOP {numeroJugadores} scorer ranking\n')
        print(f'El total de anotadores es {anotadoresTotales}')
        print(f'El número total de partidos o encuentros en que participaron los anotadores fueron: {partidosUnicos}')
        print(f'El número total de torneos donde participaron los anotadores en ese periodo: {torneosUnicos}')
        print(f'El número total de anotaciones o goles obtenidos: {GolesTotales}')
        print(f'El número total de goles por penal: {Penales}')
        print(f'El número total de autogoles: {Autogol}')

        tableData = lt.newList('SINGLE_LINKED')
       
        if int(anotadoresTotales) <= 6:
            
            data = []
            for anotador in lt.iterator(respuestaFinal):
                
                ultimo_gol_data = {
                    "Fecha": str(anotador['ultimoGol']['fecha']),
                    "Torneo": anotador['ultimoGol']['torneo'],
                    "Home Team": anotador['ultimoGol']['home_team'],
                    "Away Team": anotador['ultimoGol']['away_team'],
                    "Home Score": anotador['ultimoGol']['home_score'],
                    "Away Score": anotador['ultimoGol']['away_score'],
                    "Minuto": anotador['ultimoGol']['minute'],
                    "Penal": anotador['ultimoGol']['penalty'],
                    "Autogol": anotador['ultimoGol']['own_goal']
                }
                
                player_data = {
                "Anotadores": anotador['nombre'],
                "Puntos totales": str(anotador['puntajeAnotador']),
                "Goles totales": str(anotador['totalGoles']),
                "Penales totales": str(anotador['totalGolesPenales']),
                "Autogoles totales": str(anotador['totalAutogoles']),
                "Tiempo promedio": str(anotador['tiempoPromedio']),
                "Torneos totales": str(anotador['totalTorneos']),
                "Anots en victorias": str(anotador['totalAnotacionesVictoria']),
                "Anots en derrotas": str(anotador['totalAnotacionesDerrota']),
                "Anots en empates": str(anotador['totalAnotacionesEmpate']),
                "Ultimo gol": tabulate([ultimo_gol_data], headers='keys', tablefmt='grid', stralign='center')
                }

                data.append(player_data)         

        else:
            print('Los primeros 3 jugadores y los últimos 3 jugadores del ranking son:')
            
            data = []

            for i in range(1,4):
                anotador = lt.getElement(respuestaFinal,i)

                ultimo_gol_data = {
                    "Fecha": str(anotador['ultimoGol']['fecha']),
                    "Torneo": anotador['ultimoGol']['torneo'],
                    "Home Team": anotador['ultimoGol']['home_team'],
                    "Away Team": anotador['ultimoGol']['away_team'],
                    "Home Score": anotador['ultimoGol']['home_score'],
                    "Away Score": anotador['ultimoGol']['away_score'],
                    "Minuto": anotador['ultimoGol']['minute'],
                    "Penal": anotador['ultimoGol']['penalty'],
                    "Autogol": anotador['ultimoGol']['own_goal']
                }
                
                player_data = {
                "Anotadores": anotador['nombre'],
                "Puntos totales": str(anotador['puntajeAnotador']),
                "Goles totales": str(anotador['totalGoles']),
                "Penales totales": str(anotador['totalGolesPenales']),
                "Autogoles totales": str(anotador['totalAutogoles']),
                "Tiempo promedio": str(anotador['tiempoPromedio']),
                "Torneos totales": str(anotador['totalTorneos']),
                "Anots en victorias": str(anotador['totalAnotacionesVictoria']),
                "Anots en derrotas": str(anotador['totalAnotacionesDerrota']),
                "Anots en empates": str(anotador['totalAnotacionesEmpate']),
                "Ultimo gol": tabulate([ultimo_gol_data], headers='keys', tablefmt='grid', stralign='center')
                }
          
                data.append(player_data)

            for i in range (int(lt.size(respuestaFinal))-2,int(lt.size(respuestaFinal))+1):

                anotador = lt.getElement(respuestaFinal,i)
                ultimo_gol_data = {
                    "Fecha": str(anotador['ultimoGol']['fecha']),
                    "Torneo": anotador['ultimoGol']['torneo'],
                    "Home Team": anotador['ultimoGol']['home_team'],
                    "Away Team": anotador['ultimoGol']['away_team'],
                    "Home Score": anotador['ultimoGol']['home_score'],
                    "Away Score": anotador['ultimoGol']['away_score'],
                    "Minuto": anotador['ultimoGol']['minute'],
                    "Penal": anotador['ultimoGol']['penalty'],
                    "Autogol": anotador['ultimoGol']['own_goal']
                }
                
                player_data = {
                "Anotadores": anotador['nombre'],
                "Puntos totales": str(anotador['puntajeAnotador']),
                "Goles totales": str(anotador['totalGoles']),
                "Penales totales": str(anotador['totalGolesPenales']),
                "Autogoles totales": str(anotador['totalAutogoles']),
                "Tiempo promedio": str(anotador['tiempoPromedio']),
                "Torneos totales": str(anotador['totalTorneos']),
                "Anots en victorias": str(anotador['totalAnotacionesVictoria']),
                "Anots en derrotas": str(anotador['totalAnotacionesDerrota']),
                "Anots en empates": str(anotador['totalAnotacionesEmpate']),
                "Ultimo gol": tabulate([ultimo_gol_data], headers='keys', tablefmt='grid', stralign='center')
                }

                data.append(player_data)

        table_equipos = tabulate(data, headers='keys',tablefmt='grid',stralign='center')
        print(table_equipos)


def print_req_8(control, team1, team2, fechaInicio, fechaFin):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print('\n=============== Req. No. 8 Results (BONUS) ===============\n')

    otrosDatos1, otrosDatos2, est1, est2, comun, delta = controller.req_8(control, team1, team2, fechaInicio, fechaFin)

    print('\n      ---------- ' + team1 +' Statistics ----------      \n')
    
    print(f'      Años entre ambas fechas: {lt.getElement(otrosDatos1,1)}.')
    print(f'      Total partidos: {lt.getElement(otrosDatos1,2)}.')
    print(f'      Total partidos disputados en casa: {lt.getElement(otrosDatos1,3)}.')
    print(f'      Total partidos disputados de visitante: {lt.getElement(otrosDatos1,4)}.')
    print(f'      Fecha del partido más antigüo registrado: {str(lt.getElement(otrosDatos1,5))[0:10]}.')
    print(f'      +++ Datos del partido más reciente +++ \n')

    data1=[]
    dato1 = lt.getElement(otrosDatos1,6).copy()
    del dato1['id']
    del dato1['neutral']
    dato1['date'] = str(dato1['date'])[0:10]
    data1.append(dato1)

    table_equipo1 = tabulate(data1, headers='keys',tablefmt='grid',stralign='center')
    print(table_equipo1)

    print('\n      ---------- yearly statistics ----------      \n')

    if len(list(est1.keys())) <= 6:
        data_est1 = []
        
        for anio in est1.keys():
            dic_est1 = {}
            dic_est1['año'] = anio
            dic_est1['partidos'] = est1[anio]['elements'][0]
            dic_est1['puntos_totales'] = est1[anio]['elements'][1]
            dic_est1['diferencia_gol'] = est1[anio]['elements'][2]
            dic_est1['penalties'] = est1[anio]['elements'][3]
            dic_est1['autogoles'] = est1[anio]['elements'][4]
            dic_est1['victorias'] = est1[anio]['elements'][5]
            dic_est1['empates'] = est1[anio]['elements'][6]
            dic_est1['derrotas'] = est1[anio]['elements'][7]
            dic_est1['goles_contra'] = est1[anio]['elements'][8]
            dic_est1['goleador'] = tabulate([est1[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est1.append(dic_est1)
    else:
        print('Los primeros 3 equipos y los últimos 3 equipos del ranking son:')
        data_est1 = []

        for anio in list(est1.keys())[:3]:
            dic_est1 = {}
            dic_est1['año'] = anio
            dic_est1['partidos'] = est1[anio]['elements'][0]
            dic_est1['puntos_totales'] = est1[anio]['elements'][1]
            dic_est1['diferencia_gol'] = est1[anio]['elements'][2]
            dic_est1['penalties'] = est1[anio]['elements'][3]
            dic_est1['autogoles'] = est1[anio]['elements'][4]
            dic_est1['victorias'] = est1[anio]['elements'][5]
            dic_est1['empates'] = est1[anio]['elements'][6]
            dic_est1['derrotas'] = est1[anio]['elements'][7]
            dic_est1['goles_contra'] = est1[anio]['elements'][8]
            dic_est1['goleador'] = tabulate([est1[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est1.append(dic_est1)

        for anio in list(est1.keys())[-3:]:
            dic_est1 = {}
            dic_est1['año'] = anio
            dic_est1['partidos'] = est1[anio]['elements'][0]
            dic_est1['puntos_totales'] = est1[anio]['elements'][1]
            dic_est1['diferencia_gol'] = est1[anio]['elements'][2]
            dic_est1['penalties'] = est1[anio]['elements'][3]
            dic_est1['autogoles'] = est1[anio]['elements'][4]
            dic_est1['victorias'] = est1[anio]['elements'][5]
            dic_est1['empates'] = est1[anio]['elements'][6]
            dic_est1['derrotas'] = est1[anio]['elements'][7]
            dic_est1['goles_contra'] = est1[anio]['elements'][8]
            dic_est1['goleador'] = tabulate([est1[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est1.append(dic_est1)
    table_equipos1 = tabulate(data_est1, headers='keys',tablefmt='grid',stralign='center')
    print(table_equipos1)
    
    print('\n      ---------- ' + team2 +' Statistics ----------      \n')
    
    print(f'      Años entre ambas fechas: {lt.getElement(otrosDatos2,1)}.')
    print(f'      Total partidos: {lt.getElement(otrosDatos2,2)}.')
    print(f'      Total partidos disputados en casa: {lt.getElement(otrosDatos2,3)}.')
    print(f'      Total partidos disputados de visitante: {lt.getElement(otrosDatos2,4)}.')
    print(f'      Fecha del partido más antigüo registrado: {str(lt.getElement(otrosDatos2,5))[0:10]}.')
    print(f'      +++ Datos del partido más reciente +++ \n')

    data2=[]
    dato2 = lt.getElement(otrosDatos2,6).copy()
    del dato2['id']
    del dato2['neutral']
    dato2['date'] = str(dato2['date'])[0:10]
    data2.append(dato2)

    table_equipo2 = tabulate(data2, headers='keys',tablefmt='grid',stralign='center')
    print(table_equipo2)

    print('\n      ---------- yearly statistics ----------      \n')

    if len(list(est2.keys())) <= 6:
        data_est2 = []
        
        for anio in est2.keys():
            dic_est2 = {}
            dic_est2['año'] = anio
            dic_est2['partidos'] = est2[anio]['elements'][0]
            dic_est2['puntos_totales'] = est2[anio]['elements'][1]
            dic_est2['diferencia_gol'] = est2[anio]['elements'][2]
            dic_est2['penalties'] = est2[anio]['elements'][3]
            dic_est2['autogoles'] = est2[anio]['elements'][4]
            dic_est2['victorias'] = est2[anio]['elements'][5]
            dic_est2['empates'] = est2[anio]['elements'][6]
            dic_est2['derrotas'] = est2[anio]['elements'][7]
            dic_est2['goles_contra'] = est2[anio]['elements'][8]
            dic_est2['goleador'] = tabulate([est2[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est2.append(dic_est2)
    else:
        print('Los primeros 3 equipos y los últimos 3 equipos del ranking son:')
        data_est2 = []

        for anio in list(est2.keys())[:3]:
            dic_est2 = {}
            dic_est2['año'] = anio
            dic_est2['partidos'] = est2[anio]['elements'][0]
            dic_est2['puntos_totales'] = est2[anio]['elements'][1]
            dic_est2['diferencia_gol'] = est2[anio]['elements'][2]
            dic_est2['penalties'] = est2[anio]['elements'][3]
            dic_est2['autogoles'] = est2[anio]['elements'][4]
            dic_est2['victorias'] = est2[anio]['elements'][5]
            dic_est2['empates'] = est2[anio]['elements'][6]
            dic_est2['derrotas'] = est2[anio]['elements'][7]
            dic_est2['goles_contra'] = est2[anio]['elements'][8]
            dic_est2['goleador'] = tabulate([est2[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est2.append(dic_est2)

        for anio in list(est2.keys())[-3:]:
            dic_est2 = {}
            dic_est2['año'] = anio
            dic_est2['partidos'] = est2[anio]['elements'][0]
            dic_est2['puntos_totales'] = est2[anio]['elements'][1]
            dic_est2['diferencia_gol'] = est2[anio]['elements'][2]
            dic_est2['penalties'] = est2[anio]['elements'][3]
            dic_est2['autogoles'] = est2[anio]['elements'][4]
            dic_est2['victorias'] = est2[anio]['elements'][5]
            dic_est2['empates'] = est2[anio]['elements'][6]
            dic_est2['derrotas'] = est2[anio]['elements'][7]
            dic_est2['goles_contra'] = est2[anio]['elements'][8]
            dic_est2['goleador'] = tabulate([est2[anio]['elements'][-1]], headers = 'keys', tablefmt = 'grid', stralign = 'center')
            data_est2.append(dic_est2)
    table_equipos2 = tabulate(data_est2, headers='keys',tablefmt='grid',stralign='center')
    print(table_equipos2)

    print('\n      ---------- ' + team1 + ' vs ' + team2 +' Statistics ----------      \n')

    uno = comun['elements'][0]
    dos = comun['elements'][1]
    tres = comun['elements'][2]
    cuatro = comun['elements'][3]
    cinco = comun['elements'][4]
    seis = comun['elements'][5]
    
    print(f'      Número de partidos: {uno}.')
    print(f'      Número de victorias para {team1}: {dos}.')
    print(f'      Número de derrotas para {team1}: {tres}.')
    print(f'      Número de victorias para {team2}: {cuatro}.')
    print(f'      Número de derrotas para {team2}: {cinco}.')
    print(f'      Número de empates: {seis}. \n')
    print(f'      +++ Datos del partido más reciente +++ \n')

    table_comun = tabulate([comun['elements'][6]], headers='keys',tablefmt='grid',stralign='center')
    print(table_comun, '\n')

    print(f'      +++ Goles del partido +++ \n')

    table_gol = tabulate(comun['elements'][7]['elements'], headers='keys',tablefmt='grid',stralign='center')
    print(table_gol, '\n')

    print({f'El tiempo de ejecución fue de: {round(delta,3)}'})


# Se crea el controlador asociado a la vista
control = new_controller()

default_limit = 1000
# main del reto
def menu_cycle():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        gc.collect()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            tipo_lista = int(input('Seleccione un tipo de representación de lista:\n1) ARRAY_LIST\n2) SINGLE_LINKED\n'))
            if tipo_lista==2:
                modificar_listas(control)
            print("Cargando información de los archivos ....\n")
            printLoadedData(control)
            
        elif int(inputs) == 2:
            equipo = input('Ingrese el equipo del cuál desea conocer la información: ')
            partidos = input('Ingrese el número de partidos que desea consultar: ')
            condicion = input('Seleccione la condición del equipo:\n1) Local\n2) Visitante\n3) Indiferente\n')
            print_req_1(control, partidos, equipo, condicion)

        elif int(inputs) == 3:
            nombreJugador = input('Ingrese el nombre completo del jugador que desea consultar: ')
            numeroGoles = input('Ingrese el número de goles que desea consultar: ')
    
            print_req_2(control, nombreJugador, numeroGoles)

        elif int(inputs) == 4:

            valido = False
            nombre = input('Ingrese el nombre del equipo que desea consultar: ')

            while not valido:
                fecha_i = input('Ingrese la fecha inicial del rango que desea consultar (Año-Mes-Dia): ')
                if len (fecha_i) == 10:
                    valido = True
            valido = False
            while not valido:
                fecha_f = input('Ingrese la fecha final del rango que desea consultar (Año-Mes-Dia): ')
                if len(fecha_f) == 10:
                    valido = True
            print_req_3(control,nombre,fecha_i,fecha_f)

        elif int(inputs) == 5:
            valido = False
            nombre = input('Ingrese el nombre del torneo que desea consultar: ')

            while not valido:
                fecha_i = input('Ingrese la fecha inicial del rango que desea consultar: ')
                if len (fecha_i) == 10:
                    valido = True
            valido = False
            while not valido:
                fecha_f = input('Ingrese la fecha final del rango que desea consultar: ')
                if len(fecha_f) == 10:
                    valido = True
            print_req_4(control,nombre,fecha_i,fecha_f)

        elif int(inputs) == 6:
            valido = False
            nombre = input('Ingrese el nombre del jugador que desea consultar: ')

            while not valido:
                fecha_i = input('Ingrese la fecha inicial del rango que desea consultar: ')
                if len (fecha_i) == 10:
                    valido = True
            valido = False
            while not valido:
                fecha_f = input('Ingrese la fecha final del rango que desea consultar: ')
                if len(fecha_f) == 10:
                    valido = True
            print_req_5(control,nombre,fecha_i,fecha_f)

        elif int(inputs) == 7:
            valido = False
            torneo = input('Ingrese el nombre del torneo que desea consultar: ')
            cantidad_equipos = input('Ingrese el número de equipos que desea consultar: ')

            while not valido:
                fecha_i = input('Ingrese la fecha inicial del rango que desea consultar: ')
                if len (fecha_i) == 10:
                    valido = True
            valido = False
            while not valido:
                fecha_f = input('Ingrese la fecha final del rango que desea consultar: ')
                if len(fecha_f) == 10:
                    valido = True
            print_req_6(control, cantidad_equipos, torneo, fecha_i, fecha_f)

        elif int(inputs) == 8:
            
            valido = False
            numeroJugadores = input('Ingrese el número de jugadores que desea consultar: ')
            
            while not valido:
                fecha_i = input('Ingrese la fecha inicial del rango que desea consultar: ')
                if len (fecha_i) == 10:
                    valido = True
            valido = False
            while not valido:
                fecha_f = input('Ingrese la fecha final del rango que desea consultar: ')
                if len(fecha_f) == 10:
                    valido = True

            print_req_7(control,numeroJugadores,fecha_i,fecha_f)

        elif int(inputs) == 9:
            team1 = input("Ingrese el nombre del primer equipo a comparar: ")
            team2 = input("Ingrese el nombre del segundo equipo a comparar: ")
            fechaInicio = input("Ingrese la fecha de inicio para filtrar los partidos: ")
            fechaFin = input("Ingrese la fecha limite para filtrar los partidos: ")
            print_req_8(control, team1, team2, fechaInicio, fechaFin)
        
        elif int(inputs) == 10:
            size_muestra=input('Seleccione el tamaño de la muestra que desea cargar:\n1) 5%\n2) 20%\n3) 30%\n4) 50%\n5) 100%\n')
            orden=input('Seleccione el algoritmo de ordenamiento que desea:\n1) Select\n2) Insertion\n3) Shell\n4) Merge\n5) Quick\n')
            while size_muestra != "1" and size_muestra != "2" and size_muestra != "3" and size_muestra != "4" and size_muestra != "5":
                size_muestra=input("Ingrese opciones válidas.\n Verifique su selección del tamaño de la muestra: ")
            while orden != '1' and orden != '2' and orden!= '3' and orden != '4' and orden != '5':
                orden=input('Verifique su selección del algortimo de ordenamiento: ')
            result = controller.sortMatches(control,size_muestra,orden)
            delta_time= f"{result[0]:.3f}"
            sorted_list = result[1]
            if size_muestra=="1":
                print("Para una muestra del 5%"+ ' ('+str(lt.size(sorted_list))+' datos) '+" de los datos, delta de tiempo: "+str(delta_time))
            elif size_muestra=="2":
                print("Para una muestra del 20%"+ ' ('+str(lt.size(sorted_list))+' datos) '+" de los datos, delta de tiempo: "+str(delta_time))
            elif size_muestra=="3":
                print("Para una muestra del 30%"+' ('+str(lt.size(sorted_list))+' datos) '+" de los datos, delta de tiempo: "+str(delta_time))
            elif size_muestra=="4":
                print("Para una muestra del 50%"+' ('+str(lt.size(sorted_list))+' datos) '+" de los datos, delta de tiempo: "+str(delta_time))
            else:
                print("Para una muestra del 100%"+' ('+str(lt.size(sorted_list))+' datos) '+" de los datos, delta de tiempo: "+str(delta_time))
            # modificaciones tiempos de ejecución - Laboratorio 4
            # Avance Req ordenamientos iterativos - Reto 1

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

if __name__ == "__main__":
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()