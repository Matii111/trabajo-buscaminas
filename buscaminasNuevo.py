import random
#crea una list que simula un tablero de buscaminas
def tableroNoVisible(tamanio):
    tablero = []
    tamanio +=1
    for i in range(tamanio):        
        tablero.append([])       
        for j in range(tamanio):
            tablero[i].append(0)            
    return tablero

#da el formato al tablero
def formatoTablero(tablero):
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

tableroTest = tableroNoVisible(tamanio)

formatoTablero(tableroTest)
print(tableroTest)
printTablero(tableroTest) 


