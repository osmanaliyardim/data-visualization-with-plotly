# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:57:35 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Line Plot
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

# Citation and Teaching vs World Rank of Top 100 Universities
df = timesData.iloc[:100,:]

# Citation (Trace1)
trace1 = go.Scatter(x=df.world_rank,
                    y=df.citations,
                    mode="lines",
                    name="citations",
                    marker=dict(color='rgba(16,112,2,0.8)'), 
                    text=df.university_name)

# Teaching (Trace2)
trace2 = go.Scatter(x=df.world_rank,
                    y=df.teaching,
                    mode="lines+markers",
                    name="teaching",
                    marker=dict(color='rgba(80,26,80,0.8)'), 
                    text=df.university_name)

data = [trace1, trace2] # Combine data

layout = dict(title='Citation and Teaching vs WR of Top 100 Univs',
              xaxis=dict(title='World Rank', ticklen=5, zeroline=False)
              )

fig = dict(data=data, layout=layout)
plot(fig)