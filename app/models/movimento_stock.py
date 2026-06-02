from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.db import Base


class MovimentoStock(Base):

    __tablename__ = "movimentos_stock"

    id = Column(Integer, primary_key=True)

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id")
    )

    tipo_movimento = Column(
        String(20)
    )

    quantidade = Column(
        Integer,
        nullable=False
    )

    data_movimento = Column(
        DateTime,
        default=datetime.now
    )

    produto = relationship(
        "Produto",
        back_populates="movimentos"
    )

    """Caro docente esses são os tipos de movimentos que temos
    ENTRADA
    SAIDA
    AJUSTE

Estes dados serão usados pela IA para previsão de demanda.

"""



