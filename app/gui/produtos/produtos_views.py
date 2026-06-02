import customtkinter as ctk

from app.dao.produto_dao import ProdutoDAO
from app.gui.produtos.produto_form import ProdutoForm


class ProdutosView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.dao = ProdutoDAO()

        titulo = ctk.CTkLabel(
            self,
            text="Gestão de Produtos",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=10)

        botoes_frame = ctk.CTkFrame(self)

        botoes_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkButton(
            botoes_frame,
            text="Atualizar Lista",
            command=self.carregar_produtos
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botoes_frame,
            text="Novo Produto",
            command=self.abrir_formulario
        ).pack(
            side="left",
            padx=5
        )

        self.id_eliminar = ctk.CTkEntry(
            botoes_frame,
            width=120,
            placeholder_text="ID"
        )

        self.id_eliminar.pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botoes_frame,
            text="Eliminar",
            command=self.eliminar_produto
        ).pack(
            side="left",
            padx=5
        )

        self.lista = ctk.CTkTextbox(
            self,
            width=1000,
            height=550
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.carregar_produtos()

    def abrir_formulario(self):

        ProdutoForm(
            self,
            callback=self.carregar_produtos
        )

    def carregar_produtos(self):

        self.lista.delete(
            "1.0",
            "end"
        )

        produtos = self.dao.listar()

        cabecalho = (
            f"{'ID':<5}"
            f"{'PRODUTO':<30}"
            f"{'PREÇO (Kz)':<20}"
            f"{'STOCK':<10}\n"
        )

        self.lista.insert(
            "end",
            cabecalho
        )

        self.lista.insert(
            "end",
            "-" * 80 + "\n"
        )

        for produto in produtos:

            preco = (
                f"{produto.preco:,.2f} Kz"
            )

            linha = (
                f"{produto.id:<5}"
                f"{produto.nome:<30}"
                f"{preco:<20}"
                f"{produto.stock_atual:<10}\n"
            )

            self.lista.insert(
                "end",
                linha
            )

    def eliminar_produto(self):

        try:

            produto_id = int(
                self.id_eliminar.get()
            )

            self.dao.eliminar(
                produto_id
            )

            self.carregar_produtos()

        except Exception as erro:

            print(
                "Erro:",
                erro
            )