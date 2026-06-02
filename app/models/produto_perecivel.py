from app.models.produto import Produto

class ProdutoPerecivel(Produto):

    def __init__(
        self,
        nome,
        descricao,
        preco,
        quantidade_stock,
        data_validade
    ):
        super().__init__(
            nome,
            descricao,
            preco,
            quantidade_stock
        )

        self.data_validade = data_validade