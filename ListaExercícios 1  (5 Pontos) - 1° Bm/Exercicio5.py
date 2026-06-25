"""Nathan Mazzaro Pereira"""
class Pedido:
    """Criar objetos"""
    def __init__(self, num_pedido, item_escolhido, preco_unidade, qtd, val_total = None):
        self.num_pedido = num_pedido
        self.item = item_escolhido
        self.preco_unidade = preco_unidade
        self.qtd = qtd
        self.val_total = val_total

    def __str__(self):
        return 0
    """Calcular valor total"""
    def calcular_total(self):
        self.val_total = self.preco_unidade*self.qtd
    """Calcular desconto"""
    def calcular_desconto(self, porcentagem):
        self.preco_unidade -= (self.preco_unidade*porcentagem)/100
        print(f"{self.item} possui um desconto de {porcentagem}%!")
        print(f"{self.item} agora possui o valor de R${self.preco_unidade:.2f} após o desconto.\n")
    """Exibir comprovante"""
    def exibir_comprovante(self):
        print(f"Número do pedido: {self.num_pedido}")
        print(f"Item escolhido: {self.item}")
        print(f"Quantidade total de itens: {self.qtd}")
        print(f"Valor Total: R${self.val_total:.2f}")

nathan = Pedido(12, "Camarão", 1.99, 10)
Pedido.calcular_desconto(nathan, 6)
Pedido.calcular_total(nathan)
Pedido.exibir_comprovante(nathan)
