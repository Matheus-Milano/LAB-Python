#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#acessar e ler o arquivo .glade
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, 'glade.glade')

class App:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(ARQUIVO)
        self.builder.connect_signals(self)

        self.janela = self.builder.get_object("jan_principal")
        self.lbl_mensagem = self.builder.get_object("lbl_mensagem")

        self.janela.show_all()

        self.o = 1
    def ao_saudar(self, componente=None, dados=None):
        self.lbl_mensagem.set_text(f"Olá Mundo! Pela {self.o}° vez")
        self.o += 1 

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == "__main__":
    App()
    Gtk.main()