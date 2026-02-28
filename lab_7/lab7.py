import os
import arcpy
from arcpy.sa import Raster
from numpy import source

# --- Settings ---
arcpy.env.overwriteOutput = True

base_dir = r"C:\Users\73934\Desktop\Course Assignment\zhang-online-GEOG676-spring2026\lab_7"
landsat_dir = os.path.join(base_dir, "landsat4")
dem_dir = os.path.join(base_dir, "dem")

# --- Check out extensions ---
try:
    arcpy.CheckOutExtension("Spatial")
except:
    pass

try:
    arcpy.CheckOutExtension("3D")
except:
    pass
# =============================
#  Composite Landsat Bands
# =============================

# Load the individual bands as Raster objects
blue  = Raster(os.path.join(landsat_dir, "blue.tif"))
green = Raster(os.path.join(landsat_dir, "green.tif"))
red   = Raster(os.path.join(landsat_dir, "red.tif"))
nir   = Raster(os.path.join(landsat_dir, "nir08.tif"))

composite_out = os.path.join(base_dir, "output_composite.tif")

arcpy.management.CompositeBands([blue, green, red, nir], composite_out)

# =============================
#  Hillshade
# =============================

dem_path = os.path.join(dem_dir, "dem_30m.tif") 

hillshade_out = os.path.join(base_dir, "output_hillshade.tif")

from arcpy.sa import Hillshade
hs = Hillshade(dem_path, 315, 45)
hs.save(hillshade_out)

# =============================
#  Slope
# =============================

slope_out = os.path.join(base_dir, "output_slope.tif")

from arcpy.sa import Slope
slp = Slope(dem_path, "DEGREE")
slp.save(slope_out)

print("All rasters created successfully!")