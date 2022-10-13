from math import pi


class Circulo:
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
        perimetro = float(self.radius) * pi * 2
        perimetro = round(perimetro, 2)
        return 'El perimetro del circulo es de '+str(perimetro)+'cm'
        

    def ar(self):
        area = float(self.radius)**2 * pi
        area = round(area, 2)
        return 'El area del circulo es de '+str(area)+'cm cuadrdos'

    def set_radius(self, num):
        self.radius = num


def set_radio():
    r = float(input('Ingrese el valor del radio del circulo en cm: '))
    if r <= 0:
        raise Exception('Lamentablemente no se puede tener circulos con radios no positivos, por favor vuelva a intentarlo con un numero positivo')
    return r


def options():
    res = input("""Elija que desea hacer (ingrese el numero de la opcion a realizar): \n 
            [1] Multiplicar el radio por un factor \n
            [2] Modificar el radio \n
            Ingrese la opcion: """)
    if not res.isnumeric() or res not in ["1", "2"]:
        raise Exception("Debe ingresar un numero valido sin caracteres o espacios adicionales")
    return res        


def run():
    radio = set_radio()
    circulo = Circulo(radio)
    print(circulo)
    ans = options()
    while ans == '1':
        factor = float(input('Por favor ingrese el numero por el cual desea multiplicar el radio: '))
        mutlipied_circulo = circulo * factor
        print(mutlipied_circulo)
        ans = options()
    while ans == '2':
        radio2 = set_radio()
        circulo.set_radius(radio2)
        ans = options()
        while ans == '1':
            factor = float(input('Por favor ingrese el numero por el cual desea multiplicar el radio: '))
            mutlipied_circulo = circulo * factor
            print(mutlipied_circulo)
            ans = options()
        


if __name__=='__main__':
    run()