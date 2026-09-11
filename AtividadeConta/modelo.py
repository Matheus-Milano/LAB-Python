""" Modelo da aplicação de divisão de conta. """
"""  Gabriel Anselmo  """


class Conta:
    def __init__(self):
        self.lista_conta = []
    
    def adicionar(self, nome, valor):
        valor = float(valor) 
        if valor > 0:
            self.lista_conta.append((nome, float(valor)))
        else:
            self.lista_conta.append((nome, 0.0))
        return self.lista_conta

        
    def total_pessoas(self):
        return len(self.lista_conta)
    
    def subtotal(self):
        subtotal = 0.0
        for pessoa in self.lista_conta:
            subtotal += float(pessoa[1])
        return subtotal
    
    def valor_servico(self):
        return 0.1 * self.subtotal()
    
    def total(self):
        return self.subtotal() + self.valor_servico()
    
    def valor_por_pessoa(self):
        if len(self.lista_conta) == 0:
            return 0
        return self.total() / len(self.lista_conta)
    
    def listar(self):
        return self.lista_conta 
    
    def limpar(self):
        self.lista_conta = []
        
    def consumiu_mais(self):
        if len(self.lista_conta) == 0:
            return "Nenhuma pessoa cadastrada"
        for i in range(len(self.lista_conta)):
            if self.lista_conta[i][1] == max([x[1] for x in self.lista_conta]):
                maior_consumo = self.lista_conta[i][0]
        return maior_consumo