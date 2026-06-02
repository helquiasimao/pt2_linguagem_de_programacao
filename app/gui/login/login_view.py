import customtkinter as ctk

from app.gui.login.login_controller import LoginController


class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Inventário")
        self.geometry("500x350")

        self.controller = LoginController(self)

        ctk.CTkLabel(
            self,
            text="LOGIN",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        self.entry_user = ctk.CTkEntry(
            self,
            placeholder_text="Utilizador"
        )
        self.entry_user.pack(pady=10)

        self.entry_password = ctk.CTkEntry(
            self,
            placeholder_text="Palavra-passe",
            show="*"
        )
        self.entry_password.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Entrar",
            command=self.login
        ).pack(pady=20)

    def login(self):

        username = self.entry_user.get()
        password = self.entry_password.get()

        self.controller.login(
            username,
            password
        )