# Import of libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Path to the netCDF file
nc_path = "SRTMGL1_NC.003_Data/N21E039.SRTMGL1_NC.nc"

#  Open dataset
dset = xr.open_dataset(nc_path)

#  Breakpoint: inspect dataset + variables
pdb.set_trace()

## The next codes are the ones that were given in the assignment and are written in the bash when execting the file
#  Extract DEM variable
DEM = np.array(dset.variables["SRTMGL1_DEM"])

#  Close file
dset.close()


# Plot + save
plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label("Elevation (m asl)")
plt.savefig("assignment_1.png", dpi=300)
