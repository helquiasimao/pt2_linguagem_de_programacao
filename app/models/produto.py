from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import CheckConstraint

from sqlalchemy.orm import relationship

from app.database.db import Base


class Produto(Base):

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)

    nome = Column(
        String(100),
        nullable=False
    )

    descricao = Column(String(255))

    preco = Column(
        Float,
        nullable=False
    )

    stock_atual = Column(
        Integer,
        default=0
    )

    stock_minimo = Column(
        Integer,
        default=5
    )

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    fornecedor_id = Column(
        Integer,
        ForeignKey("fornecedores.id"),
        nullable=False
    )

    categoria = relationship(
        "Categoria",
        back_populates="produtos"
    )

    fornecedor = relationship(
        "Fornecedor",
        back_populates="produtos"
    )

    movimentos = relationship(
        "MovimentoStock",
        back_populates="produto"
    )

    __table_args__ = (
        CheckConstraint(
            "preco > 0",
            name="ck_preco"
        ),
    )