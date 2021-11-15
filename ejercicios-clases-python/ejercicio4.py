"""
4. Crea la clase Triangulo que almacene la longitud de cada uno de sus lados. Deberá contener los siguientes métodos:
• area(): devuelve el área del triángulo
• forma(): indica si se trata de un triángulo equilátero, isósceles o irregular.
• perímetro(): devuelve el perímetro del triángulo.
"""


class Triangulo:
    longitud1 = 0
    longitud2 = 0
    longitud3 = 0

    def __init__(self, longitud1, longitud2, longitud3):
        self.longitud1 = longitud1
        self.longitud2 = longitud2
        self.longitud3 = longitud3

    def area(self, base, altura):
        res = (base * altura) / 2
        return res

    def forma(self):
        formaTriangulo = ''
        if self.longitud1 == self.longitud2 == self.longitud3:
            formaTriangulo = "Triangulo Equilaero"
        elif self.longitud1 == self.longitud2 or self.longitud2 == self.longitud3 or self.longitud3 == self.longitud1:
            formaTriangulo = "Triangulo Isoseles"
        else:
            formaTriangulo = "Triangulo Irregular"
        return formaTriangulo

    def perimetro(self):
        res = self.longitud1 + self.longitud2 + self.longitud3
        return res


triangulo1 = Triangulo(20, 10, 30)

print(triangulo1.forma())
print(triangulo1.area(14, 20))
print(triangulo1.perimetro())
