# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:56:29 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Box Plot
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

# Top Score vs Researches of Top 100 Universities in 2015
df2015 = timesData[timesData.year == 2015]

trace1 = go.Box(
        y=df2015.total_score,
        name = 'Total Score of Universities in 2015',
        marker = dict(color='rgb(12,12,140)')
        )

trace2 = go.Box(
        y=df2015.research,
        name = 'Research of Universities in 2015',
        marker = dict(color='rgb(12,12,140)')
        )

data = [trace1, trace2]
plot(data)