class Conta:
    def __init__(self):
        self.lista_conta = []
    
    def adicionar(self, nome, valor):
        self.lista_conta[] = nome, valor
    
    def total_pessoas(self):
        return len(self.lista_conta)
    
    def subtotal(self):
        for pessoa in self.lista_conta:
            subtotal += self.lista_conta[pessoa][1]
        return subtotal
    
    def valor_servico(self):
        return 0.1 * self.subtotal()
    
    def total(self):
        return self.subtotal() + self.valor_servico()
    
    def valor_por_pessoa(self):
        if len(self.lista_conta) == 0:
            return 0
        return self.total()/len(self.lista_conta)
    
    def listar(self):
        return self.lista_conta 
    
    def limpar(self):
        self.lista_conta = []