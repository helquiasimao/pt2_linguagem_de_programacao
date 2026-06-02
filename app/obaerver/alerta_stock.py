from app.observer.observer import Observer

class AlertaStockObserver(Observer):

    def atualizar(self, mensagem):

        print(
            f"ALERTA: {mensagem}"
        )