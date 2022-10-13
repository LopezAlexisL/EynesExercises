import random, doctest


def new_matrix():

    """Funcion que genera matriz 2D randomizada de 5x5
    """

    m = []
    for _ in range(5):
        m.append([random.randint(1,5) for _ in range(5)])
    return m


def show_matrix(m):

    """Funcion que recibe una matriz como parametro\n
    Imprime la matriz original, y una nueva matriz con la matriz original y las posiciones de sus renglones y columnas"""

    print('-------MATRIZ ORIGINAL-------')
    for i in m:
        print(i)
    print('\n-------MATRIZ CON COORDENADAS-------')
    axis = [['',[0,1,2,3,4]]]
    axis += ([list((i,m[i])) for i in range(len(m))])
    for i in axis:
        print(i)


def consecutives(l):

    """Funcion que recibe una lista como parametro.\n
    Utiliza dos ciclos for para recorrer la lista y corroborar si los elementos numericos estan ordenados de forma creciente o decreciente.\n
    Retorna True si alguna de dichas condiciones se cumple
    
    >>> consecutives([1,2,3,4,0])
    True
    """

    res = False
    
    increasing = []
    for e in range(len(l)):
        if e < (len(l) - 1):
            if l[e] - l[e+1] == -1:
                increasing.append(1)
    
    decreasing = []
    for e in range(len(l)):
        if e < (len(l) - 1):
            if l[e] - l[e+1] == -1:
                decreasing.append(1)

    if increasing and sum(increasing) == 3 or decreasing and sum(decreasing) == 3:
        res = True
    return res
doctest.testmod(name='consecutives', verbose=True)


def check_lines(axis, index, list):

    """Funcion que recibe 3 parametros.\n
    Ejecuta una funcion dentro que corrobora si tiene elementos consecutivos dentro e imprime un mensaje acorde al resultado    
    """

    first = consecutives(list[:4])
    last = consecutives(list[1:])
    if first:
        print('Hay numeros consecutivos en el eje {eje}: {valor} desde la posicion 0 a 3 de la matriz'.format(eje=axis, valor=index))
    elif last:
        print('Hay numeros consecutivos en el eje {eje}: {valor} desde la posicion 1 a 4 de la matriz'.format(eje=axis, valor=index))
    



def get_rows(m):

    """Funcion que recibe una matriz como parametro y le asigna indice a cada elemento de los renglones matriz"""

    return [list((i,m[i])) for i in range(len(m))]


def get_columns(m):

    """Funcion que recibe una matriz como parametro y le asigna indice a cada elemento de las columnas de la matriz
    >>> get_columns([[1,1,1,4,5],[2,4,1,1,1],[5,4,3,2,1],[3,0,2,2,2],[1,5,1,4,1]])
    [[0, [1, 2, 5, 3, 1]], [1, [1, 4, 4, 0, 5]], [2, [1, 1, 3, 2, 1]], [3, [4, 1, 2, 2, 4]], [4, [5, 1, 1, 2, 1]]]
    """

    col = []
    for e in range(len(m)):
        r = []
        for i in range(len(m)):
            r.append(m[i][e])
        col.append(r)
    return [list((i,col[i])) for i in range(len(col))]
doctest.testmod(name='get_columns', verbose=True)

def run():
    matrix = new_matrix()
    show_matrix(matrix)
    row_matrix = get_rows(matrix)
    col_matrix = get_columns(matrix)

    for index, item in row_matrix:
        check_lines('y', index, item)
    
    for index, item in col_matrix:
        check_lines('x', index, item)

    

if __name__ == '__main__':
    run()