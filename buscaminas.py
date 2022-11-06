#No se puede hacer un tablero de mas de 9x9 xq la posicion es letra-numero y en 10 es letra-numero-numero

import random
mina = "*" #simbolo de mina
espaciosinabrir = "." #espacio sin abrir
espacioabierto = "-" #espacio abierto
tablerodejuego = [] #matriz del tablero
ganaste = False
perdiste = False
nivel = 0 #nivel de juego, hay 3 niveles:
bandera="X" #lo q aparece en el juego 
banderamina="Z" #interno para comprobar

def elegirnivel():
    etiquetas="" #la columna de etiquetas para cada fila
    filas,columnas=0,0
    nivel=0
    while nivel<1 or nivel> 4:
        try:
            nivel = int(input("Elegir nivel 1, 2, 3 o 4: "))
        except ValueError:
            print("Solo se aceptan NUMEROS entre el 1 y el 4")
    if nivel == 1:
        etiquetas = "ABCDEF"
    elif nivel == 2:
        etiquetas = "ABCDEFG"
    elif nivel == 3:
        etiquetas = "ABCDEFGH"
    else:
        etiquetas = "ABCDEFGHI"
    filas = len(etiquetas)
    columnas = len(etiquetas)
    return etiquetas, filas, columnas, nivel

def armartableroinicial(filas, columnas): #arma el tablero inicial sin minas con los puntos
    for f in range(filas):
        tablerodejuego.append([])
        for c in range(columnas):
            tablerodejuego[f].append(espaciosinabrir)

def crearcoordenadasminas(columnas, nivel, etiquetas): #crea las coordenadas de las minas segun los niveles (NO PONE LAS MINAS EN EL TABLERO)
    minas = ""
    if nivel == 1:
        for i in range(6): 
            minas += random.choice(etiquetas) + str(random.randint(1,columnas))
    elif nivel == 2:
        for i in range(12):
            minas += random.choice(etiquetas) + str(random.randint(1,columnas))
    elif nivel == 3:
        for i in range(18):
            minas += random.choice(etiquetas) + str(random.randint(1,columnas))
    else:
        for i in range(24):
            minas += random.choice(etiquetas) + str(random.randint(1,columnas))
    return minas
#Se podria trabajar con las posiciones numericas

