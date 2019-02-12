# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 08:40:11 2019

@author: Osman Ali Yardım

World War II Bombing Visualization: Map Plot
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

# Read Data
aerial = pd.read_csv('operations.csv')
weather_station = pd.read_csv('Weather Station Locations.csv')
weather = pd.read_csv('Summary of Weather.csv')

# Data Analysis
print(aerial.head())
aerial.info()

# Manipulate Data
aerial = aerial[pd.isna(aerial.Country)==False]
aerial = aerial[pd.isna(aerial['Target Longitude'])==False]
aerial = aerial[pd.isna(aerial['Takeoff Longitude'])==False]

drop_list = ['Mission ID', 'Unit ID', 'Target ID', 'Altitude (Hundreds of Feet)', 
             'Airborne Aircraft', 'Attacking Aircraft', 'Bombing Aircraft', 'Aircraft Returned',
             'Aircraft Failed', 'Aircraft Damaged', 'Aircraft Lost',
             'High Explosives', 'High Explosives Type','Mission Type',
             'High Explosives Weight (Pounds)', 'High Explosives Weight (Tons)',
             'Incendiary Devices', 'Incendiary Devices Type',
             'Incendiary Devices Weight (Pounds)',
             'Incendiary Devices Weight (Tons)', 'Fragmentation Devices',
             'Fragmentation Devices Type', 'Fragmentation Devices Weight (Pounds)',
             'Fragmentation Devices Weight (Tons)', 'Total Weight (Pounds)',
             'Total Weight (Tons)', 'Time Over Target', 'Bomb Damage Assessment','Source ID']

aerial.drop(drop_list, axis=1, inplace=True) # Drop unused features
aerial = aerial[aerial.iloc[:,8]!="4248"]
aerial = aerial[aerial.iloc[:,9]!=1335]

weather_station = weather_station.loc[:,['WBAN', 'NAME', 'STATE/COUNTRY ID', 'Latitude', 'Longtitude']] # Get data what we will only use
weather_station.info()

weather = weather.loc[:,['STA','Date','MeanTemp']] # Get data what we will only use
weather.info()

# Count the countries as their take-off number and visualize-------------------------------------
print(aerial['Country'].value_counts())
plt.figure(figsize=(22,10))
sns.countplot(aerial['Country'])

# Top target countries
print(aerial['Target Country'].value_counts()[:10])
plt.figure(figsize=(22,10))
sns.countplot(aerial['Target Country'])
plt.xticks(rotation=90)

# Visualization of Aircraft Models
data = aerial['Aircraft Series'].value_counts()
print(data[:10])
data = [go.Bar(x=data[:10].index, y=data[:10].values, hoverinfo='text',
               marker = dict(color='rgba(177,14,22,0.5)', 
               line=dict(color='rgb(0,0,0)', width=1.5)))]

layout = dict(title='Aircraft Models')

fig = go.Figure(data=data, layout=layout)
plot(fig)

# Visualization of Take off bases of attacking countries-----------------------------------------
aerial["color"] = ""
aerial.color[aerial.Country == "USA"] = "rgb(0,116,217)"
aerial.color[aerial.Country == "GREAT BRITAIN"] = "rgb(255,65,54)"
aerial.color[aerial.Country == "NEW ZEALAND"] = "rgb(133,20,75)"
aerial.color[aerial.Country == "SOUTH AFRICA"] = "rgb(255,133,27)"

data2 = [dict(type='scattergeo', lon=aerial['Takeoff Longitude'], lat=aerial['Takeoff Latitude'],
             hoverinfo='text', text='Country: '+aerial.Country+' Takeoff Location: '+
             aerial['Takeoff Location']+' Takeoff Base: '+aerial['Takeoff Base'], mode='markers',
             marker=dict(sizemode='area', sizeref=1, size=10, line=dict(width=1, color='white'),
             color=aerial['color'], opacity=0.7))]

layout2 = dict(title='Takeoff Bases of Countries', hovermode='closest', geo=dict(showframe=False, showland=True,
              showcountries=True, countrywidth=1, projection=dict(type='mercator'), landcolor='rgb(217,217,217)',
              subunitwidth=1, showlakes=True, lakecolor='rgb(255,255,255)', countrycolor='rgb(5,5,5)'))

fig2 = go.Figure(data=data2, layout=layout2)
plot(fig2)

# Visualization of Bombing Paths-------------------------------------------------------------------
# Trace 1
airports = [ dict(
        type = 'scattergeo', lon = aerial['Takeoff Longitude'], lat = aerial['Takeoff Latitude'],
        hoverinfo = 'text', text = "Country: " + aerial.Country + " Takeoff Location: "+
        aerial["Takeoff Location"]+" Takeoff Base: " + aerial['Takeoff Base'],
        mode = 'markers', marker = dict(size=5, color = aerial["color"], line = dict(width=1, color = "white")))]

# Trace 2
targets = [ dict(
        type = 'scattergeo', lon = aerial['Target Longitude'], lat = aerial['Target Latitude'],
        hoverinfo = 'text', text = "Target Country: "+aerial["Target Country"]+" Target City: "+aerial["Target City"],
        mode = 'markers', marker = dict(size=1, color = "red", line = dict(width=0.5, color = "red")))]
        
# Trace 3
flight_paths = [] 
for i in range(len(aerial['Target Longitude'])):
    flight_paths.append(
            dict(type = 'scattergeo',lon = [ aerial.iloc[i,9], aerial.iloc[i,16] ], 
            lat = [ aerial.iloc[i,8], aerial.iloc[i,15] ], mode = 'lines', 
            line = dict(width = 0.7,color = 'black'), opacity = 0.6)
            )
    
layout3 = dict(title = 'Bombing Paths from Attacker Country to Target ', hovermode='closest',
              geo = dict(showframe=False, showland=True, showcoastlines=True, showcountries=True,
              countrywidth=1, projection=dict(type='Mercator'), landcolor = 'rgb(217, 217, 217)',
              subunitwidth=1, showlakes = True, lakecolor = 'rgb(255, 255, 255)', countrycolor="rgb(5, 5, 5)"))
    
fig3 = dict(data=flight_paths + airports + targets, layout=layout3)
plot(fig3)