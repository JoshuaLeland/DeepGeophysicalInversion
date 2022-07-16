import unittest
import numpy as np
from mockito import when, mock, unstub
from scipy.interpolate import LinearNDInterpolator
from discretize.utils import mkvc
from dotmap import DotMap
#from src.ForwardModels.Gravity2DForwardGenerator import Gravity2DForwardGenerator
from src.ForwardModels.Geometry.Geometry import Geometry, GeometryFactoryGravity

def build_geometry_object(survey, mesh, model_map, active_index):
    return Geometry(survey, mesh, model_map, active_index)

class TestGeometry(unittest.TestCase):

    def test_geometry_values_persist(self):
        # Geometry object is not type defined, so we will use strings for now.
        some_survey = "some_survey"
        some_mesh = "some_mesh"
        some_map = "some_map"
        some_active_index = "some_active_index"

        #Trigger.
        some_geometry = build_geometry_object(some_survey, some_mesh, some_map, some_active_index)

        # validate.
        self.assertEqual(some_geometry.survery, some_survey)
        self.assertEqual(some_geometry.mesh, some_mesh)
        self.assertEqual(some_geometry.model_map, some_map)
        self.assertEqual(some_geometry.active_index, some_active_index)

class TestGeometryFactory(unittest.TestCase):

    def test_geometry_factory(self):
        # Set up.
        geometry_config = build_geometry_config()
        factory = GeometryFactoryGravity("gz")

        #Trigger.
        geometry = factory.build(geometry_config)



"""
class TestGravityGenerator(unittest.TestCase):

    def test_gravity_constructor_loads(self):
        geometry = build_geometry_object()
        generator = Gravity2DForwardGenerator(geometry)

"""  

def build_geometry_config():
    geometry_config = DotMap()
    hx = [(5,5,-1.3), (5,40), (5,5, 1.3)]
    hy = [(5,5,-1.3), (5,40), (5,5, 1.3)]
    hz = [(5,5,-1.3), (5,15)]

    # Mesh Paramters.
    geometry_config.mesh_hx = hx
    geometry_config.mesh_hy = hy
    geometry_config.mesh_hz = hz

    # Topography
    [topo_x, topo_y] = np.meshgrid(np.linspace(-200, 200, 41), np.linspace(-200, 200, 41))
    topo_z = -15*np.exp(-(topo_x ** 2 + topo_y ** 2) / 80 ** 2)
    x_topo, y_topo, z_topo = mkvc(topo_x), mkvc(topo_y), mkvc(topo_z)
    geometry_config.topography = np.c_[x_topo, y_topo, z_topo]

    # Observations.
    geometry_config.observation.x, geometry_config.observation.y = np.meshgrid(np.linspace(-80.0, 80.0, 17), np.linspace(-80.0, 80.0, 17))
    geometry_config.observation.x, geometry_config.observation.y = mkvc(geometry_config.observation.x.T), mkvc(geometry_config.observation.y.T)
    fun_interp = LinearNDInterpolator(np.c_[x_topo, y_topo], z_topo)
    geometry_config.observation.z = fun_interp(np.c_[geometry_config.observation.x, geometry_config.observation.y])
    return geometry_config



if __name__ == '__main__':
    unittest.main()