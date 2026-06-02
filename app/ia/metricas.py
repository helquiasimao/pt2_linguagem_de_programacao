import numpy as np

#docente aqui estamos AVALIANDO O MODELO

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.model_selection import (
    cross_val_predict
)

X = np.array([
    [1],[2],[3],[4],
    [5],[6],[7],[8]
])

y = np.array([
    20,25,30,35,
    40,45,50,55
])

modelo = RandomForestRegressor(
    random_state=42
)

previsoes = cross_val_predict(
    modelo,
    X,
    y,
    cv=4
)

mae = mean_absolute_error(
    y,
    previsoes
)

rmse = np.sqrt(
    mean_squared_error(
        y,
        previsoes
    )
)

r2 = r2_score(
    y,
    previsoes
)

print("MAE =", mae)
print("RMSE =", rmse)
print("R2 =", r2)

#guardar informações para o relat+orio

with open(
    "reports/relatorio_metricas.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        f"MAE: {mae}\n"
    )

    f.write(
        f"RMSE: {rmse}\n"
    )

    f.write(
        f"R²: {r2}\n"
    )