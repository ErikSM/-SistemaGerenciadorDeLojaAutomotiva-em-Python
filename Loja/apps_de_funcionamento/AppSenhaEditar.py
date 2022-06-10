from future.moves import tkinter

from entrada_de_dados.criar_e_adicionar_senha_na_loja import adicionar_nova_senha_criada_no_arquivo_da_loja
from estrutura.AppSenha import AppSenha
from estrutura.Loja import Loja


class AppSenhaEditar(AppSenha):
    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.loja = loja
        self.encerrado = False

        self.botao_adicionar.config(text="  Editar...", bd=3, command=self.modificar_senha)

        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.insert(1.0, "\n   Digite a senha no campo acima para registra-la!!")
        self.texto_relatorio.config(state=tkinter.DISABLED)

    def modificar_senha(self):
        self.loja.senha = self.captura_senha.get()
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.delete(1.0, "end")
        self.texto_relatorio.insert(1.0, "\n   !!    Senha Atualizada !!   ")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        adicionar_nova_senha_criada_no_arquivo_da_loja(self.loja)

        self.window.quit()
