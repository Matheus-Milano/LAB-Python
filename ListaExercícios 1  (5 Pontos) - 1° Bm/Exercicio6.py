"""Nathan Mazzaro Pereira"""
class Temperatura:
    """Criar objetos"""
    def __init__(self, temperatura_atual, temperatura_alvo = None):
        self.temp_atual = temperatura_atual
        self.temp_alvo = temperatura_alvo

    def __str__(self):
        return 0
    """Ajustar a temperatura"""
    def ajustar_alvo(self, nova_temp):
        self.temp_alvo = nova_temp
    """Aumentar e diminuir a temperatura"""
    def aquecer(self):
        while self.temp_atual != self.temp_alvo and self.temp_atual < self.temp_alvo:
            self.temp_atual += 1 
            print(f"A temperatura foi aumentada em 1°C.\nTemperatura atual: {self.temp_atual}°C\n")
        print(f"A temperatura de {self.temp_alvo}°C, foi alcançada!\n")
    def resfriar(self):
        while self.temp_atual != self.temp_alvo and self.temp_atual > self.temp_alvo:
            self.temp_atual -= 1
            print(f"A temperatura foi reduzida em 1°C.\nTemperatura atual: {self.temp_atual}°C\n")
        print(f"A temperatura de {self.temp_alvo}°C, foi alcançada!\n")
"""Coloquei 1 ao invés de 3 nos valores porque acho que fica mais preciso"""
temp1 = Temperatura(40)
Temperatura.ajustar_alvo(temp1, 60)
Temperatura.aquecer(temp1)
Temperatura.ajustar_alvo(temp1, 27)
Temperatura.resfriar(temp1)
