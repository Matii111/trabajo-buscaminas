import random
#Deja el tablero gucci
def tablero_gucci(tab,j,v):
    s = '  '
    con = 0
    ss = '   '
    conn = 0
    if conn == 0:
        print('    ',end='')
        print(v)
        conn = conn + 1
    for h in tab:
        for v in h:
            if con == j+1:
                con = 0
            if con == 0: 
                print(v,end=ss)
            else: print(v,end=ss)
            con = con + 1
        print()
    return ('')
#Crea el tablero no gucci
def tablero(j,i,m):
    tablero = []
    s = '  '
    num = i
    z = 65
    xd = 1
    c = chr(z)
    zz = 0
    si = ['1']
    if j >= 10:
        s = "   "
    for h in range(j):
        # if xd == num:
        #     print('   ',s.join(si))
        tablero.append([])
        if c not in tablero[h]:
            tablero[h].append(chr(z+zz))
            zz = zz + 1
            xd = xd + 1
            si.append(str(xd))
        for v in range(i):
            tablero[h].append(m)  
    return tablero
#Crea la lista de bombas
def tablero_73(bom_restantes,j):
    list_bomb = []
    v = []
    bomb = bom_restantes
    cxc = 0
    while not len(v) == bomb:
        bomb_x = random.randint(1,j)
        bomb_y = random.randint(1,j)
        list_bomb.append([])
        list_bomb[cxc].append(bomb_x)
        list_bomb[cxc].append(bomb_y)
        cxc= cxc + 1
        for i in list_bomb:
            if not i in v:
                v.append(i) 
    return v
#Planta las bombas en el tablero invisible, agregando las pistas
def enola_gay(tab_inv,bombb,bom_restantes,j):
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    xddd = 0
    zz = 0 
    jardani = 0
    while bom_restantes > 0 :
        for i in bombb:
            for n in i:
                xddd = xddd + 1
                if xddd == 1 :
                    k = n
                elif xddd == 2:
                    y = n
                    xddd = 0 
                    tab_inv[y-1][k] = '*'
                    if k <=j-1:
                        if tab_inv[y-1][k+1] != '*' and tab_inv[y-1][k+1] not in abc :
                            tab_inv[y-1][k+1] =  (tab_inv[y-1][k+1] + 1) #COOR DELTANTE(6)
                        if y > 1:    
                            if tab_inv[y-2][k+1] != '*'and tab_inv[y-2][k+1] not in abc :
                                tab_inv[y-2][k+1] = (tab_inv[y-2][k+1] + 1) #COOR ARRIBA DR.(3) 
                        if y <= j-1:       
                            if tab_inv[y][k+1] != '*' and tab_inv[y][k+1] not in abc : 
                                tab_inv[y][k+1] = (tab_inv[y][k+1] + 1) #COOR DEBAJO DR.(9)
                    if y <= j-1:
                        if tab_inv[y][k] != '*' and tab_inv[y][k] not in abc :
                            tab_inv[y][k] = (tab_inv[y][k] + 1) #COOR DEBAJO(8)
                        if tab_inv[y][k-1] != '*' and tab_inv[y][k-1] not in abc :
                            tab_inv[y][k-1] =  (tab_inv[y][k-1] + 1) #COOR DEBEAJO IZQ.(7)
                    if y > 1:
                        if tab_inv[y-2][k-1]  != '*'and tab_inv[y-2][k-1] not in abc :
                            tab_inv[y-2][k-1] =  (tab_inv[y-2][k-1] + 1) #COOR ARRIBA IZQ.(1)
                        if tab_inv[y-2][k] != '*' and tab_inv[y-2][k] not in abc :
                            tab_inv[y-2][k] = (tab_inv[y-2][k] + 1) #COOR ARRIBA(2)  
                    if tab_inv[y-1][k-1]  != '*' and tab_inv[y-1][k-1] not in abc :
                        tab_inv[y-1][k-1] =  (tab_inv[y-1][k-1] + 1) #COOR DETRAS(4) 
                    bom_restantes = bom_restantes -1
        return tab_inv
#Crea los numeros del tablero.
def num_tab(j):
    dea = 1
    tablero = []
    con = j
    while con > 0:
        if dea < 10:
            s = '   '
            tablero.append(str(dea))
            tablero.append(s)
        elif dea > 8:
            s = '  '
            tablero.append(str(dea))
            tablero.append(s)
        v = ''.join(tablero)
        con = con - 1
        dea = dea + 1
    return v
#Convierte las coordenadas ingresadas como STR en coordenadas validas en INT.
def kaleidoscope(reimu):
    c = 65
    cc = 1
    if len(reimu) == 2:
        k = reimu[0]
        y = int(reimu[1])
    
    if len(reimu) == 3:
        k = reimu[0]
        y = int(reimu[1:3])
    while c < 91:
        if k == chr(c):
            k = cc
            c = 90
        else: 
            c = c + 1
            cc = cc + 1
    k = cc-1
    k = k - 1
    y = y - 1
    return k,y
#agrega las bombas al tablero que se imprimirá en caso de perder
def enola_gay2(tab_inv,bombb,bom_restantes,j):
    xddd = 0
    zz = 0 
    jardani = 0
    while bom_restantes > 0 :
        for i in bombb:
            for n in i:
                xddd = xddd + 1
                if xddd == 1 :
                    k = n
                elif xddd == 2:
                    y = n
                    xddd = 0 
                    tab_inv[y-1][k] = '*'
        return tab_inv
