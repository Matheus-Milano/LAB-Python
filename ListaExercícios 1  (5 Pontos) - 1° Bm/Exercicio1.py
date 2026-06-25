"""Nathan Mazzaro Pereira"""
class Carro:
    """Criar objetos"""
    def __init__(self, model_car, bateria = 100):
        self.model_car = model_car
        self.bateria = bateria

    def __str__(self):
        return f"Modelo do carro: {self.model_car}\nBateria: {self.bateria}\n"

    """Função dirigir"""
    def dirigir(self, distancia):
        if self.bateria <= 0:
            print("Você não tem bateria o suficiente para poder dirigir!")
        else:
            self.bateria -= (distancia/10)
    """Função carregar"""
    def carregar(self):
        self.bateria = 100


carro1 = Carro("Tesla")
print(carro1)
Carro.dirigir(carro1, 100)
print(carro1)
Carro.carregar(carro1)
print(carro1)
