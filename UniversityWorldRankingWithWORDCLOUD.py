# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:29:48 2019

@author: Osman Ali Yardım

University World Ranking: Word Cloud
"""

import pandas as pd
import matplotlib.pyplot as plt

# Word Cloud library usage in Spyder
from wordcloud import WordCloud

# Read data
timesData = pd.read_csv('timesData.csv')

# Discover data
print(timesData.head())
timesData.info()

# Most Mentioned Countries (Universities) in 2011 
df2011 = timesData.country[timesData.year == 2011]

plt.subplots(figsize=(8,8))
wordcloud = WordCloud(background_color='white',width=512, height=384).generate(" ".join(df2011))

plt.imshow(wordcloud)
plt.axis('off')
plt.show()