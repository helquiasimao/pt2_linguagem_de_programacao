from app.exceptions.stock_error import (
    StockInsuficienteError
)

def validar_stock(func):

    def wrapper(
        self,
        produto,
        quantidade
    ):

        if produto.quantidade_stock < quantidade:

            raise StockInsuficienteError(
                "Stock insuficiente"
            )

        return func(
            self,
            produto,
            quantidade
        )

    return wrapper