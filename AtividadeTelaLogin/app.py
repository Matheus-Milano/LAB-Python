#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


CAMINHO_LOGIN = os.path.join(os.path.dirname(__file__), "login.glade")
CAMINHO_PRINCIPAL = os.path.join(os.path.dirname(__file__), "principal.glade")

USUARIOS = {
    "admin": "1234",
    "user": "9876"
}


class JanelaPrincipal:
    def __init__(self, usuario):
        self.usuario = usuario

        builder = Gtk.Builder()
        builder.add_from_file(CAMINHO_PRINCIPAL)

        self.janela = builder.get_object("jan_principal")
        self.lbl_saudacao = builder.get_object("lbl_saudacao")
        self.btn_sair = builder.get_object("btn_sair")

        builder.connect_signals(self)
        self.btn_sair.connect("clicked", self.ao_sair)
        self.janela.connect("destroy", self.ao_destruir)

        self.lbl_saudacao.set_markup(f"<big>Olá, {self.usuario}!</big>")
        self.janela.set_title(f"Sistema - {self.usuario}")

        self.janela.show_all()

    def ao_sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()


class JanelaLogin:
    def __init__(self):
        self.principal = None

        builder = Gtk.Builder()
        builder.add_from_file(CAMINHO_LOGIN)

        self.janela = builder.get_object("jan_login")
        self.txt_usuario = builder.get_object("txt_usuario")
        self.txt_senha = builder.get_object("txt_senha")
        self.btn_entrar = builder.get_object("btn_entrar")

        # Conexão manual dos sinais
        builder.connect_signals(self)
        self.btn_entrar.connect("clicked", self.ao_entrar)

        self.janela.show_all()
        self.txt_usuario.grab_focus()

    def credenciais_validas(self, usuario, senha):
        return usuario in USUARIOS and USUARIOS[usuario] == senha

    def avisar(self, mensagem):
        dialogo = Gtk.MessageDialog(
            transient_for=self.janela,
            modal=True,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=mensagem
        )

        dialogo.run()
        dialogo.destroy()

    def ao_entrar(self, componente=None, dados=None):
        usuario = self.txt_usuario.get_text().strip()
        senha = self.txt_senha.get_text()

        if self.credenciais_validas(usuario, senha):
            self.principal = JanelaPrincipal(usuario)
            self.janela.hide()
        else:
            print("login invalido")
            self.avisar("Usuário ou senha inválidos.")
            self.txt_senha.set_text('')
            self.txt_usuario.grab_focus()

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()


if __name__ == "__main__":
    tela1 = JanelaLogin()
    Gtk.main()