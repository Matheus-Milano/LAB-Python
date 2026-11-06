# -*- coding: utf-8 -*-

from conexao import conectar

def listar():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, tipo FROM categoria ORDER BY id")
        return cursor.fetchall()

def inserir(nome, tipo):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO categoria (nome, tipo) VALUES (%s, %s)", (nome, tipo))
        conexao.commit()

def atualizar(id_categoria, nome, tipo):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("UPDATE categoria SET nome = %s, tipo = %s WHERE id = %s", (nome, tipo, id_categoria))
        conexao.commit()

def excluir(id_categoria):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM categoria WHERE id = %s", (id_categoria,))
        conexao.commit()
