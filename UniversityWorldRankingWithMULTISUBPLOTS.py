# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:24:21 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Multiple Subplots
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

# Research Score vs Citations vs Income vs Total Score of Universities in 2015
df2015 = timesData[timesData.year == 2015]

trace1 = go.Scatter(x=df2015.world_rank, y=df2015.research, name='research')

trace2 = go.Scatter(x=df2015.world_rank, y=df2015.citations, 
                    xaxis='x2', yaxis='y2', name='citations')

trace3 = go.Scatter(x=df2015.world_rank, y=df2015.income, 
                    xaxis='x3', yaxis='y3', name='income')

trace4 = go.Scatter(x=df2015.world_rank, y=df2015.total_score, 
                    xaxis='x4', yaxis='y4', name='total_score')

data = [trace1, trace2, trace3, trace4]
layout = go.Layout(xaxis=dict(domain=[0,0.45]), yaxis=dict(domain=[0,0.45]),
                   xaxis2=dict(domain=[0.55,1]), yaxis2=dict(domain=[0,0.45], anchor='x2'),
                   xaxis3=dict(domain=[0,0.45], anchor='y3'), yaxis3=dict(domain=[0.55,1]),
                   xaxis4=dict(domain=[0.55,1], anchor='y4'), yaxis4=dict(domain=[0.55,1], anchor='x4'),
                   title = 'Research Score vs Citations vs Income vs Total Score of Universities in 2015')

fig = go.Figure(data=data, layout=layout)
plot(fig)                                   