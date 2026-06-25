"""Nathan Mazzaro Pereira"""
class Veiculo:
    """Criar objetos"""
    def __init__(self, placa, modelo, hora_entrada, valor = None):
        self.placa = placa
        self.modelo = modelo
        self.hora_entrada = hora_entrada
        self.valor = valor

    def __str__(self):
        return f"Placa do carro: {self.placa}\nModelo do carro: {self.modelo}\n"
    """Função registra horário de saída"""
    def registrar_saida(self, hora_saida):
        self.valor = (hora_saida - self.hora_entrada)*5
        print(f"Hora de entrada: {self.hora_entrada}")
        print(f"Hora de saída: {hora_saida}")
        print(f"Valor a ser pago: R${self.valor}")

carro1 = Veiculo("ABC123", "Tesla", 12)
print(carro1)
Veiculo.registrar_saida(carro1, 18)
print(carro1)
