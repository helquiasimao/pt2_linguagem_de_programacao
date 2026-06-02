from tkinter import messagebox
from app.services.auth_service import AuthService


class LoginController:

    def __init__(self, view):
        self.view = view
        self.auth_service = AuthService()

    def login(self, username, password):

        if self.auth_service.autenticar(
            username,
            password
        ):

            from app.gui.dashboard.dashboard_view import DashboardView

            self.view.destroy()

            dashboard = DashboardView()

            dashboard.mainloop()

        else:

            messagebox.showerror(
                "Erro",
                "Credenciais inválidas"
            )