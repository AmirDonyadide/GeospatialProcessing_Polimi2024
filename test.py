from geospatial_indices.io_utils import RasterIO
from geospatial_indices.calculators import NDVI, NDWI
from geospatial_indices.visualizer import Visualizer

# Load raster
input_filepath = "path/to/your/raster_image.tif"
raster_data, metadata = RasterIO.load_raster(input_filepath)

# Extract bands (assume NIR = band 4, Red = band 3, Green = band 2)
nir_band = raster_data[3]
red_band = raster_data[2]
green_band = raster_data[1]

# Calculate NDVI
ndvi = NDVI.calculate(nir_band, red_band)

# Save NDVI
RasterIO.save_raster("path/to/ndvi_output.tif", ndvi, metadata)

# Visualize NDVI
Visualizer.plot_raster(ndvi, title="NDVI")

# Calculate NDWI
ndwi = NDWI.calculate(green_band, nir_band)

# Save NDWI
RasterIO.save_raster("path/to/ndwi_output.tif", ndwi, metadata)

# Visualize NDWI
Visualizer.plot_raster(ndwi, title="NDWI")