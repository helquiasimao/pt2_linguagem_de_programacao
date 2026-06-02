import customtkinter as ctk

from app.gui.login.login_view import LoginView

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

if __name__ == "__main__":

    app = LoginView()

    app.mainloop()