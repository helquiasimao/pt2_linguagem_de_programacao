import customtkinter as ctk
from tkinter import messagebox

from app.dao.produto_dao import ProdutoDAO


class ProdutoForm(ctk.CTkToplevel):

    def __init__(self, master, callback=None):

        super().__init__(master)

        self.dao = ProdutoDAO()
        self.callback = callback

        self.title("Novo Produto")
        self.geometry("500x450")

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Novo Produto",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        # Nome

        ctk.CTkLabel(
            self,
            text="Nome"
        ).pack()

        self.nome_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.nome_entry.pack(pady=5)

        # Descrição

        ctk.CTkLabel(
            self,
            text="Descrição"
        ).pack()

        self.descricao_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.descricao_entry.pack(pady=5)

        # Preço

        ctk.CTkLabel(
            self,
            text="Preço (Kz)"
        ).pack()

        self.preco_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.preco_entry.pack(pady=5)

        # Stock

        ctk.CTkLabel(
            self,
            text="Stock Atual"
        ).pack()

        self.stock_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.stock_entry.pack(pady=5)

        # Stock mínimo

        ctk.CTkLabel(
            self,
            text="Stock Mínimo"
        ).pack()

        self.stock_minimo_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.stock_minimo_entry.insert(
            0,
            "5"
        )

        self.stock_minimo_entry.pack(pady=5)

        ctk.CTkButton(
            self,
            text="Guardar Produto",
            command=self.guardar_produto
        ).pack(pady=20)

    def guardar_produto(self):

        try:

            self.dao.criar(
                nome=self.nome_entry.get(),
                descricao=self.descricao_entry.get(),
                preco=float(self.preco_entry.get()),
                stock_atual=int(self.stock_entry.get()),
                stock_minimo=int(self.stock_minimo_entry.get())
            )

            messagebox.showinfo(
                "Sucesso",
                "Produto criado com sucesso."
            )

            if self.callback:
                self.callback()

            self.destroy()

        except Exception as erro:

            import traceback

            traceback.print_exc()

            messagebox.showerror(
                "Erro",
                str(erro)
            )