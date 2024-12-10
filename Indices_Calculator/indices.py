import rasterio
import numpy as np

def calculate_index(band1_path, band2_path, index_type, output_path=None):
    """
    Calculates an index (NDVI, NDWI, NDBI) based on two bands.

    Args:
        band1_path (str): Path to the first band.
        band2_path (str): Path to the second band.
        index_type (str): Type of index ("NDVI", "NDWI", "NDBI").
        output_path (str): Optional path to save the output file.

    Returns:
        np.array: The calculated index array.
    """
    with rasterio.open(band1_path) as band1, rasterio.open(band2_path) as band2:
        band1_data = band1.read(1).astype(float)
        band2_data = band2.read(1).astype(float)

        np.seterr(divide="ignore", invalid="ignore")  # Ignore divide by zero warnings

        if index_type == "NDVI":
            index = (band2_data - band1_data) / (band2_data + band1_data)
        elif index_type == "NDWI":
            index = (band1_data - band2_data) / (band1_data + band2_data)
        elif index_type == "NDBI":
            index = (band1_data - band2_data) / (band1_data + band2_data)
        else:
            raise ValueError("Invalid index type. Choose 'NDVI', 'NDWI', or 'NDBI'.")

        if output_path:
            profile = band1.profile
            profile.update(dtype=rasterio.float32, count=1)
            with rasterio.open(output_path, "w", **profile) as dst:
                dst.write(index.astype(rasterio.float32), 1)

        return index