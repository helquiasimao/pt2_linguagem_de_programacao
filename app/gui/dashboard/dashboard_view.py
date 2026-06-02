import customtkinter as ctk
from app.gui.produtos.produto_form import ProdutoForm
from app.gui.components.sidebar import Sidebar
from app.gui.produtos.produtos_views import ProdutosView
from app.gui.movimentos.movimentos_view import MovimentosView
from app.gui.previsao.previsao_view import PrevisaoView
from app.gui.relatorio.relatorios_view import RelatoriosView


class DashboardView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Dashboard Inventário")
        self.geometry("1200x700")

        self.sidebar = Sidebar(
            self,
            self.mostrar_pagina
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content_frame = ctk.CTkFrame(self)

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.mostrar_pagina("Dashboard")

    def limpar_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()
   


    def mostrar_pagina(self, pagina):

        self.limpar_content()

        if pagina == "Produtos":

            frame = ProdutosView(
                self.content_frame
            )

        elif pagina == "Movimentos":

            frame = MovimentosView(
                self.content_frame
            )

        elif pagina == "Previsoes":

            frame = PrevisaoView(
                self.content_frame
            )

        elif pagina == "Relatorios":

            frame = RelatoriosView(
                self.content_frame
            )

        else:

            from app.dao.produto_dao import ProdutoDAO

            dao = ProdutoDAO()

            frame = ctk.CTkFrame(
                self.content_frame
            )

            titulo = ctk.CTkLabel(
                frame,
                text="Dashboard",
                font=("Arial", 28, "bold")
            )

            titulo.pack(pady=20)

            cards = ctk.CTkFrame(frame)
            cards.pack(pady=20)

            total = dao.total_produtos()

            valor = dao.valor_total_stock()

            alertas = dao.produtos_stock_baixo()

            ctk.CTkLabel(
                cards,
                text=f"Produtos\n{total}",
                width=200,
                height=100
            ).grid(row=0,column=0,padx=10)

            ctk.CTkLabel(
                cards,
                text=f"Valor Stock\n{valor:,.2f} Kz",
                width=200,
                height=100
            ).grid(row=0,column=1,padx=10)

            ctk.CTkLabel(
                cards,
                text=f"Alertas\n{alertas}",
                width=200,
                height=100
            ).grid(row=0,column=2,padx=10)
        