from sqlalchemy import create_engine

class DatabaseSingleton:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.engine = create_engine(
                "sqlite:///inventario.db"
            )

        return cls._instance