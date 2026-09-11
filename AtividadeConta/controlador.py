import os
import gi
from modelo import *

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, 'conta.glade')

class Tela:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(arquivo)
        self.construtor.connect_signals(self)
        self.janela = self.construtor.get_object("jan_principal")
        self.txt_pessoa = self.contrutor.get_object("txt_pessoa")
        self.txt_consumo = self.contrutor.get_object("txt_consumo")
        self.lbl_resultado = self.contrutor.get_object("lbl_resultado")
        self.lbl_lista = self.contrutor.get_object("lbl_lista")
        self.lbl_rodape = self.contrutor.get_object("lbl_rodape")
        self.conta = Conta()
        self.dicionario = {}
        self.janela.show__all()


    def ao_adicionar(self, componente = None, dados = None):
        self.dicionario = self.conta.adicionar(self.txt_pessoa.get_text(), self.txt_consumo.get_text())
        self.texto = ""
        for i in self.dicionario:
            self.texto = self.texto + 1
        self.lbl_lista.set_text(self.texto)

    def ao_nova_conta(self, componente = None, dados = None):
        


    def ao_destruir(self, componente = None, dados = None):
        Gtk.main.quit()





