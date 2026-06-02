from sklearn.linear_model import LinearRegression
import numpy as np

class PrevisaoDemanda:

    def prever(self):

        x = np.array(
            [1,2,3,4,5]
        ).reshape(-1,1)

        y = np.array(
            [10,15,18,22,30]
        )

        modelo = LinearRegression()

        modelo.fit(x,y)

        return modelo.predict([[6]])