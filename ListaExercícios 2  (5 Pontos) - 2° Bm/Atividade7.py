#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aluno: Matheus Henrique Milano
# Turma: 2° Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class FormInscricao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Inscrição de Participantes")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        
        self.txt_nome = Gtk.Entry()
        self.txt_nome.set_placeholder_text("Nome Completo do Candidato")
        caixa.add(self.txt_nome)

        self.combo_curso = Gtk.ComboBoxText()
        self.combo_curso.append_text("Técnico em Informática")
        self.combo_curso.append_text("Técnico em Eletrônica")
        self.combo_curso.append_text("Técnico em Eletrotécnica")
        self.combo_curso.append_text("Técnico em Redes de Computadores")
        self.combo_curso.set_active(0) 
        caixa.add(self.combo_curso)

        self.chk_certificado = Gtk.CheckButton(label="Emitir comprovante de horas de participação?")
        caixa.add(self.chk_certificado)

        btn_salvar = Gtk.Button(label="Efetuar Registro")
        btn_salvar.connect("clicked", self.salvar_dados)
        caixa.add(btn_salvar)

        self.lbl_resumo = Gtk.Label(label="")
        self.lbl_resumo.set_justify(Gtk.Justification.LEFT)
        caixa.add(self.lbl_resumo)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def salvar_dados(self, componente=None, dados=None):
        nome = self.txt_nome.get_text()
        curso = self.combo_curso.get_active_text()
        quer_certificado = "Sim" if self.chk_certificado.get_active() else "Não"
        
        if nome.strip() == "":
            self.lbl_resumo.set_markup("<span foreground='red'>O campo de nome é obrigatório!</span>")
            return

        resumo = (
            f"<b>--- Dados Registrados ---</b>\n"
            f"<b>Nome:</b> {nome}\n"
            f"<b>Curso:</b> {curso}\n"
            f"<b>Deseja Certificado?</b> {quer_certificado}"
        )

        print("\n" + resumo.replace("<b>", "").replace("</b>", ""))

        self.lbl_resumo.set_markup(resumo)

if __name__ == "__main__":
    app = FormInscricao()
    Gtk.main()