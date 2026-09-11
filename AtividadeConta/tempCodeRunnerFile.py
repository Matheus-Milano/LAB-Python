    def ao_nova_conta(self, componente = None, dados = None):
        self.conta.limpar()
        self.lista = []
        self.lbl_lista.set_text("")
        self.lbl_resultado.set_text("")
        self.lbl_rodape.set_text("Total de pessoas: 0")
        self.txt_pessoa.set_text("")
        self.txt_consumo.set_text("")
        self.txt_pessoa.grab_focus()
        