from abc import ABC, abstractmethod

class IRegLoss(ABC):
    
    @abstractmethod
    def calculate(self, model):
        pass