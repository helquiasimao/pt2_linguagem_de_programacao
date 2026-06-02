import customtkinter as ctk

from app.database.db import SessionLocal
from app.database.models import MovimentoStock


class MovimentosView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Movimentos de Stock",
            font=("Arial",24,"bold")
        )

        titulo.pack(pady=20)

        self.lista = ctk.CTkTextbox(
            self,
            width=1000,
            height=500
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.carregar()

    def carregar(self):

        db = SessionLocal()

        movimentos = db.query(
            MovimentoStock
        ).all()

        self.lista.delete(
            "1.0",
            "end"
        )

        for m in movimentos:

            self.lista.insert(
                "end",
                f"{m.id} | Produto {m.produto_id} | {m.tipo} | {m.quantidade}\n"
            )

        db.close()