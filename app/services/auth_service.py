class AuthService:

    def autenticar(self, username, password):

        return (
            username == "admin"
            and password == "1234"
        )