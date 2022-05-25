from abc import ABC, abstractmethod

class IInverseModel(ABC):

    @abstractmethod
    def invert(self, data):
        pass