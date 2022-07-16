import numpy as np
from SimPEG.potential_fields import gravity
from discretize import TensorMesh
from SimPEG.utils import surface2ind_topo
from SimPEG import maps

"""
Geometry class hold the geometry information for the experiment.
    We need the following:
        survey - A simpeg object holding the survey into.
        mesh - The mesh from a simpeg object.
        model map - simpeg mapping model.
        active index - index of active parameters in the model. Used with topography.
"""
# TODO: Will need to generalize this for more forward model types.
class Geometry:

    def __init__(self, survery, mesh, model_map, active_index) -> None:
        self.survery = survery
        self.mesh = mesh
        self.model_map = model_map
        self.active_index = active_index

class GeometryFactoryGravity:

    def __init__(self, components) -> None:
        self._components = components

    def build(self, geometry_config):
        
        # Build survey.
        survey = self._build_survey(geometry_config.observations)

        # Build mesh.
        mesh = self._build_mesh(geometry_config.mesh_hx, geometry_config.mesh_hy, geometry_config.mesh_hz)

        # build ind active.
        ind_active = self._build_ind_active(mesh, geometry_config.topography)

        # build model map.
        model_map = self._build_model_map(ind_active)

        return Geometry(survey, mesh, model_map, ind_active)

    # Build the survey.s
    def _build_survey(self, observations):
        # Collect locations.
        receiver_locations = np.c_[observations.x, observations.y, observations.z]
        receiver_list = [gravity.receivers.Point(receiver_locations, components=self._components)]

        # Build list.
        source_field = gravity.sources.SourceField(receiver_list=receiver_list)
        return gravity.survey.Survey(source_field)

    def _build_mesh(self, hx, hy, hz):
        return TensorMesh([hx, hy, hz], "CCN")

    def _build_ind_active(self, mesh, topography):
        return surface2ind_topo(mesh, topography)

    def _build_model_map(self, ind_active):
        nC = int(ind_active.sum())
        return maps.IdentityMap(nP=nC)
