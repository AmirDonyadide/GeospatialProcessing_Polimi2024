import unittest
import os
from Indices_Calculator.bands import identify_bands

class TestBands(unittest.TestCase):
    def test_identify_bands(self):
        # Simulate a folder with mock file names
        folder = "mock_folder"
        os.makedirs(folder, exist_ok=True)
        open(os.path.join(folder, "image_B4.tif"), "w").close()
        open(os.path.join(folder, "image_B8.tif"), "w").close()

        bands = identify_bands(folder)
        self.assertIsInstance(bands, dict)

        # Clean up
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
        os.rmdir(folder)

if __name__ == "__main__":
    unittest.main()