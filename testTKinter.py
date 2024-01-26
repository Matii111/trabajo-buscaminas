import random
import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):        

    # funcion para iniciar un nuevo juego
    def crear_tablero_ui(self, rows, cols):                
        for i in range(rows):
            self.rowconfigure(i, weight=1)
        for j in range(cols):
            self.columnconfigure(j, weight=1)

        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
                
        bombas = self.bombas(rows-1)                
        
        insertar_bombas = self.insertar_bombas(self.tablero(rows-1), bombas)

        verificar_bombas = self.verificar_bombas(insertar_bombas)        

        for i in range(rows):                                    
            for j in range(cols):                
                button = ttk.Button(self, text='', command=lambda row=i, col=j: self.handle_button_click(row, col, rows, verificar_bombas))
                button.bind('<Button-3>', lambda event, row=i, col=j: self.handle_button_click_right(row, col, rows, verificar_bombas, event))
                if (j == 0 and i > 0):
                    button = ttk.Button(self, text=chr(64+i), command=lambda row=i, col=j: self.handle_button_click(row, col, rows, verificar_bombas))
                    button.bind('<Button-3>', lambda event, row=i, col=j: self.handle_button_click_right(row, col, rows, verificar_bombas, event))

                if (j > 0 and i == 0):
                    button = ttk.Button(self, text=j, command=lambda row=i, col=j: self.handle_button_click(row, col, rows, verificar_bombas))
                    button.bind('<Button-3>', lambda event, row=i, col=j: self.handle_button_click_right(row, col, rows, verificar_bombas, event))
                button.grid(row=i, column=j, sticky='nsew')
                self.buttons[i][j] = button  

        print('Tablero iniciado')
        

    #da estilo a los botones clickeados
    def set_button_value(self, row, col, rows, board_content):
        self.buttons[row][col]['text'] = board_content

        if(board_content == 'unSafe'):
                self.buttons[row][col]['text'] = ''
        if (board_content != 'safe' and board_content != 'unSafe' and board_content != ''):        
            self.buttons[row][col]['state'] = 'disabled'
            self.buttons[row][col]['style'] = 'TButton'
            self.contador_mov -= 1  
            print('>> Movimientos restantes: {}'.format(self.contador_mov))
            print('>> Posicion seleccionada: {},{}'.format(chr(64+row), col))
            if (self.contador_mov == 0):
                print('--FIN DEL JUEGO--')
                print('!Ganaste!')                
                messagebox.showinfo('Buscaminas', 'Haz terminado el tablero, ¡Felicidades!')                
                if (messagebox.askquestion('Buscaminas', 'Quieres jugar otro tablero?') == 'yes'):
                    self.contador_mov = int((((rows)-1)**2)-(((rows)-1)**2)*0.10)                    
                    self.crear_tablero_ui(rows, rows)
                    self.contador_mov = int(((rows)-1**2)-(((rows)-1**2)*0.10))                    
                else:
                    self.destroy()                    
        

    #reemplaza botones de tablero por valores de tablero con bombas
    def handle_button_click(self, row, col, rows, tablero):                
        empty_button = self.buttons[row][col]['text']                                
        board_content = ''        
        if (empty_button == '' ):
            board_content = str(tablero[row][col])        
        if (board_content == '*'):
            print('--FIN DEL JUEGO--')             
            messagebox.showinfo('¡Perdiste!', 'Has tocado una bomba. ¡Fin del juego!')
            self.crear_tablero_ui(rows, rows)
            self.contador_mov = int((((rows)-1)**2)-(((rows)-1)**2)*0.10)                   
        if (row > 0 and col > 0 and board_content != '*'):
            self.set_button_value(row, col, rows, board_content)                    
    
    #marca banderas
    def handle_button_click_right(self, row, col, rows, tablero, event):
        empty_button = self.buttons[row][col]['text']                                
        board_content = ''        

        if (empty_button == '' ):
            board_content = 'safe'

        if (empty_button == 'safe'):
            board_content = 'unSafe'

        if (board_content != ''):
            self.set_button_value(row, col, rows, board_content) 

        if (event.num == 3):
            print('Bomba marcada en: {},{}'.format(chr(64+row), col))
            
    #genera bombas en posiciones aleatorias
    def bombas(self, size):
        lista_bombas = []
        bombas = []
        posicion_lista_bombas = 0
        cantidad_bombas = (size*size)*0.10
        print('\nPosicion de bombas:')
        while len(bombas) < cantidad_bombas:
            bomba_pos_horizontal = random.randint(1, size)
            bomba_pos_vertical = random.randint(1, size)
            lista_bombas.append([])
            lista_bombas[posicion_lista_bombas].append(bomba_pos_horizontal)
            lista_bombas[posicion_lista_bombas].append(bomba_pos_vertical)
            posicion_lista_bombas += 1            
            for i in lista_bombas:                
                if not i in bombas:
                    bombas.append(i)
            print("{},{}".format(chr(64+i[0]), i[1]))
        print("\n")
        
        return bombas

    #crea tablero con medidas dadas
    def tablero(self, size):
        tablero = []
        size += 1
        for i in range(size):
            tablero.append([])
            for j in range(size):
                tablero[i].append(0)
        return tablero 

    #inserta bombas en tablero
    def insertar_bombas(self, tablero, bombas):
        for i in bombas:
            tablero[i[0]][i[1]] = '*'
        return tablero

    #verifica si hay bombas alrededor de cada posicion
    def verificar_bombas(self, tablero):
        rows, cols = len(tablero), len(tablero[0])

        for i in range(rows):
            for j in range(cols):
                if tablero[i][j] == '*':
                    if i+1 < rows and tablero[i+1][j] != '*':
                        tablero[i+1][j] += 1
                    if i-1 >= 0 and tablero[i-1][j] != '*':
                        tablero[i-1][j] += 1
                    if j+1 < cols and tablero[i][j+1] != '*':
                        tablero[i][j+1] += 1
                    if j-1 >= 0 and tablero[i][j-1] != '*':
                        tablero[i][j-1] += 1
                    if i+1 < rows and j+1 < cols and tablero[i+1][j+1] != '*':
                        tablero[i+1][j+1] += 1
                    if i-1 >= 0 and j-1 >= 0 and tablero[i-1][j-1] != '*':
                        tablero[i-1][j-1] += 1
                    if i+1 < rows and j-1 >= 0 and tablero[i+1][j-1] != '*':
                        tablero[i+1][j-1] += 1
                    if i-1 >= 0 and j+1 < cols and tablero[i-1][j+1] != '*':
                        tablero[i-1][j+1] += 1
        return tablero

    #inicia la interfaz grafica
    def __init__(self, rows, cols):
        super().__init__()
        self.geometry('700x600')
        self.resizable(0, 0)
        self.title('Buscaminas')
        self.crear_tablero_ui(rows, cols)
        self.style = ttk.Style(self)
        self.style.configure(
            'TButton', 
            font=('Helvetica', 12),
            background='gray',
            foreground='black',
            
            )                                    
        self.contador_mov = int((((rows)-1)**2)-(((rows)-1)**2)*0.10)
        print('asdadasda',self.contador_mov)

if __name__ == '__main__':
    app = App(7, 7)
    
    app.mainloop()
