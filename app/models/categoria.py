from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.db import Base


class Categoria(Base):

    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)

    nome = Column(
        String(100),
        nullable=False,
        unique=True
    )

    descricao = Column(String(255))

    produtos = relationship(
        "Produto",
        back_populates="categoria"
    )