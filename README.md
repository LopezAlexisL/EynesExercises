## Ejercicios Eynes

# Ejercicio Simple

Mediante el uso de funciones e importando el modulo 'random' se genera una lista de 10 diccionarios con dos key 'id' y 'age' que es un valor numerico randomizado entre 1 y 100, y se recibe esa lista, se la ordena de menor a mayor segun la edad e imprime el valor del id del menor y del mayor

Funciones
- list_gen() -> list :genera una lista de diccionarios, ver su Docstrign

- list_sort() -> list :recibe una lista como parametro y la devuelve ordenada, mas informacion en su Docstring



# Ejercicio Matriz

- new_matrix() -> list : Genera una matriz de 2 dimensiones 5x5

- show_matrix() -> None : Param m:list, muestra por consola 2 matrices, una la original recibida por param, y otra que se le agrega 'coordenadas' de columnas y lineas

- consecutives() -> Bool : Param l:list, busca 4 numeros consecutivos ascendentes o descendentes, devuelve True si se encontró

- check_lines() -> None : Params axis:str, index:int, list:list, muestra por consola en caso de econtrarse numeros consecutivos devuelto por consecutives()

- get_columns() -> List : Param m:List, recibe una matriz 2D y obtiene sus valores por columnas junto con sus indice en el eje 'y'

- get_rows() -> List : Param m:List, recibe una matriz 2D y devuelve una matriz 2D agregandole su indice en el eje 'x'


# Ejercicio Clases

- Class Circulo: -> Object: param r:Int, devuelve un objeto de tipo Circulo con la capacidad para mostrar su area, perimetro, actualizar su valor de radio, y mostrar por consola informacion userfriendly

- set_radius() -> Float : recibe un valor por input del usuario y hace una validacion de que sea una valor numerico y positivo

- options() -> None : muestra por consola opciones para el usuario con las posibilidades de uso


## Test

Los ejercicios de simple.py & matriz.py incluyen doctest para las funciones que reciben algun parametro y tienen retorno