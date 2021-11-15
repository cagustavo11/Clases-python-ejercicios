"""
3. Mejora el ejercicio anterior de forma que el robot pueda recibir una secuencia de movimientos.
Por ejemplo:
• mueve(“AADDADIR”)
También deberá tener otros dos métodos: uno que devuelva todas las órdenes recibidas y otro capaz
de listar los movimientos necesarios para volver a la posición inicial (0,0).
Aquí tienes un ejemplo de una posible ejecución del programa:

Introduce la orden: AADAD
Posición actual: 3,2
Introduce la orden: IAADR
Posición actual: 4,2
Introduce la orden: fin
Posición actual: 4,2

Órdenes recibidas: AADADIAADRfin
Secuencia para posición inicial: RRRRII
"""


class Robot:
    ordenesRecibidas = ""
    posicion_inicial = ""
    # x = 0
    # y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mueve(self, orden):

        for character in orden:
            self.ordenesRecibidas += character
            if character.lower() == 'a':
                self.x += 1
            elif character.lower() == 'r':
                self.x -= 1
            elif character.lower() == 'i':
                self.y -= 1
            elif character.lower() == 'd':
                self.y += 1

    def posicion_actual(self):
        return [self.x, self.y]

    def getOrdenesRecibidas(self):
        return self.ordenesRecibidas

    def posicion_inicial(self):
        r_totales = "R" * self.x
        y_totales = "I" * self.y

        self.posicion_inicial = r_totales + y_totales

        return self.posicion_inicial


miRobot = Robot(0, 0)
while True:
    # Pedimos Datos al usuario
    orden = input("Introduce la orden: ")
    if orden.lower() == 'fin':
        break

    miRobot.mueve(orden)
    # Obtenemos x and y
    x, y = miRobot.posicion_actual()
    print(f'Posicion actual: { x }, { y }')


totalOrdenes = miRobot.getOrdenesRecibidas()
print(f'Órdenes recibidas: { totalOrdenes.upper() }fin')
posiInicial = miRobot.posicion_inicial()
print(f'Secuencia para posición inicial: { posiInicial }')
