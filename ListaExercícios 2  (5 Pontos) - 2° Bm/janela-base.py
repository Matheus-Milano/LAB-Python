#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class Tela:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Título da janela")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        # Box
        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        
        # Atributo da classe, acessível em outros métodos
        self.lbl_msg = Gtk.Label(label="XXXX")
        caixa.add(self.lbl_msg)

        botoes = ["Amor", "Presente", "Coração"]
        for texto in botoes:
            btn = Gtk.Button(label=texto)
            btn.connect("clicked", self.imprimir)
            caixa.add(btn)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def imprimir(self, componente=None, dados=None):
        msg = componente.get_label()
        print(f":) {msg}")
        msg = msg.lower()
        self.lbl_msg.set_label(msg)

        # Utilizado para selecionar casos específicos
        """
        if msg == "amor":
            print("Passou amor!")
        """

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()