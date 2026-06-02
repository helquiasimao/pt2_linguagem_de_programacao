from app.database.db import Base, engine

# IMPORTANTE:
from app.database.models import (
    Categoria,
    Fornecedor,
    Produto,
    Utilizador,
    MovimentoStock
)


def criar_bd():
    Base.metadata.create_all(bind=engine)
    print("Base de dados criada com sucesso.")


if __name__ == "__main__":
    criar_bd()