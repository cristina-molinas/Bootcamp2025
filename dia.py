class Automovil:
    ruedas = 4
    volante = 1
    ventanas = 4
    asientos = 4
    def init(self,marca,color):
        self.marca = marca
        self.color = color

class Motos(Automovil):
    ruedas = 2
    asientos = 2
    ventanas = 0

moto1 = Motos('Kenton','Negro')

print(moto1.marca)
print(moto1.color)