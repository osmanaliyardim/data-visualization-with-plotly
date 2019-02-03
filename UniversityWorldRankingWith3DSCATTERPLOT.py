# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:14:06 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: 3D Scatter Plot
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

# World Rank vs Research Score vs Citations of Universities in 2015
df2015 = timesData[timesData.year == 2015]

trace1 = go.Scatter3d(x=df2015.world_rank, y=df2015.research, z=df2015.citations,
                      mode='markers', marker=dict(size=10, color='rgb(255,0,0)'))

data = [trace1]
layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))

fig = go.Figure(data=data, layout=layout)
plot(fig)