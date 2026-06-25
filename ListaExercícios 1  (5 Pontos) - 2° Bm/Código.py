from abc import ABC, abstractmethod
from math import pi as math# Pra usar 𝝅


class Forma(ABC):
    def __init__(self, cor):
        self.__cor = cor  # Todos possuem uma cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Círculo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio

    def exibir(self):
        print("_____Círculo_____")
        print(f"Cor: {self.cor}")
        print(f"Área do círculo: {self.area():.2f}")
        print(f"Perímetro do círculo: {self.perimetro():.2f}\n")


class Quadrado(Forma):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def exibir(self):
        print("_____Quadrado____")
        print(f"Cor: {self.cor}")
        print(f"Área do quadrado: {self.area():.2f}")
        print(f"Perímetro do quadrado: {self.perimetro():.2f}\n")


class Triângulo(Forma):
    # 3 lados que possívelmente podem ser diferentes
    def __init__(self, cor, base, altura, lado1, lado2):
        super().__init__(cor)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2

    def exibir(self):
        print("_____Triângulo_____")
        print(f"Cor: {self.cor}")
        print(f"Área do triângulo: {self.area():.2f}")
        print(f"Perímetro do quadrado: {self.perimetro():.2f}\n")


class Retângulo(Forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def exibir(self):
        print("______Retângulo_____")
        print(f"Cor: {self.cor}")
        print(f"Área do retângulo: {self.area():.2f}")
        print(f"Perímetro do quadrado: {self.perimetro():.2f}\n")


class Pentágono(Forma):
    def __init__(self, cor, lado, apotema):
        super().__init__(cor)
        self.lado = lado
        self.apotema = apotema

    def area(self):
        return (5 * self.lado * self.apotema) / 2

    def perimetro(self):
        return 5 * self.lado

    def exibir(self):
        print("_____Pentágono_____")
        print(f"Cor: {self.cor}")
        print(f"Área do pentágono: {self.area():.2f}")
        print(f"Perímetro do quadrado: {self.perimetro():.2f}\n")


def AdicionarForma():
    lista = []
    i = 0

    while True:
        try:
            formas = int(input("Quantas formas adicionar?: "))
            break
        except ValueError:
            print("Digite um número válido.")

    while i < formas:
        valor = input(
            "Qual forma geométrica adicionar? "
            "(Círculo, Quadrado, Triângulo, Retângulo, Pentágono): "
        )

        match valor.lower():
            case "círculo" | "circulo":
                cor = input("Qual a cor do círculo?: ")
                try:
                    raio = float(input("Raio: "))
                except ValueError:
                    print("Digite um número válido.")
                    continue
                lista.append(Círculo(cor, raio))
                i += 1

            case "Quadrado" | "quadrado":
                cor = input("Qual a cor do quadrado?: ")
                try:
                    lado = float(input("Lado: "))
                except ValueError:
                    print("Digite um número válido.")
                    continue
                lista.append(Quadrado(cor, lado))
                i += 1

            case "triângulo" | "triangulo":
                cor = input("Qual a cor do triângulo?: ")
                try:
                    base = float(input("Base: "))
                    altura = float(input("Altura: "))
                    lado1 = float(input("Lado 1: "))
                    lado2 = float(input("Lado 2: "))
                except ValueError:
                    print("Digite apenas números.")
                    continue
                if (
                    lado1 + lado2 > base and
                    lado2 + base > lado1 and
                    lado1 + base > lado2
                ):  # Regra para ser um triângulo
                    i += 1
                    lista.append(
                        Triângulo(cor, base, altura, lado1, lado2))
                else:
                    print("Valores inválidos para a formação de um triângulo!")

            case "retângulo" | "retangulo":
                cor = input("Qual a cor do retângulo?: ")
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                lista.append(Retângulo(cor, base, altura))
                i += 1

            case "pentágono" | "pentagono":
                cor = input("Qual a cor do pentágono?: ")
                try:
                    lado = float(input("Lado: "))
                    apotema = float(input("Apótema: "))
                except ValueError:
                    print("Digite apenas números.")
                    continue
                lista.append(Pentágono(cor, lado, apotema))
                i += 1

            case _:
                print("Forma inválida!")

    return lista


formas = AdicionarForma()
print("")
for forma in formas:
    forma.exibir()