def verificarnorepe(minas): #verifica que no hay minas repetidas
    largo=int(len(minas)//2)#es la mitad porque agarrar de a duplas A1
    ad=0 #adicional
    repe=False #repetidas
    for i in range(largo-1): #es uno menos porque no compara al principio contra si mismo
        for j in range(1,largo):
            if minas[i*2:i*2+2] == minas[j*2+ad:j*2+2+ad]: 
                repe=True
        largo=largo-1
        ad=ad+2
    return repe

def minaseneltablero(etiquetas, minas, nivel): #Minas en el tablero colocadas y en formato matriz vector
    minasenmatriz = [] #matriz/lista
    cantidaddeminas=nivel*6
    for i in range(cantidaddeminas):
        minasenmatriz.append(minas[i*2:i*2+2])
    #print(minasenmatriz)  #matriz con las minas para probar
    for j in minasenmatriz: 
        fila, columna = convierteminasaposicion(etiquetas, j)
        tablerodejuego[fila][columna] = mina 
        #agrega con la posicion al tablero las minas "*"
        #convertir el string en un vector de numeros Y va a agregar las minas al tablero

def convierteminasaposicion(etiquetas, minas): #pasa las minas en formato letra,numero a posicion en numero,numero (ej A1, 0,0)
    letra = minas[0:1] #Siempre manda 1x1 
    fila = letra_a_numero(etiquetas, letra)
    columna = int(minas[1:2]) - 1 #Ej: viene 3 el numero pero las posiciones arrancan en 0 le saca 1 
    return fila, columna #pasa el las minas (ej:A3) como posiciones(0,2) asi lo agrega

def conviertedatoaposicion(etiquetas, casilla):
    letra = casilla[0:1]
    fila = letra_a_numero(etiquetas, letra)
    columna = int(casilla[1:2]) -1
    return fila, columna
        

def letra_a_numero(etiquetas, letra): #Devuelve el numero de la letra dentro de la etiqueta
    numero = etiquetas.index(letra)
    return numero

def numero_a_letra(etiquetas, numero): #para imprimir tablero

    return etiquetas[numero] 

def obtener_minas_cercanas(filas, columnas, fila, columna): #cuenta cuantas minas hay alrededor de la posicion q uno le da
    conteo = 0                                              #algo parecido se puede hacer para abrir si da 0 
    if fila <= 0:
        fila_inicio = 0
    else:
        fila_inicio = fila - 1
    if fila + 1 >= filas:
        fila_fin = filas - 1
    else:
        fila_fin = fila + 1

    if columna <= 0:
        columna_inicio = 0
    else:
        columna_inicio = columna - 1

    if columna + 1 >= columnas:
        columna_fin = columnas - 1
    else:
        columna_fin = columna + 1

    for f in range(fila_inicio, fila_fin + 1):
        for c in range(columna_inicio, columna_fin + 1): #en vez de q chequee mas 1, chequea hasta que no hay mas 0 para abrir las casillas
            if f == fila and c == columna:
                continue
            if tablerodejuego[f][c] == mina or tablerodejuego[f][c] == banderamina:
                conteo += 1
    return str(conteo)

def imprimirtableroinicial(etiquetas, filas, columnas): #Solo lo imprime 1 vez
    print("") #decoracion 
    print("  ", end="") #desplaza la linea dos blancos para que quede alineado los numeros con el tablero y el end,para q no salte la linea
    for columna in range(columnas):
        print(columna+1,end=" ")#(str(columna + 1), end=" ")#para q lo tranforma en texto al pedo total 
    print("")#salta un renglon
    numero_fila = 0
    for fila in tablerodejuego:
        letra = numero_a_letra(etiquetas, numero_fila)#toma la letra y la ubica en el tablero
        print(letra, end=" ")
        for numero_columna, dato in enumerate(fila): 
            print(".", end=" ")
        print("")
        numero_fila += 1
        #Imprimi el tablero normal con todos los puntos


def imprimirtablero(etiquetas, filas, columnas): #imprime el tablero y decide si ganaste o perdiste
    print("") #decoracion 
    print("  ", end="") #desplaza la linea dos blancos para que quede alineado los numeros con el tablero y el end,para q no salte la linea
    for columna in range(columnas):
        print(columna+1,end=" ")#(str(columna + 1), end=" ")#para q lo tranforma en texto al pedo total 
    print("")#salta un renglon
    numero_fila = 0
    for fila in tablerodejuego:
        letra = numero_a_letra(etiquetas, numero_fila)#toma la letra y la ubica en el tablero
        print(letra, end=" ")
        
        #verdadero_dato = lo que te va a imprimir 
        #a partir de abajo comprueba si gano o perdio y te oculta las minas 
        for numero_columna, dato in enumerate(fila): #chequea en todas las filas que no este la mina 
            verdadero_dato = ""
            if dato == mina:
                if ganaste or perdiste:
                    verdadero_dato = mina
                else:
                    verdadero_dato =  espaciosinabrir #mina para probar
            elif dato == espacioabierto:
                verdadero_dato = obtener_minas_cercanas(filas, columnas, numero_fila, numero_columna)
            elif dato == espaciosinabrir:
                verdadero_dato = "."
            elif dato == bandera or dato == banderamina:
                verdadero_dato = bandera
            print(verdadero_dato, end=" ")
        print("")
        numero_fila += 1
    if ganaste:
        print("GANASTE")
    elif perdiste:
        print("PERDISTE")

def solicitarcasilla(etiquetas, columnas): #pregunta que casilla queres abrir 
    while True:
        casilla = input("Ingresa la casilla del tablero que quieres abrir: ")
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
        if not casilla[0] in etiquetas:
            print("La letra debe estar en el rango " + etiquetas)
            continue
        if int(casilla[1]) <= 0 or int(casilla[1]) > columnas:
            print(f"El número debe estar en el rango 1-{columnas}")
            continue
        return casilla
    
def ingreseopcion():
    qhacer=0
    while qhacer<1 or qhacer>2:
        try:
            qhacer=int(input("Marque 1 para excavar | Marque 2 para colocar/quitar bandera: "))
        except ValueError:
            print("Debe ingresar 1 o 2 para decidir que hacer con la casilla seleccionada")
    return qhacer

def manejobandera(etiquetas, casilla):
    fila, columna = conviertedatoaposicion(etiquetas, casilla)
    dato = tablerodejuego[fila][columna]
    #print(casilla) chequeo
    #print(fila,columna) fila columna de la casilla selecionada
    #print(dato) que hay o punto o mina o abierto 
    if dato == espaciosinabrir:
        tablerodejuego[fila][columna] = bandera
    if dato == mina:
        tablerodejuego[fila][columna] = banderamina
    if dato == espacioabierto:
        tablerodejuego[fila][columna] = espacioabierto
    if dato == bandera:
        tablerodejuego[fila][columna] = espacioabierto #saca la bandera y vuelve el .
    if dato == banderamina:
        tablerodejuego[fila][columna] = mina
    return 
        

def abrir_casilla(etiquetas, minas): 
    global ganaste, perdiste
    fila, columna = convierteminasaposicion(etiquetas, minas)
    elemento_actual = tablerodejuego[fila][columna]
    if elemento_actual == mina:
        perdiste = True
        return
    if elemento_actual == espaciosinabrir: 
        tablerodejuego[fila][columna] = espacioabierto 
    if no_hay_casillas_sin_abrir():
        ganaste = True


def no_hay_casillas_sin_abrir(): 
    for fila in tablerodejuego:
        for columna in fila:
            if columna == espaciosinabrir or columna == bandera: #    "CHEQUEADO"
                return False
    return True

def main():
    etiquetas, filas, columnas, nivel = elegirnivel()
    armartableroinicial(filas,columnas)
    minas=crearcoordenadasminas(columnas, nivel, etiquetas)
    print("Calculando...",end="") #mas de 3, es q hubo minas repetidas y volvio a calcular 
    while verificarnorepe(minas)==True:
        print(".",end="") #verifica las minas repetidas y las cambia todas hasta q sean todas distintas 
        minas=crearcoordenadasminas(columnas, nivel, etiquetas)
    print()
    print("Listo, minas ubicadas")
    minaseneltablero(etiquetas,minas,nivel)    
    imprimirtableroinicial(etiquetas,filas,columnas)
    while not perdiste and not ganaste:
        casilla=solicitarcasilla(etiquetas,columnas)
        #print(casilla)
        opcion=ingreseopcion()
        if opcion == 1:
            abrir_casilla(etiquetas, casilla)
            #print(casilla)
        elif opcion == 2:
            manejobandera(etiquetas, casilla)
        imprimirtablero(etiquetas,filas,columnas)
        
#si lleno todo de banderas, falla la primera si la quiero sacar
main()