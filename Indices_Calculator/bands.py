import os
import rasterio

def identify_bands(folder_path):
    """
    Identifies bands from the folder containing .tif files using metadata.

    Args:
        folder_path (str): Path to the folder containing .tif files.

    Returns:
        dict: A dictionary mapping bands to their file paths.
    """
    band_mapping = {}
    for file in os.listdir(folder_path):
        if file.endswith(".tif"):
            file_path = os.path.join(folder_path, file)
            try:
                with rasterio.open(file_path) as src:
                    metadata = src.tags()
                    # Identify bands based on metadata tags
                    if "BAND_NAME" in metadata:
                        band_name = metadata["BAND_NAME"]
                        if "Red" in band_name:
                            band_mapping["Red"] = file_path
                        elif "Green" in band_name:
                            band_mapping["Green"] = file_path
                        elif "Blue" in band_name:
                            band_mapping["Blue"] = file_path
                        elif "NIR" in band_name:
                            band_mapping["NIR"] = file_path
                        elif "SWIR" in band_name:
                            band_mapping["SWIR"] = file_path
            except Exception as e:
                print(f"Error reading metadata for {file}: {e}")
    return band_mapping