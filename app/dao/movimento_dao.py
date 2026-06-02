from app.models.movimento_stock import (
    MovimentoStock
)

class StockService:

    def __init__(
        self,
        produto_dao,
        movimento_dao
    ):

        self.produto_dao = produto_dao
        self.movimento_dao = movimento_dao

    def entrada_stock(
        self,
        produto,
        quantidade
    ):

        produto.quantidade_stock += quantidade

        self.produto_dao.atualizar()

        movimento = MovimentoStock(
            produto_id=produto.id,
            tipo_movimento="ENTRADA",
            quantidade=quantidade
        )

        self.movimento_dao.criar(
            movimento
        )

    def saida_stock(
        self,
        produto,
        quantidade
    ):

        produto.quantidade_stock -= quantidade

        self.produto_dao.atualizar()

        movimento = MovimentoStock(
            produto_id=produto.id,
            tipo_movimento="SAIDA",
            quantidade=quantidade
        )

        self.movimento_dao.criar(
            movimento
        )

#obtendo os movimentos (entrada saida) para o treinamento do modelo docente


def obter_historico_produto(
    self,
    produto_id
):

    return (
        self.session.query(
            MovimentoStock
        )
        .filter(
            MovimentoStock.produto_id
            == produto_id
        )
        .all()
    )