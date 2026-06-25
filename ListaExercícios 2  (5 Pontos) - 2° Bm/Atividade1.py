"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

# Aluno: Matheus Henrique Milano
# Turma: 2° Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class AplicacaoTeste:
    def __init__(self):
        tela = Gtk.Window()
        tela.connect("delete-event", self.sair)
        tela.set_title("sla")
        tela.set_default_size(400, 200)
        rotulo = Gtk.Label()
        rotulo.set_label("MATHEUS HENRIQUE MILANO\n 2° Informática")
        tela.add(rotulo)
        rotulo.show()
        tela.show()
        
    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    janela = AplicacaoTeste()
    Gtk.main()