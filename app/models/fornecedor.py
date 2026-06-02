from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.db import Base


class Fornecedor(Base):

    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True)

    nome = Column(
        String(100),
        nullable=False
    )

    telefone = Column(String(20))

    email = Column(
        String(100),
        unique=True
    )

    produtos = relationship(
        "Produto",
        back_populates="fornecedor"
    )