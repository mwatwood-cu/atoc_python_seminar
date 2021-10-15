import xarray as xr
import pandas as pd
#import matplotlib.pyplot as plt

#from Plotting_tools import example
from Plotting_tools import create_monthly_means
#from Plotting_tools import plot_means_surrounded_by_deviation

# Use this file for testing!

# First an example to show debugging and running
print("Starting the code")
#example()
print("Finishing the code")



# Group one testing
file_name = "./Data/CERES20YearAvgGlobalCloudCover.nc"
global_cloud_time_series = xr.open_dataset(file_name)

dataFrame = create_monthly_means(global_cloud_time_series)


'''
# Group two testing 
file_name_2 = "../Data/monthlyTestData.nc"
fill_in_data = xr.open_dataset(file_name_2 )
plot_means_surrounded_by_deviation(fill_in_data)
'''