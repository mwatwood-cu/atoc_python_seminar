import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

# Here we will build some functions separately then come together to use them

# An example


def example():
    first_value = 12
    second_value = 15

    some_sum = first_value+second_value
    some_difference = second_value-first_value

    some_division = second_value/first_value

    print("done")
    return



### Data Manipulation Function
# Group one will work here
def create_monthly_means(time_series_data):
    # time_series data should be an xarray coming in
    time_series_data = time_series_data['cldarea_total_daynight_mon']
    # Start by understanding the data
    num_years = int(round(len(time_series_data.time)/12))
    print(time_series_data)

    # Make a space holder for the data itself
    monthly_data = np.empty((num_years, 12))
    year_count = 0

    
    # TODO
    # loop through the time series data and put the correct data in the correct location
    for index in range(len(time_series_data.time)) :
        # 1. For simplicity first figure out which month this piece of data comes from and save it as an integer
        month = int(time_series_data[index].time.dt.month)
        # 2. Use the month and the year count to save the data into the monthly_data array
        monthly_data[year_count,month-1] = time_series_data[index]
        # 3. Update the year count.
        if(month==12):
            year_count=year_count+1
            

    # 
    column_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # TODO
    # 4. Use the monthly data and column names to build a Pandas DataFrame
    pandas_format_dataframe = pd.DataFrame(monthly_data,columns=column_names)

    # Return out a pandas DataFrame
    return pandas_format_dataframe

  
### Next Section
# Group 2 will work here
def plot_means_surrounded_by_deviation(monthly_sorted_data_frame, y_var):
    # y_var should be a sting
    # monthly_sorted_data_frame should be a pandas DataFrame with each column being a month and each row a year

    # Use this as the x-axis data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # TODO
    # 1. Calculate and save the mean values of each column

    mean = monthly_sorted_data_frame.mean()

    # 2. Calculate and save the std deviation of each column

    std = monthly_sorted_data_frame.std()

    # 3. Use matplotlib to plot the mean value against the months

    # plt.plot(months, mean)

    # 4. Use the matplotlib function fill_between to show a shape around the running mean

    plt.figure()
    plt.fill_between(months, mean-std, mean+std)
    plt.plot(months, mean, 'r')
    plt.show()
    plt.ylabel(y_var)

    # This function returns nothing but should plot the data
    return
