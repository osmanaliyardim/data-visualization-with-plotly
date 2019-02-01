# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:54:09 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Scatter Chart
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

# Citation vs World Rank of Top 100 Universities in 2014, 2015 and 2016
df2014 = timesData[timesData.year == 2014].iloc[:100,:]
df2015 = timesData[timesData.year == 2015].iloc[:100,:]
df2016 = timesData[timesData.year == 2016].iloc[:100,:]

# 2014 (Trace 1)
trace1 = go.Scatter(x = df2014.world_rank,
                    y = df2014.citations,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255,128,255,0.8)'),
                    text = df2014.university_name)

# 2015 (Trace 2)
trace2 = go.Scatter(x = df2015.world_rank,
                    y = df2015.citations,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255,128,2,0.8)'),
                    text = df2015.university_name)

# 2016 (Trace 3)
trace3 = go.Scatter(x = df2016.world_rank,
                    y = df2016.citations,
                    mode = "markers",
                    name = "2016",
                    marker = dict(color = 'rgba(0,255,200,0.8)'),
                    text = df2016.university_name)

data = [trace1, trace2, trace3] # Combine traces
layout = dict(title = 'Citation vs World Rank of Top 10 Univs in 2014-15-16',
              xaxis = dict(title = 'World Rank', ticklen = 5, zeroline = False),
              yaxis = dict(title = 'Citation', ticklen = 5, zeroline = False))

fig = dict(data=data, layout=layout)
plot(fig)