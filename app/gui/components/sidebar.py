import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, callback):
        super().__init__(master, width=200)

        self.callback = callback

        self.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self,
            text="Inventário IA",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        menus = [
            "Dashboard",
            "Produtos",
            "Movimentos",
            "Previsoes",
            "Relatorios"
        ]

        for menu in menus:

            btn = ctk.CTkButton(
                self,
                text=menu,
                command=lambda m=menu: self.callback(m)
            )

            btn.pack(
                fill="x",
                padx=10,
                pady=5
            )