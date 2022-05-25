from abc import ABC, abstractmethod

class IFowardModel(ABC):

    @abstractmethod
    def forward(self, model):
        pass