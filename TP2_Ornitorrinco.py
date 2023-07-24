import random
import copy
import doctest

#CONSTANTES
POSICION_PALABRA_INGRESADA = -1
ACIERTOS = 0
ERRORES = 1
PUNTAJE_PARCIAL = 2
PUNTAJE_PARTIDA = 3
MAX_L = 20
MIN_L = 4
MAX_JUGADORES = 4
MIN_JUGADORES = 1



#ETAPA_8
def cargar_diccionario():
    '''
    Obj: Crea diccionario con clave letra que a su vez tiene un diccionario clave palabra y valor 
    definición, partiendo de dos archivos txt.
    Autores: Dario y Luz
    '''
    diccionario = {}
    archivo_palabras = open(".\palabras.txt", "r", encoding="utf8")
    archivo_definiciones = open(".\definiciones.txt", "r", encoding="utf8")
    palabra = archivo_palabras.readline().rstrip('\n')
    definicion = archivo_definiciones.readline().rstrip('\n')
    while(palabra != ''):
        letra = palabra[0]
        if letra not in diccionario:
            diccionario[letra] = {}
        diccionario[letra][palabra] = definicion
        definicion = archivo_definiciones.readline().rstrip('\n')
        palabra = archivo_palabras.readline().rstrip('\n')
    archivo_palabras.close()
    archivo_definiciones.close()
    return diccionario

def generar_archivo_diccionario_ordenado(diccionario):
    '''
    Obj: A partir del diccionario de diccionarios crea un archivo csv ordenado alfabéticamente. 
    Autores: Dario y Luz
    '''
    archivo_csv = open(".\diccionario_ordenado.csv", "w", encoding="utf8")
    diccionario_ordenado = sorted(list(diccionario.items()), key = lambda x:x[0])
    for i in diccionario_ordenado:
        archivo_csv.write(str(i) + '\n')
    archivo_csv.close()

#ETAPA 9

def es_minimo_valido(largo):
    '''
    >>> es_minimo_valido(3)
    False
    >>> es_minimo_valido(4)
    True
    >>> es_minimo_valido(9)
    True
    '''
    return MIN_L <= largo 

def es_maximo_valido(largo):
    '''
    >>> es_maximo_valido(3)
    True
    >>> es_maximo_valido(20)
    True
    >>> es_maximo_valido(28)
    False
    '''
    return MAX_L >= largo

def validar_nombre(nombre):
    '''
    Obj: Valida la longitud del nombre ingresado.
    Autores: Dario y Luz

    >>> validar_nombre('Dario')
    True
    >>> validar_nombre('Edu')
    False
    >>> validar_nombre('Luchi')
    True
    '''
    largo_nom = len(nombre)
    return es_minimo_valido(largo_nom) and es_maximo_valido(largo_nom) and nombre.isalnum()

def preguntar_cant_jugadores():
    '''
    Obj: Pregunta la cantidad de jugadores validando el max y min de jugadores.
    Autores: Dario y Luz
    '''
    cant_jugadores = int(input('Ingrese la cantidad de jugadores (hasta un maximo de 4): '))
    while(cant_jugadores < MIN_JUGADORES or cant_jugadores > MAX_JUGADORES):
        cant_jugadores = int(input('el maximo de jugadores es 4! Ingrese nuevamente la cantidad: '))
    return cant_jugadores

def listar_jugadores(cant_jugadores):
    '''
    Obj: Crea una lista con los jugadores ingresados.
    Autores : Dario y Luz
    '''
    lista_jugadores = []
    for i in range(1, cant_jugadores + 1):
        nombre = input('Ingrese el nombre del jugador '+ str(i) +': ')
        while(not(validar_nombre(nombre)) or nombre in lista_jugadores):
            nombre = input('El nombre ' + nombre + ' no puede repetirse, debe contener como mínimo 4 caracteres y estos deben ser alfanumericos: ')
        lista_jugadores.append(nombre)
    return lista_jugadores

def cargar_diccionario_jugadores(lista_jugadores):
    '''
    Obj: Crea diccionario con clave Nombre del jugador y valor una lista con 4 valores en 0
    estos son los ACIERTOS, ERRORES, PUNTAJE_PARCIAL y PUNTAJE_PARTIDA.
    Autores: Dario y Luz
    >>> cargar_diccionario_jugadores(['Dario', 'Luz', 'Agus'])
    {'Dario': [0, 0, 0, 0], 'Luz': [0, 0, 0, 0], 'Agus': [0, 0, 0, 0]}
    >>> cargar_diccionario_jugadores(['Dario', 'Damian', 'Demian'])
    {'Dario': [0, 0, 0, 0], 'Damian': [0, 0, 0, 0], 'Demian': [0, 0, 0, 0]}
    '''
    diccionario_jugadores = {}
    lista_de_valores = [0, 0, 0, 0]
    for nombre in lista_jugadores:
        diccionario_jugadores[nombre] = lista_de_valores
    return diccionario_jugadores

