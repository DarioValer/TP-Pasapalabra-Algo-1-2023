
# En esta variante del juego, se seleccionarán al azar 10 letras de todo el conjunto de
# letras para formar el rosco.

# Ahora que tenemos nuestro diccionario, podremos utilizarlo para obtener una palabra
# candidata de cada letra a adivinar.

# Escribí una función, que reciba como primer parámetro el diccionario y como segundo la
# lista de letras participantes. La función deberá devolver aleatoriamente una palabra que
# empiece con cada letra participante de entre todas las posibles, esto será retornado
# como una lista de palabras ordenadas alfabéticamente.

# Para probar tu función, utiliza un ciclo que la invoque al menos 100 veces, y analiza lo
# que obtienes como palabras a adivinar. Repite el proceso varias veces.
# Además de la función principal de esta etapa, puedes escribir todas las que consideres
# necesarias, teniendo en cuenta los conceptos aprendidos en clase sobre programación
# estructurada y programación modular.
# Lista de letras que deben procesar:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
# 'x', 'y', 'z']

import random

def seleccionar_letras(letras_a_procesar:list):
    """
    Obj: Recibe una lista y selecciona X elementos al azar únicos de la misma. La long de la lista debe
    ser mayor que los X elementos deseados.
    Autores: Luz y Eduardo 
    """
    letras_participantes=[]
    ya_salieron=[]
    CANT_LETRAS=10

    for i in range(CANT_LETRAS):
        numero_de_letra=random.randint(0,len(letras_a_procesar)-1)
        letra=letras_a_procesar[numero_de_letra]
        while letra in ya_salieron:
            numero_de_letra=random.randint(0,len(letras_a_procesar)-1)
            letra=letras_a_procesar[numero_de_letra]
        letras_participantes.append(letra)
        ya_salieron.append(letra)

    return(letras_participantes)

def conseguir_palabra(definiciones:dict, letra_a_procesar:str):
    """
    Obj: Recibe el diccionario y una letra, retorna una palabra al azar del 
    diccionario que empieza con tal letra.
    Autores:Eduardo y Luz
    """
    numero=random.randint(0,len(definiciones[letra_a_procesar].keys())-1)
    palabra=(list(definiciones[letra_a_procesar].keys()))[numero]
    return(palabra)

def crear_palabras_del_juego (definiciones:dict, letras_participantes:list):
    """
    Obj: Recibe el diccionario y una lista de letras participantes, selecciona una palabra al azar
    por cada una de tales letras y las retorna ordenadas alfabeticamente.  
    Autores:Eduardo y Luz
    """
    palabras_rosco=[]
    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        palabras_rosco.append(palabra)
    rosco_ordenado=sorted(palabras_rosco)
    
    return (rosco_ordenado)
        
def main():
    prueba={"a":{
            "avion":"cosa que vuela",
            "azul":"color del mar","aguila":"pajaro que vuela y cazador"},
            "b":{
            "boludo":"estudiante de fiuba",
            "barco":"transporte que se usa para navegar"},
            "c":{
            "casa":"hogar dulce hogar",
            "cebolla":"vegetal que te hace llorar"},
            "d":{
            "diestro":"escribe derecho"},
            "e":{
            "eduardo":"yo","estrella":"cuerpo celeste que irradia energia",
            "excelente":"dicese de una accion realizada de forma sobresaliente"},
            "f":{
            "floricienta":"serie vieja"},
            "g":{
            "gato":"mascota mas bonita y hermosa"},
            "h":{
            "hueco":"agujero pero dicho mas fino"},
            "i":{
            "inodoro":"asiento del baño"},
            "j":{
            "jirafa":"animal cuello largo"},
            "k":{
            "kilo":"unidad de masa"},
            "l":{
            "luz":"lo que tira el foquito en el techo"},
            "m":{
            "mama":"mi ---- me quiere mucho"},
            "n":{
            "naranja":"fruta o color"},
            "o":{
            "opera":"galletitas o lugar donde canta la gente"},
            "p":{
            "papá":"progenitor que no es mama","pene":"organo reproducto masculino"},
            "q":{
            "queso":"alimento lacteo que se usa para la pizza"},
            "r":{
            "raton":"animalito o persona tacaña"},
            "s":{
            "sal":"lo que le pones a la comida para que sea salada",
            "suerte":"elemento azarozo que siempre me esquiva"},
            "t":{
            "teatro":"lugar donde hay actores","tarro":"contenedor"},
            "u":{
            "uva":"fruta que se obtiene de los viñedos"},
            "v":{
            "vaca":"nos da la leche","vino":"bebida fermentada a partir de uvas"},
            "w":{
            "waterpolo":"deporte acuatico"},
            "x":{
            "xenofobo":"persona que odia extranjeros"},
            "y":{
            "yogurt":"alimento lacteo que se obtiene por fermentacion"},
            "z":{
            "zebra":"importante jugueteria de Buenos Aires","zodiacal":"un tipo de horoscopo"}}

    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']

    for i in range(0,5):
        letras_participantes=seleccionar_letras(letras)
        print(crear_palabras_del_juego(prueba,letras_participantes))

main()

    
