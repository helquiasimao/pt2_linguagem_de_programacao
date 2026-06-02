import joblib
import numpy as np

from sklearn.ensemble import RandomForestRegressor

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

y = np.array([
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55
])

modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

modelo.fit(X, y)

joblib.dump(
    modelo,
    "app/ia/modelo_demanda.pkl"
)

print("O modelo treinou.")