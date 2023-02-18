import tkinter

from entrada_de_dados.funcoes_de_edicao import editar_arquivo_em_opcoes_avancadas
from estrutura.AppBase import AppBase
from estrutura.Loja import Loja


class AppOpcoesAvancadas(AppBase):

    def __init__(self, title, loja: Loja, tipo_de_lista):
        super().__init__(title)

        self.loja_editada = loja
        self.tipo_de_lista = tipo_de_lista

        self.copia_do_dicionario = loja.dicionario_da_loja
        self.lista_utilizada = self.copia_do_dicionario[self.tipo_de_lista]

        self.clique_no_botao_editar = False

        self.item_selecionado_da_listbox = None
        self.objeto_selecionado_para_edicao = None

        self.botao_visualizar = None
        self.botao_modo_editar = None
        self.botao_fechar_app = None
        self.botao_variavel_1 = None
        self.botao_variavel_2 = None
        self.botao_variavel_3 = None
        self.botao_variavel_4 = None
        self.botao_sair_de_edicao = None

        self.string_nova_para_edicao = str()
        self.mensagem_de_erro = str()

        self.dicionario_de_objetos_para_editar = dict()

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
            self.dicionario_de_objetos_para_editar[i.nome_da_variavel] = i

        self.frame_dados.pack()
        self.sub_frame_dados_esq = tkinter.Frame(self.frame_dados, bg="grey70", bd=4)
        self.sub_frame_dados_esq.pack(side="left", fill="y")
        self.sub_frame_dados_dir = tkinter.Frame(self.frame_dados, bg="grey70", bd=4)
        self.sub_frame_dados_dir.pack(side="right", fill="y")

        tkinter.Label(self.sub_frame_dados_esq, font="Arial 10", text="Menu de edicao:", bg="grey70").pack(fill="x")

        tkinter.Label(self.sub_frame_dados_dir, font="Consolas 8", text="Selecione uma opcao:", fg="black",
                      bg="grey30").pack(fill="x")

        self.listbox = tkinter.Listbox(self.sub_frame_dados_dir, width=40, height=9, bd=2, bg="grey90")
        self.listbox.pack(side="right")

        self.texto_relatorio.pack()

        self.ativar_modo_vizualizacao()

        self.window.mainloop()

    def ativar_modo_edicao(self):
        self.item_selecionado_da_listbox = self.listbox.get(tkinter.ANCHOR)
        if self.item_selecionado_da_listbox == "":
            self._executar_mensagem_de_erro()
        else:
            self.clique_no_botao_editar = True
            self.objeto_selecionado_para_edicao = self.dicionario_de_objetos_para_editar[self.item_selecionado_da_listbox]

            self.vizualizar_objeto()

            self.listbox.delete(0, "end")
            self.listbox.insert("end", self.item_selecionado_da_listbox)
            self.listbox.config(state=tkinter.DISABLED)

            self._excluir_botoes_de_vizualizacao()
            self._criar_botoes_de_edicao()

    def ativar_modo_vizualizacao(self):
        self.objeto_selecionado_para_edicao = None
        self.item_selecionado_da_listbox = None
        self.listbox.config(state=tkinter.NORMAL)
        self.listbox.delete(0, "end")

        for i in self.dicionario_de_objetos_para_editar:
            self.listbox.insert("end", i)

        self._criar_botoes_de_vizualizacao()
        if self.clique_no_botao_editar:
            self._excluir_botoes_de_edicao()

    def _excluir_botoes_de_vizualizacao(self):
        self.botao_visualizar.destroy()
        self.botao_modo_editar.destroy()
        self.botao_fechar_app.destroy()

    def _excluir_botoes_de_edicao(self):
        self.botao_sair_de_edicao.destroy()
        self.botao_variavel_1.destroy()
        self.botao_variavel_2.destroy()
        self.botao_variavel_3.destroy()
        self.botao_variavel_4.destroy()

    def _criar_botoes_de_edicao(self):
        self.botao_variavel_1 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_1}", bg="grey",
                                               width=19, command=lambda: self.editar_variavel(self.tipo_de_lista,
                                                                                              self.variavel_editada_1))
        self.botao_variavel_1.pack()

        self.botao_variavel_2 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_2}", bg="grey",
                                               width=19, command=lambda: self.editar_variavel(self.tipo_de_lista,
                                                                                              self.variavel_editada_2))
        self.botao_variavel_2.pack()

        self.botao_variavel_3 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_3}", bg="grey",
                                               width=19, command=lambda: self.editar_variavel(self.tipo_de_lista,
                                                                                              self.variavel_editada_3))
        self.botao_variavel_3.pack()

        self.botao_variavel_4 = tkinter.Button(self.sub_frame_dados_esq, text=f"{self.variavel_editada_4}", bg="grey",
                                               width=19, command=lambda: self.editar_variavel(self.tipo_de_lista,
                                                                                              self.variavel_editada_4))
        self.botao_variavel_4.pack()

        self.botao_sair_de_edicao = tkinter.Button(self.sub_frame_dados_esq, text="Sair de edicao", bg="grey90", bd=6,
                                                   width=18, command=self.ativar_modo_vizualizacao)
        self.botao_sair_de_edicao.pack()

    def _criar_botoes_de_vizualizacao(self):
        self.botao_visualizar = tkinter.Button(self.sub_frame_dados_esq, text="Vizualizar informacoes", bg="grey",
                                               width=19, command=self.vizualizar_objeto)
        self.botao_visualizar.pack()

        self.botao_modo_editar = tkinter.Button(self.sub_frame_dados_esq, text="Editar", bg="grey",
                                                width=19, command=self.ativar_modo_edicao)
        self.botao_modo_editar.pack()

        self.botao_fechar_app = tkinter.Button(self.sub_frame_dados_esq, text="Fechar", bg="grey90", bd=6,
                                               width=18, command=self.fechar)
        self.botao_fechar_app.pack()

    def vizualizar_objeto(self):
        self.item_selecionado_da_listbox = self.listbox.get(tkinter.ANCHOR)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        if self.item_selecionado_da_listbox == '':
            self.texto_relatorio.insert(1.0, self.mensagem_de_erro)
        else:
            dados_do_objeto = self.dicionario_de_objetos_para_editar[self.item_selecionado_da_listbox].mostrar_dados()
            self.texto_relatorio.insert(1.0, dados_do_objeto)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def editar_variavel(self, tipo_de_lista, variavel_editada):

        if self.item_selecionado_da_listbox == '':
            self._executar_mensagem_de_erro()
        else:
            objeto = self.objeto_selecionado_para_edicao

            window = tkinter.Toplevel()
            window.title(f'Editar {variavel_editada}')
            window.resizable(False, False)
            window.geometry("300x200+300+200")

            label = tkinter.Label(window, text=f'Editar {variavel_editada}', pady=30)
            label.pack()

            self.string_nova_para_edicao = tkinter.Entry(window)
            self.string_nova_para_edicao.pack()

            botao_de_execucao = tkinter.Button(window, text="OK")
            botao_de_execucao.config(
                command=lambda: self._executar_edicao_do_conteudo(window, objeto, tipo_de_lista, variavel_editada))
            botao_de_execucao.pack()

    def _executar_edicao_do_conteudo(self, window, objeto, tipo_de_lista, variavel_editada):
        novo_conteudo = self.string_nova_para_edicao.get()
        editar_arquivo_em_opcoes_avancadas(objeto, tipo_de_lista, variavel_editada, novo_conteudo)
        self.window.quit()
        window.destroy()

    def _executar_mensagem_de_erro(self):
        self.mensagem_de_erro = "  ERRor  \n\nSelecione uma opcao na lista..."

        self.texto_relatorio.config(state=tkinter.NORMAL)
        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, self.mensagem_de_erro)
        self.texto_relatorio.config(state=tkinter.DISABLED)

    def fechar(self):
        self.window.quit()
        self.window.destroy()