#ETAPA 10

def crear_dicc_de_valores(valores):
    '''
    Obj: Crea una lista de listas, donde cada sublista es una línea del archivo configuracion.csv
    Autores: Dario y Luz
    '''
    diccionario_de_valores = {}
    linea = valores.readline()
    while linea != '':
        opcion, valor = linea.rstrip('\n').split(',')
        diccionario_de_valores[opcion] = valor
        linea = valores.readline()
    return diccionario_de_valores


#FUNCIONES ETAPA 3
def seleccionar_letras(letras_a_procesar, configuracion):
    """
    Obj: Recibe una lista y devuelve otra con X elementos al azar únicos de la misma ordenados alfabeticamente. La long de la lista debe
    ser mayor que los X elementos deseados.
    Autores: Luz y Eduardo 
    """
    cant_letras = int(configuracion['CANTIDAD_LETRAS_ROSCO'])
    letras_participantes=[]
    copia_de_letras=copy.deepcopy(letras_a_procesar)
    #si solo igualo las listas, python considera que copia de letras y letras a procesar
    #son la misma variable, es necesario usar el metodo deepcopy para diferenciar y para eso
    #es necesario el import copy al principio

    for i in range(cant_letras):
        numero_de_letra=random.randint(0,len(copia_de_letras)-1)
        letra=copia_de_letras[numero_de_letra]
        letras_participantes.append(letra)
        copia_de_letras.pop(numero_de_letra)

    return(sorted(letras_participantes))

def conseguir_palabra(definiciones, letra_a_procesar):
    """
    Obj: Recibe el diccionario y una letra, retorna una palabra al azar del 
    diccionario que empieza con tal letra.
    Autores: Luz
    """
    numero=random.randint(0,len(definiciones[letra_a_procesar].keys())-1)
    palabra=(list(definiciones[letra_a_procesar].keys()))[numero]
    return(palabra)

def crear_palabras_del_juego (definiciones, letras_participantes, configuracion):
    """
    Obj: Recibe el diccionario y una lista de letras participantes, selecciona una palabra al azar
    por cada una de tales letras y las retorna ordenadas alfabeticamente.  
    Autores: Dario y Luz
    """
    longitud_palabra_minima = int(configuracion['LONGITUD_PALABRA_MINIMA'])
    palabras_rosco=[]
    
    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        longitud_incorrecta = True
        while longitud_incorrecta:
            if len(palabra) >= longitud_palabra_minima:
                palabras_rosco.append(palabra)
                longitud_incorrecta = False
            else:
                palabra = conseguir_palabra(definiciones, letra)
        
    return (palabras_rosco)



#FUNCIONES ETAPA 1
def verificador_de_palabra(palabra_del_turno):
    '''
    Obj: La funcion verificador_de_palabra recibe el turno y las palabras_del_juego, va a llamar a 
    obtener_longitud_palabra para luego verificar que la palabra ingresada cumpla con las
    condiciones necesarias para usarse ,en caso contrario volvera a preguntar hasta devolver la palabra pedida.
    Autores: Dario y Luz
    '''
    palabra = input("Ingrese palabra: ")
    palabra_ingresada= palabra.lower()
    longitud_de_palabra= len(palabra_del_turno)
    palabra_valida=False
    while not palabra_valida:
        if len(palabra_ingresada) == longitud_de_palabra and palabra_ingresada.isalpha():
            palabra_valida=True
        else:
            print("Revise la palabra que escribio,la misma no debe contener espacios, caracteres especiales, numeros, y debe tener",longitud_de_palabra,"caracteres")
            palabra = input("Ingrese palabra: ")
            palabra_ingresada=palabra.lower()
    return palabra_ingresada

def confirmar_palabra(palabra_a_confirmar,lista_palabras_ingresadas,palabras_del_juego:list):
    '''
    Obj: Devuelve True o False dependiendo de si la palabra ingresada por el usuario 
    este en la lista de palabras del juego y a su vez que su posicion sea la correcta.
    Autor: Dario y Luz
    >>> confirmar_palabra('cabra', ['cabra', 'cabra'], ['ancla', 'cabra'])
    True
    >>> confirmar_palabra('cabra', ['cabra'], ['ancla', 'cabra'])
    False
    >>> confirmar_palabra('ancla', ['ancla'], ['ancla', 'cabra'])
    True
    '''
    lista_indices = [indice for indice, dato in enumerate(lista_palabras_ingresadas) if dato == palabra_a_confirmar]
    if palabra_a_confirmar in palabras_del_juego and palabra_a_confirmar == palabras_del_juego[lista_indices[-1]]:
        resultado = True
    else:
        resultado = False
    return resultado

