from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.db import Base


# =========================
# CATEGORIA
# =========================

class Categoria(Base):

    __tablename__ = "categorias"

    id = Column(
        Integer,
        primary_key=True
    )

    nome = Column(
        String(100),
        unique=True,
        nullable=False
    )

    produtos = relationship(
        "Produto",
        back_populates="categoria"
    )


# =========================
# FORNECEDOR
# =========================

class Fornecedor(Base):

    __tablename__ = "fornecedores"

    id = Column(
        Integer,
        primary_key=True
    )

    nome = Column(
        String(150),
        nullable=False
    )

    telefone = Column(
        String(30)
    )

    email = Column(
        String(100)
    )

    produtos = relationship(
        "Produto",
        back_populates="fornecedor"
    )


# =========================
# UTILIZADOR
# =========================

class Utilizador(Base):

    __tablename__ = "utilizadores"

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    tentativas_login = Column(
        Integer,
        default=0
    )

    bloqueado = Column(
        Integer,
        default=0
    )

    movimentos = relationship(
        "MovimentoStock",
        back_populates="utilizador"
    )


# =========================
# PRODUTO
# =========================

class Produto(Base):

    __tablename__ = "produtos"

    id = Column(
        Integer,
        primary_key=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    descricao = Column(
        String(255)
    )

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
        ForeignKey("categorias.id")
    )

    fornecedor_id = Column(
        Integer,
        ForeignKey("fornecedores.id")
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

    def __repr__(self):

        return (
            f"<Produto {self.nome}>"
        )


# =========================
# MOVIMENTO STOCK
# =========================

class MovimentoStock(Base):

    __tablename__ = "movimentos_stock"

    id = Column(
        Integer,
        primary_key=True
    )

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id")
    )

    utilizador_id = Column(
        Integer,
        ForeignKey("utilizadores.id")
    )

    tipo = Column(
        String(20)
    )

    quantidade = Column(
        Integer
    )

    data_movimento = Column(
        DateTime,
        default=datetime.utcnow
    )

    produto = relationship(
        "Produto",
        back_populates="movimentos"
    )

    utilizador = relationship(
        "Utilizador",
        back_populates="movimentos"
    )