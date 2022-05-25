from abc import ABC, abstractmethod

class IParameterGenerator(ABC):
    
    @abstractmethod
    def generate(self):
        pass