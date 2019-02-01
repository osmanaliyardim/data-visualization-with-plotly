# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:13:03 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Pie Chart
"""

import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

# Read data
timesData = pd.read_csv('timesData.csv')

# Discover data
print(timesData.head())
timesData.info()

# Student Rate of Top 7 Universities in 2016
# Data Preperation
df2016 = timesData[timesData.year == 2016].iloc[:7,:]
df2016.info()

pie1 = df2016.num_students
pie1_list = [float(each.replace(',','.')) for each in df2016.num_students]
labels = df2016.university_name

fig = {"data":[{"values":pie1_list, "labels":labels, "domain":{"x":[0,.5]},
                "name":"Number of Student Rates", "hoverinfo":"label+percent+name",
                "hole":.3, "type":"pie"
               },],
       "layout":{"title":"Student Rate of Top 7 Universities in 2016",
                 "annotations":[{"font":{"size":20}, "showarrow":False, "text":"Number of Students",
                                 "x":0.20, "y":1},]
               } 
      }

plot(fig)