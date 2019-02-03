# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:08:28 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Bubble Plot
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
print(timesData.international.head())

# Teaching Score with Number of Students and International Score in 2016
df2016 = timesData[timesData.year == 2016].iloc[:20,:]
num_students_size = [float(each.replace(',','.')) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]

data = [{
        'y': df2016.teaching,
        'x': df2016.world_rank,
        'mode': 'markers',
        'marker': {
                'color': international_color,
                'size': num_students_size,
                'showscale': True
                },
        'text': df2016.university_name
        }]

plot(data)