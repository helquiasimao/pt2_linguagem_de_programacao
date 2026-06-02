import customtkinter as ctk


class KPICard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        titulo,
        valor
    ):
        super().__init__(
            master,
            width=180,
            height=120
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=titulo,
            font=("Arial", 16)
        ).pack(
            pady=10
        )

        ctk.CTkLabel(
            self,
            text=str(valor),
            font=("Arial", 30, "bold")
        ).pack()