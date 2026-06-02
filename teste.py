from app.database.db import SessionLocal

from app.database.models import (
    Produto,
    Categoria,
    Fornecedor,
    MovimentoStock
)

db = SessionLocal()

print(
    "Produtos:",
    db.query(Produto).count()
)

print(
    "Categorias:",
    db.query(Categoria).count()
)

print(
    "Fornecedores:",
    db.query(Fornecedor).count()
)

print(
    "Movimentos:",
    db.query(MovimentoStock).count()
)

db.close()
#depois da istalação, teste para vereficar se está tudo ok caro docente.