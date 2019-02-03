# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:01:58 2019

@author: Osman Ali Yardım

University World Ranking with Plotly: Scatter Plot Matrix
"""

import pandas as pd
import numpy as np

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Read data
timesData = pd.read_csv('timesData.csv')

# Discover data
print(timesData.head())
timesData.info()

# Top Score vs Researches of Top 100 Universities in 2015
df2015 = timesData[timesData.year == 2015]
data2015 = df2015.loc[:,["research","international","total_score"]]
data2015["index"] = np.arange(1, len(data2015)+1)

fig = ff.create_scatterplotmatrix(data2015, diag='box', index='index', colormap='Portland',
                                  colormap_type='cat', height=700, width=700)

plot(fig)