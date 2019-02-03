# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:20:47 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Histogram
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

# Student-Staff Ratio in 2011 and 2012
df2011 = timesData.student_staff_ratio[timesData.year == 2011]
df2012 = timesData.student_staff_ratio[timesData.year == 2012]

trace1 = go.Histogram(x=df2011,opacity=0.75,name="2011",marker=dict(color='rgba(171,50,96,0.6)'))
trace2 = go.Histogram(x=df2012,opacity=0.75,name="2012",marker=dict(color='rgba(12,50,196,0.6)'))   

data = [trace1, trace2]
layout = go.Layout(barmode='overlay', title='Student-Staff Ratio in 2011 and 2012',
                   xaxis=dict(title='Student-Staff Ratio'), yaxis=dict(title='Count'))

fig = go.Figure(data=data, layout=layout)
plot(fig)