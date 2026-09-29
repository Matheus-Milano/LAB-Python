"""
    Nome: Matheus Milano, Nathan Mazzaro, Bulacha
    Data: 29/09/2026
    Descrição: Programa para dividir uma conta entre várias pessoas,
    incluindo gorjeta. 
"""

import os
import gi
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, 'divide_conta.glade')

def calcular_divisao(str_valor, str_pessoas, str_gorjeta):

    valor = float(str_valor)
    pessoas = math.ceil(float(str_pessoas))
    gorjeta = float(str_gorjeta) / 100

    if valor < 0 or pessoas < 0 or gorjeta < 0:
        raise ValueError("Valores negativos não são permitidos.")

    if pessoas == 0:
        raise ZeroDivisionError("O número de pessoas não pode ser zero.")

    total = valor + (valor * gorjeta)
    return total / pessoas

def formatar_moeda(valor):
    formatado = f"{valor:,.2f}"
    formatado = formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatado}"

class Tela:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arquivo)
        self.builder.connect_signals(self)
        self.janela = self.builder.get_object("jan_principal")
        self.entry_pessoas = self.builder.get_object("entry_pessoas")
        self.entry_valor = self.builder.get_object("entry_valor")
        self.entry_gorjeta = self.builder.get_object("entry_gorjeta")
        self.lbl_resultado = self.builder.get_object("lbl_resultado")
        self.status = self.builder.get_object("lbl_status")       
        self.arquivo_comprovante = os.path.join(pasta, "comprovante.txt")
        self.janela.show_all()
        self.janela.set_focus(None)

    def exibir_mensagem(self, tipo, titulo, mensagem):
        dialogo = Gtk.MessageDialog(
            transient_for=self.janela,
            flags=0,
            message_type=tipo,
            buttons=Gtk.ButtonsType.OK,
            text=titulo
        )
        dialogo.format_secondary_text(mensagem)
        dialogo.run()
        dialogo.destroy()

    
    def ao_calcular(self, componente=None, dados=None): 
        try:
            val_txt = self.entry_valor.get_text()
            pess_txt = self.entry_pessoas.get_text()
            gorj_txt = self.entry_gorjeta.get_text()

            resultado = calcular_divisao(val_txt, pess_txt, gorj_txt)

        except ValueError as err:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro de Entrada",
                f"Entrada inválida ou valor negativo! ({err})"
            )
        except ZeroDivisionError:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro no Número de Pessoas",
                "O número de pessoas deve ser maior que zero."
            )
        except Exception as erro:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro Inesperado",
                f"Ocorreu um erro não previsto: {erro}"
            )
        else:
            self.lbl_resultado.set_text(f"R$ {resultado:.2f}")
            self.status.set_text("Cálculo Concluído!")
        finally:
            print("Tentativa de cálculo finalizada.")

    def ao_limpar(self, componente=None, dados=None):
        self.entry_valor.set_text("")
        self.entry_pessoas.set_text("")
        self.entry_gorjeta.set_text("10")
        self.lbl_resultado.set_text("R$ 0.00")
        self.status.set_text("Aguardando...")

    def ao_salvar(self, componente=None, dados=None):
        try:
            valor_conta = float(self.entry_valor.get_text())
            pessoas = math.ceil(float(self.entry_pessoas.get_text()))
            percentual_gorjeta = float(self.entry_gorjeta.get_text())
            valor_por_pessoa = calcular_divisao(
                self.entry_valor.get_text(),
                self.entry_pessoas.get_text(),
                self.entry_gorjeta.get_text(),
            )
        except ValueError as erro:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro nos Dados",
                f"Confira os valores informados: {erro}"
            )
            return
        except ZeroDivisionError:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Número de Pessoas Inválido",
                "O número de pessoas deve ser maior que zero."
            )
            return
        
       #Utilizamos aquela IAzinha de leves
        valor_gorjeta = valor_conta * percentual_gorjeta / 100
        total = valor_conta + valor_gorjeta
        self.lbl_resultado.set_text(formatar_moeda(valor_por_pessoa))
        comprovante = "\n".join((
            "COMPROVANTE DA DIVISÃO DA CONTA",
            "================================",
            f"{'Valor da conta':<22}{formatar_moeda(valor_conta):>12}",
            f"{f'Gorjeta ({percentual_gorjeta:g}%)':<22}{formatar_moeda(valor_gorjeta):>12}",
            f"{'Total com gorjeta':<22}{formatar_moeda(total):>12}",
            f"{'Pessoas':<22}{pessoas:>12}",
            "--------------------------------",
            f"{'VALOR POR PESSOA':<22}{formatar_moeda(valor_por_pessoa):>12}",
        ))

        try:
            with open(self.arquivo_comprovante, 'w', encoding='utf-8') as f:
                f.write(comprovante + "\n")
        except OSError as erro:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro ao Salvar",
                f"Não foi possível salvar o arquivo: {erro}"
            )
        else:
            self.status.set_text("Comprovante salvo!")
            
    def ao_abrir(self, componente=None, dados=None):
        try:
            with open(self.arquivo_comprovante, 'r', encoding='utf-8') as f:
                conteudo = f.read()
        except FileNotFoundError as err:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Arquivo Não Encontrado",
                "Salve um comprovante antes de abri-lo."
            )
        except OSError as erro:
            self.exibir_mensagem(
                Gtk.MessageType.ERROR,
                "Erro ao Abrir",
                f"Não foi possível abrir o comprovante: {erro}"
            )
        else:
            self.exibir_mensagem(
                Gtk.MessageType.INFO,
                "Comprovante",
                conteudo
            )
            self.status.set_text("Comprovante aberto com sucesso!")
            
        

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = Tela()
    Gtk.main()
    os.system("clear")


