"""Nathan Mazzaro Pereira"""
class Produto:
    """Criar objetos"""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"\nNome: {self.nome} Preço: {self.preco}"
class CarrinhoCompras:
    """Criar objetos"""
    def __init__(self, lista_produtos = [], val_total = 0):
        self.lista = lista_produtos
        self.val_total = val_total
    
    def __str__(self):
        return f"{self.lista}"
    """Adicionar produtos a lista"""
    def adicionar_produto(self, produto):
        self.lista.append(produto)
    """Calcular valor total da lista"""
    def calcular_total(self):
        for items in self.lista:
            self.val_total += items.preco
        print(f"O valor total da compra é: {self.val_total}")

carrinho1 = CarrinhoCompras()
CarrinhoCompras.adicionar_produto(carrinho1, Produto("Laranja", 2.19))
CarrinhoCompras.adicionar_produto(carrinho1, Produto("Cenoura", 1.69))
CarrinhoCompras.adicionar_produto(carrinho1, Produto("Banana", 1.99))
print(f"Carrinho: {carrinho1}\n")
CarrinhoCompras.calcular_total(carrinho1)

