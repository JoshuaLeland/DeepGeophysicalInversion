import unittest
from ..src.ForwardOperator.VSPForwardOperator import VSPForwardOperator
from ..src.Geometry.VSPGeometry import VSPGeometry


class TestVSPOperator(unittest.TestCase):

    def test_constructor_values_persist(self):
        # Set up.
        some_height_step = 5
        some_num_steps = 100
        some_geometry = VSPGeometry(some_height_step, some_num_steps)

        # Trigger.
        vsp_operator = VSPForwardOperator(some_geometry)

        # Validate.
        self.assertEqual(some_height_step, vsp_operator._geometry.height_step)
        self.assertEqual(some_num_steps, vsp_operator._geometry.number_steps)

if __name__ == '__main__':
    unittest.main()