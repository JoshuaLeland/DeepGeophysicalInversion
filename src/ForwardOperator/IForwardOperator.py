from abc import ABC, abstractclassmethod

class IForwardOperator(ABC):

    @abstractclassmethod
    def forward(self, model):
        pass