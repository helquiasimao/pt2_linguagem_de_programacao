import joblib
import numpy as np

class PrevisaoDemandaService:

    def __init__(self):

        self.modelo = joblib.load(
            "app/ia/modelo_demanda.pkl"
        )

    def prever(
        self,
        produto_id,
        semanas
    ):

        previsao = self.modelo.predict(
            np.array([[semanas]])
        )

        return round(
            float(previsao[0]),
            2
        )