#aqui vao mostrar o stock atual e o stock recomendado dpcente
from app.gui.produtos.produtos_views import ProdutosView
from matplotlib.figure import Figure

fig = Figure(
    figsize=(6,4)
)

ax = fig.add_subplot(111)

categorias = [
    "Atual",
    "Recomendado"
]

valores = [
    50,
    120
]

ax.bar(
    categorias,
    valores,
    color=[
        "blue",
        "green"
    ]
)

ax.set_title(
    "Recomendação de Stock"
)