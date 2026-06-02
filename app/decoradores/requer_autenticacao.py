from app.exceptions.auth_error import (
    AutenticacaoInvalidaError
)

def requer_autenticacao(func):

    def wrapper(
        self,
        *args,
        **kwargs
    ):

        if not self.utilizador_logado:

            raise AutenticacaoInvalidaError(
                "Login obrigatório"
            )

        return func(
            self,
            *args,
            **kwargs
        )

    return wrapper