def incrementar_error_jugador(validacion, error_jugador):
    '''    
    Autor: Dario y Luz
    >>> incrementar_error_jugador(True, 0)
    0
    >>> incrementar_error_jugador(False, 0)
    1
    '''
    if not(validacion):
        error_jugador+=1
    return error_jugador

def mostrar_rosco_letras(letras_participantes):
    '''
    Obj: Devuelve el rosco de las letras participantes
    Autor: Dario
    >>> mostrar_rosco_letras(['A','B','C'])
    '[A][B][C]'
    >>> mostrar_rosco_letras(['D','E','F'])
    '[D][E][F]'
    '''
    letras=''
    
    for letra in letras_participantes:
        letras += '['+letra.upper()+']'
    return letras

# ETAPA 9

def mostrar_rosco_jugadores(letras_participantes, lista_jugadores, lista_jugadores_por_turno, lista_resultados):
    '''
    Obj: Devuelve el rosco de jugadores, dependiendo de quien jugo en cada turno.
    Autores: Dario y Luz
    >>> mostrar_rosco_jugadores(['A','B','C'], ['Dario', 'Luchi'], [], [])
    '[ ][ ][ ]'
    >>> mostrar_rosco_jugadores(['D','E','F'], ['Dario','Luchi'], ['Dario','Dario','Luchi'], [True,False,True])
    '[1][1][2]'
    >>> mostrar_rosco_jugadores(['A','B','C'], ['Dario', 'Luchi'], ['Dario'], [True])
    '[1][ ][ ]'
    '''
    resultado=''
    indice_jugador = 1
    i = 0
    
        
    if len(lista_jugadores_por_turno) == 0:
        for letra in letras_participantes:
            resultado += '[ ]'
    else:
        for jugador in lista_jugadores_por_turno:
            indice_jugador = lista_jugadores.index(jugador) + 1
            if not(lista_resultados[i]):
                resultado += '['+str(indice_jugador)+']'
                if indice_jugador > len(lista_jugadores): indice_jugador = 1
            else:
                resultado += '['+str(indice_jugador)+']'
            i += 1
            
        espacios_vacios = len(letras_participantes) - len(lista_resultados)
        for vacio in range(0, espacios_vacios):
            resultado += '[ ]'
    return resultado

