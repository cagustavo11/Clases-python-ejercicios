"""
2. Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá realizar los siguientes movimientos:
• Avanzar hacia adelante (A)
• Retroceder (R)
• Avanzar hacia la izquierda (I) o hacia la derecha (D)
El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método, posicion_actual(), que indicará su posición en las coordenadas X e Y. Al crear el robot este se
inicializará a las coordenadas (0,0).
Puedes utilizar el siguiente código para probar la clase creada:

miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    print(miRobot.posicion_actual())
Ejemplo:
>> Introduce la orden: A
Posición actual: 1,0
>> Introduce la orden: A
Posición actual: 2,0
>> Introduce la orden: I
Posición actual: 2,-1
>> Introduce la orden: A
Posición actual: 3,-1
>> Introduce la orden: I
Posición actual: 3,-2
>> Introduce la orden: D
Posición actual: 3,-1
>> Introduce la orden: R
Posición actual: 2,-1
>> Introduce la orden: fin
"""


class Robot:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mueve(self, orden):
        if orden.lower() == 'a':
            self.x += 1
        if orden.lower() == 'r':
            self.x -= 1
        if orden.lower() == 'i':
            self.y -= 1
        if orden.lower() == 'd':
            self.y += 1

    def posicion_actual(self):
        return [self.x, self.y]


miRobot = Robot(0, 0)
while True:
    orden = input("Introduce la orden: ")
    if orden.lower() == 'fin':
        break
    miRobot.mueve(orden)
    x, y = miRobot.posicion_actual()
    print(f'Posicion actual: {x}, {y}')
