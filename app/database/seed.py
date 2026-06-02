#vamos gerar dados automatica mente neste ficheuiro docente

import random
import bcrypt

from app.database.db import SessionLocal

from app.database.models import (
    Categoria,
    Fornecedor,
    Produto,
    Utilizador,
    MovimentoStock
)


db = SessionLocal()


# =========================
# CATEGORIAS
# =========================

categorias_nomes = [
    "Alimentação",
    "Bebidas",
    "Higiene",
    "Limpeza",
    "Escritório",
    "Eletrónica",
    "Vestuário",
    "Farmácia",
    "Construção",
    "Diversos"
]

categorias = []

for nome in categorias_nomes:

    categoria = Categoria(nome=nome)

    db.add(categoria)

    categorias.append(categoria)


# =========================
# FORNECEDORES
# =========================

fornecedores = []

for i in range(1, 21):

    fornecedor = Fornecedor(
        nome=f"Fornecedor {i}",
        telefone=f"923000{i:03}",
        email=f"fornecedor{i}@empresa.com"
    )

    db.add(fornecedor)

    fornecedores.append(fornecedor)


db.commit()


# =========================
# UTILIZADOR ADMIN
# =========================

password = bcrypt.hashpw(
    "1234".encode(),
    bcrypt.gensalt()
).decode()

admin = Utilizador(
    username="admin",
    password_hash=password
)

db.add(admin)

db.commit()


# =========================
# PRODUTOS
# =========================

nomes_produtos = [

    "Arroz",
    "Feijão",
    "Açúcar",
    "Sal",
    "Óleo",
    "Leite",
    "Iogurte",
    "Massa",
    "Água",
    "Coca-Cola",
    "Fanta",
    "Sumo",
    "Sabão",
    "Detergente",
    "Champô",
    "Papel Higiénico",
    "Caneta",
    "Caderno",
    "Marcador",
    "Borracha",

] * 5


produtos = []

for nome in nomes_produtos[:100]:

    produto = Produto(

        nome=nome,

        descricao=f"Produto {nome}",

        preco=random.randint(
            500,
            15000
        ),

        stock_atual=random.randint(
            20,
            500
        ),

        stock_minimo=random.randint(
            5,
            30
        ),

        categoria=random.choice(
            categorias
        ),

        fornecedor=random.choice(
            fornecedores
        )
    )

    db.add(produto)

    produtos.append(produto)

db.commit()


# =========================
# MOVIMENTOS
# =========================

tipos = [
    "ENTRADA",
    "SAIDA",
    "AJUSTE"
]

for _ in range(5000):

    movimento = MovimentoStock(

        produto=random.choice(
            produtos
        ),

        utilizador=admin,

        tipo=random.choice(
            tipos
        ),

        quantidade=random.randint(
            1,
            50
        )
    )

    db.add(movimento)

db.commit()

db.close()

print("Seed executado om sucesso.")