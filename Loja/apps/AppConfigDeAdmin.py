import tkinter

from entrada_de_dados.cargos_e_salarios import dicionario_de_cargos_da_loja
from entrada_de_dados.edicoes_de_administrador import adicionar_cargo_em_cargos_e_salarios
from estrutura.AppBase import AppBase
from estrutura.Cargo import Cargo
from estrutura.Loja import Loja


def criar_texto(local, conteudo):
    texto = tkinter.Label(local, text=f'{conteudo}:', font="Arial 10", bg="white", bd=5, width=9, anchor="e")
    return texto


def criar_entrada(local, variavel):
    entrada = tkinter.Entry(local, font="Consolas 15", textvariable=variavel)
    return entrada


def criar_botao(local, texto):
    botao = tkinter.Button(local, text=texto)
    return botao


def janela_de_erro(ex):
    tipo_de_erro = ex

    erro = tkinter.Toplevel()
    erro.title("Mensagem de ERRo")
    erro.resizable(False, False)
    erro.geometry("300x200+400+200")

    tkinter.Label(erro, text=f'{tipo_de_erro}').pack(side=tkinter.BOTTOM)

    tkinter.Label(erro,
                  text=f"\n\n\n\nErro ao Executar Acao \n\n\n\n"
                  ).pack(fill="both", anchor="center")

    erro.mainloop()


class AppConfigDeAdmin(AppBase):

    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.loja = loja
        self.dicionario_de_cargos = dicionario_de_cargos_da_loja[self.loja.cnpj]
        self.sub_window = None
        self.cargo_criado = None

        self.window.geometry("+400+200")

        self.label_principal = tkinter.Label(self.window, text="Configuracoes De Administrador")
        self.label_principal.pack(fill="x")

        self.frame_dados.pack(side="left")

        self.label_botoes = tkinter.Label(self.frame_dados, text="Opcoes:")
        self.label_botoes.pack()
        self.botao_cargo_novo = tkinter.Button(self.frame_dados, text="Criar Cargo Novo")
        self.botao_cargo_novo.config(command=self.abrir_janela_de_cargo_novo)
        self.botao_cargo_novo.pack()
        self.botao_editar_cargo = criar_botao(self.frame_dados, "Editar Cargo")
        self.botao_editar_cargo.config(command=self.print_para_testar_botao)
        self.botao_editar_cargo.pack()

        self.frame_dados_2.pack(side="right")

        self.label_listbox = tkinter.Label(self.frame_dados_2, text="Cargos existentes:")
        self.label_listbox.pack()
        self.listbox = tkinter.Listbox(self.frame_dados_2)
        self.listbox.pack(fill="both")
        for i in self.dicionario_de_cargos:
            self.listbox.insert("end", i)

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
        self.sub_window.geometry("+400+200")

        tkinter.Label(self.sub_window, text="Criar Novo Cargo")

        frame_esqu = tkinter.Frame(self.sub_window, bg="white", bd=1)
        frame_esqu.grid(row=0, column=0)
        frame_dir = tkinter.Frame(self.sub_window, bg="white", bd=1)
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

        if len(cargo) == 0:
            janela_de_erro("Cargo em Branco ou invalido")
        else:
            try:
                int(cargo)
                janela_de_erro("Nome de Cargo invalido")
            except Exception as ex:
                try:
                    self.cargo_criado = Cargo(cargo, salario, bonus, comissao, cnpj)
                    int(salario)
                    float(bonus)
                    float(comissao)
                    adicionar_cargo_em_cargos_e_salarios(self.cargo_criado)
                    window.destroy()
                    return ex
                except Exception as ex:
                    janela_de_erro(ex)

    def print_para_testar_botao(self):
        print("\n")
        print("teste")
        try:
            item_selecionado_da_listbox = self.listbox.get(tkinter.ANCHOR)
            for i in self.dicionario_de_cargos[item_selecionado_da_listbox]:
                print(self.dicionario_de_cargos[item_selecionado_da_listbox][i])
        except Exception as ex:
            janela_de_erro(f'{ex}: Selecione um item na lista de cargos')


