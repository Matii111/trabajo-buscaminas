import random
#crea una lista que simula un tablero de buscaminas
def tableroNoVisible(tamanio):
    tablero = []
    tamanio +=1
    for i in range(tamanio):        
        tablero.append([])       
        for j in range(tamanio):
            tablero[i].append(0)            
    return tablero

#da el formato al tablero
def tableroVisible(tablero):
    letrasHorizontales = 65
    numerosVerticales = 0
    posicionHorizontal =0
    for i in tablero:                  
        i[0] = numerosVerticales   
        for j in i:                
            if numerosVerticales == 0 and posicionHorizontal > 0:
                i[posicionHorizontal] = chr(letrasHorizontales)
                letrasHorizontales +=1
            posicionHorizontal +=1
        numerosVerticales +=1
    return tablero

#imprime el tablero
def printTablero(tablero):
    contador = 0
    for i in tablero:                
        for j in i:
            if contador > 0:
                print(j,end="  ")
            else:
                contador +=1
                print("  ",end=" ")
        print("\n")

#crea bombas en las dimensiones y las agrega a una lista de bombas comprobadas para comprobar si no se repiten
def tableroBomba(tamanioTablero,dificultad):
    listaBombas = []
    bombasComprobadas = []
    posListaBombas = 0
    while len(bombasComprobadas) < dificultad:
        bombaPosHorizontal = random.randint(1,tamanioTablero)
        bombaPosVertical = random.randint(1,tamanioTablero)
        listaBombas.append([])
        listaBombas[posListaBombas].append(bombaPosHorizontal)
        listaBombas[posListaBombas].append(bombaPosVertical)
        posListaBombas +=1
        for i in listaBombas:
            if not i in bombasComprobadas:
                bombasComprobadas.append(i)
    return bombasComprobadas

#inserta en un tabler la lista de las posiciones de las bombas
def plantarBombas(tablero,listaBombas):
    bombasRestantes = len(listaBombas)
    while bombasRestantes > 0:
        for i in listaBombas:              
            for j in i:                     
                tablero[i[1]][i[0]] = "*"
        bombasRestantes -= bombasRestantes    
        return tablero
#comprueba las posiciones para definir las pistas para las bombas   
''''
Si encuentra una bomba comienza con las posiciones
las pistas seran la forma:
╔═╦═╦═╗
║1║2║3║
╠═╬═╬═╣
║4║B║6║
╠═╬═╬═╣
║7║8║9║
╚═╩═╩═╝
Donde 'B' es la bomba
'''     
def pistasTablero(tablero):
    posHorizontal = 0
    posVertical = 0
    tamanio = len(tablero[0]) -1 
    for i in tablero:        
        for j in i:        
            if j == "*":   
                #condiciones para pista '6'
                if posHorizontal+1 <= tamanio and tablero[posVertical][posHorizontal+1] != "*":                                                                                        
                    tablero[posVertical][posHorizontal+1] += 1
                #condiciones para pista '4'
                if posHorizontal-1 >= 1 and tablero[posVertical][posHorizontal-1] != "*":
                    tablero[posVertical][posHorizontal-1] += 1
            if not posHorizontal == tamanio:
                posHorizontal += 1      
            elif posVertical == tamanio and posHorizontal == tamanio:
                return tablero                      
            else:
                posHorizontal = 0
                posVertical +=1    

#TODO: CREAR FUNCION PARA INTRODUCIR BOMBAS A LA LISTA YA CREADAD
#TODO: CREAR FUNCION PARA PLANTAR BOMBAS EN LAS COORDENADAS DE LA FUNCION ANTERIOR
#TODO: CREAR FUNCION PARA LEER ARCHIVOS
#TODO: CREAR FUNCION PARA ESCRIBIR ARCHIVOS
#TODO: CREAR CONDICIONES PARA GANAR Y PERDER


# opcionMenu = 0
# while opcionMenu > 3 or opcionMenu < 1:
#     opcionMenu = int(input("Escoga una opcion: \n\
#         (1) Generar tablero\n\
#         (2) Cargar tablero\n\
#         (3) SALIR\n"))    

tamanio = 9
#se crea tablero no visible para posiciones y bombas
tableroTest = tableroNoVisible(tamanio)
#se crea tablero visible con la misma informacion pero mejor disenio
tableroTestVisual = tableroVisible(tableroNoVisible(tamanio))
#se crea lista de las posiciones de las bombas
listaBombas = tableroBomba(tamanio,5)
#se insertan las bombas en el tablero
tableroTest = plantarBombas(tableroTestVisual,listaBombas)



pistasTablero(tableroTest)
printTablero(tableroTest)
print("\n")
print(listaBombas)





