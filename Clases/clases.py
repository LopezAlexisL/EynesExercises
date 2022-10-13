from math import pi


class Circulo:

    """Clase que instancia un objeto con las propiedades de un circulo.\n
    Recibe un valor tipo float que representa el radio.\n
    Contiene metodos para calcular el perimetro y el area de acorde al radio dado.\n
    Utiliza los metodos __mul__ para multiplicar el radio con otro numero, __str__ para imprimir las caracteristicas del circulo, y set_radius para modificar el valor del radio."""


    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f'Tu circulo tiene las siguientes caracteristicas: \n El radio del circulo es de {str(self.radius)}cm \n {self.per()}\n {self.ar()}'

    def __mul__(self, num):
        if num <= 0:
            raise Exception('Lamentablemente no se puede tener circulos con radios no positivos, por favor vuelva a intentarlo con un numero positivo')
        new_circle = Circulo(self.radius * num)
        return new_circle


    def per(self):
        perimeter = float(self.radius) * pi * 2
        perimeter = round(perimeter, 2)
        return 'El perimetro del circulo es de '+str(perimeter)+'cm'
        

    def ar(self):
        area = float(self.radius)**2 * pi
        area = round(area, 2)
        return 'El area del circulo es de '+str(area)+'cm cuadrdos'

    def set_radius(self, num):
        self.radius = num


def set_radius():

    """Funcion destinada a permitir que el usuario asigne un valor numerico a ser usado como radio del circulo.\n
    Si el valor no es numerico o no es positivo eleva un error"""

    r = input('Ingrese el valor del radio del circulo en cm: ')
    if not r.isnumeric() or float(r) <= 0:
        raise Exception('Lamentablemente no se puede tener circulos con radios no positivos, por favor vuelva a intentarlo con un numero positivo')
    return float(r)


def options():

    """Funcion que utiliza input para que el usuario elija entre dos opciones.\n
    Retorna el valor elegido.\n
    Si se ingresa un valor que no esta dentro de las opciones eleva un error tipo Exception"""

    res = input("""Elija que desea hacer (ingrese el numero de la opcion a realizar): \n 
            [1] Multiplicar el radio por un factor \n
            [2] Modificar el radio \n
            Ingrese la opcion: """)
    if not res.isnumeric() or res not in ["1", "2"]:
        raise Exception("Debe ingresar un numero valido sin caracteres o espacios adicionales")
    return res        


def run():
    radius = set_radius()
    circle = Circulo(radius)
    print(circle)
    ans = options()
    while ans == '1':
        factor = float(input('Por favor ingrese el numero por el cual desea multiplicar el radio: '))
        mutlipied_circle = circle * factor
        print(mutlipied_circle)
        ans = options()
    while ans == '2':
        new_radius = set_radius()
        circle.set_radius(new_radius)
        print(circle)
        ans = options()
        while ans == '1':
            factor = float(input('Por favor ingrese el numero por el cual desea multiplicar el radio: '))
            mutlipied_circle = circle * factor
            print(mutlipied_circle)
            ans = options()
        


if __name__=='__main__':
    run()