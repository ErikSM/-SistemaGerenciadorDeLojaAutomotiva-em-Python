from estrutura.AppBase import AppBase


class AppVenda(AppBase):

    def __init__(self, title):
        super().__init__(title)

        #  conteudo ????????

        self.window.mainloop()

obj = AppVenda("Relatorio de Venda")
