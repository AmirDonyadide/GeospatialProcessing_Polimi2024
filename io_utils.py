import rasterio
import numpy as np

class RasterIO:
    """
    Handles loading and saving of raster files using Rasterio.
    """
    @staticmethod
    def load_raster(filepath: str):
        """
        Load a raster file as a numpy array and its metadata.
        """
        with rasterio.open(filepath) as src:
            bands = src.read()  # All bands
            metadata = src.meta  # Metadata for saving
        return bands, metadata

    @staticmethod
    def save_raster(filepath: str, array: np.ndarray, metadata: dict):
        """
        Save a numpy array as a raster file.
        """
        metadata.update({
            "dtype": array.dtype,
            "count": 1  # Single-band output
        })
        with rasterio.open(filepath, "w", **metadata) as dst:
            dst.write(array, 1)