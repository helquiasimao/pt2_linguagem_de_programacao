class GestorAlertas:

    def __init__(self):

        self.observers = []

    def adicionar(self, observer):

        self.observers.append(observer)

    def notificar(self, mensagem):

        for observer in self.observers:
            observer.atualizar(mensagem)