from Indices_Calculator import identify_bands, calculate_index

# Identify bands in a folder
bands = identify_bands("path/to/tif/files")

# Calculate NDVI
calculate_index(bands["Red"], bands["NIR"], "NDVI", output_path="NDVI.tif")