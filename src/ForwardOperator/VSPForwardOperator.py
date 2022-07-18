import torch
from .IForwardOperator import IForwardOperator

class VSPForwardOperator(IForwardOperator):

    def __init__(self, geometry) -> None:
        self._geometry = geometry
        self._model = self._build_model(self._geometry)

    def forward(self, model):
        pass

    def _build_model(self, geometry):
        return geometry.height_step * torch.ones(geometry.number_steps)