import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app.dao.produto_dao import ProdutoDAO


class PrevisaoView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Previsão IA",
            font=("Arial",24,"bold")
        )

        titulo.pack(pady=20)

        dao = ProdutoDAO()

        produtos = dao.listar()

        nomes = [
            p.nome
            for p in produtos[:10]
        ]

        atual = [
            p.stock_atual
            for p in produtos[:10]
        ]

        previsto = [
            int(p.stock_atual * 1.2)
            for p in produtos[:10]
        ]

        fig = Figure(
            figsize=(8,4),
            dpi=100
        )

        ax = fig.add_subplot(111)

        ax.plot(
            nomes,
            atual,
            label="Atual"
        )

        ax.plot(
            nomes,
            previsto,
            label="Previsto"
        )

        ax.legend()

        canvas = FigureCanvasTkAgg(
            fig,
            self
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )