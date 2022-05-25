from abc import ABC, abstractmethod

class IModelGenerator(ABC):
    
    @abstractmethod
    def build(self):
        pass