import tkinter

from entrada_de_dados.editar_senha_na_loja import adicionar_nova_senha_criada_no_arquivo_da_loja, \
    apagar_senha_criada_no_arquivo_da_loja
from estrutura.AppSenha import AppSenha
from estrutura.Loja import Loja


class AppSenhaEditar(AppSenha):
    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.loja = loja
        self.encerrado = False

        self.frame_dados.pack(fill="both", side="top")

        self.botao_executar.config(text="  Editar...", bd=3, command=self.modificar_senha)
        self.botao_executar.grid(row=0, column=2)

        self.label.grid(row=0, column=0)
        self.captura_senha.grid(row=0, column=1)

        self.texto_relatorio.pack(fill="both", side="bottom")
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.insert(1.0, "\n   Digite a senha no campo acima para registra-la!!")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        self.botao_remover = tkinter.Button(self.frame_dados, text="Deletar atual", bd=3,
                                            command=self.deletar_senha_atual)
        self.botao_remover.grid(row=0, column=3)

    def modificar_senha(self):
        self.loja.senha = self.captura_senha.get()
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.delete(1.0, "end")
        self.texto_relatorio.insert(1.0, "\n   !!    Senha Atualizada !!   ")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        adicionar_nova_senha_criada_no_arquivo_da_loja(self.loja)

        self.window.destroy()

    def deletar_senha_atual(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.delete(1.0, "end")
        self.texto_relatorio.insert(1.0, "\n   !!    Senha Deletada !!   ")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        apagar_senha_criada_no_arquivo_da_loja(self.loja)

        self.window.destroy()
