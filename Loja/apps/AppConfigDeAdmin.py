import tkinter

from entrada_de_dados.dicionario_cargos import dicionario_de_cargos_da_loja
from entrada_de_dados.editar_dicionario_cargos import adicionar_cargo_em_dicionario_cargos
from entrada_de_dados.funcoes_de_edicao import editar_arquivo_em_config_de_admim
from estrutura.AppBase import AppBase
from estrutura.Cargo import Cargo
from estrutura.Loja import Loja


def criar_texto(local, conteudo):
    texto = tkinter.Label(local, text=f'{conteudo}:', font="Arial 10", bg="white", bd=5, width=9, anchor="e")
    return texto


def criar_entrada(local, variavel):
    entrada = tkinter.Entry(local, font="Consolas 15", textvariable=variavel)
    return entrada


def criar_botao(local, texto, largura=10, altura=1):
    botao = tkinter.Button(local, text=texto, width=largura, height=altura)
    return botao


def criar_janela_de_edicoes(tilulo, tamanho="300x200+400+200"):
    janela = tkinter.Toplevel()
    janela.title(tilulo)
    janela.resizable(False, False)
    janela.geometry(tamanho)
    return janela


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

        self.label_principal = tkinter.Label(self.window, text="Configuracoes De Administrador", font='Arial 10 bold')
        self.label_principal.pack(fill="x")

        self.frame_dados.pack(side="left", fill="both")

        self.label_botoes = tkinter.Label(self.frame_dados, text="Opcoes:")
        self.label_botoes.pack(fill="x")
        self.botao_cargo_novo = criar_botao(self.frame_dados, "Criar Cargo Novo", 15)
        self.botao_cargo_novo.config(command=self.abrir_janela_de_cargo_novo)
        self.botao_cargo_novo.pack()
        self.botao_editar_cargo = criar_botao(self.frame_dados, "Editar Cargo", 15)
        self.botao_editar_cargo.config(command=self.abrir_janela_editar_itens_do_cargo)
        self.botao_editar_cargo.pack()

        self.frame_dados_2.pack(side="right")

        self.label_listbox = tkinter.Label(self.frame_dados_2, text="Cargos existentes:")
        self.label_listbox.pack(fill="x")
        self.listbox = tkinter.Listbox(self.frame_dados_2)
        self.listbox.pack(fill="both")

        try:
            for i in self.dicionario_de_cargos:
                if self.dicionario_de_cargos[i]["cnpj"] == loja.cnpj:
                    self.listbox.insert("end", i)
        except Exception as ex:
            self.botao_editar_cargo.destroy()
            janela_de_erro(ex)

    def abrir_janela_de_cargo_novo(self):
        self.window.destroy()

        dicionario_de_variaveis = dict()
        dicionario_de_variaveis['cargo'] = "cargo"
        dicionario_de_variaveis['salario'] = "salario"
        dicionario_de_variaveis['bonus'] = "bonus"
        dicionario_de_variaveis['comissao'] = "comissao"

        self.sub_window = criar_janela_de_edicoes("Criar Novo Cargo", "+400+200")

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

        botao_adicionar = tkinter.Button(frame_rodape, text="Adicionar Cargo", bg="grey70", bd=1)
        botao_adicionar.config(command=lambda: self._criar_cargo_novo_da_loja(dicionario_de_variaveis, self.sub_window))
        botao_adicionar.grid(row=0, column=1)

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
                    adicionar_cargo_em_dicionario_cargos(self.cargo_criado)
                    window.destroy()
                    return ex
                except Exception as ex:
                    janela_de_erro(ex)

    def abrir_janela_editar_itens_do_cargo(self):
        try:
            self.sub_window = criar_janela_de_edicoes("Editar Iten do Cargo", "400x200+400+300")

            frame_dir = tkinter.Frame(self.sub_window)
            frame_dir.pack(side="right", fill="both")
            frame_esq = tkinter.Frame(self.sub_window)
            frame_esq.pack(side="left", fill="both")

            tkinter.Label(frame_esq, text=" Editar Itens do Cargo", font="Arial 10 bold", height=2).pack()

            tkinter.Label(frame_esq, text="Selecione para editar:").pack()
            spinbox_de_variaveis_para_editar = tkinter.Spinbox(frame_esq, width=18, bg="grey70")
            spinbox_de_variaveis_para_editar.pack()

            tkinter.Label(frame_esq, text="\nNovo conteudo:").pack()
            Entry_conteudo_novo = tkinter.Entry(frame_esq, bd=7)
            Entry_conteudo_novo.pack()

            editar_atributo = criar_botao(frame_esq, "Modificar", 15)
            editar_atributo.config(bd=9, bg="grey",
                                   command=lambda: self._editar_iten_selecionado(spinbox_de_variaveis_para_editar.get(),
                                                                                 Entry_conteudo_novo.get(),
                                                                                 cargo_selecionado_para_listbox))
            editar_atributo.pack()

            tkinter.Label(frame_dir, text="Detalhes do Cargo Selecionado:").pack()
            listbox_de_exibicao = tkinter.Listbox(frame_dir, font="Consolas 10", width=35, height=10, fg="black")
            listbox_de_exibicao.pack(fill='both')

            lista_para_spinbox = list()
            cargo_selecionado_para_listbox = self.listbox.get(tkinter.ANCHOR)
            for i in self.dicionario_de_cargos[cargo_selecionado_para_listbox]:
                if i == "linha no arquivo":
                    pass
                else:
                    lista_para_spinbox.append(i)
                    listbox_de_exibicao.config(state=tkinter.NORMAL)
                    listbox_de_exibicao.insert("end",
                                               f' {i}:  {self.dicionario_de_cargos[cargo_selecionado_para_listbox][i]}')
                    listbox_de_exibicao.config(state=tkinter.DISABLED)

            spinbox_de_variaveis_para_editar.config(values=lista_para_spinbox)
            self.window.destroy()

            self.sub_window.mainloop()

        except Exception as ex:
            self.sub_window.destroy()
            janela_de_erro(ex)

    def _editar_iten_selecionado(self, variavel_para_editar, novo_conteudo, cargo_selecionado):
        editar_arquivo_em_config_de_admim(
            self.dicionario_de_cargos[f"{cargo_selecionado}"],
            variavel_para_editar,
            novo_conteudo
        )

        self.sub_window.destroy()
