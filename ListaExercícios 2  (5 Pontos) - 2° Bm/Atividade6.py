#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aluno: Matheus Henrique Milano
# Turma: 2° Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class TelaNotas:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Painel de Rendimento Escolar")
        janela.set_border_width(20)
        janela.set_default_size(400, 350)

        self.caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )

        self.nota1 = Gtk.Entry()
        self.nota1.set_placeholder_text("Nota da Primeira Etapa")
        self.caixa.add(self.nota1)

        self.nota2 = Gtk.Entry()
        self.nota2.set_placeholder_text("Nota da Segunda Etapa")
        self.caixa.add(self.nota2)

        self.nota3 = Gtk.Entry()
        self.nota3.set_placeholder_text("Nota da Terceira Etapa")
        self.caixa.add(self.nota3)

        self.btn_calcular = Gtk.Button(label="Verificar Média Final")
        self.btn_calcular.connect("clicked", self.calcular_media)
        self.caixa.add(self.btn_calcular)

        self.lbl_resultado = Gtk.Label(label="")
        self.caixa.add(self.lbl_resultado)

        self.lbl_recup_instrucao = Gtk.Label(label="Insira a pontuação obtida na Recuperação:")
        self.nota_recup = Gtk.Entry()
        self.nota_recup.set_placeholder_text("Pontuação da Recuperação")
        self.btn_recalcular = Gtk.Button(label="Recalcular Média Final")
        self.btn_recalcular.connect("clicked", self.recalcular_recuperacao)

        janela.add(self.caixa)
        janela.show_all()
        
    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def calcular_media(self, componente=None, dados=None):
        try:
            n1 = float(self.nota1.get_text())
            n2 = float(self.nota2.get_text())
            n3 = float(self.nota3.get_text())
            
            self.media = (n1 + n2 + n3) / 3
            
            if self.media >= 6.0:
                self.lbl_resultado.set_markup(f"Média: <b>{self.media:.1f}</b> - <span foreground='green'><b>Situação: Regularizado</b></span>")
                self.remover_campos_recuperacao()
            else:
                self.lbl_resultado.set_markup(f"Média: <b>{self.media:.1f}</b> - <span foreground='red'><b>Situação: Avaliação Suplementar</b></span>")
                self.mostrar_campos_recuperacao()
                
        except ValueError:
            self.lbl_resultado.set_label("Erro: Insira pontuações válidas.")

    def mostrar_campos_recuperacao(self):
        if self.lbl_recup_instrucao.get_parent() is None:
            self.caixa.add(self.lbl_recup_instrucao)
            self.caixa.add(self.nota_recup)
            self.caixa.add(self.btn_recalcular)
            self.caixa.show_all()

    def remover_campos_recuperacao(self):
        if self.lbl_recup_instrucao.get_parent() is not None:
            self.caixa.remove(self.lbl_recup_instrucao)
            self.caixa.remove(self.nota_recup)
            self.caixa.remove(self.btn_recalcular)

    def recalcular_recuperacao(self, componente=None, dados=None):
        try:
            n_rec = float(self.nota_recup.get_text())
            nova_media = (self.media + n_rec) / 2
            
            if nova_media >= 6.0:
                self.lbl_resultado.set_markup(f"Nova Média: <b>{nova_media:.1f}</b> - <span foreground='green'><b>Aprovado pós-exame</b></span>")
            else:
                self.lbl_resultado.set_markup(f"Nova Média: <b>{nova_media:.1f}</b> - <span foreground='red'><b>Reprovado no período</b></span>")
        except ValueError:
            self.lbl_resultado.set_label("Erro: Insira um valor de recuperação válido.")

if __name__ == "__main__":
    app = TelaNotas()
    Gtk.main()