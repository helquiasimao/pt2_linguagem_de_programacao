import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app.dao.produto_dao import ProdutoDAO


class RelatoriosView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        dao = ProdutoDAO()

        produtos = dao.listar()

        nomes = [
            p.nome
            for p in produtos[:10]
        ]

        stock = [
            p.stock_atual
            for p in produtos[:10]
        ]

        fig = Figure(
            figsize=(8,4),
            dpi=100
        )

        ax = fig.add_subplot(111)

        ax.bar(
            nomes,
            stock
        )

        ax.set_title(
            "Stock por Produto"
        )

        canvas = FigureCanvasTkAgg(
            fig,
            self
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )