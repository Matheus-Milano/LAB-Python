"""Nathan Mazzaro Pereira"""
class Personagem:
    """Criar objetos"""
    def __init__(self, nome):
        self.nome = nome
        self.lvl = 1
        self.vida = 100
        self.xp = 0
    
    def __str__(self):
        return f"Nome: {self.nome}\nNível: {self.lvl}\nVida: {self.vida}\n"
    """Função tomar dano"""
    def tomar_dano(self, qtd):
        self.vida -= qtd
        print(f"{self.nome} recebeu {qtd} de dano")
        if self.vida == 0:
            print(f"{self.nome} foi derrotado")
    """Função ganhar exp"""
    def ganhar_experiencia(self, pontos):
        self.xp += pontos
        if self.xp > 100:       
            self.lvl += 1
            print(f"{self.nome} subiu de nível!")
    """Função curar vida"""
    def curar(self):
        self.vida = 100
        print(f"{self.nome} se curou completamente")

nathan = Personagem("Nathan")
print(nathan)
Personagem.tomar_dano(nathan, 99)
print(nathan)
Personagem.ganhar_experiencia(nathan, 120)
print(nathan)
Personagem.curar(nathan)
print(nathan)
Personagem.tomar_dano(nathan, 100)
print(nathan)
