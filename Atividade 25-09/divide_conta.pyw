import os
import gi
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, 'divide_conta.glade')

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
        self.janela.show_all()
        self.janela.set_focus(None)
 
    def ao_calcular(self, componente=None, dados=None):
        try:
            valor = float(self.entry_valor.get_text())
            pessoas = math.ceil(float(self.entry_pessoas.get_text()))
            gorjeta = float(self.entry_gorjeta.get_text())/100  

            valor += gorjeta * valor
            valor /= pessoas    

            self.lbl_resultado.set_text(f"R$ {valor:.2f}") 
            self.status.set_text("Cálculo Concluído!")

        except ValueError:
            self.status.set_text("Impossível converter Letras em Números!")

        except ZeroDivisionError:
            self.status.set_text("O número de pessoas não pode ser Nulo!")

    def ao_limpar(self, componente=None, dados=None):
        self.entry_valor.set_text("")
        self.entry_pessoas.set_text("")
        self.entry_gorjeta.set_text("10")
        self.lbl_resultado.set_text("R$ 0.00")
        self.status.set_text("Aguardando...")

    def ao_salvar(self, componente=None, dados=None):
        pass

    def ao_abrir(self, componente=None, dados=None):
        pass

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = Tela()
    Gtk.main()
    os.system("clear")


