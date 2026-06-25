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
        janela.set_title("Conversor de Câmbio Monetário")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        # Box
        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        
        self.real = Gtk.Entry()
        self.real.set_placeholder_text("Quantia em Reais (R$)")
        caixa.add(self.real)

        btn_dolar = Gtk.Button(label="Converter para USD")
        btn_dolar.connect("clicked", self.converter_dolar)
        caixa.add(btn_dolar)

        btn_euro = Gtk.Button(label="Converter para EUR")
        btn_euro.connect("clicked", self.converter_euro)
        caixa.add(btn_euro)

        btn_bitcoin = Gtk.Button(label="Converter para BTC")
        btn_bitcoin.connect("clicked", self.converter_bitcoin)
        caixa.add(btn_bitcoin)

        self.lbl_msg = Gtk.Label(label="")
        caixa.add(self.lbl_msg)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def converter_dolar(self, componente=None, dados=None):
        real = float(self.real.get_text())
        dolar = real / 5.08
        self.lbl_msg.set_label(f"R$ {real} = $ {dolar:.2f}")

    def converter_euro(self, componente=None, dados=None):
        real = float(self.real.get_text())
        euro = real / 5.88
        self.lbl_msg.set_label(f"R$ {real} = € {euro:.2f}")

    def converter_bitcoin(self, componente=None, dados=None):
        real = float(self.real.get_text())
        btc = real / 336677.51
        self.lbl_msg.set_label(f"R$ {real} =  ₿ {btc:.4f}")

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()