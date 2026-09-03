#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(PASTA, 'cantina.glade')

class Metodos:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(ARQ)
        self.builder.connect_signals(self)
        self.janela = self.builder.get_object('jan_principal')
        self.entry_1 = self.builder.get_object('txt_produto')
        self.entry_2 = self.builder.get_object('txt_preco')
        self.spn_btn = self.builder.get_object('spn_qtd')
        self.lbl_ultimo = self.builder.get_object('lbl_ultimo')
        self.lbl_rodape = self.builder.get_object('lbl_rodape')
        self.janela.show_all()

        self.lista = []
        self.cont = 0
        self.total = 0.0
        self.minimo = 5
        self.maximo = 12
        self.desconto = 0.9

    def ao_adicionar(self, componente=None, dados=None):

        self.nome = self.entry_1.get_text().strip()
        self.preco = float(self.entry_2.get_text().replace(',', '.'))
        self.quantidade = int(self.spn_btn.get_value())

        self.valor = self.preco * self.quantidade
        if self.quantidade >= self.maximo:
            self.valor *= self.desconto

        if self.quantidade < self.minimo:
            self.estoque = 'ESTOQUE BAIXO'
            self.cor = 'red'
        else:
            self.estoque = 'ok'
            self.cor = 'green'

        self.lista.append([self.nome, self.preco, self.quantidade, self.valor, self.estoque])
        self.cont = self.cont + 1
        self.total = self.total + self.valor

        self.lbl_ultimo.set_markup('<big>' + self.nome + '</big>\n' +
                           str(self.quantidade) + ' x R$ ' + format(self.preco, '.2f') +
                           ' = R$ ' + format(self.valor, '.2f') +
                           ' <span foreground="' + self.cor + '">' + self.estoque + '</span>')

        b = 0
        for x in self.lista:
            if x[2] < self.minimo:
                b = b + 1

        self.lbl_rodape.set_text(str(self.cont) + ' produto(s) - R$ ' + format(self.total, '.2f') +
                         ' - ' + str(b) + ' com estoque baixo')

        self.entry_1.set_text('')
        self.entry_2.set_text('')
        self.spn_btn.set_value(1)
        self.entry_1.grab_focus()

    def ao_relatorio(self, componente=None, dados=None):

        texto = ''
        maior = 0.0
        nome_maior = '-'

        for x in self.lista:
            self.valor_verificado = x[1] * x[2]
            if x[2] >= self.maximo:
                self.valor_verificado = self.valor_verificado * self.desconto
            if self.valor_verificado > maior:
                maior = self.valor_verificado
                nome_maior = x[0]
            if x[2] < self.minimo:
                texto = texto + x[0] + ' (' + str(x[2]) + ') REPOR\n'
            else:
                texto = texto + x[0] + ' (' + str(x[2]) + ')\n'

        if len(self.lista) > 0:
            m = self.total / len(self.lista)
        else:
            m = 0.0

        d = Gtk.MessageDialog(transient_for=self.janela, modal=True,
                              message_type=Gtk.MessageType.INFO,
                              buttons=Gtk.ButtonsType.OK,
                              text='Relatorio do estoque')
        d.format_secondary_text(
            texto + '\nTotal: R$ ' + format(self.total, '.2f') +
            '\nMedia por produto: R$ ' + format(m, '.2f') +
            '\nMaior valor: ' + nome_maior + ' (R$ ' + format(maior, '.2f') + ')')
        d.run()
        d.destroy()

    def ao_zerar(self, componente=None, dados=None):
    
        self.lista = []
        self.cont = 0
        self.total = 0.0
        self.lbl_ultimo.set_text('—')
        self.lbl_rodape.set_text('0 produto(s)')
        self.entry_1.set_text('')
        self.entry_2.set_text('')
        self.spn_btn.set_value(1)

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = Metodos()
    Gtk.main()
