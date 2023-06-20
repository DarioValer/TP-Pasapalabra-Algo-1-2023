# Hasta ahora nuestro jugador, simplemente gana o pierde.
# En esta etapa vamos a permitir que obtenga puntaje y que el mismo se acumule de
# partida tras partida.
# Por cada palabra correcta el usuario suma 10 puntos, por cada palabra incorrecta el
# jugador pierde 3 puntos. El puntaje final obtenido podrá ser negativo.
# Al finalizar una partida, se le ofrecerá si desea jugar otra; así hasta que responda que
# no. El puntaje obtenido en la última partida, se tomará como inicio de la siguiente. Al
# inicio de la ejecución del 1er. juego, el puntaje se encuentra en cero.

def calcular_puntaje_ronda(cant_aciertos:int,cant_errores:int):
    """Calcula y devuelve el puntaje de una ronda determinada dados los aciertos y erores cometidos.
        Autor:Eduardo
    """
    PUNTOS_ACIERTO=10
    PUNTOS_ERROR=-3
    puntaje=0
    puntaje+= PUNTOS_ACIERTO*cant_aciertos+PUNTOS_ERROR*cant_errores
    return(puntaje)

def mostrar_puntajes(puntaje_anterior,cant_aciertos,cant_errores):
    """Muestra el puntaje de ronda y el total acumulado dados los aciertos y erores cometidos en la ronda
    actual.
        Autor:Eduardo
    """
    puntos_ronda=calcular_puntaje_ronda(cant_aciertos,cant_errores)
    print("Puntaje Final de esta ronda:",puntos_ronda)
    print("El puntaje total acumulado es:")
    print(puntaje_anterior+puntos_ronda)

#ESTE MAIN ES UNICAMENTE PARA PROBAR LAS FUNCIONES Y LA LOGICA QUE "JUEGA" SIGUE PARA ACUMULAR LOS PUNTOS
def main():
    sigue_jugando=True
    puntaje=0
    while sigue_jugando:

        aciertos=int(input("cuantos aciertos obtuvo?"))
        errores=int(input("cuantos errores obtuvo?"))
        mostrar_puntajes(puntaje,aciertos,errores)
        puntaje+=calcular_puntaje_ronda(aciertos,errores)
        continua=input("Desea jugar otra partida? Presione la tecla ""S"", cualquier otra para salir:")
        if continua.lower()=="s":
            sigue_jugando=True
        else:
            sigue_jugando=False

main()






