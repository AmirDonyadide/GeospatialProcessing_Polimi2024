import numpy as np

class BaseIndexCalculator:
    """
    Base class for geospatial index calculations.
    """
    @staticmethod
    def calculate_index(band1: np.ndarray, band2: np.ndarray, formula: callable) -> np.ndarray:
        """
        Generic method to calculate an index using a custom formula.
        """
        return formula(band1, band2)

class NDVI(BaseIndexCalculator):
    """
    Normalized Difference Vegetation Index calculator.
    """
    @staticmethod
    def calculate(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
        """
        Calculate NDVI using NIR and Red bands.
        NDVI = (NIR - Red) / (NIR + Red)
        """
        return BaseIndexCalculator.calculate_index(nir, red, lambda nir, red: (nir - red) / (nir + red + 1e-10))

class NDWI(BaseIndexCalculator):
    """
    Normalized Difference Water Index calculator.
    """
    @staticmethod
    def calculate(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
        """
        Calculate NDWI using Green and NIR bands.
        NDWI = (Green - NIR) / (Green + NIR)
        """
        return BaseIndexCalculator.calculate_index(green, nir, lambda green, nir: (green - nir) / (green + nir + 1e-10))