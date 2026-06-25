"""Nathan Mazzaro Pereira"""
class SensorIrrigacao:
    """Criar objetos"""
    def __init__(self, nome_setor, status_bomba = None):
        self.nome_setor = nome_setor
        self.status_bomba = status_bomba

    def __str__(self):
        return f"Setor: {self.nome_setor}\nStatus Bomba: {self.status_bomba}\n"
    """Funções on/off"""
    def ligar_bomba(self):
        self.status_bomba = "On"
        print("A bomba foi ligada.")
    def desligar_bomba(self):
        self.status_bomba = "Off"
        print("A bomba foi desligada.")
    """Função verificar umidade do solo"""
    def verificar_solo(self, umidade):
        if umidade < 30:
            self.status_bomba = "On"
            print("A bomba será ligada.")
        if umidade > 70:
            self.status_bomba = "Off"
            print("A bomba será desligada.")

plant1 = SensorIrrigacao("Trigo")
print(plant1)
SensorIrrigacao.verificar_solo(plant1, 75)
print(plant1)
SensorIrrigacao.ligar_bomba(plant1)
print(plant1)
