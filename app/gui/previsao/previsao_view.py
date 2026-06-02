import customtkinter as ctk


class PrevisaoView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Previsão de Demanda",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)