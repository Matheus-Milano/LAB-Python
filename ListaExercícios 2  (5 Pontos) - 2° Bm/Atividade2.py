#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aluno: Matheus Henrique Milano
# Turma: 2° Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class Tela:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Contador Interativo")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )

        self.valor = 0
        self.rotulo = Gtk.Label(label=str(self.valor))
        caixa.add(self.rotulo)

        btn = Gtk.Button(label="Incrementar Valor")
        btn.connect("clicked", self.clicar)
        caixa.add(btn)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def clicar(self, componente=None, dados=None):
        self.valor += 1
        self.rotulo.set_label(str(self.valor))

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()