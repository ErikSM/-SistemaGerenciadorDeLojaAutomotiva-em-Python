import tkinter

from entrada_de_dados.edicoes_de_administrador import adicionar_cargo_em_cargos_e_salarios
from estrutura.AppBase import AppBase
from estrutura.Cargo import Cargo
from estrutura.Loja import Loja


def criar_texto(local, conteudo):
    texto = tkinter.Label(local, text=f'{conteudo}:', font="Arial 10", bg="grey", bd=5, width=8, anchor="e")
    return texto


def criar_entrada(local, variavel):
    entrada = tkinter.Entry(local, font="Consolas 15", textvariable=variavel)
    return entrada


class AppConfigDeAdmin(AppBase):

    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.loja = loja
        self.sub_window = None
        self.cargo_criado = None

        self.frame_dados.pack()

        self.label = tkinter.Label(self.window, text="Configuracoes De Administrador")
        self.label.pack(side="top")

        self.botao_cargo_novo = tkinter.Button(self.window, text="Criar Cargo Novo")
        self.botao_cargo_novo.config(command=self.abrir_janela_de_cargo_novo)
        self.botao_cargo_novo.pack()

    def abrir_janela_de_cargo_novo(self):
        self.window.destroy()

        cargo = "cargo"
        salario = "salario"
        bonus = "bonus"
        comissao = "comissao"

        dicionario_de_variaveis = {'cargo': cargo, "salario": salario,
                                   "bonus": bonus, "comissao": comissao}

        self.sub_window = tkinter.Toplevel()
        self.sub_window.title("Criar Novo Cargo")
        self.sub_window.resizable(False, False)
        self.sub_window.geometry()

        tkinter.Label(self.sub_window, text="Criar Novo Cargo")

        frame_esqu = tkinter.Frame(self.sub_window, bg="grey", bd=1)
        frame_esqu.grid(row=0, column=0)
        frame_dir = tkinter.Frame(self.sub_window, bg="grey", bd=1)
        frame_dir.grid(row=0, column=1)
        frame_rodape = tkinter.Frame(self.sub_window, bd=2)
        frame_rodape.grid(row=1, column=1)

        for i in dicionario_de_variaveis:
            if str(i) == "bonus" or str(i) == "comissao":
                marca = "%"
            elif str(i) == "salario":
                marca = "R$"
            else:
                marca = ""
            criar_texto(frame_esqu, f'{i} {marca}').pack()
            dicionario_de_variaveis[str(i)] = criar_entrada(frame_dir, i)
            dicionario_de_variaveis[str(i)].pack()

        botao_teste = tkinter.Button(frame_rodape, text="Adicionar Cargo", bg="grey70", bd=1)
        botao_teste.config(command=lambda: self._criar_cargo_novo_da_loja(dicionario_de_variaveis, self.sub_window))
        botao_teste.grid(row=0, column=1)

        self.sub_window.mainloop()

    def _criar_cargo_novo_da_loja(self, dicionario_de_variaveis, window):
        cargo = dicionario_de_variaveis["cargo"].get()
        salario = dicionario_de_variaveis["salario"].get()
        bonus = dicionario_de_variaveis["bonus"].get()
        comissao = dicionario_de_variaveis["comissao"].get()
        cnpj = self.loja.cnpj

        try:
            self.cargo_criado = Cargo(cargo, salario, bonus, comissao, cnpj)
            adicionar_cargo_em_cargos_e_salarios(self.cargo_criado)
            window.destroy()
        except Exception as ex:
            self.janela_de_erro(ex)

    def janela_de_erro(self, ex):
        tipo_de_erro = ex

        erro = tkinter.Toplevel()
        erro.title("Mensagem de ERRo")
        erro.resizable(False, False)
        erro.geometry("200x200+200+200")

        tkinter.Label(erro, text=f'{tipo_de_erro}')

        tkinter.Label(erro,
                      text=f"\n\n\n\nErro ao criar Cargo Novo \n Preencha todos os campos corretamente... "
                      ).pack(fill="both", anchor="center")

        erro.mainloop()