menu = [1,2,3]
a = int(input('Escoge una opcion:     (1)   Generar Tablero:   (2)   Cargar tablero   (3)   Salir:  '))
while a not in menu:
    a = int(input('Escoge una opcion:     (1)   Generar Tablero:   (2)   Cargar tablero   (3)   Salir:  '))
if a == 1:
    dificultades = ['f','m','d','k','F','M','D','X']
    n_arch = str(input("Ingrese el nombre del archivo: "))
    archivo = open(n_arch,'r')
    num = archivo.readlines()
    numm = []
    for i in num:
        a = i.strip('\n')
        numm.append(a)
    archivo.close()
    j = int(numm[0])
    dificul = numm[1]

    if dificul == 'f' or dificul == 'F':
        bom_restantes = int((j*j)*0.1)

    if dificul == 'm' or dificul == 'M':
        bom_restantes = int((j*j)*0.15)

    if dificul == 'd' or dificul == 'D':
        bom_restantes = int((j*j)*0.2)
         
    if dificul == 'x' or dificul == 'X':
        bom_restantes = int((j*j)*0.3)
    
    bombb = tablero_73(bom_restantes,j)
    #Se reescribe el tamano del tablero en el archivo .txt , ademas de las coor de las bombas.
    si = len(n_arch)
    si = si - 4
    n_arch = n_arch[0:si] 
    archivowo = open(n_arch +'.sal','w')
    coco = 0
    archivowo.write(str(j))
    archivowo.write('\n')
    for i in bombb:
        for j in i:
            mimi = 64
            if coco == 0: 
                j = chr(mimi+j)
                archivowo.write(str(j))    
            if coco == 1:
                archivowo.write(str(j))
            if coco == 2:
                j = chr(mimi+j)
                archivowo.write('\n')
                archivowo.write(str(j))
                coco = coco - 2
            coco = coco + 1
    n_arch = n_arch + '.sal'
    archivowo.close()  
if a == 2:
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    namnam = str(input('Ingrese el nombre del archivo: '))
    #Se lee el archivo y se cambian las coordenadas del archivo .txt a unas validas para el tablero.
    takataka = open(namnam,'r')
    s = takataka.readlines() 
    bombb = []
    bombbb = []
    bombbbb =[]
    bombbbbb = []
    kanbaru = 0
    for i in s:
        if kanbaru == 0:
            j = int(i)
            kanbaru = kanbaru + 1
        else:
            a = i.strip('\n')
            bombb.append(a)
    takataka.close()
    o = -1
    for i in bombb:
        bombbb.append([])
        o = o + 1
        for k in i:
            c = 65
            cc = 1
            if k in abc:
                while c < 91:
                    if k == chr(c):
                        k = cc
                        c = 90
                        bombbb[o].append(k)
                    else: 
                        c = c + 1
                        cc = cc + 1
            else: 
                bombbb[o].append(k)
    for i in bombbb:
        if len(i) > 2:
            i[1] = int(i[1] + i[2])
            bombbbb.append([i[1],i[0]])

        else: bombbbb.append([int(i[1]),i[0]])

    bombb = bombbbb
    #Se hace uso de las funciones creadas para generar los tableros necesarios para el juego.
    bumbum = len(bombbbb)
    i = j
    tab = tablero(j,i,'.')
    tab_inv = tablero(j,i,0)
    tab_inv_part2 = tablero(j,i,'.')
    v = num_tab(j)
    enola_gay(tab_inv,bombb,bumbum,j)
    enola_gay2(tab_inv_part2,bombb,bumbum,j)
    ganar = True
    casillas_x_abrir = (j**2) - bumbum
    bomb_coloc = [] 
    #Comienza el juego, mientras la cantidad casillas_x_abrir sea > 0 y ganar sea disinto de TRUE no se podra ganar la partida.
    while casillas_x_abrir > 0:
        print(tablero_gucci(tab,j,v))
        reimu = str(input('Ingrese la casilla que desea abrir: ')).upper()
        while len(reimu) > 3 or len(reimu) < 2:
            reimu = str(input('Ingrese la casilla que desea abrir: ')).upper()
        k = kaleidoscope(reimu)[0]
        y = kaleidoscope(reimu)[1]
        while k > j-1 or y > j-1 or len(reimu) > 3  or len(reimu) < 2 or reimu[0] not in abc:
            reimu = str(input('Ingrese la casilla que desea abrir: ')).upper()
            k = kaleidoscope(reimu)[0]
            y = kaleidoscope(reimu)[1]
        tab[k][y+1] = tab_inv[k][y+1]
        tab_inv_part2[k][y+1] = tab_inv[k][y+1]
        if tab[k][y+1] == '*':
            ganar = False
            print(tablero_gucci(tab_inv_part2,j,v))
            print('PERDISTE')
            casillas_x_abrir = 0
        if [k,y] not in bomb_coloc:
            bomb_coloc.append([k,y]) 
            casillas_x_abrir = casillas_x_abrir - 1          
    if casillas_x_abrir == 0 and ganar == True:
        print(tablero_gucci(tab_inv,j,v))
        print('GANASTE')  
if a == 3:
    print('Gracias por jugar , hasta la proxima!!!')