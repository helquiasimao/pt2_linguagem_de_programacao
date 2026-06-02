from app.decoradores.validar_stock import (
    validar_stock
)

class StockService:

    @validar_stock
    def saida_stock(
        self,
        produto,
        quantidade
    ):

        produto.quantidade_stock -= quantidade