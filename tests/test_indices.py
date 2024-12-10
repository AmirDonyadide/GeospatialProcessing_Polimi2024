import unittest
import numpy as np
from Indices_Calculator.indices import calculate_index

class TestIndices(unittest.TestCase):
    def test_calculate_index(self):
        # Create mock raster data
        band1 = np.array([[1, 2], [3, 4]])
        band2 = np.array([[5, 6], [7, 8]])
        ndvi = (band2 - band1) / (band2 + band1)

        # Mock paths and function call
        with self.assertRaises(ValueError):
            calculate_index("band1.tif", "band2.tif", "INVALID")

if __name__ == "__main__":
    unittest.main()