import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
import sys
import glob

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into pandas dataframe and transpose

if sys.argv[1] == '-a' :
    file_list = glob.glob("*gdp*.csv")
else:
    file_list = sys.argv[1:]
for filename in file_list:
     data = pandas.read_csv(filename, index_col = 'country').T

     # create a plot the transposed data

     ax = data.plot (title=filename)

     # axes labels
     ax.set_xlabel('year')
     ax.set_ylabel('GDP Per Capita')

     #set axes ticks
     ax.set_xticks(range(len(data.index)))
     ax.set_xticklabels(data.index, rotation=45)


     # display the plot
     plt.show()
