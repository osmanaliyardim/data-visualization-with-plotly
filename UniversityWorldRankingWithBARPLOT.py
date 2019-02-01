# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:49:41 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Bar Plot
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

# Citation and Teaching of Top 3 Universities in 2014
# Prepare Data Frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]

# Creating trace1
trace1 = go.Bar(x=df2014.university_name, 
                y=df2014.citations, 
                name="citation",
                marker=dict(color='rgba(255,174,255,0.5)', 
                line=dict(color='rgb(0,0,0)', width=1.5)),
                text = df2014.country)

# Creating trace2
trace2 = go.Bar(x=df2014.university_name, 
                y=df2014.teaching, 
                name="teaching",
                marker=dict(color='rgba(255,255,128,0.5)', 
                line=dict(color='rgb(0,0,0)', width=1.5)),
                text = df2014.country)

data = [trace1,trace2]
layout = go.Layout(barmode="group")
fig = go.Figure(data=data, layout=layout)
plot(fig)

# Example 2 -------------------------------------------------
# Citation and Teaching of Top 3 Universities in 2014 - 2
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
x = df2014.university_name

trace3 = {'x':x, 'y':df2014.citations,'name':'citation','type':'bar'}
trace4 = {'x':x, 'y':df2014.teaching,'name':'teaching','type':'bar'}

data2 = [trace3,trace4]

layout2 = {
        'xaxis': {'title':'Top 3 Universities'},
        'barmode': 'relative',
        'title': 'Citation and Teaching of Top 3 Universities in 2014'
        }

fig2 = go.Figure(data=data2, layout=layout2)
plot(fig2)