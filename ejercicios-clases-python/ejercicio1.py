"""
1. Crea la clase Coche que contenga las siguientes propiedades:
• matrícula (string)
• marca (string)
• kilometros_recorridos (float)
• gasolina (float)
La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. El método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0’1.
La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable gasolina.
Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: “Es necesario repostar para recorrer la cantidad indicada de kilómetros”.
Ejemplo:
- avanzar(50) # gasolina = 50
- avanzar(100) # kilometros_recorridos = 100, gasolina = 40
- avanzar(40) # kilometros_recorridos = 140, gasolina = 36
- avanzar(180) # kilometros_recorridos = 320, gasolina = 18
"""


class Coche:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina

    def avanzar(self, numero_kilometros_conducir):
        self.kilometros_recorridos += numero_kilometros_conducir
        if self.gasolina < 0:
            print(
                "Es necesario repostar para recorrer la cantidad indicada de kilómetros")
        else:
            restarGasolina = numero_kilometros_conducir * 0.1
            self.gasolina -= restarGasolina

    def repostar(self, litros_introducidos):
        self.gasolina += litros_introducidos

    def getKilometrosRecorridos(self):
        return self.kilometros_recorridos

    def getGasolina(self):
        return self.gasolina


cocheTesla = Coche('F1F1F', 'Tesla', 0, 55)
kilometros_a_conducir = [100, 40, 180]

cocheTesla.avanzar(50)
print(f'Gasolina: { cocheTesla.getGasolina() }')

for el in kilometros_a_conducir:
    cocheTesla.avanzar(el)
    print(f'Kilometros Recorridos: { cocheTesla.getKilometrosRecorridos() }')
    print(f'Gasolina: { cocheTesla.getGasolina() }')
