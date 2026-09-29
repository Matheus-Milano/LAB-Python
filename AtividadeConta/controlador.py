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
        self.chk_taxa = self.construtor.get_object("chk_taxa")
        self.lbl_resultado = self.construtor.get_object("lbl_resultado")
        self.lbl_lista = self.construtor.get_object("lbl_lista")
        self.lbl_rodape = self.construtor.get_object("lbl_rodape")
        self.conta = Conta()
        self.lista = []
        self.janela.show_all()
        self.janela.set_focus(None)


    def ao_adicionar(self, componente = None, dados = None):
        nome = self.txt_pessoa.get_text().strip()
        valor = self.txt_consumo.get_text().strip()

        if not nome or nome.isdigit():
            self.mostrar_erro("Digite um nome válido.")
            self.txt_pessoa.grab_focus()
            return

        try:
            float(valor)
        except ValueError:
            self.mostrar_erro("Digite um valor numérico.")
            self.txt_consumo.grab_focus()
            return

        self.lista = self.conta.adicionar(nome, valor, self.chk_taxa.get_active())
        self.texto = ""
        for i in self.lista:
            taxa = self.conta.valor_servico_pessoa(i)
            total_pessoa = self.conta.valor_total_pessoa(i)
            self.texto += (
                f"{i[0]}: Consumo: R$ {i[1]:.2f} + Taxa: R$ {taxa:.2f} "
                f"= R$ {total_pessoa:.2f}\n"
            )
        self.lbl_lista.set_text(self.texto)

                    
        self.subtotal = self.conta.subtotal()
        self.servico = self.conta.valor_servico()
        self.total = self.conta.total()
        self.por_pessoa = self.conta.valor_por_pessoa()
        
        self.texto_resultado = (
            f"Subtotal: R$ {self.subtotal:.2f}\n"
            f"Serviço (10%): R$ {self.servico:.2f}\n"   
            f"Total: R$ {self.total:.2f}\n"
            f"Média por pessoa: R$ {self.por_pessoa:.2f}\n"
            f"Consumiu mais: {self.conta.consumiu_mais()}\n"
        )
        self.lbl_resultado.set_text(self.texto_resultado)
        self.txt_pessoa.set_text("")
        self.txt_consumo.set_text("")
        self.chk_taxa.set_active(False)
        self.txt_pessoa.grab_focus()
        self.lbl_rodape.set_text(f"Total de pessoas: {len(self.lista)}") 

    def mostrar_erro(self, mensagem):
        dialogo = Gtk.MessageDialog(
            transient_for=self.janela,
            modal=True,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=mensagem
        )
        dialogo.run()
        dialogo.destroy()

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
        self.chk_taxa.set_active(False)
        self.txt_pessoa.grab_focus()
        
    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = Tela()
    Gtk.main()
    os.system("cls")



