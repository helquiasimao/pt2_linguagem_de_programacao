from app.database.db import SessionLocal
from app.database.models import Produto


class ProdutoDAO:

    def listar(self):

        db = SessionLocal()

        try:
            return db.query(
                Produto
            ).all()

        finally:
            db.close()

    def obter_por_id(self, produto_id):

        db = SessionLocal()

        try:

            return db.query(
                Produto
            ).filter(
                Produto.id == produto_id
            ).first()

        finally:
            db.close()

    def criar(
        self,
        nome,
        descricao,
        preco,
        stock_atual,
        stock_minimo
    ):

        db = SessionLocal()

        try:

            produto = Produto(
                nome=nome,
                descricao=descricao,
                preco=preco,
                stock_atual=stock_atual,
                stock_minimo=stock_minimo
            )

            db.add(produto)

            db.commit()

            return produto

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def eliminar(self, produto_id):

        db = SessionLocal()

        try:

            produto = db.query(
                Produto
            ).filter(
                Produto.id == produto_id
            ).first()

            if produto:

                db.delete(produto)

                db.commit()

        finally:

            db.close()

    # ==========================
    # KPIs DASHBOARD
    # ==========================

    def total_produtos(self):

        db = SessionLocal()

        try:

            return db.query(
                Produto
            ).count()

        finally:

            db.close()

    def valor_total_stock(self):

        db = SessionLocal()

        try:

            produtos = db.query(
                Produto
            ).all()

            total = sum(
                p.preco * p.stock_atual
                for p in produtos
            )

            return total

        finally:

            db.close()

    def produtos_stock_baixo(self):

        db = SessionLocal()

        try:

            produtos = db.query(
                Produto
            ).all()

            alertas = sum(
                1
                for p in produtos
                if p.stock_atual <= p.stock_minimo
            )

            return alertas

        finally:

            db.close()