def mostrar_lista_participantes(diccionario_jugadores):
    '''
    Obj: Muestra por pantalla los jugadores activos con sus respectivos aciertos y errores.
    Autores: Dario y Luz
    '''
    print('\nJugadores:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' -  Aciertos: ' + str(diccionario_jugadores[jugador][ACIERTOS]) + ' - Errores: ' + str(diccionario_jugadores[jugador][ERRORES]))
    print('\n')

def resultado_palabra(lista_resultados,letras_participantes:list):
    '''
    Obj: Devuelve el rosco de aciertos y errores dependiendo del turno.
    Autor: Dario.
    >>> resultado_palabra([True, True, False],['A','B','C'])
    '[a][a][e]'
    >>> resultado_palabra([False, True, False],['A','B','C'])
    '[e][a][e]'
    >>> resultado_palabra([],['A','B','C'])
    '[ ][ ][ ]'
    '''
    respuesta=''
    if len(lista_resultados) == 0:
        for letra in letras_participantes:
            respuesta += '[ ]'
    else:
        for resultado in lista_resultados:
            if resultado:
                respuesta += '[a]'
            else:
                respuesta += '[e]'
        espacios_vacios = len(letras_participantes) - len(lista_resultados)
        for vacio in range(0, espacios_vacios):
            respuesta += '[ ]'
    return respuesta



# Funciones Etapa 5

def calcular_puntaje_partida(diccionario_jugadores, configuracion):
    """
    Obj: Calcula y devuelve el puntaje de una ronda determinada dados los aciertos y errores cometidos.
    Autores:Dario y Luz
    """
    puntos_acierto = int(configuracion['PUNTAJE_ACIERTO'])
    puntos_error = int(configuracion['PUNTAJE_DESACIERTO'])
    for jugador in diccionario_jugadores:
        puntaje = puntos_acierto*diccionario_jugadores[jugador][ACIERTOS]+puntos_error*diccionario_jugadores[jugador][ERRORES]
        diccionario_jugadores[jugador][PUNTAJE_PARTIDA] = puntaje

def mostrar_puntajes(diccionario_jugadores):
    """
    Obj: Muestra el puntaje de ronda y el total acumulado dados los aciertos y errores cometidos en la ronda
    actual.
    Autores:Dario y Luz
    """
    print('\n')
    print('Puntaje de la partida:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARTIDA]) + ' puntos')
    print('\n')
    print('Puntaje parcial:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARCIAL]) + ' puntos')

def modificar_lista_del_diccionario(validacion, nombre_j, lista_valores_jugador, diccionario_jugadores):
    '''
    Obj: Modifica la lista de valores de cada jugador en el diccionario_jugadores, dependiendo del 
    resultado de la validación.
    Autores: Dario y Luz
    '''
    if validacion:
            lista_valores_jugador[ACIERTOS] += 1
            diccionario_jugadores[nombre_j] = lista_valores_jugador
    else:
            lista_valores_jugador[ERRORES] += 1
            diccionario_jugadores[nombre_j] = lista_valores_jugador

def turnos(letra, largo_palabra, lista_jugadores, nombre_jugador):
    '''
    Obj: Muestra por pantalla el turno de la letra, el jugador a quien le toca y el 
    largo de la palabra.
    Autores: Dario y Luz
    '''
    print('Turno Jugador '+ str(lista_jugadores.index(nombre_jugador)+1) + ' ' + nombre_jugador + ' ' + '- letra '+ letra.upper() + ' - Palabra de '+ str(largo_palabra) + ' letras')

def mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, lista_palabras_ordenadas, lista_jugadores_por_turno):
    """
    Obj: Muestra por pantalla el resultado turno por turno de la ronda que acaba de concluir. 
    Autores: Luz y Dario
    """
    indice = 0
    numero_jugador = 1
    for palabra in lista_palabras_ingresadas:
        if palabra == lista_palabras_ordenadas[indice]:
            print('Turno letra '+ str(letras_participantes[indice]).upper() + ' Jugador ' + str(numero_jugador) + ' ' + lista_jugadores_por_turno[indice] + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - acierto')
        else:
            print('Turno letra '+ str(letras_participantes[indice]).upper() + ' Jugador ' + str(numero_jugador) + ' ' + lista_jugadores_por_turno[indice] + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - error - Palabra Correcta: ' + str(lista_palabras_ordenadas[indice]))
            numero_jugador += 1
        indice += 1

def setear_diccionario_jugadores(diccionario_jugadores):
    '''
    Obj: Setear en 0 los valores del diccionario a todos los jugadores, excepto el puntaje parcial.
    Autores: Dario y Luz
    >>> setear_diccionario_jugadores({'Dario': [3, 0, 30, 30], 'Luchi': [0, 0, 0, 0]})
    {'Dario': [0, 0, 30, 0], 'Luchi': [0, 0, 0, 0]}
    >>> setear_diccionario_jugadores({'Dario': [3, 1, 63, 33], 'Luchi': [2, 1, 23, 23]})
    {'Dario': [0, 0, 63, 0], 'Luchi': [0, 0, 23, 0]}
    '''
    for jugador in diccionario_jugadores : 
        diccionario_jugadores[jugador][PUNTAJE_PARTIDA] = 0
        diccionario_jugadores[jugador][ACIERTOS] = 0
        diccionario_jugadores[jugador][ERRORES] = 0
    return diccionario_jugadores

def agregar_puntaje_parcial(diccionario_jugadores):
    '''
    Obj: Agrega o suma el PUNTAJE_PARTIDA de cada jugadro al PUNTAJE_PARCIAL de cada jugador.
    Autores: Dario y Luz
    '''
    for jugador in diccionario_jugadores:
        diccionario_jugadores[jugador][PUNTAJE_PARCIAL] += diccionario_jugadores[jugador][PUNTAJE_PARTIDA]

def mostrar_tablero(letras_participantes,lista_jugadores_por_turno,palabras_del_juego, lista_jugadores, lista_resultados):
    '''
    Autores: Dario y Luz
    '''
    print(mostrar_rosco_letras(letras_participantes))
    print(mostrar_rosco_jugadores(letras_participantes, lista_jugadores, lista_jugadores_por_turno, lista_resultados))
    print(resultado_palabra(lista_resultados,letras_participantes))

def mostrar_reporte_final(diccionario_jugadores, numero_partidas):
    '''
    Obj: Muestra el puntaje Final de cada jugador.
    Autores: Dario y Luz
    '''
    print('\n')
    print('Reporte Final:')
    print('Partidas jugadas:' + str(numero_partidas))
    print('\n')
    print('Puntaje Final:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARCIAL]) + ' puntos')

def leer_configuracion():
    return open('.\configuracion.csv', 'r', encoding="utf8")

def jugar(letras_participantes,palabras_del_juego:list,definiciones:dict, lista_jugadores, diccionario_jugadores, configuracion):
    """
    Obj: Ejecuta el juego completo, interactuando con el usuario.
    Autores: Luz y Dario
    """
    turno=0
    error_jugador = 0
    lista_palabras_ingresadas = []
    lista_jugadores_por_turno = []
    lista_resultados = []
    while turno < len(palabras_del_juego):
        largo_palabra = len(palabras_del_juego[turno])
        letra = letras_participantes[turno]
        mostrar_tablero(letras_participantes,lista_jugadores_por_turno,palabras_del_juego, lista_jugadores, lista_resultados)
        nombre_jugador = lista_jugadores[error_jugador]
        lista_valores_jugador= [diccionario_jugadores[nombre_jugador][ACIERTOS], diccionario_jugadores[nombre_jugador][ERRORES], diccionario_jugadores[nombre_jugador][PUNTAJE_PARCIAL], 0]
        mostrar_lista_participantes(diccionario_jugadores)
        lista_jugadores_por_turno.append(nombre_jugador)
        turnos(letra ,largo_palabra, lista_jugadores, nombre_jugador)
        print('Definición: '+ definiciones[letras_participantes[turno]][palabras_del_juego[turno]])
        palabra_del_turno = palabras_del_juego[turno]
        palabra_ingresada=verificador_de_palabra(palabra_del_turno) 
        lista_palabras_ingresadas.append(palabra_ingresada)
        validacion = confirmar_palabra(palabra_ingresada,lista_palabras_ingresadas,palabras_del_juego)
        lista_resultados.append(validacion)
        modificar_lista_del_diccionario(validacion, nombre_jugador, lista_valores_jugador, diccionario_jugadores)
        error_jugador = incrementar_error_jugador(validacion, error_jugador)
        if error_jugador == len(lista_jugadores): error_jugador = 0
        turno += 1 
    mostrar_tablero(letras_participantes,lista_jugadores_por_turno,palabras_del_juego, lista_jugadores, lista_resultados)
    mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, palabras_del_juego, lista_jugadores_por_turno)
    calcular_puntaje_partida(diccionario_jugadores, configuracion) 
    agregar_puntaje_parcial(diccionario_jugadores)
    mostrar_puntajes(diccionario_jugadores) 
    setear_diccionario_jugadores(diccionario_jugadores)
    

def main():
    '''
    Autores: Dario y Luz
    '''
    
    #DEFINICIONES
    definiciones={}
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    contador_partidas = 1
    sigue_jugando = True
    cant_jugadores = preguntar_cant_jugadores()
    #PREARMADO DEL JUEGO
    definiciones = cargar_diccionario()
    lista_jugadores = listar_jugadores(cant_jugadores)
    diccionario_jugadores = cargar_diccionario_jugadores(lista_jugadores)
    
    #JUEGO
    while sigue_jugando:
        valores = leer_configuracion()
        configuracion = crear_dicc_de_valores(valores)
        valores.close()
        max_partidas = int(configuracion['MAXIMO_PARTIDAS'])
        print('\nLa configuracion es: ')
        for opcion in configuracion:
            print('\n' + f'{opcion}, {configuracion[opcion]}')
        letras_del_juego=seleccionar_letras(letras, configuracion) 
        palabras_del_juego=crear_palabras_del_juego(definiciones,letras_del_juego, configuracion)
        print('\n',palabras_del_juego)
    #POST Ronda(PUNTUACION+nueva partida)
        jugar(letras_del_juego,palabras_del_juego,definiciones, lista_jugadores, diccionario_jugadores, configuracion)
        if(contador_partidas < max_partidas):
            continua=input('\nDesea jugar otra partida? (s/n): ')
        else:
            print('\nLlegaste al máximo de partidas')
        acepta_continuar='s'
        if not continua.lower()==acepta_continuar or contador_partidas >= max_partidas:
            sigue_jugando=False
        else:
            contador_partidas += 1
    
    mostrar_reporte_final(diccionario_jugadores, contador_partidas)
    print(':::::::::::::::\n   GAME OVER\n:::::::::::::::')

if __name__ == "__main__":
    main()