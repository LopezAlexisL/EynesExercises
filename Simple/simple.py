import random


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
    """
    l.sort(key=lambda x: x["age"])
    return l


def run():
    my_list = list_gen()
    sorted_list = list_sort(my_list)
    print("El id del item con menor 'age' es {}".format(sorted_list[0]['id']))
    print("El id del item con mayor 'age' es {}".format(sorted_list[-1]['id']))


if __name__=='__main__':
    run()