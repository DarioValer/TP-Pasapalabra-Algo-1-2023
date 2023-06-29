import random
import copy
import doctest
import pandas as pd

#CONSTANTES
POSICION_PALABRA_INGRESADA = -1
ACIERTOS = 0
ERRORES = 1
PUNTAJE_PARCIAL = 2
PUNTAJE_PARTIDA = 3

#ETAPA_8
def cargar_diccionario():
    '''
    Autores: Dario y Luz
    '''
    diccionario = {}
    archivo_palabras = open("TP-Pasapalabra-Algo-1-2023\palabras.txt", "r", encoding="utf8")
    archivo_definiciones = open("TP-Pasapalabra-Algo-1-2023\definiciones.txt", "r", encoding="utf8")
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
    Autores: Dario y Luz
    '''
    archivo_csv = open(".\diccionario_ordenado.csv", "w", encoding="utf8")
    diccionario_ordenado = sorted(list(diccionario.items()), key = lambda x:x[0])
    for i in diccionario_ordenado:
        archivo_csv.write(str(i) + '\n')
    archivo_csv.close()

#ETAPA 9
def validar_nombre(nombre, longitud_palabra_minima):
    '''
    Autores: Dario y Luz

    >>> validar_nombre('Dario')
    True
    >>> validar_nombre('Edu')
    False
    >>> validar_nombre('Luchi')
    True
    '''
    respuesta = False
    largo_nom = len(nombre)
    if(largo_nom >= longitud_palabra_minima and largo_nom <= 20 and nombre.isalnum()):
        respuesta = True
    return respuesta

def preguntar_cant_jugadores():
    cant_jugadores = int(input('Ingrese la cantidad de jugadores (hasta un maximo de 4): '))
    while(cant_jugadores <= 0 or cant_jugadores > 4):
        cant_jugadores = int(input('el maximo de jugadores es 4! Ingrese nuevamente la cantidad: '))
    return cant_jugadores

def listar_jugadores(cant_jugadores, lista_de_valores):
    lista_jugadores = []
    longitud_palabra_minima = int(lista_de_valores[0][1])
    for i in range(1, cant_jugadores + 1):
        nombre = input('Ingrese el nombre del jugador '+ str(i) +': ')
        while(validar_nombre(nombre, longitud_palabra_minima) == False or (nombre in lista_jugadores)):
            nombre = input('El nombre ingresado no puede repetirse, debe contener como mínimo 4 caracteres y estos deben ser alfanumericos: ')
        lista_jugadores.append(nombre)
    return lista_jugadores

def cargar_diccionario_jugadores(lista_jugadores):
    '''
    Autores: Dario y Luz
    >>> cargar_diccionario_jugadores(['Dario', 'Luz', 'Agus'])
    {'Dario': [0, 0, 0, 0], 'Luz': [0, 0, 0, 0], 'Agus': [0, 0, 0, 0]}
    >>> cargar_diccionario_jugadores(['Dario', 'Damian', 'Demian'])
    {'Dario': [0, 0, 0, 0], 'Damian': [0, 0, 0, 0], 'Demian': [0, 0, 0, 0]}
    '''
    diccionario_jugadores = {}
    lista_de_valores = [0, 0, 0, 0]
    for nombre in lista_jugadores:
        if(nombre in diccionario_jugadores):
            while(nombre in diccionario_jugadores):
                nombre = input('Este nombre ya esta en uso, ingrese uno nuevo: ')
        diccionario_jugadores[nombre] = lista_de_valores
    return diccionario_jugadores

def mostrar_jugadores(diccionario_jugadores):
    num_jugador = 1
    print('jugadores:')
    for i in diccionario_jugadores.keys():
        print(str(num_jugador) +'. '+ i +' - aciertos: '+ str(diccionario_jugadores[i][ACIERTOS]) + ' - errores: ' + str(diccionario_jugadores[i][ERRORES]))
        num_jugador += 1

#ETAPA 10
def continuar_cambio_configuracion(pregunta):
    '''
    Autor: Dario
    >>> continuar_cambio_configuracion('n')
    False
    >>> continuar_cambio_configuracion('s')
    True
    '''
    respuesta = False
    if pregunta == 's' or pregunta == 'S':
        respuesta = True
    return respuesta

def pregunta_opcion():
    '''
    Autor: Luz
    '''
    opcion = int(input('Ingrese el numero de la opcion que desea modificar: '))
    while(0 > opcion or opcion > 4):
        opcion = int(input('La opcion debe estar entre 0 y 4: '))
    return opcion

def configuracion(configuracion_original, lista_de_valores):
    '''
    Autor: Luz y Dario
    '''
    pregunta = input('¿Desea modificar los valores de la configuración del juego? (s/n): ')
    respuesta = continuar_cambio_configuracion(pregunta)
    while(respuesta):
        print(configuracion_original)
        opcion = pregunta_opcion()
        if(opcion == 0):
            valor = int(input('Ingrese el valor: '))
            lista_de_valores[opcion][1] = valor
        elif(opcion == 1):
            valor = int(input('Ingrese el valor: '))
            lista_de_valores[opcion][1] = valor
        elif(opcion == 2):
            valor = int(input('Ingrese el valor: '))
            lista_de_valores[opcion][1] = valor
        elif(opcion == 3):
            valor = int(input('Ingrese el valor: '))
            lista_de_valores[opcion][1] = valor
        elif(opcion == 4):
            valor = int(input('Ingrese el valor: '))
            lista_de_valores[opcion][1] = valor
        pregunta = input('¿Desea seguir modificando? (s/n): ')
        respuesta = continuar_cambio_configuracion(pregunta)
    return lista_de_valores

#FUNCIONES ETAPA 3
def seleccionar_letras(letras_a_procesar, lista_de_valores):
    """
    Obj: Recibe una lista y devuelve otra con X elementos al azar únicos de la misma ordenados alfabeticamente. La long de la lista debe
    ser mayor que los X elementos deseados.
    Autores: Luz y Eduardo 
    """
    cant_letras = int(lista_de_valores[1][1])
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
    Autores:Eduardo y Luz
    """
    numero=random.randint(0,len(definiciones[letra_a_procesar].keys())-1)
    palabra=(list(definiciones[letra_a_procesar].keys()))[numero]
    return(palabra)

def crear_palabras_del_juego (definiciones, letras_participantes, longitud_palabra_minima):
    """
    Obj: Recibe el diccionario y una lista de letras participantes, selecciona una palabra al azar
    por cada una de tales letras y las retorna ordenadas alfabeticamente.  
    Autores:Eduardo y Luz
    """
    palabras_rosco=[]
    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        palabras_rosco.append(palabra)
        
    return (palabras_rosco)



#FUNCIONES ETAPA 1
def verificador_de_palabra(palabra_del_turno):
    '''
    La funcion verificador_de_palabra recibe el turno y las palabras_del_juego, va a llamar a 
    obtener_longitud_palabra para luego verificar que la palabra ingresada cumpla con las
    condiciones necesarias para usarse ,en caso contrario volvera a preguntar hasta devolver la palabra pedida.
    AUTOR: Dario y Luz.
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
    Esta funcion devuelve True o False dependiendo de si la palabra ingresada por el usuario 
    este en la lista de palabras del juego y a su vez que su posicion sea la correcta.
    AUTOR: Dario.
    '''
    lista_indices = [indice for indice, dato in enumerate(lista_palabras_ingresadas) if dato == palabra_a_confirmar]
    if palabra_a_confirmar in palabras_del_juego and palabra_a_confirmar == palabras_del_juego[lista_indices[-1]]:
        resultado = True
    else:
        resultado = False
    return resultado

def incrementar_aciertos_errores(validacion, cant_aciertos, cant_errores):
    '''    
    La funcion incrementar_aciertos_errores recibe palabra_ingresada,cant_aciertos, cant_errores,
    lista_palabras_ingresadas,palabras_del_juego va a llamar a la funcion confirmar_palabra,
    contara los aciertos y los errores y los devolvera.
    Autor:Sebastián
    
    >>> incrementar_aciertos_errores(True, 0, 0)
    (1, 0)

    >>> incrementar_aciertos_errores(False, 1, 0)
    (1, 1)

    >>> incrementar_aciertos_errores(False, 6, 0)
    (6, 1)

    '''
    if validacion:
        cant_aciertos+=1
    else:
        cant_errores+=1
    return cant_aciertos,cant_errores

def mostrar_rosco_letras(letras_participantes):
    '''
    Muestra por pantalla el rosco de las letras participantes
    AUTOR: Dario
    >>> mostrar_rosco_letras(['A','B','C'])
    '[A][B][C]'
    >>> mostrar_rosco_letras(['D','E','F'])
    '[D][E][F]'
    '''
    letras=''
    
    for letra in letras_participantes:
        letras += '['+letra.upper()+']'
    return letras

def mostrar_rosco_jugadores(letras_participantes, lista_jugadores, lista_palabras_ingresadas, palabras_del_juego):
    resultado=''
    indice_jugador = 1
    i = 0
    if len(lista_palabras_ingresadas) == 0:
        for letra in letras_participantes:
            resultado += '[ ]'
    else:
        while(indice_jugador <= len(lista_jugadores) and i < len(lista_palabras_ingresadas)):
            if confirmar_palabra(lista_palabras_ingresadas[i],lista_palabras_ingresadas,palabras_del_juego) == False:
                resultado += '['+str(indice_jugador)+']'
                indice_jugador += 1
            else:
                resultado += '['+str(indice_jugador)+']'
            i += 1
        espacios_vacios = len(letras_participantes) - len(lista_palabras_ingresadas)
        for vacio in range(0, espacios_vacios):
            resultado += '[ ]'
    return resultado

def resultado_palabra(lista_palabras_ingresadas:list,letras_participantes:list,palabras_del_juego:list):
    '''
    Muestra por pantalla [ ] vacios si todavia no se ingreso una palabra, una [e] si la palabra 
    ingresada es un error o una [a] si es un acierto.
    AUTOR: Dario.
    '''
    resultado=''
    if len(lista_palabras_ingresadas) == 0:
        for letra in letras_participantes:
            resultado += '[ ]'
    else:
        for ingresada in lista_palabras_ingresadas:
            if confirmar_palabra(ingresada,lista_palabras_ingresadas,palabras_del_juego) == True :
                resultado += '[a]'
            else:
                resultado += '[e]'
        espacios_vacios = len(letras_participantes) - len(lista_palabras_ingresadas)
        for vacio in range(0, espacios_vacios):
            resultado += '[ ]'
    return resultado

def mostrar_lista_participantes(diccionario_jugadores):
    print('\nJugadores:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' -  Aciertos: ' + str(diccionario_jugadores[jugador][ACIERTOS]) + ' - Errores: ' + str(diccionario_jugadores[jugador][ERRORES]))
    print('\n')
# Funciones Etapa 5

def calcular_puntaje_partida(diccionario_jugadores, lista_de_valores):
    """Calcula y devuelve el puntaje de una ronda determinada dados los aciertos y errores cometidos.
        Autor:Dario y Luz
    """
    puntos_acierto = int(lista_de_valores[3][1])
    puntos_error = int(lista_de_valores[4][1])
    for jugador in diccionario_jugadores:
        puntaje = puntos_acierto*diccionario_jugadores[jugador][ACIERTOS]+puntos_error*diccionario_jugadores[jugador][ERRORES]
        diccionario_jugadores[jugador][PUNTAJE_PARTIDA] = puntaje

def mostrar_puntajes(diccionario_jugadores):
    """Muestra el puntaje de ronda y el total acumulado dados los aciertos y errores cometidos en la ronda
    actual.
        Autor:Dario y Luz
    """
    print('\n')
    print('Puntaje de la partida:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARTIDA]) + ' puntos')
    print('\n')
    print('Puntaje parcial:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARCIAL]) + ' puntos')


def turnos(letra, largo_palabra, lista_jugadores, nombre_jugador):
    print('Turno Jugador '+ str(lista_jugadores.index(nombre_jugador)+1) + ' ' + nombre_jugador + ' ' + '- letra '+ letra.upper() + ' - Palabra de '+ str(largo_palabra) + ' letras')

def mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, lista_palabras_ordenadas, lista_jugadores_por_turno):
    """
    La funcion imprime por pantalla el resultado turno por turno de la ronda que acaba de concluir. 
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

def agregar_puntaje_parcial(diccionario_jugadores):
    for jugador in diccionario_jugadores:
        diccionario_jugadores[jugador][PUNTAJE_PARCIAL] += diccionario_jugadores[jugador][PUNTAJE_PARTIDA]

def mostrar_tablero(letras_participantes,lista_palabras_ingresadas,palabras_del_juego, lista_jugadores):
    print(mostrar_rosco_letras(letras_participantes))
    print(mostrar_rosco_jugadores(letras_participantes, lista_jugadores, lista_palabras_ingresadas, palabras_del_juego))
    print(resultado_palabra(lista_palabras_ingresadas,letras_participantes,palabras_del_juego))

def mostrar_reporte_final(diccionario_jugadores, numero_partidas):
    print('\n')
    print('Reporte Final:')
    print('Partidas jugadas:' + str(numero_partidas))
    print('\n')
    print('Puntaje Final:')
    for jugador in diccionario_jugadores:
        print(str(list(diccionario_jugadores.keys()).index(jugador)+1) + '. ' + jugador + ' - ' + str(diccionario_jugadores[jugador][PUNTAJE_PARCIAL]) + ' puntos')


def jugar(letras_participantes,palabras_del_juego:list,definiciones:dict, puntaje, lista_jugadores, diccionario_jugadores, lista_de_valores):
    """
    La funcion jugar es el encargado de mostrar por pantalla el tablero,tambien se encarga de manejar el juego
    interactuando con el usuario y mostrando como avanza la partida
    Autores:Luz y Dario
    """
    turno=0
    cant_aciertos= 0
    cant_errores= 0
    error_jugador = 0
    lista_palabras_ingresadas = []
    lista_jugadores_por_turno = []
    
    
    while turno < len(palabras_del_juego) and error_jugador < len(lista_jugadores) :

        largo_palabra = len(palabras_del_juego[turno])
        letra = letras_participantes[turno]
        mostrar_tablero(letras_participantes,lista_palabras_ingresadas,palabras_del_juego, lista_jugadores)
        nombre_jugador = lista_jugadores[error_jugador]
        lista_valores_jugador= [0, 0, diccionario_jugadores[nombre_jugador][PUNTAJE_PARCIAL], 0]
        mostrar_lista_participantes(diccionario_jugadores)
        lista_jugadores_por_turno.append(nombre_jugador)
        turnos(letra ,largo_palabra, lista_jugadores, nombre_jugador)
        print('Definición: '+ definiciones[letras_participantes[turno]][palabras_del_juego[turno]])
        palabra_del_turno = palabras_del_juego[turno]
        palabra_ingresada=verificador_de_palabra(palabra_del_turno) 
        lista_palabras_ingresadas.append(palabra_ingresada)
        validacion = confirmar_palabra(palabra_ingresada,lista_palabras_ingresadas,palabras_del_juego)
        aciertos, errores=incrementar_aciertos_errores(validacion, cant_aciertos, cant_errores)
        turno += 1 
        if errores == 1 : error_jugador += 1
        cant_aciertos = aciertos
        cant_errores = errores
        lista_valores_jugador[ACIERTOS] = cant_aciertos
        lista_valores_jugador[ERRORES] = cant_errores
        diccionario_jugadores[nombre_jugador] = lista_valores_jugador
        if error_jugador > int(lista_jugadores.index(nombre_jugador)):
            cant_aciertos = 0
            cant_errores = 0
    
    mostrar_tablero(letras_participantes,lista_palabras_ingresadas,palabras_del_juego, lista_jugadores)
    mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, palabras_del_juego, lista_jugadores_por_turno)
    calcular_puntaje_partida(diccionario_jugadores, lista_de_valores) 
    agregar_puntaje_parcial(diccionario_jugadores)
    mostrar_puntajes(diccionario_jugadores) 
    for jugador in diccionario_jugadores : 
        diccionario_jugadores[jugador][PUNTAJE_PARTIDA] = 0
        diccionario_jugadores[jugador][ACIERTOS] = 0
        diccionario_jugadores[jugador][ERRORES] = 0
    
    return puntaje
        
def main():
    
    #DEFINICIONES
    definiciones={}
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    puntaje = 0
    contador_partidas = 1
    jugando = 1
    continuar_jugando = True

    cant_jugadores = preguntar_cant_jugadores()
    configuracion_original = pd.read_csv('TP-Pasapalabra-Algo-1-2023\configuracion.csv')
    lista_de_valores = configuracion_original.to_numpy().tolist()

    #PREARMADO DEL JUEGO
    definiciones = cargar_diccionario()
    lista_jugadores = listar_jugadores(cant_jugadores, lista_de_valores)
    diccionario_jugadores = cargar_diccionario_jugadores(lista_jugadores)

    #JUEGO
    while(continuar_jugando):
        if(jugando > 1):
            lista_de_valores = configuracion_nueva.to_numpy().tolist()
        sigue_jugando = True
        while sigue_jugando:
            max_partidas = int(lista_de_valores[2][1])
            print('\nLa configuracion es: ')
            if(jugando > 1):
                print('\n', configuracion_nueva)
            else:
                print('\n', configuracion_original)
            letras_del_juego=seleccionar_letras(letras, lista_de_valores) 
            palabras_del_juego=crear_palabras_del_juego(definiciones,letras_del_juego)
            print('\n',palabras_del_juego)
        #POST Ronda(PUNTUACION+nueva partida)
            puntaje = jugar(letras_del_juego,palabras_del_juego,definiciones, puntaje, lista_jugadores, diccionario_jugadores, lista_de_valores)
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
        continua_jugando=input('\nDesea jugar de nuevo? (s/n): ')
        continuar = 's'
        if(continua_jugando == continuar):
            lista_nueva = configuracion(configuracion_original, lista_de_valores)
            configuracion_nueva = pd.DataFrame(lista_nueva)
            jugando += 1
            print(configuracion_nueva)
        else: 
            continuar_jugando = False
    print('\nGAME OVER')

if __name__ == "__main__":
    main()