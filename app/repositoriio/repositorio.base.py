from abc import ABC, abstractmethod

class RepositorioBase(ABC):

    @abstractmethod
    def criar(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def eliminar(self, id_obj):
        pass