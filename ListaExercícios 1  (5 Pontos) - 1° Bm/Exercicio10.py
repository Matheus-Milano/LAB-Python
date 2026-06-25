"""Nathan Mazzaro Pereira"""
class Carga:
    """Criar objetos"""
    def __init__(self, descricao, peso_kg):
        self.descricao = descricao
        self.peso_kg = peso_kg

    def __repr__(self):
        return f"\nDescrição da carga: {self.descricao} | Peso(kg): {self.peso_kg}"


class Caminhao:
    """Criar objetos"""
    def __init__(self, placa, capacidade_maxima_kg):
        self.placa = placa
        self.cap_max_kg = capacidade_maxima_kg
        self.carga_atual = 0
        self.cargas = []
    """Adicionar cargas ao caminhão"""
    def carregar_item(self, carga):
        if self.carga_atual + carga.peso_kg <= self.cap_max_kg:
            self.carga_atual += carga.peso_kg
            self.cargas.append(carga)
        else:
            print(
                f"\nO peso de {carga.peso_kg} ultrapassa a carga máxima permitida!\n")
    """Exibir informações sobre as cargas presentes no caminhão"""
    def exibir_relatorio(self):
        print(f"Placa do caminhão: {self.placa}")
        print(self.cargas)


cam1 = Caminhao("ABC123", 1000)
carg1 = Carga("Carga de 600kg", 600)
carg2 = Carga("Carga de 500kg", 500)
carg3 = Carga("Carga de 500kg", 400)
Caminhao.carregar_item(cam1, carg1)
Caminhao.carregar_item(cam1, carg2)
Caminhao.carregar_item(cam1, carg3)
Caminhao.exibir_relatorio(cam1)
