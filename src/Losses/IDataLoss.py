from abc import ABC, abstractmethod

class IDataLoss(ABC):
    
    @abstractmethod
    def calculate(self, field_data, predictied_data):
        pass