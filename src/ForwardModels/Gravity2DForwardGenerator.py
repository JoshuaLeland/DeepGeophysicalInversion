import IForwardModel
from SimPEG.potential_fields import gravity
import torch


# Take in survey information and compute forward data.
class Gravity2DForwardGenerator(IForwardModel):

    def __init__(self, geometry, simulation: gravity.simulation.Simulation3DIntegral) -> None:
        self._gravity_simulation = simulation(survey=geometry.survey, 
            mesh=geometry.mesh, rhoMap=geometry.model_map, actInd=geometry.ind_active, 
            store_sensitivities="forward_only")
        self._geometry = geometry
        self._forward_matrix = torch.from_numpy(self._gravity_simulation.G())

    def forward(self, model):
        pass