""" 
    Controlador da aplicação:  Matheus Milano  
    Modelo da aplicação:  Gabriel Anselmo
    Construtoraas da janela:  Maria Luiza Farias, Fernanda Morais, Rafaela Silva  
"""

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
        self.txt_pessoa = self.construtor.get_object("txt_pessoa")
        self.txt_consumo = self.construtor.get_object("txt_consumo")
        self.lbl_resultado = self.construtor.get_object("lbl_resultado")
        self.lbl_lista = self.construtor.get_object("lbl_lista")
        self.lbl_rodape = self.construtor.get_object("lbl_rodape")
        self.conta = Conta()
        self.lista = []
        self.janela.show_all()
        self.janela.set_focus(None)


    def ao_adicionar(self, componente = None, dados = None):
        self.lista = self.conta.adicionar(self.txt_pessoa.get_text(), self.txt_consumo.get_text())
        self.texto = ""
        for i in self.lista:
            self.texto = self.texto + str(i[0]) + ": " + "R$" +  str(i[1]) +"\n"
        self.lbl_lista.set_text(self.texto)

                    
        self.subtotal = self.conta.subtotal()
        self.servico = self.conta.valor_servico()
        self.total = self.conta.total()
        self.por_pessoa = self.conta.valor_por_pessoa()
        
        self.texto_resultado = (
            f"Subtotal: R$ {self.subtotal:.2f}\n"
            f"Serviço (10%): R$ {self.servico:.2f}\n"   
            f"Total: R$ {self.total:.2f}\n"
            f"Cada um paga: R$ {self.por_pessoa:.2f}\n"
            f"Consumiu mais: {self.conta.consumiu_mais()}\n"
        )
        self.lbl_resultado.set_text(self.texto_resultado)
        self.txt_pessoa.set_text("")
        self.txt_consumo.set_text("")
        self.txt_pessoa.grab_focus()
        self.lbl_rodape.set_text(f"Total de pessoas: {len(self.lista)}") 

    def ao_pessoa_ativada(self, componente = None, dados = None):
        self.txt_consumo.grab_focus()
        
    def ao_nova_conta(self, componente = None, dados = None):
        self.conta.limpar()
        self.lista = []
        self.lbl_lista.set_text("")
        self.lbl_resultado.set_text("")
        self.lbl_rodape.set_text("Total de pessoas: 0")
        self.txt_pessoa.set_text("")
        self.txt_consumo.set_text("")
        self.txt_pessoa.grab_focus()
        
    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = Tela()
    Gtk.main()
    os.system("cls")



