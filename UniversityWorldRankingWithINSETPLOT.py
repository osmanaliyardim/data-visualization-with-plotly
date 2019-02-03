# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:02:30 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Inset Plot
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

# Teaching Score vs Income of Universities in 2015
df2015 = timesData[timesData.year == 2015]

trace1 = go.Scatter(x=df2015.world_rank, y=df2015.teaching, name='teaching',
                    marker=dict(color='rgba(16,112,2,0.8)'))

trace2 = go.Scatter(x=df2015.world_rank, y=df2015.income, xaxis='x2', yaxis='y2',
                    name='income', marker=dict(color='rgba(160,112,20,0.8)'))

data = [trace1, trace2]
layout = go.Layout(xaxis2=dict(domain=[0.6,0.95], anchor='y2'),
                   yaxis2=dict(domain=[0.6,0.95], anchor='x2'),
                   title='Teaching Score vs Income of Universities in 2015')

fig = go.Figure(data=data, layout=layout)
plot(fig)