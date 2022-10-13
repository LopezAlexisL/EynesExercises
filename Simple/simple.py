import random, doctest


def list_gen():
    """
    No toma argumentos \n
    Devuelve una lista de diccionarios
    con dos key 'id' y 'age'
    """
    list_of_dict = []
    for i in range(1, 11):
        age = random.randint(1, 100)
        dictionary = {'id': i,
        'age': age}
        list_of_dict.append(dictionary)
    return list_of_dict


def list_sort(l):
    """
    Recibe un parametro 'l': list() \n
    de diccionarios con la estructura {'id':int, 'age':int} \n
    y la ordena sobre su key 'age'
    >>> list_sort([{'id':1, 'age': 15},{'id':2, 'age': 45},{'id':3, 'age': 17},{'id':4, 'age': 9},{'id':5, 'age': 36},{'id':6, 'age': 100},{'id':7, 'age': 98},{'id':8, 'age': 21},{'id':9, 'age': 74},{'id':10, 'age': 55}])
    [{'id': 4, 'age': 9}, {'id': 1, 'age': 15}, {'id': 3, 'age': 17}, {'id': 8, 'age': 21}, {'id': 5, 'age': 36}, {'id': 2, 'age': 45}, {'id': 10, 'age': 55}, {'id': 9, 'age': 74}, {'id': 7, 'age': 98}, {'id': 6, 'age': 100}]
    """
    l.sort(key=lambda x: x["age"])
    return l
doctest.testmod(name='list_sort', verbose=True)


def run():
    my_list = list_gen()
    sorted_list = list_sort(my_list)
    print("El id del item con menor 'age' es {}".format(sorted_list[0]['id']))
    print("El id del item con mayor 'age' es {}".format(sorted_list[-1]['id']))


if __name__=='__main__':
    run()