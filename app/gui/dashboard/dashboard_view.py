import customtkinter as ctk

from app.gui.components.sidebar import Sidebar
from app.gui.produtos.produtos_views import ProdutosView
from app.gui.movimentos.movimentos_view import MovimentosView
from app.gui.previsao.previsao_view import PrevisaoView
from app.gui.relatorio.relatorios_view import RelatoriosView


class DashboardView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Inventário")
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

            frame = ctk.CTkFrame(
                self.content_frame
            )

            ctk.CTkLabel(
                frame,
                text="Dashboard",
                font=("Arial", 28, "bold")
            ).pack(pady=20)

        frame.pack(
            fill="both",
            expand=True
        )