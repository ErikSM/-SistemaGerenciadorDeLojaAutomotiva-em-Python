import tkinter

from entrada_de_dados.funcoes_de_edicao import editar_arquivo_em_opcoes_avancadas
from estrutura.AppBase import AppBase
from estrutura.Loja import Loja


class AppOpcoesAvancadas(AppBase):

    def __init__(self, title, loja: Loja, tipo_de_lista):
        super().__init__(title)

        self.loja_editada = loja
        self.tipo_de_lista = tipo_de_lista

        self.mensagem_de_erro = "  ERRor  \n\nSelecione uma opcao na lista..."

        self.entrada_de_conteudo_novo = None
        self.item_selecionado = None

        self.variavel_editada_1 = None
        self.variavel_editada_2 = None
        self.variavel_editada_3 = None
        self.variavel_editada_4 = None

        self.dicionario_temporario = dict()

        self.copia_do_dicionario = loja.dicionario_da_loja
        self.lista_utilizada = self.copia_do_dicionario[self.tipo_de_lista]

        if tipo_de_lista == "carros":
            self.variavel_editada_1 = "montadora"
            self.variavel_editada_2 = "nome"
            self.variavel_editada_3 = "ano"
            self.variavel_editada_4 = "valor_de_aquisicao"
        else:
            self.variavel_editada_1 = "nome"
            self.variavel_editada_2 = "cpf"
            self.variavel_editada_3 = "telefone"
            self.variavel_editada_4 = "email"

        for i in self.lista_utilizada:
            self.dicionario_temporario[i.nome_da_variavel] = i

        self.frame_dados.pack()
        self.sub_frame_dados_esq = tkinter.Frame(self.frame_dados, bg="grey70", bd=4)
        self.sub_frame_dados_esq.pack(side="left", fill="y")
        self.sub_frame_dados_dir = tkinter.Frame(self.frame_dados, bg="grey70", bd=4)
        self.sub_frame_dados_dir.pack(side="right", fill="y")

        tkinter.Label(self.sub_frame_dados_esq, font="Arial 10", text="Opcoes:", bg="grey70").pack(fill="x")

        self.botao_visualizar = None
        self.botao_modo_editar = None
        self.botao_fechar_app = None

        self.botao_variavel_1 = None
        self.botao_variavel_2 = None
        self.botao_variavel_3 = None
        self.botao_variavel_4 = None
        self.botao_sair_de_edicao = None

        self.modo_vizualizacao()

        tkinter.Label(self.sub_frame_dados_dir, font="Consolas 8", text="Selecione uma opcao:", fg="black",
                      bg="grey30").pack(fill="x")

        self.listbox = tkinter.Listbox(self.sub_frame_dados_dir, width=40, height=9, bd=2, bg="grey90")
        self.listbox.pack(side="right")

        self.texto_relatorio.pack()

        for i in self.dicionario_temporario:
            self.listbox.insert("end", i)

        self.window.mainloop()

    def ativar_edicao(self):
        self.botao_visualizar.destroy()
        self.botao_modo_editar.destroy()
        self.botao_fechar_app.destroy()
        self.modo_edicao()

    def desativar_edicao(self):
        self.botao_sair_de_edicao.destroy()
        self.botao_variavel_1.destroy()
        self.botao_variavel_2.destroy()
        self.botao_variavel_3.destroy()
        self.botao_variavel_4.destroy()
        self.modo_vizualizacao()

    def modo_edicao(self):
        self.botao_variavel_1 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_1}", bg="grey",
                                               width=19, command=lambda:
            self.editar_variavel(self.tipo_de_lista, self.variavel_editada_1))
        self.botao_variavel_1.pack()

        self.botao_variavel_2 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_2}", bg="grey",
                                               width=19, command=lambda:
            self.editar_variavel(self.tipo_de_lista, self.variavel_editada_2))
        self.botao_variavel_2.pack()

        self.botao_variavel_3 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_3}", bg="grey",
                                               width=19, command=lambda:
            self.editar_variavel(self.tipo_de_lista, self.variavel_editada_3))
        self.botao_variavel_3.pack()

        self.botao_variavel_4 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_4}", bg="grey",
                                               width=19, command=lambda:
            self.editar_variavel(self.tipo_de_lista, self.variavel_editada_4))
        self.botao_variavel_4.pack()

        self.botao_sair_de_edicao = tkinter.Button(self.sub_frame_dados_esq, text="Sair de edicao", bg="grey90", bd=6,
                                                   width=18, command=self.desativar_edicao)
        self.botao_sair_de_edicao.pack()

    def modo_vizualizacao(self):
        self.botao_visualizar = tkinter.Button(self.sub_frame_dados_esq, text="Vizualizar informacoes", bg="grey",
                                               width=19, command=self.vizualizar_objeto)
        self.botao_visualizar.pack()

        self.botao_modo_editar = tkinter.Button(self.sub_frame_dados_esq, text="Editar", bg="grey",
                                                width=19, command=self.ativar_edicao)
        self.botao_modo_editar.pack()

        self.botao_fechar_app = tkinter.Button(self.sub_frame_dados_esq, text="Fechar", bg="grey90", bd=6,
                                               width=18, command=self.fechar)
        self.botao_fechar_app.pack()

    def vizualizar_objeto(self):
        self.item_selecionado = self.listbox.get(tkinter.ANCHOR)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        if self.item_selecionado == '':
            self.texto_relatorio.insert(1.0, self.mensagem_de_erro)
        else:
            self.texto_relatorio.insert(1.0, self.dicionario_temporario[self.item_selecionado].mostrar_dados())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def editar_variavel(self, tipo_de_lista, variavel_editada):
        self.item_selecionado = self.listbox.get(tkinter.ANCHOR)

        if self.item_selecionado == '':
            self.texto_relatorio.config(state=tkinter.NORMAL)
            self._apagar_relatorio()
            self.texto_relatorio.insert(1.0, self.mensagem_de_erro)
            self.texto_relatorio.config(state=tkinter.DISABLED)
        else:
            objeto = self.dicionario_temporario[self.item_selecionado]

            window = tkinter.Toplevel()
            window.title(f'Editar {variavel_editada}')
            window.resizable(False, False)
            window.geometry("300x200+300+200")

            label = tkinter.Label(window, text=f'Editar {variavel_editada}', pady=30)
            label.pack()

            self.entrada_de_conteudo_novo = tkinter.Entry(window)
            self.entrada_de_conteudo_novo.pack()

            button_exit = tkinter.Button(window, text="OK",
                                         command=lambda: self.executar_edicao_do_conteudo(window, objeto,
                                                                                          tipo_de_lista,
                                                                                          variavel_editada))
            button_exit.pack()

    def executar_edicao_do_conteudo(self, window, objeto, tipo_de_lista, variavel_editada):
        novo_conteudo = self.entrada_de_conteudo_novo.get()
        editar_arquivo_em_opcoes_avancadas(objeto, tipo_de_lista, variavel_editada, novo_conteudo)
        self.window.quit()
        window.destroy()

    def fechar(self):
        self.window.quit()
        self.window.destroy()
