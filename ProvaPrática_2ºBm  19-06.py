#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  - Nathan Mazzaro e Matheus Milano 

from abc import ABC, abstractmethod
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class AtividadeFisica(ABC):
    def __init__(self, data, distancia):
        self.__data = data
        self.__distancia = distancia

    @property
    def data(self):
        return self.__data
    
    @property
    def distancia(self):
        return self.__distancia

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @distancia.setter
    def distancia(self, nova_distancia):
        self.__distancia = nova_distancia
    
    @abstractmethod
    def calcular_calorias(self):
        pass

class Corrida(AtividadeFisica):
    def __init__(self, data, distancia):
        super().__init__(data, distancia)
    
    def calcular_calorias(self):
        return self.distancia * 70

class Caminhada(AtividadeFisica):
    def __init__(self, data, distancia):
        super().__init__(data, distancia)
    
    def calcular_calorias(self):
        return self.distancia * 35
    
class DiarioDeTreino:
    def __init__(self, diario):
        self.diario = diario

    def resumo_calorico(self):
        calorias_gastas = 0
        for treino in self.diario:
            calorias_gastas += treino.calcular_calorias()
        return calorias_gastas
    
class Tela:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Tracker de Treinos")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        self.caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        
        btn_registrar_corrida = Gtk.Button(label = "Registrar Corrida")
        btn_registrar_corrida.connect("clicked", self.registrar_corrida)
        self.caixa.add(btn_registrar_corrida)

        self.distancia_corrida = Gtk.Entry()
        self.distancia_corrida.set_placeholder_text("Distancia(KM)")
        self.caixa.add(self.distancia_corrida)
        
        btn_registrar_caminhada = Gtk.Button(label = "Registrar Caminhada")
        btn_registrar_caminhada.connect("clicked", self.registrar_caminhada)
        self.caixa.add(btn_registrar_caminhada)

        self.distancia_caminhada = Gtk.Entry()
        self.distancia_caminhada.set_placeholder_text("Distancia(KM)")
        self.caixa.add(self.distancia_caminhada)


        self.lbl_msg = Gtk.Label(label="")
        self.caixa.add(self.lbl_msg)

        janela.add(self.caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def registrar_corrida(self, componente=None, dados=None):
        try:
            val_distancia = float(self.distancia_corrida.get_text())
        except ValueError:
            self.lbl_msg.set_label("Entrada Inválida")
        corrida = Corrida(0, val_distancia)
        self.lbl_msg.set_label(str(corrida.calcular_calorias()))
        print("Corrida:")
        print(corrida.calcular_calorias())
        return corrida
    
    def registrar_caminhada(self, componente=None, dados=None): 
        try:
            val_distancia = float(self.distancia_caminhada.get_text())
        except ValueError:
            self.lbl_msg.set_label("Entrada Inválida")
        caminhada = Caminhada(0, val_distancia)
        self.lbl_msg.set_label(str(caminhada.calcular_calorias()))
        print("Caminhada:")
        print(caminhada.calcular_calorias())
        return caminhada

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()

