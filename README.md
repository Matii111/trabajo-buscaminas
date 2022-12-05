# Trabajo Buscaminas en Python 

Este repositorio contiene tanto el programa como la documentación respectiva (que en su momento no fue realizada) para un proyecto de primer año de programación. 

## Objetivo 

El objetivo de este proyecto fue elaborar un minijuego de buscaminas con reglas y jugabilidad modificada (la cual será explicada más adelante), con esto se buscó que el estudiante aprendiera conceptos básicos de programación, principalmente en Python, a manejar listas y buscar en las mismas, además de aprender a leer y escribir archivos. 

## Reglas del juego 

  + El juego es similar a un buscaminas de toda la vida, hay un tablero con sus respectivas casillas y hay que "abrirlas" todas para ganar el juego.  

  + Cada casilla tiene su correspondiente coordenada, tanto para posición vertical como horizontal, similar a un tablero de ajedrez con números en la parte superior para las coordenadas horizontales y números al costado izquierdo para las verticales. 

  + Para ingresar las coordenadas se debe ingresar primero la letra de la fila y luego el numero de la columna, ambos valores juntos sin importar si es mayúscula o minúscula. 

  + De esta manera se irán abriendo las cajas una a una hasta completar el tablero. 

  + Si se cae en una casilla de bomba perderás automáticamente y se mostraran las posiciones de las bombas y la de las casillas abiertas al momento de perder. 

  ### Pistas 

  + En este juego se llama pista al número de 0 en adelante que rellena cada casilla abierta de la siguiente manera:
  
    <p align="center">
      <img src="https://github.com/Matii111/trabajo-buscaminas/blob/master/bombaIMG1.png?raw=true" width="200">
    </p>
    
  + Esto indica cuantas bombas están cerca de esta posición en un radio de 1 desde el centro de la bomba incrementando en 1 si la posición entre dos bombas coincide     como se muestra a continuación:
  
  <p align="center">
    <img src="https://github.com/Matii111/trabajo-buscaminas/blob/master/bombaIMG2.png?raw=true" width="500">
  </p>

## Flujo del programa 

  + El programa comienza con un menú en terminal que da 3 opciones:  

    + Generar tablero, opción que solicita el nombre de un archivo .txt el cual a continuación es leído para encontrar en la primera línea el tamaño del tablero (por       ejemplo, si el número es 6 la dimensión es 6x6, 8 será 8x8, etc.), la segunda línea será una letra F, M, D y X el cual representa una dificultad: fácil, medio,         difícil y extremo, respectivamente. Es importante destacar que la dificultad se diferencia en la cantidad de bombas en tablero. 
    Tras ser leído, se crea un archivo .sal que contine las dimensiones del tablero en la primera línea y las siguientes líneas serán las posiciones de las bombas         indicadas por una letra para las coordenadas de las filas y un numero para las columnas. 

    + Cargar tablero, es la opción que lee el archivo .sal anteriormente creado generando un tablero con esas dimensiones y las bombas en dichas coordenadas. 

    + Salir, dicha opción es literalmente para salir del menú. 

  + Importante: Para iniciar el programa es necesario tener un archivo inicial .txt que contiene las dimensiones y la dificultad. 
