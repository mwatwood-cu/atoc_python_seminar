import xarray as xr
import pandas as pd
#import matplotlib.pyplot as plt

from Plotting_tools import example
from Plotting_tools import create_monthly_means
from Plotting_tools import plot_means_surrounded_by_deviation

# Use this file for testing!

# First an example to show debugging and running
#print("Starting the code")
#example()
#print("Finishing the code")


# Group one testing
file_name = "./Data/CERES20YearAvgGlobalCloudCover.nc"
global_cloud_time_series = xr.open_dataset(file_name)

glob_dataFrame = create_monthly_means(global_cloud_time_series, 'cldarea_total_daynight_mon')

# Group two testing
#file_name_2 = "Data/monthlyTestData.nc"
#fill_in_data = xr.open_dataset(file_name_2)
#data = fill_in_data.to_dataframe()
plot_means_surrounded_by_deviation(glob_dataFrame, 'Global Cloud Cover')

