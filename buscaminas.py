import string, random

MINA = "*"
ESPACIO_SIN_ABRIR = "."
ESPACIO_ABIERTO = "-"
LETRAS = "ABCDEF"
FILAS = len(LETRAS)
COLUMNAS = 6
tablero = []
HA_GANADO = False
HA_PERDIDO = False


def inicializar_tablero():
    global tablero
    tablero = []

    for fila in range(FILAS):
        tablero.append([])
        for columna in range(COLUMNAS):
            tablero[fila].append(ESPACIO_SIN_ABRIR)


def numero_a_letra(numero):

    return LETRAS[numero]


def letra_a_numero(letra):
    numero = LETRAS.index(letra)
    return numero


def obtener_indices_a_partir_de_coordenadas(coordenadas):

    letra = coordenadas[0:1]
    fila = letra_a_numero(letra)
    columna = int(coordenadas[1:2]) - 1
    return fila, columna


def colocar_minas_en_tablero(posiciones):
    global tablero
    for posicion in posiciones:
        fila, columna = obtener_indices_a_partir_de_coordenadas(posicion)
        tablero[fila][columna] = MINA


def iniciar_tablero_con_string(posiciones_string):
    posiciones_string = posiciones_string.upper()
    posiciones_separadas = []
    primera_posicion = posiciones_string[0:2]
    segunda_posicion = posiciones_string[2:4]
    tercera_posicion = posiciones_string[4:6]
    if not primera_posicion in posiciones_separadas:
        posiciones_separadas.append(primera_posicion)
    if not segunda_posicion in posiciones_separadas:
        posiciones_separadas.append(segunda_posicion)
    if not tercera_posicion in posiciones_separadas:
        posiciones_separadas.append(tercera_posicion)
    colocar_minas_en_tablero(posiciones_separadas)


def obtener_minas_cercanas(fila, columna):
    conteo = 0
    if fila <= 0:
        fila_inicio = 0
    else:
        fila_inicio = fila - 1
    if fila + 1 >= FILAS:
        fila_fin = FILAS - 1
    else:
        fila_fin = fila + 1

    if columna <= 0:
        columna_inicio = 0
    else:
        columna_inicio = columna - 1

    if columna + 1 >= COLUMNAS:
        columna_fin = COLUMNAS - 1
    else:
        columna_fin = columna + 1

    for f in range(fila_inicio, fila_fin + 1):
        for c in range(columna_inicio, columna_fin + 1):
            if f == fila and c == columna:
                continue
            if tablero[f][c] == MINA:
                conteo += 1
    return str(conteo)


def imprimir_tablero():
    print("")
    ultima_casilla = False
    print("  ", end="")
    for columna in range(COLUMNAS):
        print(str(columna + 1), end=" ")
    print("")
    numero_fila = 0
    for fila in tablero:
        letra = numero_a_letra(numero_fila)
        print(letra, end=" ")
        for numero_columna, dato in enumerate(fila):
            verdadero_dato = ""
            if dato == MINA:
                if HA_GANADO or HA_PERDIDO:
                    verdadero_dato = MINA
                else:
                    verdadero_dato = ESPACIO_SIN_ABRIR
            elif dato == ESPACIO_ABIERTO:
                verdadero_dato = obtener_minas_cercanas(numero_fila, numero_columna)
            elif dato == ESPACIO_SIN_ABRIR:
                verdadero_dato = "."

            print(verdadero_dato, end=" ")
        print("")
        numero_fila += 1
    if HA_GANADO:
        print("GANASTE")
    elif HA_PERDIDO:
        print("PERDISTE")


def abrir_casilla(coordenadas):
    global HA_GANADO, HA_PERDIDO, tablero
    fila, columna = obtener_indices_a_partir_de_coordenadas(coordenadas)
    elemento_actual = tablero[fila][columna]
    if elemento_actual == MINA:
        HA_PERDIDO = True
        return

    if elemento_actual == ESPACIO_SIN_ABRIR:
        tablero[fila][columna] = ESPACIO_ABIERTO
    if no_hay_casillas_sin_abrir():
        HA_GANADO = True


def no_hay_casillas_sin_abrir():
    for fila in tablero:
        for columna in fila:
            if columna == ESPACIO_SIN_ABRIR:
                return False
    return True


def solicitar_coordenadas():
    while True:
        coordenadas = input("Ingresa el string con las posiciones de las minas formato A2B2C3, A2 representa la primer mina, B2 la segunda y C3 la tercera: ")
        if len(coordenadas) == COLUMNAS:
            return coordenadas
        else:
            print("Coordenadas no válidas. Intenta de nuevo")


numeros = []
for i in range(3):
    numeros.append(random.randint(1,9))
print(numeros)

letras=[]
for i in range(3):
    letras.append(random.choice(string.ascii_letters))
    
print(letras)

total_minas = []
for i in range(len(numeros)-1):
    for j in range(len(letras)-1):
        lugar_minas = letras[j].upper() + str(numeros[i])
        total_minas.append(lugar_minas)
        j = j+1
        i = i+1
print(lugar_minas)
print(total_minas)


def solicitar_casilla():
    while True:
        casilla = input("Ingresa la casilla del tablero que quieres abrir, formato letraNumero(ej: A1): ")
        casilla = casilla.upper()
        if len(casilla) != 2:
            print("Debes introducir una letra y un número")
            continue
        if not casilla[0].isalpha():
            print("El primer valor debe ser una letra")
            continue
        if not casilla[1].isdigit():
            print("El segundo valor debe ser un número")
            continue
        if not casilla[0] in LETRAS:
            print("La letra debe estar en el rango " + LETRAS)
            continue
        if int(casilla[1]) <= 0 or int(casilla[1]) > COLUMNAS:
            print(f"El número debe estar en el rango 1-{COLUMNAS}")
            continue
        return casilla


def main():
    inicializar_tablero()
    coordenadas = solicitar_coordenadas()
    iniciar_tablero_con_string(coordenadas)
    imprimir_tablero()
    while not HA_PERDIDO and not HA_GANADO:
        casilla = solicitar_casilla()
        abrir_casilla(casilla)
        imprimir_tablero()


main()
